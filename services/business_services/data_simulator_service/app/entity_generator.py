"""Entity data generator for the Data Simulator Service.

Generates realistic entity data based on KPI set_based_definitions.
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple
import random
import uuid
import logging
from faker import Faker

from .models import (
    EntityConfig,
    EntityEvent,
    SimulationScenario,
    TimeAccelerationConfig,
)

logger = logging.getLogger(__name__)

fake = Faker()


class EntityGenerator:
    """Generates entity data for simulation based on KPI definitions."""
    
    # Scenario modifiers for churn/growth rates
    SCENARIO_MODIFIERS = {
        SimulationScenario.HEALTHY: {
            "churn_multiplier": 0.5,
            "growth_multiplier": 1.5,
            "conversion_multiplier": 1.2,
            "volatility": 0.1,
        },
        SimulationScenario.STRUGGLING: {
            "churn_multiplier": 2.0,
            "growth_multiplier": 0.3,
            "conversion_multiplier": 0.6,
            "volatility": 0.2,
        },
        SimulationScenario.SEASONAL: {
            "churn_multiplier": 1.0,
            "growth_multiplier": 1.0,
            "conversion_multiplier": 1.0,
            "volatility": 0.3,
            "seasonal_amplitude": 0.4,
        },
        SimulationScenario.GROWTH_SPURT: {
            "churn_multiplier": 0.7,
            "growth_multiplier": 3.0,
            "conversion_multiplier": 1.5,
            "volatility": 0.15,
        },
        SimulationScenario.STABLE: {
            "churn_multiplier": 1.0,
            "growth_multiplier": 1.0,
            "conversion_multiplier": 1.0,
            "volatility": 0.05,
        },
        SimulationScenario.VOLATILE: {
            "churn_multiplier": 1.0,
            "growth_multiplier": 1.0,
            "conversion_multiplier": 1.0,
            "volatility": 0.5,
        },
    }
    
    def __init__(
        self,
        entity_config: EntityConfig,
        scenario: SimulationScenario = SimulationScenario.HEALTHY,
        random_seed: Optional[int] = None,
    ):
        self.config = entity_config
        self.scenario = scenario
        self.modifiers = self.SCENARIO_MODIFIERS[scenario]
        
        if random_seed is not None:
            random.seed(random_seed)
            Faker.seed(random_seed)
        
        # Track active entities: {entity_id: {attributes}}
        self.active_entities: Dict[str, Dict[str, Any]] = {}
        
        # Track entity history for temporal queries
        self.entity_history: List[EntityEvent] = []
        
    def initialize_entities(
        self,
        simulated_time: datetime,
        count: Optional[int] = None
    ) -> List[EntityEvent]:
        """
        Initialize the starting set of entities.
        
        Creates entities with active_date spread over the past to simulate
        a realistic customer base with varying tenure.
        """
        count = count or self.config.initial_count
        events = []
        
        for i in range(count):
            # Spread active_date over past 2 years for realistic tenure distribution
            days_ago = random.randint(1, 730)
            active_date = simulated_time - timedelta(days=days_ago)
            
            entity_id = str(uuid.uuid4())
            attributes = self._generate_entity_attributes(active_date)
            
            self.active_entities[entity_id] = attributes
            
            event = EntityEvent(
                event_type="create",
                entity_name=self.config.entity_name,
                entity_id=entity_id,
                simulated_time=active_date,
                attributes=attributes,
            )
            events.append(event)
            self.entity_history.append(event)
        
        logger.info(f"Initialized {count} {self.config.entity_name}")
        return events
    
    def generate_tick_events(
        self,
        simulated_time: datetime,
        time_config: TimeAccelerationConfig,
    ) -> Tuple[List[EntityEvent], Dict[str, int]]:
        """
        Generate events for a single simulation tick.
        
        Returns:
            Tuple of (events, entity_counts)
        """
        events = []
        
        # Calculate rates adjusted for the simulated time interval
        hours_per_tick = time_config.simulated_interval_hours
        monthly_fraction = hours_per_tick / (30 * 24)  # Fraction of a month
        
        # Apply scenario modifiers and volatility
        volatility = self.modifiers["volatility"]
        
        # Seasonal adjustment (if applicable)
        seasonal_factor = 1.0
        if "seasonal_amplitude" in self.modifiers:
            # Use month to create seasonal pattern (peak in Q4, low in Q1)
            month = simulated_time.month
            seasonal_factor = 1.0 + self.modifiers["seasonal_amplitude"] * \
                (0.5 * (1 + ((month - 1) / 11) * 2 - 1))  # Ramps up through year
        
        # Calculate churn for this tick
        churn_rate = self.config.base_churn_rate * \
            self.modifiers["churn_multiplier"] * \
            seasonal_factor * \
            (1 + random.uniform(-volatility, volatility))
        
        churn_rate_per_tick = churn_rate * monthly_fraction
        
        # Calculate growth for this tick
        growth_rate = self.config.base_growth_rate * \
            self.modifiers["growth_multiplier"] * \
            seasonal_factor * \
            (1 + random.uniform(-volatility, volatility))
        
        growth_rate_per_tick = growth_rate * monthly_fraction
        
        # Process churns
        churn_events = self._process_churns(simulated_time, churn_rate_per_tick)
        events.extend(churn_events)
        
        # Process new acquisitions
        new_events = self._process_acquisitions(simulated_time, growth_rate_per_tick)
        events.extend(new_events)
        
        # Store events in history
        self.entity_history.extend(events)
        
        entity_counts = {
            self.config.entity_name: len(self.active_entities),
            f"{self.config.entity_name}_churned": len(churn_events),
            f"{self.config.entity_name}_new": len(new_events),
        }
        
        return events, entity_counts
    
    def _process_churns(
        self,
        simulated_time: datetime,
        churn_rate: float
    ) -> List[EntityEvent]:
        """Process entity churns for this tick."""
        events = []
        
        # Calculate expected churns
        expected_churns = int(len(self.active_entities) * churn_rate)
        
        # Add some randomness
        actual_churns = max(0, expected_churns + random.randint(-1, 1))
        
        if actual_churns > 0 and self.active_entities:
            # Select entities to churn (prefer older entities slightly)
            entity_ids = list(self.active_entities.keys())
            churned_ids = random.sample(
                entity_ids, 
                min(actual_churns, len(entity_ids))
            )
            
            for entity_id in churned_ids:
                attributes = self.active_entities.pop(entity_id)
                attributes["inactive_date"] = simulated_time
                
                event = EntityEvent(
                    event_type="deactivate",
                    entity_name=self.config.entity_name,
                    entity_id=entity_id,
                    simulated_time=simulated_time,
                    attributes=attributes,
                )
                events.append(event)
        
        return events
    
    def _process_acquisitions(
        self,
        simulated_time: datetime,
        growth_rate: float
    ) -> List[EntityEvent]:
        """Process new entity acquisitions for this tick."""
        events = []
        
        # Calculate expected new entities
        base_count = max(len(self.active_entities), self.config.initial_count)
        expected_new = int(base_count * growth_rate)
        
        # Add some randomness
        actual_new = max(0, expected_new + random.randint(-1, 2))
        
        for _ in range(actual_new):
            entity_id = str(uuid.uuid4())
            attributes = self._generate_entity_attributes(simulated_time)
            
            self.active_entities[entity_id] = attributes
            
            event = EntityEvent(
                event_type="create",
                entity_name=self.config.entity_name,
                entity_id=entity_id,
                simulated_time=simulated_time,
                attributes=attributes,
            )
            events.append(event)
        
        return events
    
    def _generate_entity_attributes(
        self,
        active_date: datetime
    ) -> Dict[str, Any]:
        """Generate realistic attributes for an entity."""
        entity_name = self.config.entity_name.lower()
        
        base_attrs = {
            "active_date": active_date,
            "inactive_date": None,
            "created_at": active_date,
        }
        
        # Generate entity-specific attributes
        if "customer" in entity_name or "client" in entity_name:
            base_attrs.update(self._generate_customer_attributes())
        elif "policy" in entity_name:
            base_attrs.update(self._generate_policy_attributes())
        elif "subscription" in entity_name:
            base_attrs.update(self._generate_subscription_attributes())
        elif "lead" in entity_name or "opportunity" in entity_name:
            base_attrs.update(self._generate_lead_attributes())
        elif "order" in entity_name or "transaction" in entity_name:
            base_attrs.update(self._generate_transaction_attributes())
        
        # Add any custom attributes from config
        for attr_name, attr_config in self.config.attributes.items():
            if attr_name not in base_attrs:
                base_attrs[attr_name] = self._generate_attribute_value(attr_config)
        
        return base_attrs
    
    def _generate_customer_attributes(self) -> Dict[str, Any]:
        """Generate customer-specific attributes."""
        return {
            "name": fake.name(),
            "email": fake.email(),
            "tier": random.choice(["basic", "standard", "premium"]),
            "segment": random.choice(["enterprise", "mid-market", "smb", "consumer"]),
            "region": random.choice(["north", "south", "east", "west"]),
            "monthly_value": round(random.uniform(50, 5000), 2),
        }
    
    def _generate_policy_attributes(self) -> Dict[str, Any]:
        """Generate policy-specific attributes."""
        return {
            "policy_type": random.choice(["auto", "home", "life", "health"]),
            "coverage_amount": random.choice([50000, 100000, 250000, 500000, 1000000]),
            "premium": round(random.uniform(100, 2000), 2),
            "risk_score": round(random.uniform(1, 10), 1),
        }
    
    def _generate_subscription_attributes(self) -> Dict[str, Any]:
        """Generate subscription-specific attributes."""
        return {
            "plan": random.choice(["free", "starter", "professional", "enterprise"]),
            "billing_cycle": random.choice(["monthly", "annual"]),
            "mrr": round(random.uniform(10, 500), 2),
            "seats": random.randint(1, 100),
        }
    
    def _generate_lead_attributes(self) -> Dict[str, Any]:
        """Generate lead/opportunity-specific attributes."""
        return {
            "source": random.choice(["organic", "paid", "referral", "partner"]),
            "stage": random.choice(["new", "qualified", "proposal", "negotiation"]),
            "expected_value": round(random.uniform(1000, 100000), 2),
            "converted_at": None,  # Set when converted
        }
    
    def _generate_transaction_attributes(self) -> Dict[str, Any]:
        """Generate transaction-specific attributes."""
        return {
            "amount": round(random.uniform(10, 10000), 2),
            "currency": "USD",
            "payment_method": random.choice(["credit_card", "bank_transfer", "paypal"]),
            "status": random.choice(["completed", "pending", "refunded"]),
        }
    
    def _generate_attribute_value(self, config: Any) -> Any:
        """Generate a value based on attribute configuration."""
        if isinstance(config, dict):
            attr_type = config.get("type", "string")
            if attr_type == "choice":
                return random.choice(config.get("values", ["default"]))
            elif attr_type == "int":
                return random.randint(
                    config.get("min", 0),
                    config.get("max", 100)
                )
            elif attr_type == "float":
                return round(random.uniform(
                    config.get("min", 0.0),
                    config.get("max", 100.0)
                ), 2)
            elif attr_type == "bool":
                return random.random() < config.get("probability", 0.5)
        return config
    
    def get_active_count(self) -> int:
        """Get current count of active entities."""
        return len(self.active_entities)
    
    def get_entities_at_time(
        self,
        simulated_time: datetime
    ) -> List[Dict[str, Any]]:
        """Get all entities that were active at a specific simulated time."""
        active_at_time = []
        
        for event in self.entity_history:
            if event.event_type == "create" and event.simulated_time <= simulated_time:
                # Check if still active at that time
                inactive_date = event.attributes.get("inactive_date")
                if inactive_date is None or inactive_date > simulated_time:
                    active_at_time.append({
                        "entity_id": event.entity_id,
                        **event.attributes
                    })
        
        return active_at_time
