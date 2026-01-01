"""
List all objects in the ontology database and verify relationship structure.
"""

import asyncio
import httpx
import json

METADATA_SERVICE_URL = "http://127.0.0.1:8020"

DEFINITION_KINDS = [
    "value_chain_pattern_definition",
    "business_process_definition", 
    "entity_definition",
    "metric_definition",
    "relationship_definition",
    "actor_definition",
    "beneficiary_definition",
    "strategic_objective_definition",
    "benchmark_definition",
]


async def list_ontology():
    """List all objects in the ontology."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        print("=" * 70)
        print("ONTOLOGY MODEL - CURRENT STATE")
        print("=" * 70)
        
        total_objects = 0
        all_objects = {}
        
        for kind in DEFINITION_KINDS:
            try:
                response = await client.get(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/{kind}",
                    params={"limit": 100}
                )
                if response.status_code == 200:
                    objects = response.json()
                    count = len(objects)
                    total_objects += count
                    all_objects[kind] = objects
                    
                    if count > 0:
                        print(f"\n📦 {kind}: {count} objects")
                        for obj in objects:
                            code = obj.get("code", "N/A")
                            name = obj.get("name", "N/A")
                            print(f"   • {code}: {name}")
            except Exception as e:
                print(f"   ❌ Error fetching {kind}: {e}")
        
        print(f"\n{'=' * 70}")
        print(f"TOTAL OBJECTS: {total_objects}")
        print("=" * 70)
        
        # Check relationships table
        print("\n📊 RELATIONSHIPS (from metadata_relationships table):")
        try:
            response = await client.get(
                f"{METADATA_SERVICE_URL}/api/v1/metadata/relationships",
                params={"limit": 100}
            )
            if response.status_code == 200:
                relationships = response.json()
                print(f"   Total relationships: {len(relationships)}")
                for rel in relationships[:20]:
                    from_code = rel.get("from_entity_code", "?")
                    to_code = rel.get("to_entity_code", "?")
                    rel_type = rel.get("relationship_type", "?")
                    print(f"   • {from_code} --[{rel_type}]--> {to_code}")
            else:
                print(f"   Status: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Check for embedded relationship fields on node objects
        print("\n🔍 CHECKING FOR EMBEDDED RELATIONSHIP FIELDS ON NODES:")
        relationship_fields = [
            "relationships", "related_to", "belongs_to", "has_many",
            "parent", "children", "linked_entities", "associated_with"
        ]
        
        issues_found = []
        for kind, objects in all_objects.items():
            if kind == "relationship_definition":
                continue
            for obj in objects:
                for field in relationship_fields:
                    if field in obj and obj[field]:
                        issues_found.append({
                            "kind": kind,
                            "code": obj.get("code"),
                            "field": field,
                            "value": obj[field]
                        })
        
        if issues_found:
            print("   ⚠️  ISSUES FOUND - Embedded relationship fields:")
            for issue in issues_found:
                print(f"      • {issue['kind']}/{issue['code']}: {issue['field']} = {issue['value']}")
        else:
            print("   ✅ No embedded relationship fields found on node objects")
        
        # Check value_chain field on business_process_definition
        print("\n🔍 CHECKING value_chain FIELD ON BUSINESS PROCESSES:")
        bp_objects = all_objects.get("business_process_definition", [])
        if bp_objects:
            for bp in bp_objects:
                vc = bp.get("value_chain")
                if vc:
                    print(f"   ⚠️  {bp.get('code')}: value_chain = '{vc}' (embedded, should be relationship)")
        else:
            print("   No business processes found")
        
        print("\n" + "=" * 70)
        print("ANALYSIS COMPLETE")
        print("=" * 70)


if __name__ == "__main__":
    asyncio.run(list_ontology())
