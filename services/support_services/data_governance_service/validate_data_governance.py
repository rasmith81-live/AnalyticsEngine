
import asyncio
import sys
import os
import unittest
from datetime import datetime
from typing import Dict, Any, List

# Add parent directory to path to allow importing app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.models import (
    DataQualityRule, ValidationResult, 
    LineageNode, LineageEdge, LineageGraph
)
from app.engine.rules_engine import RulesEngine
from app.engine.lineage_engine import LineageEngine

class TestDataGovernanceService(unittest.TestCase):
    def setUp(self):
        self.rules_engine = RulesEngine()
        self.lineage_engine = LineageEngine()

    def test_rules_engine_validation(self):
        """Test rule validation logic."""
        print("\nTesting Rules Engine...")
        
        # Define a rule
        rule = DataQualityRule(
            id="rule_1",
            name="Non-negative Price",
            description="Price must be >= 0",
            target_attribute="price", # Fixed from field="price"
            target_entity="Product",
            rule_type="range",
            parameters={"min": 0}
        )
        
        # Test valid record
        valid_record = {"id": 1, "price": 10.5, "product": "Widget"}
        results_valid = self.rules_engine.validate_record(valid_record, [rule])
        
        self.assertTrue(all(r.is_valid for r in results_valid))
        print("✅ Valid record check passed")
        
        # Test invalid record
        invalid_record = {"id": 2, "price": -5.0, "product": "BadWidget"}
        results_invalid = self.rules_engine.validate_record(invalid_record, [rule])
        
        self.assertFalse(all(r.is_valid for r in results_invalid))
        self.assertEqual(len(results_invalid), 1)
        self.assertEqual(results_invalid[0].rule_id, "rule_1")
        print("✅ Invalid record check passed")

    def test_lineage_engine(self):
        """Test lineage tracking logic."""
        print("\nTesting Lineage Engine...")
        
        # Create nodes
        source_node = LineageNode(
            id="source_db",
            name="Source Database",
            type="source",  # Changed from 'database'
            metadata={"connection": "sql_server"}
        )
        
        process_node = LineageNode(
            id="etl_job",
            name="Daily ETL",
            type="transformation",  # Changed from 'process'
            metadata={"schedule": "daily"}
        )
        
        target_node = LineageNode(
            id="target_dw",
            name="Data Warehouse",
            type="source",  # Changed from 'database'
            metadata={"schema": "analytics"}
        )
        
        self.lineage_engine.add_node(source_node)
        self.lineage_engine.add_node(process_node)
        self.lineage_engine.add_node(target_node)
        print("✅ Nodes added")
        
        # Create edges
        edge1 = LineageEdge(
            source_id="source_db",
            target_id="etl_job",
            type="data_flow"
        )
        
        edge2 = LineageEdge(
            source_id="etl_job",
            target_id="target_dw",
            type="data_flow"
        )
        
        self.lineage_engine.add_edge(edge1)
        self.lineage_engine.add_edge(edge2)
        print("✅ Edges added")
        
        # Test Downstream Lineage (Source -> Target)
        downstream = self.lineage_engine.get_downstream_lineage("source_db")
        # get_downstream_lineage includes the start node, so source_db, etl_job, target_dw = 3 nodes
        self.assertEqual(len(downstream.nodes), 3) 
        
        node_ids = [n.id for n in downstream.nodes]
        self.assertIn("etl_job", node_ids)
        self.assertIn("target_dw", node_ids)
        print("✅ Downstream lineage verified")
        
        # Test Upstream Lineage (Target -> Source)
        upstream = self.lineage_engine.get_upstream_lineage("target_dw")
        node_ids_up = [n.id for n in upstream.nodes]
        self.assertIn("etl_job", node_ids_up)
        self.assertIn("source_db", node_ids_up)
        print("✅ Upstream lineage verified")

if __name__ == "__main__":
    unittest.main()
