import logging
import json
from typing import Dict, Any

from database_service.app.database_manager import DatabaseManager
from database_service.app.messaging_client import MessagingClient
from messaging_service.app.event_publisher import EventPublisher

from .services.metadata_service import MetadataService
from .services.metadata_instantiation_service import MetadataInstantiationService
from .repositories.metadata_write_repository import MetadataWriteRepository
from .repositories.metadata_query_repository import MetadataQueryRepository

logger = logging.getLogger(__name__)

class ConversationEventConsumer:
    """Consumer for conversation service events."""

    def __init__(
        self, 
        db_manager: DatabaseManager, 
        messaging_client: MessagingClient,
        event_publisher: EventPublisher
    ):
        self.db_manager = db_manager
        self.messaging_client = messaging_client
        self.event_publisher = event_publisher
        self.running = False

    async def start(self):
        """Start consuming events."""
        if self.running:
            return
        self.running = True
        logger.info("Starting conversation event consumer...")
        
        await self.messaging_client.subscribe(
            topic="business_metadata.events.value_chain_generated",
            callback=self._handle_value_chain_generated
        )

    async def stop(self):
        """Stop consuming events."""
        self.running = False
        await self.messaging_client.unsubscribe("business_metadata.events.value_chain_generated")
        logger.info("Stopped conversation event consumer.")

    async def _handle_value_chain_generated(self, payload: Dict[str, Any]):
        """Handle value chain generation event."""
        try:
            logger.info(f"Received value chain model generation event for session {payload.get('session_id')}")
            
            session_id = payload.get("session_id")
            user_id = payload.get("user_id")
            model_data = payload.get("model")
            
            if session_id and model_data:
                # Create a new database session for this operation
                async with self.db_manager.session_factory() as session:
                    try:
                        # Initialize repositories and service
                        write_repo = MetadataWriteRepository(session, self.event_publisher)
                        query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
                        instantiation_service = MetadataInstantiationService()
                        
                        metadata_service = MetadataService(write_repo, query_repo, instantiation_service)
                        
                        # Persist the model
                        model_id = await metadata_service.persist_generated_model(
                            session_id=session_id,
                            user_id=user_id or "system",
                            model_data=model_data
                        )
                        
                        await session.commit()
                        logger.info(f"Successfully persisted generated model {model_id}")
                        
                    except Exception as e:
                        await session.rollback()
                        logger.error(f"Error persisting generated model: {e}", exc_info=True)
                        raise
                
        except Exception as e:
            logger.error(f"Failed to process value chain generation event: {e}", exc_info=True)
