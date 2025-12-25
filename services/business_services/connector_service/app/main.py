
import logging
import sys
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient
from app.connection_manager import ConnectionManager, ConnectionProfile
from app.schema_discovery import SchemaDiscoveryEngine
from app.database_client import DatabaseClient

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global instances
messaging_client: Optional[MessagingClient] = None
db_client: Optional[DatabaseClient] = None
connection_manager = ConnectionManager()
schema_engine = SchemaDiscoveryEngine()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global messaging_client, db_client
    
    # Initialize messaging client
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    messaging_client = MessagingClient(
        redis_url=redis_url,
        service_name="connector_service",
        pool_size=5
    )
    await messaging_client.connect()
    logger.info("MessagingClient connected")
    
    # Initialize database client
    database_service_url = os.getenv("DATABASE_SERVICE_URL", "http://database_service:8000")
    db_client = DatabaseClient(
        base_url=database_service_url,
        service_name="connector_service"
    )
    logger.info("DatabaseClient initialized for secure credential storage")
    
    yield
    
    # Cleanup
    if messaging_client:
        await messaging_client.disconnect()
        logger.info("MessagingClient disconnected")
    
    if db_client:
        await db_client.close()
        logger.info("DatabaseClient closed")

app = FastAPI(
    title="Connector Service",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "connector_service"}

@app.post("/connections")
async def create_connection(profile: ConnectionProfile):
    """Create or update a connection profile."""
    # Store in database
    if db_client:
        success = await db_client.store_connection_profile(
            profile_id=profile.id,
            profile_data=profile.model_dump()
        )
        if not success:
            raise HTTPException(status_code=500, detail="Failed to store connection profile")
    
    # Publish event that connection was created
    if messaging_client:
        await messaging_client.publish_event(
            event_type="connection.created",
            payload={
                "connection_id": profile.id,
                "connection_type": profile.type.value if hasattr(profile.type, 'value') else str(profile.type)
            },
            correlation_id=profile.id
        )
        logger.info(f"Published connection.created event for {profile.id}")
    
    return {"message": "Connection profile saved", "id": profile.id}

@app.get("/connections/{connection_id}")
async def get_connection(connection_id: str):
    if db_client:
        profile_data = await db_client.get_connection_profile(connection_id)
        if not profile_data:
            raise HTTPException(status_code=404, detail="Connection not found")
        return profile_data
    else:
        raise HTTPException(status_code=503, detail="Database client not available")

@app.post("/connections/test")
async def test_connection(profile: ConnectionProfile):
    """Test connectivity for a profile."""
    success = await connection_manager.test_connection(profile)
    
    # Publish event about connection test result
    if messaging_client:
        await messaging_client.publish_event(
            event_type="connection.tested",
            payload={
                "connection_id": profile.id,
                "success": success
            },
            correlation_id=profile.id
        )
    
    return {"success": success}

@app.post("/discovery/schema")
async def discover_schema(connection_id: str):
    """Discover schema for a registered connection."""
    # Retrieve profile from database
    if not db_client:
        raise HTTPException(status_code=503, detail="Database client not available")
    
    profile_data = await db_client.get_connection_profile(connection_id)
    if not profile_data:
        raise HTTPException(status_code=404, detail="Connection not found")
    
    # Reconstruct ConnectionProfile from stored data
    profile = ConnectionProfile(**profile_data)
    
    try:
        # Map profile to schema engine params
        params = {}
        connection_type = ""
        
        if "sql" in profile.type.value:
            connection_type = "sql"
            # Construct connection string based on type (simplified)
            if profile.type.value == "sql_postgres":
                params['connection_string'] = f"postgresql://{profile.username}:{profile.password}@{profile.host}:{profile.port}/{profile.database}"
        elif "rest" in profile.type.value:
            connection_type = "rest"
            params['base_url'] = profile.api_url
            params['endpoint'] = profile.extra_params.get("default_endpoint", "")
            
        if not connection_type:
             raise HTTPException(status_code=400, detail="Unsupported connection type for discovery")

        schema = schema_engine.discover(connection_type, params)
        
        # Publish event that schema was discovered
        if messaging_client:
            await messaging_client.publish_event(
                event_type="schema.discovered",
                payload={
                    "connection_id": connection_id,
                    "connection_type": connection_type,
                    "table_count": len(schema.get("tables", [])) if isinstance(schema, dict) else 0
                },
                correlation_id=connection_id
            )
            logger.info(f"Published schema.discovered event for {connection_id}")
        
        return schema
    except Exception as e:
        logger.error(f"Discovery failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/discovery/preview")
async def preview_data(connection_id: str, table_name: str, limit: int = 5):
    """Preview data from a source table."""
    # Logic similar to discover_schema to get adapter and call preview_data
    # For brevity, implementing a stub or simplified logic would go here
    return {"message": "Not implemented in this stub"}
