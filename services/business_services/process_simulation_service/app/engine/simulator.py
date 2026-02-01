"""Discrete Event Simulation Engine for Process Scenarios.

This module implements a SimPy-based discrete event simulation engine
for simulating business process execution and what-if scenarios.
"""

import logging
import random
from datetime import datetime, timedelta
from typing import Any, Dict, Generator, List, Optional
from uuid import UUID, uuid4

import simpy

from ..models import (
    ArrivalDistribution,
    BottleneckInfo,
    DistributionType,
    DurationDistribution,
    KPIPrediction,
    ImpactDirection,
    ParameterChange,
    ProcessDefinition,
    ProcessStep,
    RiskLevel,
    ScenarioDefinition,
    SimulationConfig,
    SimulationEvent,
    SimulationResult,
    SimulationStatus,
    StepType,
)

logger = logging.getLogger(__name__)


class ProcessEntity:
    """Represents a work item flowing through the process."""
    
    def __init__(self, entity_id: str, arrival_time: float):
        self.entity_id = entity_id
        self.arrival_time = arrival_time
        self.start_times: Dict[str, float] = {}
        self.end_times: Dict[str, float] = {}
        self.queue_times: Dict[str, float] = {}
        self.completed = False
        self.defect = False
        self.rework_count = 0
        self.total_cost = 0.0


class ProcessSimulationEngine:
    """Discrete event simulation engine for process scenarios."""
    
    def __init__(self):
        self.env: Optional[simpy.Environment] = None
        self.resources: Dict[str, simpy.Resource] = {}
        self.step_stats: Dict[str, Dict[str, Any]] = {}
        self.entities: List[ProcessEntity] = []
        self.event_log: List[SimulationEvent] = []
        self.random_seed: Optional[int] = None
        
    def _sample_duration(self, distribution: DurationDistribution) -> float:
        """Sample a duration from the given distribution."""
        params = distribution.parameters
        
        if distribution.distribution_type == DistributionType.FIXED:
            return params.get("value", 0)
        elif distribution.distribution_type == DistributionType.NORMAL:
            mean = params.get("mean", 0)
            std = params.get("std", 0)
            return max(0, random.gauss(mean, std))
        elif distribution.distribution_type == DistributionType.EXPONENTIAL:
            rate = params.get("rate", 1)
            return random.expovariate(rate) if rate > 0 else 0
        elif distribution.distribution_type == DistributionType.TRIANGULAR:
            min_val = params.get("min", 0)
            mode = params.get("mode", 0)
            max_val = params.get("max", 0)
            return random.triangular(min_val, max_val, mode)
        elif distribution.distribution_type == DistributionType.UNIFORM:
            min_val = params.get("min", 0)
            max_val = params.get("max", 0)
            return random.uniform(min_val, max_val)
        else:
            return 0
    
    def _sample_arrival(self, distribution: ArrivalDistribution) -> float:
        """Sample inter-arrival time from the given distribution."""
        params = distribution.parameters
        
        if distribution.distribution_type == DistributionType.POISSON:
            rate = params.get("rate", 1)  # arrivals per hour
            return random.expovariate(rate) if rate > 0 else 1
        elif distribution.distribution_type == DistributionType.FIXED:
            rate = params.get("rate", 1)
            return 1 / rate if rate > 0 else 1
        else:
            return 1  # Default to 1 hour between arrivals
    
    def _get_next_steps(
        self,
        current_step_id: str,
        process: ProcessDefinition
    ) -> List[str]:
        """Get the next step(s) after a given step."""
        next_steps = []
        for transition in process.transitions:
            if transition.from_step == current_step_id:
                # Handle probabilistic routing
                if random.random() < transition.probability:
                    next_steps.append(transition.to_step)
        return next_steps
    
    def _get_step_by_id(
        self,
        step_id: str,
        process: ProcessDefinition
    ) -> Optional[ProcessStep]:
        """Get a step by its ID."""
        for step in process.steps:
            if step.id == step_id:
                return step
        return None
    
    def _apply_parameter_changes(
        self,
        process: ProcessDefinition,
        changes: List[ParameterChange]
    ) -> ProcessDefinition:
        """Apply scenario parameter changes to process definition."""
        # Create a deep copy to avoid modifying the original
        import copy
        modified_process = copy.deepcopy(process)
        
        for change in changes:
            for step in modified_process.steps:
                if step.id == change.target:
                    if change.change_type.value == "step_duration":
                        # Modify duration distribution
                        if "mean" in step.duration_distribution.parameters:
                            step.duration_distribution.parameters["mean"] = change.new_value
                        else:
                            step.duration_distribution.parameters["value"] = change.new_value
                    elif change.change_type.value == "defect_rate":
                        step.defect_rate = change.new_value
                    elif change.change_type.value == "cost":
                        if change.parameter == "fixed_cost":
                            step.fixed_cost = change.new_value
                        else:
                            step.variable_cost_per_unit = change.new_value
                    elif change.change_type.value == "resource_capacity":
                        step.max_concurrent = int(change.new_value)
                        step.resource_quantity = int(change.new_value)
        
        return modified_process
    
    def _log_event(
        self,
        simulation_id: UUID,
        event_type: str,
        step_id: Optional[str] = None,
        entity_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        event_data: Optional[Dict[str, Any]] = None
    ):
        """Log a simulation event."""
        event = SimulationEvent(
            time=datetime.utcnow(),  # In real sim, use sim time
            event_type=event_type,
            step_id=step_id,
            entity_id=entity_id,
            resource_id=resource_id,
            event_data=event_data or {}
        )
        self.event_log.append(event)
    
    def _process_entity(
        self,
        entity: ProcessEntity,
        process: ProcessDefinition,
        simulation_id: UUID
    ) -> Generator:
        """Process a single entity through the process steps."""
        # Find start step
        start_step = None
        for step in process.steps:
            if step.step_type == StepType.START:
                start_step = step
                break
        
        if not start_step:
            # Use first step if no explicit start
            start_step = process.steps[0] if process.steps else None
        
        if not start_step:
            return
        
        current_steps = [start_step.id]
        
        while current_steps:
            step_id = current_steps.pop(0)
            step = self._get_step_by_id(step_id, process)
            
            if not step:
                continue
            
            # Skip start/end steps for processing
            if step.step_type in [StepType.START, StepType.END]:
                current_steps.extend(self._get_next_steps(step_id, process))
                if step.step_type == StepType.END:
                    entity.completed = True
                continue
            
            # Initialize step stats if needed
            if step_id not in self.step_stats:
                self.step_stats[step_id] = {
                    "name": step.name,
                    "processing_count": 0,
                    "total_wait_time": 0,
                    "total_processing_time": 0,
                    "queue_lengths": [],
                    "utilizations": [],
                }
            
            # Request resource if needed
            resource_name = step_id
            if resource_name not in self.resources:
                capacity = step.max_concurrent or step.resource_quantity or 1
                self.resources[resource_name] = simpy.Resource(self.env, capacity=capacity)
            
            resource = self.resources[resource_name]
            
            # Log queue entry
            queue_start = self.env.now
            self.step_stats[step_id]["queue_lengths"].append(len(resource.queue))
            
            self._log_event(
                simulation_id, "queue",
                step_id=step_id,
                entity_id=entity.entity_id,
                event_data={"queue_length": len(resource.queue)}
            )
            
            # Wait for resource
            with resource.request() as request:
                yield request
                
                # Calculate wait time
                wait_time = self.env.now - queue_start
                entity.queue_times[step_id] = wait_time
                self.step_stats[step_id]["total_wait_time"] += wait_time
                
                # Start processing
                entity.start_times[step_id] = self.env.now
                self._log_event(
                    simulation_id, "start",
                    step_id=step_id,
                    entity_id=entity.entity_id
                )
                
                # Process (sample duration)
                duration = self._sample_duration(step.duration_distribution)
                yield self.env.timeout(duration)
                
                # End processing
                entity.end_times[step_id] = self.env.now
                self.step_stats[step_id]["processing_count"] += 1
                self.step_stats[step_id]["total_processing_time"] += duration
                
                # Calculate cost
                entity.total_cost += step.fixed_cost + (step.variable_cost_per_unit * 1)
                
                # Check for defect
                if random.random() < step.defect_rate:
                    entity.defect = True
                    entity.rework_count += 1
                
                self._log_event(
                    simulation_id, "complete",
                    step_id=step_id,
                    entity_id=entity.entity_id,
                    event_data={"duration": duration, "cost": step.fixed_cost + step.variable_cost_per_unit}
                )
            
            # Get next steps
            current_steps.extend(self._get_next_steps(step_id, process))
    
    def _arrival_generator(
        self,
        process: ProcessDefinition,
        scenario: ScenarioDefinition,
        simulation_id: UUID,
        warm_up_hours: float
    ) -> Generator:
        """Generate arrivals for the simulation."""
        entity_count = 0
        
        while True:
            # Sample inter-arrival time
            inter_arrival = self._sample_arrival(scenario.arrival_distribution)
            yield self.env.timeout(inter_arrival)
            
            # Create new entity
            entity_count += 1
            entity = ProcessEntity(
                entity_id=f"E{entity_count:06d}",
                arrival_time=self.env.now
            )
            
            # Only track entities after warm-up period
            if self.env.now >= warm_up_hours:
                self.entities.append(entity)
            
            self._log_event(
                simulation_id, "arrival",
                entity_id=entity.entity_id,
                event_data={"arrival_time": self.env.now}
            )
            
            # Start processing this entity
            self.env.process(self._process_entity(entity, process, simulation_id))
    
    async def run_simulation(
        self,
        process: ProcessDefinition,
        scenario: ScenarioDefinition,
        simulation_id: Optional[UUID] = None
    ) -> SimulationResult:
        """
        Run a discrete event simulation of the process.
        
        Args:
            process: The process definition to simulate
            scenario: The scenario with parameter changes
            simulation_id: Optional ID for tracking
            
        Returns:
            SimulationResult with KPI predictions and metrics
        """
        if simulation_id is None:
            simulation_id = uuid4()
        
        config = scenario.simulation_config
        
        # Set random seed for reproducibility
        if config.random_seed is not None:
            random.seed(config.random_seed)
            self.random_seed = config.random_seed
        
        # Apply parameter changes to process
        modified_process = self._apply_parameter_changes(
            process, scenario.parameter_changes
        )
        
        # Initialize simulation
        self.env = simpy.Environment()
        self.resources = {}
        self.step_stats = {}
        self.entities = []
        self.event_log = []
        
        # Start arrival generator
        self.env.process(self._arrival_generator(
            modified_process,
            scenario,
            simulation_id,
            config.warm_up_period_hours
        ))
        
        # Run simulation
        total_sim_time = config.warm_up_period_hours + config.simulation_duration_hours
        self.env.run(until=total_sim_time)
        
        # Calculate results
        result = self._calculate_results(simulation_id, scenario.id, modified_process)
        
        return result
    
    def _calculate_results(
        self,
        simulation_id: UUID,
        scenario_id: UUID,
        process: ProcessDefinition
    ) -> SimulationResult:
        """Calculate simulation results from collected data."""
        completed_entities = [e for e in self.entities if e.completed]
        
        # Cycle time calculations
        cycle_times = []
        for entity in completed_entities:
            if entity.start_times and entity.end_times:
                # Total time from first start to last end
                first_start = min(entity.start_times.values()) if entity.start_times else entity.arrival_time
                last_end = max(entity.end_times.values()) if entity.end_times else first_start
                cycle_time = last_end - first_start
                # Add queue times
                cycle_time += sum(entity.queue_times.values())
                cycle_times.append(cycle_time)
        
        avg_cycle_time = sum(cycle_times) / len(cycle_times) if cycle_times else 0
        min_cycle_time = min(cycle_times) if cycle_times else 0
        max_cycle_time = max(cycle_times) if cycle_times else 0
        
        import statistics
        cycle_time_std = statistics.stdev(cycle_times) if len(cycle_times) > 1 else 0
        
        # Throughput
        total_completed = len(completed_entities)
        
        # Resource utilization
        resource_utilization = {}
        for step_id, stats in self.step_stats.items():
            if stats["processing_count"] > 0:
                # Simple utilization calculation
                utilization = min(100, (stats["total_processing_time"] / (self.env.now or 1)) * 100)
                resource_utilization[step_id] = utilization
        
        # Cost
        total_cost = sum(e.total_cost for e in completed_entities)
        cost_per_unit = total_cost / total_completed if total_completed > 0 else 0
        
        # Quality
        defect_count = sum(1 for e in self.entities if e.defect)
        defect_rate = defect_count / len(self.entities) if self.entities else 0
        rework_count = sum(e.rework_count for e in self.entities)
        
        # Bottleneck analysis
        bottlenecks = []
        for step_id, stats in self.step_stats.items():
            if stats["processing_count"] > 0:
                avg_wait = stats["total_wait_time"] / stats["processing_count"]
                utilization = resource_utilization.get(step_id, 0)
                
                # Determine severity
                if utilization > 90:
                    severity = RiskLevel.CRITICAL
                elif utilization > 80:
                    severity = RiskLevel.HIGH
                elif utilization > 70:
                    severity = RiskLevel.MEDIUM
                else:
                    severity = RiskLevel.LOW
                
                bottlenecks.append(BottleneckInfo(
                    step_id=step_id,
                    step_name=stats["name"],
                    utilization=utilization,
                    wait_time_avg=avg_wait,
                    wait_time_max=max(stats["queue_lengths"]) if stats["queue_lengths"] else 0,
                    queue_length_avg=sum(stats["queue_lengths"]) / len(stats["queue_lengths"]) if stats["queue_lengths"] else 0,
                    severity=severity
                ))
        
        # Sort bottlenecks by utilization
        bottlenecks.sort(key=lambda b: b.utilization, reverse=True)
        
        # Generate KPI predictions based on process linked KPIs
        kpi_predictions = {}
        for kpi_code in process.linked_kpis:
            # Simplified prediction logic - would be enhanced with actual ML models
            baseline = 100.0  # Would come from actual data
            
            # Estimate impact based on simulation results
            if "cycle_time" in kpi_code.lower():
                predicted = avg_cycle_time
                change = ((predicted - baseline) / baseline) * 100 if baseline else 0
            elif "throughput" in kpi_code.lower():
                predicted = total_completed
                change = ((predicted - baseline) / baseline) * 100 if baseline else 0
            elif "cost" in kpi_code.lower():
                predicted = cost_per_unit
                change = ((predicted - baseline) / baseline) * 100 if baseline else 0
            elif "quality" in kpi_code.lower() or "defect" in kpi_code.lower():
                predicted = defect_rate * 100
                change = ((predicted - baseline) / baseline) * 100 if baseline else 0
            else:
                predicted = baseline
                change = 0
            
            direction = ImpactDirection.POSITIVE if change < 0 else ImpactDirection.NEGATIVE if change > 0 else ImpactDirection.NEUTRAL
            
            kpi_predictions[kpi_code] = KPIPrediction(
                kpi_code=kpi_code,
                baseline_value=baseline,
                predicted_value=predicted,
                change_percent=change,
                confidence_interval=(predicted * 0.9, predicted * 1.1),
                impact_direction=direction
            )
        
        return SimulationResult(
            id=simulation_id,
            scenario_id=scenario_id,
            status=SimulationStatus.COMPLETED,
            progress=100,
            avg_cycle_time=avg_cycle_time,
            min_cycle_time=min_cycle_time,
            max_cycle_time=max_cycle_time,
            cycle_time_std=cycle_time_std,
            total_completed=total_completed,
            throughput_rate=total_completed / (self.env.now or 1) if self.env else 0,
            resource_utilization=resource_utilization,
            total_cost=total_cost,
            cost_per_unit=cost_per_unit,
            defect_count=defect_count,
            defect_rate=defect_rate,
            rework_count=rework_count,
            bottlenecks=bottlenecks,
            kpi_predictions=kpi_predictions,
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow()
        )
    
    async def compare_scenarios(
        self,
        process: ProcessDefinition,
        scenarios: List[ScenarioDefinition],
        comparison_kpis: List[str]
    ) -> Dict[str, Any]:
        """
        Compare multiple scenarios side-by-side.
        
        Args:
            process: Base process definition
            scenarios: List of scenarios to compare
            comparison_kpis: KPIs to compare across scenarios
            
        Returns:
            Comparison results with rankings
        """
        results = {}
        
        for scenario in scenarios:
            result = await self.run_simulation(process, scenario)
            results[str(scenario.id)] = result
        
        # Build comparison
        kpi_comparison = {}
        for kpi in comparison_kpis:
            kpi_comparison[kpi] = {}
            for scenario_id, result in results.items():
                if kpi in result.kpi_predictions:
                    kpi_comparison[kpi][scenario_id] = result.kpi_predictions[kpi].predicted_value
        
        return {
            "scenario_results": results,
            "kpi_comparison": kpi_comparison
        }
