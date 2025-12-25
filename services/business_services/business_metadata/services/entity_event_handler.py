"""
Entity Event Handler

Handles entity lifecycle events and triggers automated schema extraction.
Implements event-driven automation for schema generation.
"""

import asyncio
from typing import Dict, Any
from pathlib import Path
import logging

from ..services.schema_extractor import SchemaExtractor
from ..repositories.metadata_query_repository import MetadataQueryRepository

logger = logging.getLogger(__name__)


class EntityEventHandler:
    """
    Handles entity lifecycle events and automates schema extraction.
    
    This service subscribes to entity events (created, updated) and automatically
    triggers schema extraction, ensuring schemas are always up-to-date.
    """
    
    def __init__(
        self,
        db_manager,
        messaging_client,
        event_publisher,
        output_dir: Path = Path("schemas")
    ):
        """
        Initialize EntityEventHandler.
        
        Args:
            db_manager: DatabaseManager instance for querying entities
            messaging_client: MessagingClient for subscribing to events
            event_publisher: EventPublisher for publishing extraction results
            output_dir: Directory for schema JSON files
        """
        self.db_manager = db_manager
        self.messaging_client = messaging_client
        self.event_publisher = event_publisher
        self.extractor = SchemaExtractor(output_dir=output_dir)
        self.query_repo = MetadataQueryRepository(db_manager)
        self._running = False
    
    async def start(self):
        """
        Start listening for entity events.
        
        Subscribes to:
        - metadata.entity.created
        - metadata.entity.updated
        """
        if self._running:
            logger.warning("EntityEventHandler already running")
            return
        
        self._running = True
        
        # Subscribe to entity events
        await self.messaging_client.subscribe(
            topic="metadata.entity.created",
            callback=self._handle_entity_created
        )
        
        await self.messaging_client.subscribe(
            topic="metadata.entity.updated",
            callback=self._handle_entity_updated
        )
        
        logger.info("EntityEventHandler started - listening for entity events")
    
    async def stop(self):
        """Stop listening for entity events."""
        self._running = False
        
        # Unsubscribe from events
        await self.messaging_client.unsubscribe("metadata.entity.created")
        await self.messaging_client.unsubscribe("metadata.entity.updated")
        
        logger.info("EntityEventHandler stopped")
    
    async def _handle_entity_created(self, message: Dict[str, Any]):
        """
        Handle entity.created event.
        
        Args:
            message: Event message containing entity_code and entity_name
        """
        try:
            entity_code = message.get("entity_code")
            if not entity_code:
                logger.error("entity.created event missing entity_code")
                return
            
            logger.info(f"Entity created: {entity_code} - triggering schema extraction")
            
            # Extract schema for the new entity
            result = await self._extract_schema_for_entity(entity_code)
            
            if result["success"]:
                logger.info(f"Schema extracted successfully for {entity_code}")
                
                # Publish schema.extracted event
                await self.event_publisher.publish_event(
                    channel="metadata.schema.extracted",
                    message={
                        "entity_code": entity_code,
                        "entity_name": result.get("entity_name"),
                        "output_file": result.get("output_file"),
                        "trigger": "entity.created"
                    }
                )
            else:
                logger.error(f"Schema extraction failed for {entity_code}: {result.get('error')}")
        
        except Exception as e:
            logger.error(f"Error handling entity.created event: {e}", exc_info=True)
    
    async def _handle_entity_updated(self, message: Dict[str, Any]):
        """
        Handle entity.updated event.
        
        Args:
            message: Event message containing entity_code and changes
        """
        try:
            entity_code = message.get("entity_code")
            if not entity_code:
                logger.error("entity.updated event missing entity_code")
                return
            
            # Check if table_schema was updated
            changes = message.get("changes", {})
            if "table_schema" not in changes:
                logger.debug(f"Entity {entity_code} updated but table_schema unchanged - skipping extraction")
                return
            
            logger.info(f"Entity updated: {entity_code} - table_schema changed, re-extracting schema")
            
            # Re-extract schema for the updated entity
            result = await self._extract_schema_for_entity(entity_code)
            
            if result["success"]:
                logger.info(f"Schema re-extracted successfully for {entity_code}")
                
                # Publish schema.extracted event
                await self.event_publisher.publish_event(
                    channel="metadata.schema.extracted",
                    message={
                        "entity_code": entity_code,
                        "entity_name": result.get("entity_name"),
                        "output_file": result.get("output_file"),
                        "trigger": "entity.updated"
                    }
                )
            else:
                logger.error(f"Schema re-extraction failed for {entity_code}: {result.get('error')}")
        
        except Exception as e:
            logger.error(f"Error handling entity.updated event: {e}", exc_info=True)
    
    async def _extract_schema_for_entity(self, entity_code: str) -> Dict[str, Any]:
        """
        Extract schema for a specific entity.
        
        Args:
            entity_code: Entity code to extract
            
        Returns:
            Result dictionary with success status and details
        """
        try:
            # Get entity from database
            entity = await self.query_repo.get_entity_by_code(entity_code)
            
            if not entity:
                return {
                    "success": False,
                    "entity_code": entity_code,
                    "error": f"Entity not found: {entity_code}"
                }
            
            # Extract schema
            schema = await self.extractor.extract_schema_from_entity(entity)
            
            # Save to JSON file
            filename = entity_code.lower()
            output_path = await self.extractor.save_schema_to_json(schema, filename)
            
            return {
                "success": True,
                "entity_code": entity_code,
                "entity_name": entity.name,
                "output_file": str(output_path),
                "schema": schema
            }
        
        except Exception as e:
            return {
                "success": False,
                "entity_code": entity_code,
                "error": str(e)
            }
    
    async def extract_all_schemas(self) -> Dict[str, Any]:
        """
        Extract schemas for all entities (manual trigger).
        
        Returns:
            Summary of extraction results
        """
        try:
            logger.info("Extracting schemas for all entities")
            
            # Get all entities
            entities = await self.query_repo.get_all_entities()
            
            results = []
            for entity in entities:
                result = await self._extract_schema_for_entity(entity.code)
                results.append(result)
            
            # Generate summary
            summary = self.extractor.get_extraction_summary(results)
            
            logger.info(
                f"Bulk extraction complete: {summary['successful_extractions']}/{summary['total_entities']} successful"
            )
            
            # Publish bulk extraction event
            await self.event_publisher.publish_event(
                channel="metadata.schema.bulk_extracted",
                message={
                    "total_entities": summary["total_entities"],
                    "successful_extractions": summary["successful_extractions"],
                    "failed_extractions": summary["failed_extractions"],
                    "output_directory": summary["output_directory"]
                }
            )
            
            return summary
        
        except Exception as e:
            logger.error(f"Error during bulk schema extraction: {e}", exc_info=True)
            raise
