"""Simple script to clear metadata database using requests to the running service."""

import requests

try:
    # First, let's try to add a simple clear endpoint via the API
    # Since the service is running, we'll use a workaround - call the bulk endpoint with empty data
    # Actually, let's just make a direct SQL call through a custom endpoint
    
    # For now, let's just verify we can connect
    response = requests.get("http://localhost:8020/health", timeout=5)
    print(f"Service is running: {response.json()}")
    
    # Try to get current count
    response = requests.get("http://localhost:8020/api/v1/metadata/definitions/metric_definition?limit=1", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"Current KPIs in database: {len(data)} (showing first page)")
    
    print("\nTo clear the database, you need to:")
    print("1. Stop the business_metadata service")
    print("2. Connect to PostgreSQL and run:")
    print("   TRUNCATE TABLE metadata_definitions, metadata_relationships, metadata_versions CASCADE;")
    print("3. Restart the business_metadata service")
    print("\nOr wait for the service to be restarted with the new clear-all endpoint.")
    
except Exception as e:
    print(f"Error: {e}")
