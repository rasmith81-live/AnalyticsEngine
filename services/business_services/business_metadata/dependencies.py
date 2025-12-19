"""Dependency injection using backend services."""

import sys
from pathlib import Path
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.database_manager import DatabaseManager
from messaging_service.app.event_publisher import EventPublisher
from database_service.app.messaging_client import MessagingClient

from .config import settings

# Global instances (initialized in main.py startup)
db_manager: DatabaseManager = None
event_publisher: EventPublisher = None
messaging_client: MessagingClient = None


async def initialize_backend_services():
    """Initialize backend service connections.
    
    Called during FastAPI startup.
    """
    global db_manager, event_publisher, messaging_client
    
    # Initialize database manager
    db_manager = DatabaseManager(settings)
    await db_manager.initialize()
    
    # Initialize event publisher
    event_publisher = EventPublisher(settings)
    await event_publisher.initialize()

    # Initialize messaging client (consumer)
    messaging_client = MessagingClient(
        redis_url=settings.redis_url,
        service_name=settings.service_name,
        pool_size=5
    )
    await messaging_client.connect()


async def shutdown_backend_services():
    """Shutdown backend service connections.
    
    Called during FastAPI shutdown.
    """
    global db_manager, event_publisher, messaging_client
    
    if db_manager:
        await db_manager.shutdown()
    
    if event_publisher:
        await event_publisher.shutdown()

    if messaging_client:
        await messaging_client.disconnect()


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session from database_service.
    
    FastAPI dependency for database access.
    
    Yields:
        AsyncSession instance
    """
    if not db_manager:
        raise RuntimeError("DatabaseManager not initialized. Call initialize_backend_services() first.")
    
    async with db_manager.session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


def get_redis_client():
    """Get Redis client from database_service.
    
    FastAPI dependency for Redis access.
    
    Returns:
        Redis client instance
    """
    if not db_manager:
        raise RuntimeError("DatabaseManager not initialized.")
    
    return db_manager.redis_client


def get_event_publisher() -> EventPublisher:
    """Get event publisher from messaging_service.
    
    FastAPI dependency for event publishing.
    
    Returns:
        EventPublisher instance
    """
    if not event_publisher:
        raise RuntimeError("EventPublisher not initialized.")
    
    return event_publisher
