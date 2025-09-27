"""
API endpoints for News Provider Service.

This module provides the API endpoints for News Provider Service functionality.
"""

import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status, BackgroundTasks
import asyncio
import random
from pydantic import BaseModel, Field

from ..messaging_client import MessagingClient, get_messaging_client
from ..models import DataModel, CommandModel, ResponseModel

# Configure logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

# In-memory state for streaming control
streaming_active = False

async def stream_news(messaging_client: MessagingClient):
    """
    Background task to stream news data.
    """
    global streaming_active
    logger.info("News streaming task started.")
    while streaming_active:
        try:
            # In a real implementation, you would fetch news from a live source.
            # For this example, we'll simulate generating a news article.
            news_article = {
                "source": "MarketNova News",
                "title": "Breaking News: Market Hits All-Time High",
                "content": "The stock market surged today, driven by strong tech earnings. This is a sample article content.",
                "published_at": asyncio.get_event_loop().time(),
                "related_symbols": ["AAPL", "GOOGL"],
                "article_type": "Market News",
                "sentiment": round(random.uniform(-1, 1), 2)
            }
            
            await messaging_client.publish_event(
                event_type="news.streaming.article",
                event_data=news_article
            )
            logger.debug(f"Published news article: {news_article['title']}")
            
            # Simulate a delay between articles
            await asyncio.sleep(5)  # Publish an article every 5 seconds
            
        except Exception as e:
            logger.error(f"Error during news streaming: {e}")
            # Avoid tight loop on continuous errors
            await asyncio.sleep(10)
            
    logger.info("News streaming task stopped.")

@router.get("/status", response_model=Dict[str, Any])
async def get_service_status(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Get the current status of News Provider Service and its dependencies.
    
    Returns:
        Dict: Service status information
    """
    status_info = {
        "service": "news_provider_service",
        "status": "operational",
        "dependencies": {}
    }
    
    # Check messaging connection (primary dependency for event-driven architecture)
    try:
        msg_health = await messaging_client.check_health()
        is_healthy = isinstance(msg_health, dict) and msg_health.get("status") in ["ok", "healthy", "operational"]

        status_info["dependencies"]["messaging"] = {
            "status": "connected" if is_healthy else "error",
            "details": msg_health
        }

        if not is_healthy:
            status_info["status"] = "degraded"
            
    except Exception as e:
        logger.error(f"Error checking messaging connection: {e}")
        status_info["dependencies"]["messaging"] = {
            "status": "error",
            "details": {"error": str(e)}
        }
        status_info["status"] = "degraded"
    
    return status_info

@router.post("/data/request", response_model=Dict[str, Any], status_code=status.HTTP_202_ACCEPTED)
async def request_data(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request data from the service with pagination via messaging.
    
    Args:
        limit: Maximum number of records to return
        offset: Number of records to skip
        messaging_client: Messaging client dependency
        
    Returns:
        Dict: Data request status with request ID for tracking
    """
    try:
        # Publish data request event for database service to process
        request_data = {
            "service": "news_provider_service",
            "operation": "get_data",
            "parameters": {
                "limit": limit,
                "offset": offset
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="data.request.news_provider_service",
            event_data=request_data,
            correlation_id=None
        )
        
        return {
            "status": "accepted",
            "message": "Data request submitted successfully",
            "request_id": message_id,
            "note": "Data will be processed asynchronously. Use request_id to track status."
        }
    except Exception as e:
        logger.error(f"Error requesting data: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to request data: {str(e)}"
        )

@router.post("/command", response_model=Dict[str, Any], status_code=status.HTTP_202_ACCEPTED)
async def execute_command(
    command: CommandModel,
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Execute a command through the messaging system.
    
    Args:
        command: Command model with action and parameters
        messaging_client: Messaging client dependency
        
    Returns:
        Dict: Command execution status
    """
    try:
        # Publish command event for processing
        message_id = await messaging_client.publish_event(
            event_type="command.news_provider_service.execute",
            event_data={
                "command": command.dict(),
                "service": "news_provider_service"
            },
            correlation_id=None
        )
        
        return {
            "status": "accepted",
            "message_id": message_id,
            "command_id": command.command_id
        }
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to execute command: {str(e)}"
        )

@router.post("/stream/start", status_code=status.HTTP_200_OK)
async def start_streaming(
    background_tasks: BackgroundTasks,
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Start the news stream.
    """
    global streaming_active
    if streaming_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Streaming is already active."
        )
    
    streaming_active = True
    background_tasks.add_task(stream_news, messaging_client)
    logger.info("Streaming started by API request.")
    return {"status": "success", "message": "News streaming started."}

@router.post("/stream/stop", status_code=status.HTTP_200_OK)
async def stop_streaming():
    """
    Stop the news stream.
    """
    global streaming_active
    if not streaming_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Streaming is not active."
        )
    
    streaming_active = False
    logger.info("Streaming stopped by API request.")
    return {"status": "success", "message": "News streaming stopped."}

@router.post("/archive/request", status_code=status.HTTP_202_ACCEPTED)
async def request_archive(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request the database service to archive old news data.
    """
    try:
        command_data = {
            "service": "database_service",
            "operation": "archive_news_data",
            "parameters": {
                "age_days": 1
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="command.database_service.archive",
            event_data=command_data
        )
        
        return {
            "status": "accepted",
            "message": "Archive request submitted successfully",
            "request_id": message_id
        }
    except Exception as e:
        logger.error(f"Error requesting archive: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to request archive: {str(e)}"
        )
