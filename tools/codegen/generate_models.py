import argparse
import requests
import os
import sys
import json
from typing import List, Dict, Any
from unittest.mock import MagicMock

# Add project root to sys.path to import business_metadata modules
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, project_root)

# Mock heavy dependencies to avoid importing the entire backend application
# when we just need the CodeGenerator and Models.
sys.modules["opentelemetry"] = MagicMock()
sys.modules["opentelemetry.trace"] = MagicMock()
sys.modules["opentelemetry.instrumentation"] = MagicMock()
sys.modules["opentelemetry.instrumentation.fastapi"] = MagicMock()
sys.modules["opentelemetry.instrumentation.httpx"] = MagicMock()
sys.modules["messaging_service"] = MagicMock()
sys.modules["messaging_service.app"] = MagicMock()
sys.modules["messaging_service.app.event_publisher"] = MagicMock()

try:
    # We try to import directly from the file to avoid package initialization if possible,
    # but since it uses relative imports, we might still trigger package init.
    # The mocks above should handle the side effects of package init.
    from services.business_services.business_metadata.services.code_generator import CodeGenerator
    from services.business_services.business_metadata.ontology_models import EntityDefinition, MetricDefinition
except ImportError as e:
    # Fallback if running from a different context or if paths are slightly different
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
    from services.business_services.business_metadata.services.code_generator import CodeGenerator
    from services.business_services.business_metadata.ontology_models import EntityDefinition, MetricDefinition

# Default Metadata Service URL
METADATA_API_URL = os.getenv("METADATA_SERVICE_URL", "http://localhost:8020/api/v1/metadata")

def fetch_definitions(kind: str) -> List[Dict]:
    """Fetch all definitions of a specific kind from the Metadata Service."""
    url = f"{METADATA_API_URL}/definitions/{kind}"
    try:
        print(f"Fetching {kind} from {url}...")
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Endpoint not found: {url}")
            return []
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {kind}: {e}")
        # Return empty list if service is down to allow tool to run in offline/test mode if needed
        return []

def generate_models(output_dir: str):
    """Generate Pydantic models and SQL DDL from fetched definitions."""
    generator = CodeGenerator()
    
    # 1. Fetch Entities
    entities_data = fetch_definitions("entity_definition")
    
    pydantic_models = []
    timescale_ddls = []
    entity_table_map = {}
    
    print(f"Found {len(entities_data)} entities.")
    
    for data in entities_data:
        try:
            # Reconstruct EntityDefinition object
            # The API returns serialized data (dict), pydantic validates it
            entity = EntityDefinition(**data)
            
            # Determine table name
            table_name = entity.code.lower()
            if entity.table_schema and entity.table_schema.table_name:
                table_name = entity.table_schema.table_name
            
            entity_table_map[entity.code] = table_name
            
            # Generate Pydantic Model
            pydantic_code = generator.generate_pydantic_model(entity)
            pydantic_models.append(pydantic_code)
            
            # Generate TimescaleDB DDL
            ddl = generator.generate_timescaledb_ddl(entity)
            timescale_ddls.append(ddl)
            
        except Exception as e:
            print(f"Skipping entity {data.get('code')}: {e}")

    # 2. Write Pydantic Models
    models_file = os.path.join(output_dir, "generated_models.py")
    with open(models_file, "w") as f:
        f.write("# Auto-generated Pydantic Models\n")
        f.write(f"# Generated from {METADATA_API_URL}\n\n")
        f.write("from pydantic import BaseModel, Field\n")
        f.write("from typing import Optional, Any\n")
        f.write("from datetime import datetime\n\n")
        if pydantic_models:
            f.write("\n\n".join(pydantic_models))
        else:
            f.write("# No entity definitions found.\n")
    print(f"Wrote models to {models_file}")

    # 3. Write DDLs
    ddl_file = os.path.join(output_dir, "schema.sql")
    with open(ddl_file, "w") as f:
        f.write("-- Auto-generated TimescaleDB Schema\n")
        f.write(f"-- Generated from {METADATA_API_URL}\n\n")
        if timescale_ddls:
            f.write("\n\n".join(timescale_ddls))
        else:
            f.write("-- No entity definitions found for DDL generation.\n")
    print(f"Wrote DDL to {ddl_file}")
    
    # 4. Fetch Metrics for KPI Views
    metrics_data = fetch_definitions("metric_definition")
    kpi_views = []
    
    print(f"Found {len(metrics_data)} metrics.")
    
    for data in metrics_data:
        try:
            metric = MetricDefinition(**data)
            
            # Resolve source table from formula (Entity.Attribute)
            source_table = "analytics_data" # Default fallback
            if metric.formula and "." in metric.formula:
                entity_code = metric.formula.split(".")[0]
                # Look up table name from entity code (case-insensitive check might be needed)
                # entity_table_map keys are original codes.
                if entity_code in entity_table_map:
                    source_table = entity_table_map[entity_code]
                else:
                     # Try case-insensitive matching if direct lookup fails
                    for code, table in entity_table_map.items():
                        if code.lower() == entity_code.lower():
                            source_table = table
                            break

            view_ddl = generator.generate_kpi_view_ddl(metric, source_table)
            kpi_views.append(view_ddl)
        except Exception as e:
            print(f"Skipping metric {data.get('code')}: {e}")
            
    # Append KPI Views to DDL
    with open(ddl_file, "a") as f:
        f.write("\n\n-- KPI Continuous Aggregates\n\n")
        if kpi_views:
            f.write("\n\n".join(kpi_views))
        else:
            f.write("-- No metrics found for KPI views.\n")
    print(f"Appended KPI views to {ddl_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate code from Metadata Definitions")
    parser.add_argument("--output", "-o", default="./generated", help="Output directory")
    parser.add_argument("--url", help="Metadata Service URL", default=None)
    
    args = parser.parse_args()
    
    if args.url:
        METADATA_API_URL = args.url
        
    os.makedirs(args.output, exist_ok=True)
    generate_models(args.output)
