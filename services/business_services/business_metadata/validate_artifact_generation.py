import sys
import os
import unittest
from typing import Dict, Any, List

# Add the directory ABOVE business_metadata to sys.path
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

# Mock SQLAlchemy
mock_sqlalchemy = MagicMock()
sys.modules["sqlalchemy"] = mock_sqlalchemy
sys.modules["sqlalchemy.dialects"] = MagicMock()
sys.modules["sqlalchemy.dialects.postgresql"] = MagicMock()
sys.modules["sqlalchemy.orm"] = MagicMock()
sys.modules["sqlalchemy.ext.asyncio"] = MagicMock()

# Mock definitions module
sys.modules["definitions"] = MagicMock()
sys.modules["definitions.ontology_models"] = MagicMock()

# Mock database_service
sys.modules["database_service"] = MagicMock()
sys.modules["database_service.app"] = MagicMock()
sys.modules["database_service.app.base_models"] = MagicMock()

# Import models as package
from business_metadata.ontology_models import (
    EntityDefinition,
    TableSchemaDefinition,
    ColumnDefinition
)
from business_metadata.services.code_generator import CodeGenerator

class TestArtifactGeneration(unittest.TestCase):
    def test_pydantic_generation(self):
        """Test generating Pydantic model code."""
        print("\nTesting Pydantic Code Generation...")
        
        entity = EntityDefinition(
            kind="entity_definition",
            id="ent_product",
            code="PRODUCT",
            name="Product",
            description="A product definition",
            table_schema=TableSchemaDefinition(
                table_name="products",
                columns=[
                    ColumnDefinition(name="sku", type="string", description="Stock Keeping Unit"),
                    ColumnDefinition(name="price", type="decimal", description="Unit price")
                ]
            )
        )
        
        generator = CodeGenerator()
        code = generator.generate_pydantic_model(entity)
        
        print(f"Generated Code:\n{code}")
        
        self.assertIn("class Product(BaseModel):", code)
        self.assertIn("sku: str = Field", code)
        self.assertIn("price: float = Field", code)
        print("✅ Pydantic code generation correct")

    def test_timescaledb_ddl_generation(self):
        """Test generating TimescaleDB DDL."""
        print("\nTesting TimescaleDB DDL Generation...")
        
        entity = EntityDefinition(
            kind="entity_definition",
            id="ent_sensor",
            code="SENSOR_READING",
            name="SensorReading",
            table_schema=TableSchemaDefinition(
                table_name="sensor_readings",
                columns=[
                    ColumnDefinition(name="temperature", type="decimal"),
                    ColumnDefinition(name="status", type="string")
                ]
            )
        )
        
        generator = CodeGenerator()
        ddl = generator.generate_timescaledb_ddl(entity)
        
        print(f"Generated DDL:\n{ddl}")
        
        self.assertIn("CREATE TABLE IF NOT EXISTS sensor_readings", ddl)
        self.assertIn("temperature NUMERIC", ddl)
        self.assertIn("create_hypertable('sensor_readings'", ddl)
        print("✅ TimescaleDB DDL generation correct")

    def test_kpi_view_ddl_generation(self):
        """Test generating TimescaleDB Continuous Aggregate view DDL for KPIs."""
        print("\nTesting KPI View DDL Generation...")
        
        # Mock a MetricDefinition since we can't easily import it due to circular deps/mocking
        # We'll use a simple object or MagicMock that mimics the structure
        metric = MagicMock()
        metric.code = "REVENUE_DAILY"
        metric.default_aggregation = "sum"
        metric.formula = "Entity.amount"
        metric.dimensions = ["region", "product_category"]
        
        generator = CodeGenerator()
        ddl = generator.generate_kpi_view_ddl(metric, "sales_data")
        
        print(f"Generated View DDL:\n{ddl}")
        
        self.assertIn("CREATE MATERIALIZED VIEW kpi_revenue_daily_daily", ddl)
        self.assertIn("WITH (timescaledb.continuous) AS", ddl)
        self.assertIn("time_bucket('1 day', time)", ddl)
        self.assertIn("SUM(amount) as value", ddl)
        self.assertIn("FROM sales_data", ddl)
        self.assertIn("GROUP BY bucket, region, product_category", ddl)
        self.assertIn("add_continuous_aggregate_policy", ddl)
        print("✅ KPI View DDL generation correct")

if __name__ == "__main__":
    unittest.main()
