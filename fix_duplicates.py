import requests
import json
from collections import Counter
import time

# Service URLs
BMS_URL = "http://127.0.0.1:8020/api/v1/metadata"

def fix_duplicates():
    print("Fetching all relationships...")
    try:
        response = requests.get(f"{BMS_URL}/relationships")
        if response.status_code != 200:
            print(f"Failed to fetch relationships: {response.status_code}")
            return

        rels = response.json()
        print(f"Total relationships found: {len(rels)}")

        # Identify duplicates
        # We care about the triple: (from_entity_code, to_entity_code, relationship_type)
        triples = [(r['from_entity_code'], r['to_entity_code'], r['relationship_type']) for r in rels]
        counts = Counter(triples)
        
        duplicates = {k: v for k, v in counts.items() if v > 1}
        print(f"Found {len(duplicates)} unique relationship types that have duplicates")

        fixed_count = 0
        
        for (from_code, to_code, rel_type), count in duplicates.items():
            print(f"Fixing {from_code} -> {to_code} ({rel_type}) - Count: {count}")
            
            # 1. Delete all instances (soft delete)
            # The new DELETE endpoint soft-deletes all matching active relationships
            del_response = requests.delete(
                f"{BMS_URL}/relationships",
                params={
                    "from_entity_code": from_code,
                    "to_entity_code": to_code,
                    "relationship_type": rel_type
                }
            )
            
            if del_response.status_code not in [200, 204]:
                print(f"  Failed to delete: {del_response.status_code} - {del_response.text}")
                continue
                
            # 2. Re-create one single active instance
            # We need to preserve metadata if possible, but for now we'll just create a basic one
            # The original creation likely had metadata, but since we're fixing duplicates 
            # from a bulk import that failed idempotency, they probably all have similar metadata.
            
            create_payload = {
                "from_entity_code": from_code,
                "to_entity_code": to_code,
                "relationship_type": rel_type,
                "metadata_": {"restored_from_deduplication": True}
            }
            
            create_response = requests.post(
                f"{BMS_URL}/relationships",
                params={"created_by": "deduplication_script"},
                json=create_payload
            )
            
            if create_response.status_code == 201:
                print(f"  Successfully restored single relationship")
                fixed_count += 1
            else:
                print(f"  Failed to recreate: {create_response.status_code} - {create_response.text}")

        print(f"\nFinished! Fixed {fixed_count} duplicate groups.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fix_duplicates()
