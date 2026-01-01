"""Simulation Engine for the Data Simulator Service.

Orchestrates the simulation loop with time acceleration.
"""

import asyncio
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, List, Optional
import logging
import uuid

from .models import (
    EntityConfig,
    EntityEvent,
    SimulationConfig,
    SimulationScenario,
    SimulationState,
    SimulationTick,
    TimeAccelerationConfig,
)
from .entity_generator import EntityGenerator
from .kpi_analyzer import KPIAnalyzer
from .messaging_client import SimulatorMessagingClient

logger = logging.getLogger(__name__)


class SimulationEngine:
    """
    Orchestrates the simulation with time acceleration.
    
    Time Acceleration Model:
    - real_interval_seconds: How often data is generated (e.g., 10 seconds)
    - simulated_interval_hours: What each interval represents (e.g., 1 hour)
    
    Example: 10 seconds real = 1 hour simulated
    - 1 minute real = 6 hours simulated
    - 10 minutes real = 2.5 days simulated
    - 1 hour real = 15 days simulated
    """
    
    def __init__(
        self,
        config: SimulationConfig,
        metadata_service_url: Optional[str] = None,
        redis_url: Optional[str] = None,
    ):
        self.config = config
        self.metadata_service_url = metadata_service_url
        self.redis_url = redis_url
        
        self.kpi_analyzer = KPIAnalyzer(redis_url)
        
        # Messaging client for publishing events
        self.messaging_client: Optional[SimulatorMessagingClient] = None
        if redis_url:
            self.messaging_client = SimulatorMessagingClient(redis_url)
        
        # Entity generators by entity name
        self.generators: Dict[str, EntityGenerator] = {}
        
        # Simulation state
        self.state = SimulationState(
            simulation_id=config.simulation_id,
            config=config,
            current_simulated_time=config.start_simulated_time,
        )
        
        # Event callbacks
        self._on_tick_callbacks: List[Callable[[SimulationTick], None]] = []
        self._on_event_callbacks: List[Callable[[EntityEvent], None]] = []
        
        # Control flags
        self._running = False
        self._paused = False
        self._stop_requested = False
    
    async def initialize(self) -> None:
        """Initialize the simulation by analyzing KPIs and setting up generators."""
        logger.info(f"Initializing simulation: {self.config.simulation_id}")
        
        # Connect to messaging service if configured
        if self.messaging_client:
            try:
                await self.messaging_client.connect()
                logger.info("Connected to messaging service")
            except Exception as e:
                logger.warning(f"Failed to connect to messaging service: {e}")
                self.messaging_client = None
        
        # Analyze KPIs to determine entity requirements
        # Uses required_objects field from KPI definitions
        if self.config.kpi_codes:
            entity_configs, kpi_definitions = await self.kpi_analyzer.analyze_kpis(self.config.kpi_codes)
            
            # Store KPI definitions for reference
            self._kpi_definitions = kpi_definitions
            
            # Merge with explicitly configured entities
            existing_names = {e.entity_name for e in self.config.entities}
            for config in entity_configs:
                if config.entity_name not in existing_names:
                    self.config.entities.append(config)
        
        # Create generators for each entity type
        for entity_config in self.config.entities:
            generator = EntityGenerator(
                entity_config=entity_config,
                scenario=self.config.scenario,
                random_seed=self.config.random_seed,
            )
            
            # Initialize starting entities
            events = generator.initialize_entities(
                simulated_time=self.config.start_simulated_time
            )
            
            # Notify callbacks of initial events
            for event in events:
                await self._emit_event(event)
            
            self.generators[entity_config.entity_name] = generator
            self.state.entity_counts[entity_config.entity_name] = generator.get_active_count()
        
        logger.info(f"Simulation initialized with {len(self.generators)} entity types")
    
    async def start(self) -> None:
        """Start the simulation loop."""
        if self._running:
            logger.warning("Simulation already running")
            return
        
        self._running = True
        self._stop_requested = False
        self.state.status = "running"
        self.state.started_at = datetime.utcnow()
        
        logger.info(
            f"Starting simulation with time acceleration: "
            f"{self.config.time_config.real_interval_seconds}s real = "
            f"{self.config.time_config.simulated_interval_hours}h simulated "
            f"({self.config.time_config.acceleration_factor:.1f}x)"
        )
        
        try:
            await self._run_loop()
        except Exception as e:
            logger.error(f"Simulation error: {e}", exc_info=True)
            self.state.status = "stopped"
            self.state.error_message = str(e)
        finally:
            self._running = False
    
    async def _run_loop(self) -> None:
        """Main simulation loop."""
        while not self._stop_requested:
            if self._paused:
                await asyncio.sleep(0.1)
                continue
            
            # Generate tick
            tick = await self._generate_tick()
            
            # Emit tick to callbacks
            await self._emit_tick(tick)
            
            # Publish events to messaging service
            # Database service and calculation engine subscribe to these events
            if self.messaging_client:
                await self._publish_events(tick)
            
            # Wait for next real-time interval
            await asyncio.sleep(self.config.time_config.real_interval_seconds)
        
        self.state.status = "stopped"
        logger.info(f"Simulation stopped after {self.state.ticks_completed} ticks")
    
    async def _generate_tick(self) -> SimulationTick:
        """Generate a single simulation tick."""
        tick_number = self.state.ticks_completed + 1
        real_time = datetime.utcnow()
        
        # Advance simulated time
        self.state.current_simulated_time += self.config.time_config.simulated_interval_timedelta
        simulated_time = self.state.current_simulated_time
        
        all_events: List[EntityEvent] = []
        entity_counts: Dict[str, int] = {}
        
        # Generate events for each entity type
        for entity_name, generator in self.generators.items():
            events, counts = generator.generate_tick_events(
                simulated_time=simulated_time,
                time_config=self.config.time_config,
            )
            all_events.extend(events)
            entity_counts.update(counts)
            
            # Update main count
            entity_counts[entity_name] = generator.get_active_count()
        
        # Update state
        self.state.ticks_completed = tick_number
        self.state.last_tick_at = real_time
        self.state.entity_counts = entity_counts
        
        tick = SimulationTick(
            tick_number=tick_number,
            simulated_time=simulated_time,
            real_time=real_time,
            events=all_events,
            entity_counts=entity_counts,
        )
        
        if tick_number % 10 == 0:
            logger.info(
                f"Tick {tick_number}: simulated_time={simulated_time.isoformat()}, "
                f"events={len(all_events)}, counts={entity_counts}"
            )
        
        return tick
    
    async def _publish_events(self, tick: SimulationTick) -> None:
        """
        Publish tick events to the messaging service.
        
        The Database Service and Calculation Engine subscribe to these events:
        - Database Service persists the data
        - Calculation Engine calculates KPIs in real-time
        """
        if not self.messaging_client:
            return
        
        try:
            # Publish each entity event
            for event in tick.events:
                await self.messaging_client.publish_entity_event(
                    entity_name=event.entity_name,
                    event_type=event.event_type,
                    entity_id=event.entity_id,
                    attributes=event.attributes,
                    simulated_time=event.simulated_time,
                    simulation_id=self.config.simulation_id,
                )
            
            # Publish tick summary
            await self.messaging_client.publish_tick(
                simulation_id=self.config.simulation_id,
                tick_number=tick.tick_number,
                simulated_time=tick.simulated_time,
                entity_counts=tick.entity_counts,
                event_count=len(tick.events),
            )
            
            if tick.tick_number % 10 == 0:
                logger.debug(f"Published {len(tick.events)} events for tick {tick.tick_number}")
                
        except Exception as e:
            logger.warning(f"Failed to publish events: {e}")
    
    async def _emit_tick(self, tick: SimulationTick) -> None:
        """Emit tick to registered callbacks."""
        for callback in self._on_tick_callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(tick)
                else:
                    callback(tick)
            except Exception as e:
                logger.error(f"Tick callback error: {e}")
    
    async def _emit_event(self, event: EntityEvent) -> None:
        """Emit event to registered callbacks."""
        for callback in self._on_event_callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(event)
                else:
                    callback(event)
            except Exception as e:
                logger.error(f"Event callback error: {e}")
    
    def on_tick(self, callback: Callable[[SimulationTick], None]) -> None:
        """Register a callback for each simulation tick."""
        self._on_tick_callbacks.append(callback)
    
    def on_event(self, callback: Callable[[EntityEvent], None]) -> None:
        """Register a callback for each entity event."""
        self._on_event_callbacks.append(callback)
    
    def pause(self) -> None:
        """Pause the simulation."""
        self._paused = True
        self.state.status = "paused"
        logger.info("Simulation paused")
    
    def resume(self) -> None:
        """Resume the simulation."""
        self._paused = False
        self.state.status = "running"
        logger.info("Simulation resumed")
    
    async def stop(self) -> None:
        """Stop the simulation and disconnect from messaging."""
        self._stop_requested = True
        logger.info("Simulation stop requested")
        
        # Disconnect from messaging service
        if self.messaging_client:
            await self.messaging_client.disconnect()
        
        # Close KPI analyzer's metadata client
        if self.kpi_analyzer:
            await self.kpi_analyzer.close()
    
    def get_state(self) -> SimulationState:
        """Get current simulation state."""
        return self.state
    
    def get_entity_count(self, entity_name: str) -> int:
        """Get current count of an entity type."""
        if entity_name in self.generators:
            return self.generators[entity_name].get_active_count()
        return 0
    
    def get_entities_at_time(
        self,
        entity_name: str,
        simulated_time: datetime
    ) -> List[Dict[str, Any]]:
        """Get entities that were active at a specific simulated time."""
        if entity_name in self.generators:
            return self.generators[entity_name].get_entities_at_time(simulated_time)
        return []


def create_simulation(
    name: str,
    kpi_codes: Optional[List[str]] = None,
    entities: Optional[List[EntityConfig]] = None,
    scenario: SimulationScenario = SimulationScenario.HEALTHY,
    real_interval_seconds: float = 10.0,
    simulated_interval_hours: float = 1.0,
    start_simulated_time: Optional[datetime] = None,
    random_seed: Optional[int] = None,
    metadata_service_url: Optional[str] = None,
    redis_url: Optional[str] = None,
) -> SimulationEngine:
    """
    Factory function to create a simulation engine.
    
    Args:
        name: Human-readable name for the simulation
        kpi_codes: List of KPI codes to generate data for
        entities: Explicit entity configurations
        scenario: Pre-defined scenario (healthy, struggling, etc.)
        real_interval_seconds: How often to generate data (real time)
        simulated_interval_hours: What each interval represents (simulated time)
        start_simulated_time: Starting point in simulated time
        random_seed: Random seed for reproducibility
        metadata_service_url: URL for metadata service
        redis_url: Redis URL for messaging (pub/sub)
        
    Returns:
        Configured SimulationEngine ready to start
    """
    config = SimulationConfig(
        simulation_id=str(uuid.uuid4()),
        name=name,
        time_config=TimeAccelerationConfig(
            real_interval_seconds=real_interval_seconds,
            simulated_interval_hours=simulated_interval_hours,
        ),
        scenario=scenario,
        entities=entities or [],
        kpi_codes=kpi_codes or [],
        start_simulated_time=start_simulated_time or (datetime.utcnow() - timedelta(days=365)),
        random_seed=random_seed,
    )
    
    return SimulationEngine(
        config=config,
        metadata_service_url=metadata_service_url,
        redis_url=redis_url,
    )
