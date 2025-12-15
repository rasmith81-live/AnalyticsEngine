
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
from datetime import datetime

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.telemetry_consumers import TelemetryEventConsumer
from app.news_consumer import NewsConsumer
from app.market_data_consumer import MarketDataConsumer
from app.database_manager import DatabaseManager
from app.messaging_client import MessagingClient

@pytest.fixture
def mock_db_manager():
    return MagicMock(spec=DatabaseManager)

@pytest.fixture
def mock_messaging_client():
    return AsyncMock(spec=MessagingClient)

@pytest.mark.asyncio
async def test_telemetry_consumer_dependency_ingestion(mock_db_manager, mock_messaging_client):
    consumer = TelemetryEventConsumer(mock_db_manager, mock_messaging_client)
    
    event_data = {
        "dependency": {
            "service": "test-service",
            "name": "test-dependency",
            "type": "database",
            "target": "postgres",
            "duration_ms": 10.5,
            "success": True,
            "timestamp": datetime.utcnow().isoformat()
        },
        "correlation_id": "test-correlation-id"
    }
    
    # Configure mock to be awaitable
    mock_db_manager.store_dependency_data = AsyncMock()
    
    await consumer._handle_dependency_ingestion(event_data)
    
    mock_db_manager.store_dependency_data.assert_called_once_with(event_data["dependency"])

@pytest.mark.asyncio
async def test_news_consumer_ingestion(mock_db_manager, mock_messaging_client):
    consumer = NewsConsumer(mock_messaging_client, mock_db_manager)
    
    article_data = {
        "source": "Test Source",
        "headline": "Test Headline",
        "content": "Test Content",
        "timestamp": datetime.utcnow().timestamp(),
        "related_symbols": ["AAPL"],
        "article_type": "News",
        "sentiment": 0.5
    }
    
    # Configure mock to be awaitable
    mock_db_manager.insert_news_article = AsyncMock()
    
    await consumer.handle_news_article(article_data)
    
    # Verify call args
    call_args = mock_db_manager.insert_news_article.call_args[0][0]
    assert call_args['publisher'] == "Test Source"
    assert call_args['title'] == "Test Headline"

@pytest.mark.asyncio
async def test_market_data_consumer_ingestion(mock_db_manager, mock_messaging_client):
    consumer = MarketDataConsumer(mock_messaging_client, mock_db_manager)
    
    market_data = {
        "symbol": "AAPL",
        "price": 150.0,
        "volume": 1000,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    # Mock session context manager
    session_mock = AsyncMock()
    # session.add is synchronous
    session_mock.add = MagicMock()
    mock_db_manager.get_session.return_value.__aenter__.return_value = session_mock
    
    await consumer.handle_market_data(market_data)
    
    # Verify session usage
    mock_db_manager.get_session.assert_called_once()
    session_mock.add.assert_called_once()
    session_mock.commit.assert_called_once()
