import unittest
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path to allow importing app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.models import SourceRecord
from app.engine.matching import BatchMatcher
from app.engine.merging import MergeEngine
from app.engine.retroactive_fix import RetroactiveFixEngine

class TestEntityResolution(unittest.TestCase):
    def setUp(self):
        self.matcher = BatchMatcher(threshold=0.8)
        self.merger = MergeEngine()
        self.fix_engine = RetroactiveFixEngine()

    def test_matching_logic(self):
        """Test fuzzy matching and blocking."""
        print("\nTesting Matching Logic...")
        
        records = [
            SourceRecord(
                record_id="rec_1",
                source_system="CRM",
                entity_type="Customer",
                attributes={"name": "John Doe", "email": "john@example.com"}
            ),
            SourceRecord(
                record_id="rec_2",
                source_system="Billing",
                entity_type="Customer",
                attributes={"name": "Jon Doe", "email": "john@example.com"}
            ),
            SourceRecord(
                record_id="rec_3",
                source_system="CRM",
                entity_type="Customer",
                attributes={"name": "Alice Smith", "email": "alice@example.com"}
            )
        ]
        
        matches = self.matcher.find_matches(records)
        
        # rec_1 and rec_2 should match (similar name, same email)
        # rec_3 should not match anyone
        
        match_found = False
        for m in matches:
            print(f"Match found: {m.record_a_id} <-> {m.record_b_id} (Score: {m.score})")
            if (m.record_a_id == "rec_1" and m.record_b_id == "rec_2") or \
               (m.record_a_id == "rec_2" and m.record_b_id == "rec_1"):
                match_found = True
                
        self.assertTrue(match_found, "Failed to match John Doe and Jon Doe")
        print("✅ Matching logic verified")

    def test_merging_survivorship(self):
        """Test Golden Record creation with time-based survivorship."""
        print("\nTesting Merging & Survivorship...")
        
        now = datetime.utcnow()
        yesterday = now - timedelta(days=1)
        
        rec_old = SourceRecord(
            record_id="old_1",
            source_system="Legacy",
            entity_type="Product",
            attributes={"name": "Old Name", "price": 10.0},
            timestamp=yesterday.isoformat()
        )
        
        rec_new = SourceRecord(
            record_id="new_1",
            source_system="Modern",
            entity_type="Product",
            attributes={"name": "New Name"}, # Price missing in new record
            timestamp=now.isoformat()
        )
        
        cluster = [rec_old, rec_new]
        golden = self.merger.create_golden_record(cluster)
        
        # Name should come from rec_new (newer)
        self.assertEqual(golden.attributes["name"], "New Name")
        
        # Price should come from rec_old (missing in new)
        self.assertEqual(golden.attributes["price"], 10.0)
        
        self.assertIn("old_1", golden.source_record_ids)
        self.assertIn("new_1", golden.source_record_ids)
        
        # Verify lineage
        print("Verifying lineage...")
        name_lineage = next(l for l in golden.lineage if l["attribute"] == "name")
        self.assertEqual(name_lineage["source_record_id"], "new_1")
        self.assertEqual(name_lineage["value"], "New Name")
        
        price_lineage = next(l for l in golden.lineage if l["attribute"] == "price")
        self.assertEqual(price_lineage["source_record_id"], "old_1")
        self.assertEqual(price_lineage["value"], 10.0)
        
        print("✅ Merging logic verified")

    def test_retroactive_fix(self):
        """Test impact analysis trigger."""
        print("\nTesting Retroactive Fix...")
        
        results = self.fix_engine.trigger_recalculation(
            golden_record_id="gold_123",
            merged_source_ids=["user_1_crm", "user_1_web"]
        )
        
        # Should find 'kpi_customer_lifetime_value' impacted by 'user_1'
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]["kpi_id"], "kpi_customer_lifetime_value")
        self.assertEqual(results[0]["reason"], "entity_resolution_merge")
        print("✅ Retroactive fix verified")

if __name__ == "__main__":
    unittest.main()
