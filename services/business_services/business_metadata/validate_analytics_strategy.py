import sys
import os
import unittest
from typing import Dict, Any, List
from unittest.mock import MagicMock

# Add the directory ABOVE business_metadata to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import models as package
from business_metadata.ontology_models import (
    AnalyticsStrategyDefinition,
    AnalyticsUseCaseDefinition,
    DataSourceDefinition,
    EntityDefinition,
    MetricDefinition
)

class TestAnalyticsStrategy(unittest.TestCase):
    def test_analytics_strategy_definition(self):
        """Test AnalyticsStrategyDefinition model."""
        print("\nTesting AnalyticsStrategyDefinition...")
        strategy = AnalyticsStrategyDefinition(
            kind="analytics_strategy_definition",
            id="strat_2025",
            code="STRAT_2025",
            name="2025 Data Strategy",
            company_code="ACME",
            analytics_maturity_level="predictive",
            primary_use_cases=["customer_churn", "inventory_opt"]
        )
        self.assertEqual(strategy.analytics_maturity_level, "predictive")
        print("✅ Valid AnalyticsStrategyDefinition created")

    def test_data_source_definition(self):
        """Test DataSourceDefinition model."""
        print("\nTesting DataSourceDefinition...")
        source = DataSourceDefinition(
            kind="data_source_definition",
            id="ds_salesforce",
            code="SALESFORCE_CRM",
            name="Salesforce CRM",
            source_type="transactional",
            source_system="salesforce",
            connection_type="api",
            refresh_frequency="hourly"
        )
        self.assertEqual(source.source_system, "salesforce")
        print("✅ Valid DataSourceDefinition created")

    def test_analytics_use_case_linking(self):
        """Test AnalyticsUseCaseDefinition and linking to entities/metrics."""
        print("\nTesting AnalyticsUseCaseDefinition Linking...")
        
        # 1. Define Entities and Metrics (simulated existence)
        entity_code = "CUSTOMER"
        metric_code = "CHURN_RATE"
        
        # 2. Define Use Case linking to them
        use_case = AnalyticsUseCaseDefinition(
            kind="analytics_use_case_definition",
            id="uc_churn_pred",
            code="CHURN_PREDICTION",
            name="Customer Churn Prediction",
            use_case_type="prediction",
            business_problem="Reduce customer attrition",
            business_owner="act_cmo",
            technical_owner="act_cto",
            maturity_stage="pilot",
            # Linking occurs here via list of codes
            required_entities=[entity_code],
            required_metrics=[metric_code],
            required_data_sources=["SALESFORCE_CRM"]
        )
        
        self.assertIn("CUSTOMER", use_case.required_entities)
        self.assertIn("CHURN_RATE", use_case.required_metrics)
        print(f"✅ Use Case linked to Entity: {use_case.required_entities}")
        print(f"✅ Use Case linked to Metric: {use_case.required_metrics}")

if __name__ == "__main__":
    unittest.main()
