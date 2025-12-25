import requests
import json
from collections import Counter

def check_duplicates():
    try:
        # Check Relationships
        print("Checking Relationships...")
        response = requests.get("http://127.0.0.1:8090/api/v1/metadata/relationships")
        if response.status_code == 200:
            rels = response.json()
            print(f"Total relationships: {len(rels)}")
            
            pairs = [f"{r['from_entity_code']} -> {r['to_entity_code']} ({r['relationship_type']})" for r in rels]
            counts = Counter(pairs)
            duplicates = {k: v for k, v in counts.items() if v > 1}
            
            print(f"Duplicate relationship pairs found: {len(duplicates)}")
            if duplicates:
                print("Examples of duplicates:")
                for k, v in list(duplicates.items())[:10]:
                    print(f"  {k}: {v} times")
        else:
            print(f"Failed to fetch relationships: {response.status_code}")

        # Check KPI Definitions
        print("\nChecking KPI Definitions...")
        response = requests.get("http://127.0.0.1:8090/api/v1/metadata/definitions/metric_definition")
        if response.status_code == 200:
            kpis = response.json()
            print(f"Total KPIs: {len(kpis)}")
            
            codes = [k['code'] for k in kpis]
            code_counts = Counter(codes)
            dup_kpis = {k: v for k, v in code_counts.items() if v > 1}
            
            print(f"Duplicate KPI codes found: {len(dup_kpis)}")
            if dup_kpis:
                print("Examples of duplicates:")
                for k, v in list(dup_kpis.items())[:10]:
                    print(f"  {k}: {v} times")
        else:
            print(f"Failed to fetch KPIs: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_duplicates()
