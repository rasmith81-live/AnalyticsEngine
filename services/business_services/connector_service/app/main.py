
import logging
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

from app.connection_manager import ConnectionManager, ConnectionProfile
from app.schema_discovery import SchemaDiscoveryEngine

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Connector Service", version="1.0.0")

connection_manager = ConnectionManager()
schema_engine = SchemaDiscoveryEngine()

# In-memory store for profiles (Replace with secure storage in production)
connection_profiles: Dict[str, ConnectionProfile] = {}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "connector_service"}

@app.post("/connections")
async def create_connection(profile: ConnectionProfile):
    """Create or update a connection profile."""
    connection_profiles[profile.id] = profile
    return {"message": "Connection profile saved", "id": profile.id}

@app.get("/connections/{connection_id}")
async def get_connection(connection_id: str):
    profile = connection_profiles.get(connection_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Connection not found")
    return profile

@app.post("/connections/test")
async def test_connection(profile: ConnectionProfile):
    """Test connectivity for a profile."""
    success = await connection_manager.test_connection(profile)
    return {"success": success}

@app.post("/discovery/schema")
async def discover_schema(connection_id: str):
    """Discover schema for a registered connection."""
    profile = connection_profiles.get(connection_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Connection not found")
    
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
