import sys
import os
import unittest
from typing import Dict, Any, List
from pydantic import ValidationError

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Import models
from ontology_models import (
    EntityDefinition,
    MetricDefinition,
    EdgeDefinition,
    ValueChainPatternDefinition,
    ActorDefinition,
    TableSchemaDefinition,
    ColumnDefinition
)

class TestOntologyManagement(unittest.TestCase):
    def test_entity_definition_valid(self):
        """Test creating a valid EntityDefinition."""
        print("\nTesting Valid EntityDefinition...")
        entity_data = {
            "kind": "entity_definition",
            "id": "ent_customer",
            "code": "CUSTOMER",
            "name": "Customer",
            "description": "A customer entity",
            "table_schema": {
                "table_name": "customers",
                "columns": [
                    {"name": "id", "type": "UUID", "primary_key": True},
                    {"name": "name", "type": "VARCHAR"}
                ]
            }
        }
        entity = EntityDefinition(**entity_data)
        self.assertEqual(entity.code, "CUSTOMER")
        print("✅ Valid EntityDefinition created successfully")

    def test_entity_definition_invalid(self):
        """Test creating an invalid EntityDefinition (missing required field)."""
        print("\nTesting Invalid EntityDefinition...")
        entity_data = {
            "kind": "entity_definition",
            "id": "ent_customer",
            # Missing "code"
            "name": "Customer"
        }
        with self.assertRaises(ValidationError):
            EntityDefinition(**entity_data)
        print("✅ ValidationError raised correctly for missing 'code'")

    def test_metric_definition_valid(self):
        """Test creating a valid MetricDefinition."""
        print("\nTesting Valid MetricDefinition...")
        metric_data = {
            "kind": "metric_definition",
            "id": "met_revenue",
            "code": "REVENUE",
            "name": "Revenue",
            "data_type": "decimal",
            "aggregation_methods": ["sum", "avg"],
            "default_aggregation": "sum"
        }
        metric = MetricDefinition(**metric_data)
        self.assertEqual(metric.code, "REVENUE")
        print("✅ Valid MetricDefinition created successfully")

    def test_relationship_definition_valid(self):
        """Test creating a valid EdgeDefinition."""
        print("\nTesting Valid EdgeDefinition...")
        rel_data = {
            "kind": "relationship_definition",
            "id": "rel_cust_order",
            "name": "Customer places Order",
            "from_entity": "CUSTOMER",
            "to_entity": "ORDER",
            "relationship_type": "one_to_many"
        }
        rel = EdgeDefinition(**rel_data)
        self.assertEqual(rel.from_entity, "CUSTOMER")
        print("✅ Valid EdgeDefinition created successfully")

    def test_value_chain_pattern_valid(self):
        """Test creating a valid ValueChainPatternDefinition."""
        print("\nTesting Valid ValueChainPatternDefinition...")
        vc_data = {
            "kind": "value_chain_pattern_definition",
            "id": "vc_supply_chain",
            "name": "Supply Chain",
            "domain": "industry",
            "graph_pattern": {
                "nodes": [
                    {"id": "node_supplier", "class_": "Supplier"},
                    {"id": "node_manufacturer", "class_": "Manufacturer"}
                ],
                "edges": [
                    {"from_": "node_supplier", "to": "node_manufacturer", "relationship_type": "supplies"}
                ]
            }
        }
        vc = ValueChainPatternDefinition(**vc_data)
        self.assertEqual(vc.domain, "industry")
        print("✅ Valid ValueChainPatternDefinition created successfully")

    def test_actor_definition_valid(self):
        """Test creating a valid ActorDefinition."""
        print("\nTesting Valid ActorDefinition...")
        actor_data = {
            "kind": "actor_definition",
            "id": "act_manager",
            "code": "MANAGER",
            "name": "Manager",
            "actor_type": "role",
            "responsibilities": ["approve_budget", "manage_team"]
        }
        actor = ActorDefinition(**actor_data)
        self.assertEqual(actor.actor_type, "role")
        print("✅ Valid ActorDefinition created successfully")

if __name__ == "__main__":
    unittest.main()
