import sys
import os
import unittest
from typing import Dict, Any, List

# Add the directory ABOVE business_metadata to sys.path
# This allows us to import business_metadata as a package
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Mock missing dependencies to avoid ImportErrors from transitive imports
from unittest.mock import MagicMock
sys.modules["opentelemetry"] = MagicMock()
sys.modules["opentelemetry.instrumentation"] = MagicMock()
sys.modules["opentelemetry.instrumentation.httpx"] = MagicMock()
sys.modules["messaging_service"] = MagicMock()
sys.modules["messaging_service.app"] = MagicMock()
sys.modules["messaging_service.app.event_publisher"] = MagicMock()

# Mock database_service to avoid importing base_models (which imports sqlalchemy)
sys.modules["database_service"] = MagicMock()
sys.modules["database_service.app"] = MagicMock()
sys.modules["database_service.app.base_models"] = MagicMock()

# Mock SQLAlchemy to avoid DB driver issues
mock_sqlalchemy = MagicMock()
sys.modules["sqlalchemy"] = mock_sqlalchemy
sys.modules["sqlalchemy.dialects"] = MagicMock()
sys.modules["sqlalchemy.dialects.postgresql"] = MagicMock()
sys.modules["sqlalchemy.orm"] = MagicMock()
sys.modules["sqlalchemy.ext.asyncio"] = MagicMock()

# Mock definitions module (used by metadata_service.py)
sys.modules["definitions"] = MagicMock()
sys.modules["definitions.ontology_models"] = MagicMock()

# Import models as package
from business_metadata.ontology_models import (
    ClientDefinition,
    RoleDefinition,
    PermissionDefinition,
    RowLevelSecurityDefinition,
    DataQualityRuleDefinition,
    MetricPermissionDefinition
)
from business_metadata.services.rls_service import RowLevelSecurityService

class TestAccessControl(unittest.TestCase):
    def test_client_definition(self):
        """Test ClientDefinition model."""
        print("\nTesting ClientDefinition...")
        client = ClientDefinition(
            kind="client_definition",
            id="cli_acme",
            code="ACME_CORP",
            name="Acme Corp",
            contact_email="admin@acme.com",
            country_code="US"
        )
        self.assertEqual(client.code, "ACME_CORP")
        print("✅ Valid ClientDefinition created")

    def test_role_definition(self):
        """Test RoleDefinition model."""
        print("\nTesting RoleDefinition...")
        role = RoleDefinition(
            kind="role_definition",
            id="role_analyst",
            code="ANALYST",
            name="Data Analyst",
            actor_type="role",
            client_code="ACME_CORP",
            permissions={"can_view_dashboard": True}
        )
        self.assertEqual(role.client_code, "ACME_CORP")
        print("✅ Valid RoleDefinition created")

    def test_data_quality_rule(self):
        """Test DataQualityRuleDefinition model."""
        print("\nTesting DataQualityRuleDefinition...")
        rule = DataQualityRuleDefinition(
            kind="data_quality_rule_definition",
            id="dq_null_check",
            code="DQ_REV_NOT_NULL",
            name="Revenue Not Null",
            rule_type="completeness",
            target_entity="REVENUE",
            target_attributes=["amount"],
            rule_expression="amount IS NOT NULL",
            severity="high",
            check_frequency="daily"
        )
        self.assertEqual(rule.severity, "high")
        print("✅ Valid DataQualityRuleDefinition created")

    def test_rls_sql_generation_equality(self):
        """Test RLS SQL generation for simple equality."""
        print("\nTesting RLS SQL Generation (Equality)...")
        service = RowLevelSecurityService()
        
        rls_def = RowLevelSecurityDefinition(
            kind="row_level_security_definition",
            id="rls_us_only",
            code="RLS_US",
            name="US Only",
            role_code="ANALYST",
            entity_code="SALES",
            attribute_filters={"region": {"eq": "US"}},
            filter_logic="AND"
        )
        
        sql = service.generate_sql_filter(rls_def)
        print(f"   Generated SQL: {sql}")
        self.assertEqual(sql, "region = 'US'")
        print("✅ SQL generation correct")

    def test_rls_sql_generation_complex(self):
        """Test RLS SQL generation for complex logic."""
        print("\nTesting RLS SQL Generation (Complex)...")
        service = RowLevelSecurityService()
        
        rls_def = RowLevelSecurityDefinition(
            kind="row_level_security_definition",
            id="rls_complex",
            code="RLS_COMPLEX",
            name="Complex Rule",
            role_code="MANAGER",
            entity_code="SALES",
            attribute_filters={
                "region": {"in": ["US", "CA"]},
                "amount": {"gt": 1000},
                "category": {"startswith": "TECH"}
            },
            filter_logic="AND"
        )
        
        sql = service.generate_sql_filter(rls_def)
        print(f"   Generated SQL: {sql}")
        
        # Order of dict items is insertion order in Python 3.7+, so this should be deterministic
        expected_parts = [
            "region IN ('US', 'CA')",
            "amount > 1000",
            "category LIKE 'TECH%'"
        ]
        for part in expected_parts:
            self.assertIn(part, sql)
        
        print("✅ Complex SQL generation correct")

if __name__ == "__main__":
    unittest.main()
