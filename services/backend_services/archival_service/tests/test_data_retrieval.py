"""
Test script for the archival data retrieval functionality.

This script tests the retrieve_archived_data method in the ArchivalManager class,
focusing on the cost optimization features and column filtering capabilities.
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timedelta

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.management import ArchivalManager
from app.lakehouse_client import LakehouseClient
from app.config import settings


async def test_data_retrieval():
    """Test the data retrieval functionality with various parameters."""
    # Create an instance of ArchivalManager
    archival_manager = ArchivalManager()
    
    # Test parameters
    table_name = "sensor_data"  # Replace with an actual table name in your archive
    now = datetime.utcnow()
    end_time = now.isoformat()
    start_time = (now - timedelta(days=7)).isoformat()
    
    print(f"\n{'='*80}")
    print(f"TESTING ARCHIVAL DATA RETRIEVAL")
    print(f"{'='*80}")
    
    # Test 1: Basic retrieval with cost optimization (default)
    print(f"\n[TEST 1] Basic retrieval with cost optimization")
    print(f"Retrieving data for table '{table_name}' from {start_time} to {end_time}")
    try:
        result = await archival_manager.retrieve_archived_data(
            table_name=table_name,
            start_time=start_time,
            end_time=end_time,
            limit=10,
            offset=0
        )
        print(f"Success! Retrieved {len(result.get('data', []))} records")
        print(f"Metadata: {json.dumps(result.get('metadata', {}), indent=2)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test 2: Metadata-only retrieval (lowest cost)
    print(f"\n[TEST 2] Metadata-only retrieval (lowest cost)")
    print(f"Retrieving metadata for table '{table_name}' from {start_time} to {end_time}")
    try:
        result = await archival_manager.retrieve_archived_data(
            table_name=table_name,
            start_time=start_time,
            end_time=end_time,
            limit=0,  # Metadata only
            offset=0
        )
        print(f"Success! Retrieved metadata only")
        print(f"Metadata: {json.dumps(result.get('metadata', {}), indent=2)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test 3: Column filtering
    print(f"\n[TEST 3] Column filtering")
    print(f"Retrieving specific columns for table '{table_name}' from {start_time} to {end_time}")
    try:
        # Replace with actual column names from your data
        columns = ["timestamp", "value", "device_id"]
        result = await archival_manager.retrieve_archived_data(
            table_name=table_name,
            start_time=start_time,
            end_time=end_time,
            limit=10,
            offset=0,
            columns=columns
        )
        print(f"Success! Retrieved {len(result.get('data', []))} records with columns: {columns}")
        if result.get('data'):
            print(f"Sample record: {json.dumps(result['data'][0], indent=2)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test 4: Performance mode (optimize_cost=False)
    print(f"\n[TEST 4] Performance mode (optimize_cost=False)")
    print(f"Retrieving data with performance optimization for table '{table_name}' from {start_time} to {end_time}")
    try:
        result = await archival_manager.retrieve_archived_data(
            table_name=table_name,
            start_time=start_time,
            end_time=end_time,
            limit=10,
            offset=0,
            optimize_cost=False
        )
        print(f"Success! Retrieved {len(result.get('data', []))} records in performance mode")
        print(f"Metadata: {json.dumps(result.get('metadata', {}), indent=2)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test 5: Test with a larger time range (should fail in cost-optimized mode)
    print(f"\n[TEST 5] Large time range in cost-optimized mode")
    large_start_time = (now - timedelta(days=60)).isoformat()
    print(f"Retrieving data with large time range for table '{table_name}' from {large_start_time} to {end_time}")
    try:
        result = await archival_manager.retrieve_archived_data(
            table_name=table_name,
            start_time=large_start_time,
            end_time=end_time,
            limit=10,
            offset=0
        )
        print(f"Unexpected success! Retrieved {len(result.get('data', []))} records")
    except Exception as e:
        print(f"Expected error: {str(e)}")
    
    # Test 6: Test with a larger time range in performance mode (should succeed)
    print(f"\n[TEST 6] Large time range in performance mode")
    print(f"Retrieving data with large time range in performance mode for table '{table_name}' from {large_start_time} to {end_time}")
    try:
        result = await archival_manager.retrieve_archived_data(
            table_name=table_name,
            start_time=large_start_time,
            end_time=end_time,
            limit=10,
            offset=0,
            optimize_cost=False
        )
        print(f"Success! Retrieved {len(result.get('data', []))} records in performance mode with large time range")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print(f"\n{'='*80}")
    print(f"TESTING COMPLETE")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    asyncio.run(test_data_retrieval())
