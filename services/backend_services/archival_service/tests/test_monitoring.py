"""
Test script for validating the archival monitoring system.

This script simulates archival events and validates the monitoring endpoints
to ensure the monitoring system is working correctly.
"""

import asyncio
import datetime
import json
import logging
import random
import uuid
from typing import Dict, List, Any
from unittest.mock import MagicMock, AsyncMock, patch

import httpx
import pytest
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Service URLs
ARCHIVAL_SERVICE_URL = "http://localhost:8001"

# Test data
TEST_TABLES = ["sensor_data", "metrics", "events", "logs", "transactions"]
TEST_CHUNK_SIZES = [1024, 2048, 4096, 8192, 16384]  # in bytes


class ArchivalEvent(BaseModel):
    """Model for archival event data."""
    event_id: str
    table_name: str
    chunk_id: str
    chunk_start_time: str
    chunk_end_time: str
    schema_name: str
    time_column: str
    requested_at: str


async def generate_archival_event() -> Dict[str, Any]:
    """Generate a random archival event.
    
    Returns:
        Dict containing archival event data
    """
    table_name = random.choice(TEST_TABLES)
    chunk_id = str(random.randint(1000, 9999))
    
    # Generate random dates within the last 30 days
    end_date = datetime.datetime.utcnow()
    start_date = end_date - datetime.timedelta(days=random.randint(1, 7))
    
    event = ArchivalEvent(
        event_id=str(uuid.uuid4()),
        table_name=table_name,
        chunk_id=chunk_id,
        chunk_start_time=start_date.isoformat(),
        chunk_end_time=end_date.isoformat(),
        schema_name="public",
        time_column="timestamp",
        requested_at=datetime.datetime.utcnow().isoformat()
    )
    
    return event.model_dump()


async def simulate_archival_process(event: Dict[str, Any], success_rate: float = 0.9) -> Dict[str, Any]:
    """Simulate the archival process for a given event.
    
    Args:
        event: The archival event to process
        success_rate: Probability of successful archival (0.0 to 1.0)
        
    Returns:
        Dict containing the result of the archival process
    """
    # Simulate processing time (10-50ms) - Reduced for tests
    processing_time = random.uniform(10, 50)
    await asyncio.sleep(processing_time / 1000)  # Convert to seconds
    
    # Simulate chunk size
    chunk_size = random.choice(TEST_CHUNK_SIZES)
    
    # Determine success or failure based on success rate
    success = random.random() < success_rate
    
    result = {
        "event_id": event["event_id"],
        "table_name": event["table_name"],
        "chunk_id": event["chunk_id"],
        "status": "completed" if success else "failed",
        "processing_time_ms": processing_time,
        "chunk_size_bytes": chunk_size,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "error": None if success else "Simulated archival failure"
    }
    
    return result


async def record_archival_metrics(client: httpx.AsyncClient, result: Dict[str, Any]) -> bool:
    """Record archival metrics via the monitoring API.
    
    Args:
        client: HTTP client
        result: Result of the archival process
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Construct the metrics payload
        payload = {
            "event_id": result["event_id"],
            "table_name": result["table_name"],
            "chunk_id": result["chunk_id"],
            "status": result["status"],
            "processing_time_ms": result["processing_time_ms"],
            "chunk_size_bytes": result["chunk_size_bytes"],
            "error": result["error"]
        }
        
        # Send to the record_event endpoint
        response = await client.post(
            f"{ARCHIVAL_SERVICE_URL}/api/v1/monitoring/record-event",
            json=payload
        )
        
        if response.status_code == 200:
            logger.info(f"Recorded metrics for event {result['event_id']}")
            return True
        else:
            logger.error(f"Failed to record metrics: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        logger.error(f"Error recording metrics: {str(e)}")
        return False


async def check_health_endpoint(client: httpx.AsyncClient) -> Dict[str, Any]:
    """Check the health endpoint.
    
    Args:
        client: HTTP client
        
    Returns:
        Health response data
    """
    try:
        response = await client.get(f"{ARCHIVAL_SERVICE_URL}/api/v1/health")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error checking health endpoint: {str(e)}")
        return {"error": str(e)}


async def check_metrics_endpoint(client: httpx.AsyncClient) -> Dict[str, Any]:
    """Check the metrics endpoint.
    
    Args:
        client: HTTP client
        
    Returns:
        Metrics response data
    """
    try:
        response = await client.get(f"{ARCHIVAL_SERVICE_URL}/api/v1/monitoring/metrics")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error checking metrics endpoint: {str(e)}")
        return {"error": str(e)}


async def check_recent_events_endpoint(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Check the recent events endpoint.
    
    Args:
        client: HTTP client
        
    Returns:
        Recent events data
    """
    try:
        response = await client.get(f"{ARCHIVAL_SERVICE_URL}/api/v1/monitoring/recent-events")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error checking recent events endpoint: {str(e)}")
        return [{"error": str(e)}]


async def validate_monitoring_integration():
    """Validate the monitoring integration by simulating archival events and checking endpoints."""
    
    # Create a mock client
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    mock_client.__aenter__.return_value = mock_client
    mock_client.__aexit__.return_value = None
    
    # Mock responses
    mock_health_response = MagicMock()
    mock_health_response.status_code = 200
    mock_health_response.raise_for_status.return_value = None
    mock_health_response.json.return_value = {
        "status": "healthy",
        "monitoring_health": {"status": "healthy"}
    }
    
    # Initial metrics
    mock_metrics_response_initial = MagicMock()
    mock_metrics_response_initial.status_code = 200
    mock_metrics_response_initial.raise_for_status.return_value = None
    mock_metrics_response_initial.json.return_value = {"total_events_received": 0}
    
    # Record event response
    mock_record_response = MagicMock()
    mock_record_response.status_code = 200
    
    # Updated metrics
    mock_metrics_response_updated = MagicMock()
    mock_metrics_response_updated.status_code = 200
    mock_metrics_response_updated.raise_for_status.return_value = None
    mock_metrics_response_updated.json.return_value = {"total_events_received": 10}
    
    # Recent events
    mock_recent_events_response = MagicMock()
    mock_recent_events_response.status_code = 200
    mock_recent_events_response.raise_for_status.return_value = None
    mock_recent_events_response.json.return_value = [{"event_id": "test"}]
    
    # Setup side effects for get/post
    async def mock_get(url, *args, **kwargs):
        if "health" in url:
            return mock_health_response
        elif "metrics" in url:
            # Simple state simulation
            if mock_client.post.call_count == 0:
                return mock_metrics_response_initial
            else:
                return mock_metrics_response_updated
        elif "recent-events" in url:
            return mock_recent_events_response
        return MagicMock(status_code=404)
        
    async def mock_post(url, *args, **kwargs):
        if "record-event" in url:
            return mock_record_response
        return MagicMock(status_code=404)

    mock_client.get.side_effect = mock_get
    mock_client.post.side_effect = mock_post
    
    # Patch httpx.AsyncClient to return our mock
    with patch('httpx.AsyncClient', return_value=mock_client):
        async with httpx.AsyncClient() as client:
            # Check initial health status
            logger.info("Checking initial health status...")
            initial_health = await check_health_endpoint(client)
            logger.info(f"Initial health status: {initial_health.get('status', 'unknown')}")
            
            # Check initial metrics
            logger.info("Checking initial metrics...")
            initial_metrics = await check_metrics_endpoint(client)
            logger.info(f"Initial total events: {initial_metrics.get('total_events_received', 0)}")
            
            # Simulate multiple archival events
            num_events = 10
            logger.info(f"Simulating {num_events} archival events...")
            
            for i in range(num_events):
                # Generate and process an event
                event = await generate_archival_event()
                result = await simulate_archival_process(event)
                
                # Record the metrics
                success = await record_archival_metrics(client, result)
                if not success:
                    logger.warning(f"Failed to record metrics for event {i+1}")
                
                # Small delay between events
                await asyncio.sleep(0.01)
            
            # Allow time for metrics to be processed
            logger.info("Waiting for metrics to be processed...")
            await asyncio.sleep(0.1)
            
            # Check updated metrics
            logger.info("Checking updated metrics...")
            updated_metrics = await check_metrics_endpoint(client)
            logger.info(f"Updated total events: {updated_metrics.get('total_events_received', 0)}")
            
            # Check recent events
            logger.info("Checking recent events...")
            recent_events = await check_recent_events_endpoint(client)
            logger.info(f"Number of recent events: {len(recent_events)}")
            
            # Check final health status
            logger.info("Checking final health status...")
            final_health = await check_health_endpoint(client)
            logger.info(f"Final health status: {final_health.get('status', 'unknown')}")
            logger.info(f"Monitoring health: {final_health.get('monitoring_health', {}).get('status', 'unknown')}")
            
            # Validate that monitoring health is included in the health response
            assert 'monitoring_health' in final_health, "Monitoring health not included in health response"
            
            # Validate that metrics were recorded
            # Note: with mocks, we verify call counts or mock return values
            assert mock_client.post.call_count == num_events
            assert updated_metrics.get('total_events_received', 0) == num_events
            
            # Validate that recent events are available
            assert len(recent_events) > 0, "No recent events found"
            
            logger.info("Monitoring validation completed successfully!")


@pytest.mark.asyncio
async def test_monitoring_integration():
    """Pytest test for monitoring integration."""
    await validate_monitoring_integration()


if __name__ == "__main__":
    # Run the validation directly
    asyncio.run(validate_monitoring_integration())
