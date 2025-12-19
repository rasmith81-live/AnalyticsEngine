
import unittest
import sys
import os
import ast

# Add service dir to path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.engine.sql_generator import SQLGenerator
from app.engine.parser import FormulaParser

class TestApproximateAnalytics(unittest.TestCase):
    
    def setUp(self):
        self.parser = FormulaParser()
        self.generator = SQLGenerator()

    def test_approximate_count_distinct(self):
        """Test approximate count distinct generation (HyperLogLog)."""
        print("\nTesting Approximate Count Distinct...")
        
        formula = "count_distinct(user_id)"
        parsed = self.parser.parse(formula)
        
        # Test Exact
        sql_exact = self.generator.generate_query(parsed, "events", approximate=False)
        self.assertIn("COUNT(DISTINCT user_id)", sql_exact)
        print("✅ Exact mode correct")
        
        # Test Approximate
        sql_approx = self.generator.generate_query(parsed, "events", approximate=True)
        self.assertIn("distinct_count(hyperloglog(user_id))", sql_approx)
        print("✅ Approximate mode correct (HyperLogLog)")

    def test_approximate_percentile(self):
        """Test approximate percentile generation (t-digest)."""
        print("\nTesting Approximate Percentile...")
        
        formula = "percentile(response_time, 0.95)"
        parsed = self.parser.parse(formula)
        
        # Test Exact
        sql_exact = self.generator.generate_query(parsed, "metrics", approximate=False)
        self.assertIn("percentile_cont(0.95) WITHIN GROUP (ORDER BY response_time)", sql_exact)
        print("✅ Exact mode correct")
        
        # Test Approximate
        sql_approx = self.generator.generate_query(parsed, "metrics", approximate=True)
        self.assertIn("approx_percentile(0.95, percentile_agg(response_time))", sql_approx)
        print("✅ Approximate mode correct (t-digest)")

    def test_explicit_approx_distinct(self):
        """Test explicit approx_distinct function."""
        print("\nTesting Explicit Approx Distinct...")
        
        formula = "approx_distinct(session_id)"
        parsed = self.parser.parse(formula)
        
        # Should generate approx SQL regardless of mode setting, 
        # but our implementation relies on the flag for standard functions.
        # For explicit 'approx_distinct', it maps to approx SQL always.
        
        sql = self.generator.generate_query(parsed, "sessions", approximate=False)
        self.assertIn("distinct_count(hyperloglog(session_id))", sql)
        print("✅ Explicit function correct")

if __name__ == "__main__":
    unittest.main()
