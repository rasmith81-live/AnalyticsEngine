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
from unittest.mock import MagicMock, AsyncMock, patch

# Add parent directory to path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.management import ArchivalManager
from app.config import settings

# Mock the clients before they are imported/used in management.py
sys.modules['app.clients'] = MagicMock()
sys.modules['app.clients'].lakehouse_client = AsyncMock()
sys.modules['app.clients'].messaging_client = AsyncMock()

import pytest

@pytest.mark.asyncio
async def test_data_retrieval():
    """Test the data retrieval functionality with various parameters."""
    
    # Setup mocks
    mock_lakehouse = sys.modules['app.clients'].lakehouse_client
    mock_messaging = sys.modules['app.clients'].messaging_client
    
    # Mock Redis responses
    mock_messaging.get.return_value = None  # Cache miss
    mock_messaging.set.return_value = True
    
    # Mock Lakehouse responses
    mock_lakehouse.path_exists.return_value = True
    mock_lakehouse.list_files.return_value = ["file1.parquet", "file2.parquet"]
    
    # Mock read_data to return a DataFrame-like object (or list of dicts since we mocked it)
    # The management code expects read_data to return a DataFrame
    # and then calls df.to_dict(orient='records')
    # So we need to mock that behavior
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 1, "value": 100, "timestamp": datetime.utcnow().isoformat()},
        {"id": 2, "value": 200, "timestamp": datetime.utcnow().isoformat()}
    ]
    mock_lakehouse.read_data.return_value = mock_df

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
        import traceback
        traceback.print_exc()
    
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
    except ValueError as e:
        print(f"Expected error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error type: {type(e).__name__}: {str(e)}")
    
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
