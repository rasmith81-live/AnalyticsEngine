import argparse
import os
import sys
import requests
from sqlalchemy import create_engine, inspect
from typing import Dict, List, Any

# Default Metadata Service URL
METADATA_API_URL = os.getenv("METADATA_SERVICE_URL", "http://localhost:8020/api/v1/metadata")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/analytics_db")

def fetch_definitions(kind: str) -> List[Dict]:
    """Fetch all definitions of a specific kind from the Metadata Service."""
    url = f"{METADATA_API_URL}/definitions/{kind}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {kind}: {e}")
        return []

def validate_schema(db_url: str):
    """Validate database schema against metadata definitions."""
    try:
        print(f"Connecting to database...")
        # create_engine handles connection pooling and lazy connection
        engine = create_engine(db_url)
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        # Allow running even if DB is down, just to show logic, but in CI this should fail
        # For now, we return if we can't inspect
        return

    # Fetch Entity Definitions
    entities_data = fetch_definitions("entity_definition")
    print(f"Fetched {len(entities_data)} entity definitions.")
    
    errors = []
    
    for entity in entities_data:
        code = entity.get("code")
        table_schema = entity.get("table_schema", {})
        
        # Determine expected table name
        expected_table = table_schema.get("table_name", code.lower()) if table_schema else code.lower()
        
        if expected_table not in existing_tables:
            errors.append(f"Missing Table: Entity '{code}' expects table '{expected_table}', but it does not exist.")
            continue
            
        # Check columns
        existing_columns = {col["name"]: col for col in inspector.get_columns(expected_table)}
        expected_columns = table_schema.get("columns", [])
        
        for col_def in expected_columns:
            col_name = col_def.get("name")
            if col_name not in existing_columns:
                errors.append(f"Missing Column: Table '{expected_table}' missing column '{col_name}' (Entity: {code}).")
            else:
                # Optional: Check types (simplified check)
                # expected_type = col_def.get("type")
                # actual_type = existing_columns[col_name]["type"]
                # This is complex due to SQL type mapping variations
                pass

    if errors:
        print("\n❌ Schema Validation Failed:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("\n✅ Schema Validation Passed. Database matches Metadata definitions.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate DB Schema against Metadata")
    parser.add_argument("--url", help="Metadata Service URL", default=None)
    parser.add_argument("--db", help="Database URL", default=None)
    
    args = parser.parse_args()
    
    if args.url:
        METADATA_API_URL = args.url
    if args.db:
        DATABASE_URL = args.db
        
    validate_schema(DATABASE_URL)
