# =============================================================================
# Metadata Command Consumer
# Processes commands from multi_agent_service and other services via Redis Streams
# =============================================================================
"""
Command consumer for business_metadata service.

Handles:
- Entity CRUD operations
- KPI CRUD operations
- Module operations
- Value chain operations

Commands arrive via Redis Streams, responses sent via Pub/Sub.
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Any, Dict, Optional

# Add shared path for imports
shared_path = Path(__file__).parent.parent.parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from events.schemas import (
    ServiceCommand,
    CommandType,
    ResponseType,
)
from events.consumer import BaseCommandConsumer

logger = logging.getLogger(__name__)


class MetadataCommandConsumer(BaseCommandConsumer):
    """
    Command consumer for business_metadata service.
    
    Processes entity, KPI, module, and value chain commands
    from other services via Redis Streams.
    """
    
    def __init__(
        self,
        db_manager,
        event_publisher,
        redis_url: Optional[str] = None
    ):
        """
        Initialize consumer.
        
        Args:
            db_manager: Database manager for persistence
            event_publisher: Event publisher for notifications
            redis_url: Redis connection URL
        """
        super().__init__(
            service_name="business_metadata",
            redis_url=redis_url
        )
        self.db_manager = db_manager
        self.event_publisher = event_publisher
    
    async def _register_handlers(self) -> None:
        """Register command handlers."""
        # Entity handlers
        self.register_handler(CommandType.CREATE_ENTITY, self._handle_create_entity)
        self.register_handler(CommandType.UPDATE_ENTITY, self._handle_update_entity)
        self.register_handler(CommandType.DELETE_ENTITY, self._handle_delete_entity)
        self.register_handler(CommandType.GET_ENTITY, self._handle_get_entity)
        self.register_handler(CommandType.LIST_ENTITIES, self._handle_list_entities)
        
        # KPI handlers
        self.register_handler(CommandType.CREATE_KPI, self._handle_create_kpi)
        self.register_handler(CommandType.UPDATE_KPI, self._handle_update_kpi)
        self.register_handler(CommandType.DELETE_KPI, self._handle_delete_kpi)
        self.register_handler(CommandType.GET_KPI, self._handle_get_kpi)
        self.register_handler(CommandType.LIST_KPIS, self._handle_list_kpis)
        
        # Module handlers
        self.register_handler(CommandType.CREATE_MODULE, self._handle_create_module)
        self.register_handler(CommandType.UPDATE_MODULE, self._handle_update_module)
        self.register_handler(CommandType.GET_MODULE, self._handle_get_module)
        self.register_handler(CommandType.LIST_MODULES, self._handle_list_modules)
        
        # Value chain handlers
        self.register_handler(CommandType.CREATE_VALUE_CHAIN, self._handle_create_value_chain)
        self.register_handler(CommandType.UPDATE_VALUE_CHAIN, self._handle_update_value_chain)
        self.register_handler(CommandType.GET_VALUE_CHAIN, self._handle_get_value_chain)
        self.register_handler(CommandType.LIST_VALUE_CHAINS, self._handle_list_value_chains)
        
        # Health check
        self.register_handler(CommandType.HEALTH_CHECK, self._handle_health_check)
        
        logger.info("Registered metadata command handlers")
    
    # =========================================================================
    # Entity Handlers
    # =========================================================================
    
    async def _handle_create_entity(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle entity creation."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        from ..services.metadata_service import MetadataService
        from ..services.metadata_instantiation_service import MetadataInstantiationService
        
        payload = command.payload
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            instantiation_service = MetadataInstantiationService()
            service = MetadataService(write_repo, query_repo, instantiation_service)
            
            entity = await service.create_entity(
                code=payload.get("code"),
                name=payload.get("name"),
                description=payload.get("description", ""),
                module_code=payload.get("module_code"),
                attributes=payload.get("attributes", [])
            )
            
            await session.commit()
            
            logger.info(f"Created entity: {entity.code}")
            return {"id": str(entity.uuid_ref), "code": entity.code, "name": entity.name}
    
    async def _handle_update_entity(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle entity update."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        from ..services.metadata_service import MetadataService
        from ..services.metadata_instantiation_service import MetadataInstantiationService
        
        payload = command.payload
        entity_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            instantiation_service = MetadataInstantiationService()
            service = MetadataService(write_repo, query_repo, instantiation_service)
            
            entity = await service.update_entity(
                code=entity_code,
                updates=payload.get("updates", {})
            )
            
            await session.commit()
            
            logger.info(f"Updated entity: {entity_code}")
            return {"code": entity.code, "updated": True}
    
    async def _handle_delete_entity(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle entity deletion."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        
        payload = command.payload
        entity_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            await write_repo.delete_entity(entity_code)
            await session.commit()
            
            logger.info(f"Deleted entity: {entity_code}")
            return {"code": entity_code, "deleted": True}
    
    async def _handle_get_entity(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle entity retrieval."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        entity_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            entity = await query_repo.get_entity_by_code(entity_code)
            
            if not entity:
                raise ValueError(f"Entity not found: {entity_code}")
            
            return {
                "code": entity.code,
                "name": entity.name,
                "description": entity.description,
                "module_code": entity.module_code,
                "uuid_ref": str(entity.uuid_ref) if entity.uuid_ref else None
            }
    
    async def _handle_list_entities(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle entity listing."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        module_code = payload.get("module_code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            
            if module_code:
                entities = await query_repo.get_entities_by_module(module_code)
            else:
                entities = await query_repo.get_all_entities()
            
            return {
                "entities": [
                    {"code": e.code, "name": e.name, "module_code": e.module_code}
                    for e in entities
                ],
                "count": len(entities)
            }
    
    # =========================================================================
    # KPI Handlers
    # =========================================================================
    
    async def _handle_create_kpi(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle KPI creation."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        from ..services.metadata_service import MetadataService
        from ..services.metadata_instantiation_service import MetadataInstantiationService
        
        payload = command.payload
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            instantiation_service = MetadataInstantiationService()
            service = MetadataService(write_repo, query_repo, instantiation_service)
            
            kpi = await service.create_kpi(
                code=payload.get("code"),
                name=payload.get("name"),
                description=payload.get("description", ""),
                formula=payload.get("formula", ""),
                module_code=payload.get("module_code"),
                unit=payload.get("unit", ""),
                calculation_type=payload.get("calculation_type", "simple")
            )
            
            await session.commit()
            
            logger.info(f"Created KPI: {kpi.code}")
            return {"id": str(kpi.uuid_ref), "code": kpi.code, "name": kpi.name}
    
    async def _handle_update_kpi(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle KPI update."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        from ..services.metadata_service import MetadataService
        from ..services.metadata_instantiation_service import MetadataInstantiationService
        
        payload = command.payload
        kpi_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            instantiation_service = MetadataInstantiationService()
            service = MetadataService(write_repo, query_repo, instantiation_service)
            
            kpi = await service.update_kpi(
                code=kpi_code,
                updates=payload.get("updates", {})
            )
            
            await session.commit()
            
            logger.info(f"Updated KPI: {kpi_code}")
            return {"code": kpi.code, "updated": True}
    
    async def _handle_delete_kpi(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle KPI deletion."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        
        payload = command.payload
        kpi_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            await write_repo.delete_kpi(kpi_code)
            await session.commit()
            
            logger.info(f"Deleted KPI: {kpi_code}")
            return {"code": kpi_code, "deleted": True}
    
    async def _handle_get_kpi(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle KPI retrieval."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        kpi_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            kpi = await query_repo.get_kpi_by_code(kpi_code)
            
            if not kpi:
                raise ValueError(f"KPI not found: {kpi_code}")
            
            return {
                "code": kpi.code,
                "name": kpi.name,
                "description": kpi.description,
                "formula": kpi.formula,
                "module_code": kpi.module_code,
                "unit": kpi.unit,
                "uuid_ref": str(kpi.uuid_ref) if kpi.uuid_ref else None
            }
    
    async def _handle_list_kpis(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle KPI listing."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        module_code = payload.get("module_code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            
            if module_code:
                kpis = await query_repo.get_kpis_by_module(module_code)
            else:
                kpis = await query_repo.get_all_kpis()
            
            return {
                "kpis": [
                    {"code": k.code, "name": k.name, "module_code": k.module_code}
                    for k in kpis
                ],
                "count": len(kpis)
            }
    
    # =========================================================================
    # Module Handlers
    # =========================================================================
    
    async def _handle_create_module(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle module creation."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        
        payload = command.payload
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            
            module = await write_repo.create_module(
                code=payload.get("code"),
                name=payload.get("name"),
                description=payload.get("description", ""),
                value_chain_code=payload.get("value_chain_code")
            )
            
            await session.commit()
            
            logger.info(f"Created module: {module.code}")
            return {"id": str(module.uuid_ref), "code": module.code, "name": module.name}
    
    async def _handle_update_module(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle module update."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        
        payload = command.payload
        module_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            
            module = await write_repo.update_module(
                code=module_code,
                updates=payload.get("updates", {})
            )
            
            await session.commit()
            
            logger.info(f"Updated module: {module_code}")
            return {"code": module.code, "updated": True}
    
    async def _handle_get_module(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle module retrieval."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        module_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            module = await query_repo.get_module_by_code(module_code)
            
            if not module:
                raise ValueError(f"Module not found: {module_code}")
            
            return {
                "code": module.code,
                "name": module.name,
                "description": module.description,
                "value_chain_code": module.value_chain_code
            }
    
    async def _handle_list_modules(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle module listing."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        value_chain_code = payload.get("value_chain_code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            
            if value_chain_code:
                modules = await query_repo.get_modules_by_value_chain(value_chain_code)
            else:
                modules = await query_repo.get_all_modules()
            
            return {
                "modules": [
                    {"code": m.code, "name": m.name, "value_chain_code": m.value_chain_code}
                    for m in modules
                ],
                "count": len(modules)
            }
    
    # =========================================================================
    # Value Chain Handlers
    # =========================================================================
    
    async def _handle_create_value_chain(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle value chain creation."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        
        payload = command.payload
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            
            vc = await write_repo.create_value_chain(
                code=payload.get("code"),
                name=payload.get("name"),
                description=payload.get("description", ""),
                industry=payload.get("industry", "")
            )
            
            await session.commit()
            
            logger.info(f"Created value chain: {vc.code}")
            return {"id": str(vc.uuid_ref), "code": vc.code, "name": vc.name}
    
    async def _handle_update_value_chain(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle value chain update."""
        from ..repositories.metadata_write_repository import MetadataWriteRepository
        
        payload = command.payload
        vc_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            write_repo = MetadataWriteRepository(session, self.event_publisher)
            
            vc = await write_repo.update_value_chain(
                code=vc_code,
                updates=payload.get("updates", {})
            )
            
            await session.commit()
            
            logger.info(f"Updated value chain: {vc_code}")
            return {"code": vc.code, "updated": True}
    
    async def _handle_get_value_chain(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle value chain retrieval."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        payload = command.payload
        vc_code = payload.get("code")
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            vc = await query_repo.get_value_chain_by_code(vc_code)
            
            if not vc:
                raise ValueError(f"Value chain not found: {vc_code}")
            
            return {
                "code": vc.code,
                "name": vc.name,
                "description": vc.description,
                "industry": vc.industry
            }
    
    async def _handle_list_value_chains(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle value chain listing."""
        from ..repositories.metadata_query_repository import MetadataQueryRepository
        
        async with self.db_manager.session_factory() as session:
            query_repo = MetadataQueryRepository(session, self.db_manager.redis_client)
            value_chains = await query_repo.get_all_value_chains()
            
            return {
                "value_chains": [
                    {"code": vc.code, "name": vc.name, "industry": vc.industry}
                    for vc in value_chains
                ],
                "count": len(value_chains)
            }
    
    # =========================================================================
    # Health Check
    # =========================================================================
    
    async def _handle_health_check(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle health check."""
        return {
            "service": "business_metadata",
            "status": "healthy",
            "consumer": self.consumer_name
        }
