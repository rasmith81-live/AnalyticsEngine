"""
Script to remove relationship data from entity metadata fields.
Relationships should ONLY be stored in the metadata_relationships table.

This script removes the following fields from metadata_:
- value_chain (on modules)
- kpis (on modules)
- module (on KPIs/entities)
- modules (on KPIs/entities)
"""

import asyncio
import httpx
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use direct business_metadata service port (8020) instead of API gateway (8090)
# API gateway may not route PUT requests correctly
BASE_URL = "http://127.0.0.1:8020/api/v1/metadata"

# Fields to remove from metadata_
RELATIONSHIP_FIELDS = ["value_chain", "kpis", "module", "modules", "object_models"]


async def clean_definition_metadata(kind: str):
    """Clean relationship fields from metadata_ for a specific definition kind."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        # Fetch all definitions of this kind
        response = await client.get(f"{BASE_URL}/definitions/{kind}", params={"limit": 1000})
        response.raise_for_status()
        definitions = response.json()
        
        cleaned_count = 0
        
        for defn in definitions:
            code = defn.get("code")
            metadata = defn.get("metadata_") or {}
            
            # Check if any relationship fields exist
            fields_to_remove = [f for f in RELATIONSHIP_FIELDS if f in metadata]
            
            if fields_to_remove:
                logger.info(f"Cleaning {kind}/{code}: removing {fields_to_remove}")
                
                # Create cleaned metadata
                cleaned_metadata = {k: v for k, v in metadata.items() if k not in RELATIONSHIP_FIELDS}
                
                # Update the definition with cleaned metadata
                update_data = {
                    "kind": defn.get("kind"),
                    "code": code,
                    "name": defn.get("name"),
                    "description": defn.get("description"),
                    "metadata_": cleaned_metadata
                }
                
                # Add kind-specific fields
                if kind == "business_process_definition":
                    update_data["process_type"] = defn.get("process_type", "support")
                elif kind == "value_chain_pattern_definition":
                    update_data["domain"] = defn.get("domain", "industry")
                
                try:
                    put_response = await client.put(
                        f"{BASE_URL}/definitions/{kind}/{code}",
                        json=update_data,
                        params={"changed_by": "cleanup_script"}
                    )
                    put_response.raise_for_status()
                    cleaned_count += 1
                except Exception as e:
                    logger.error(f"Failed to update {kind}/{code}: {e}")
        
        return cleaned_count


async def main():
    """Clean relationship data from all entity metadata fields."""
    print("=" * 60)
    print("CLEANING RELATIONSHIP DATA FROM ENTITY METADATA FIELDS")
    print("=" * 60)
    print()
    print("Relationship data should ONLY be in metadata_relationships table.")
    print(f"Removing fields: {RELATIONSHIP_FIELDS}")
    print()
    
    total_cleaned = 0
    
    # Clean modules (business_process_definition)
    print("Cleaning modules (business_process_definition)...")
    count = await clean_definition_metadata("business_process_definition")
    print(f"  Cleaned {count} modules")
    total_cleaned += count
    
    # Clean value chains (value_chain_pattern_definition)
    print("Cleaning value chains (value_chain_pattern_definition)...")
    count = await clean_definition_metadata("value_chain_pattern_definition")
    print(f"  Cleaned {count} value chains")
    total_cleaned += count
    
    # Clean KPIs (kpi_definition)
    print("Cleaning KPIs (kpi_definition)...")
    count = await clean_definition_metadata("kpi_definition")
    print(f"  Cleaned {count} KPIs")
    total_cleaned += count
    
    # Clean entities (entity_definition)
    print("Cleaning entities (entity_definition)...")
    count = await clean_definition_metadata("entity_definition")
    print(f"  Cleaned {count} entities")
    total_cleaned += count
    
    print()
    print("=" * 60)
    print(f"TOTAL CLEANED: {total_cleaned} definitions")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
