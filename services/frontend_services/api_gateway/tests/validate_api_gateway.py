import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock, patch
import sys
import os
import asyncio
from contextlib import asynccontextmanager

# Add the parent directory to sys.path to ensure app imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Create mocks
mock_redis_pool = MagicMock()
mock_redis_pool.close = AsyncMock()
mock_redis_pool.wait_closed = AsyncMock()
# Add async methods called by middleware
mock_redis_pool.incr = AsyncMock(return_value=1)
mock_redis_pool.expire = AsyncMock(return_value=True)
mock_redis_pool.ttl = AsyncMock(return_value=60)
mock_redis_pool.get = AsyncMock(return_value=None)
mock_redis_pool.set = AsyncMock(return_value=True)
mock_redis_pool.delete = AsyncMock(return_value=True)
mock_redis_pool.ping = AsyncMock(return_value=True)
# Allow pubsub to be called
mock_redis_pool.pubsub = MagicMock()

mock_pubsub = MagicMock()
mock_pubsub.start = AsyncMock()
mock_pubsub.stop = AsyncMock()
mock_pubsub.publish = AsyncMock(return_value=True)
mock_pubsub.subscribe = MagicMock(return_value="sub_id")
mock_pubsub.unsubscribe = MagicMock(return_value=True)

mock_ws_manager = MagicMock()
mock_ws_manager.start = AsyncMock()
mock_ws_manager.stop = AsyncMock()

mock_registry = MagicMock()
mock_registry.check_all_services_health = AsyncMock(return_value={})
mock_registry.register_service = AsyncMock()
mock_registry.get_all_services = AsyncMock(return_value=[])

# Mock CacheService
mock_cache_service = MagicMock()
# Setup cache get to handle token and permissions
async def mock_cache_get(key):
    if key.startswith("token:"):
        return {
            "sub": "test_user",
            "exp": 9999999999,
            "roles": ["admin"],
            "token_type": "bearer"
        }
    return None

mock_cache_service.get = AsyncMock(side_effect=mock_cache_get)
mock_cache_service.set = AsyncMock(return_value=True)

# Define a context manager for redis_client_context
@asynccontextmanager
async def mock_redis_context():
    yield mock_redis_pool

# Patch the modules
with patch('app.core.redis_client.get_redis_pool', AsyncMock(return_value=mock_redis_pool)), \
     patch('app.core.redis_client.redis_client_context', side_effect=mock_redis_context), \
     patch('app.core.pubsub.pubsub_service', mock_pubsub), \
     patch('app.core.websocket_manager.websocket_manager', mock_ws_manager), \
     patch('app.services.registry.service_registry', mock_registry), \
     patch('app.services.init_registry.initialize_service_registry', AsyncMock(return_value=[])), \
     patch('app.core.cache.CacheService', mock_cache_service), \
     patch('app.middleware.authentication.CacheService', mock_cache_service), \
     patch('app.middleware.authorization.CacheService', mock_cache_service):

    from app.main import app
    from app.api.dependencies import get_metadata_client
    from app.clients.metadata_client import MetadataServiceClient
    
    # We need to recreate the client to ensure middleware uses patched dependencies?
    # No, TestClient uses the app as is.
    client = TestClient(app)

    def test_api_gateway_health():
        """Test the health endpoint to ensure the app is running."""
        print("\nTesting API Gateway Health Endpoint...")
        try:
            response = client.get("/health")
            if response.status_code == 200:
                print("✅ Health check passed")
            else:
                print(f"❌ Health check failed: {response.status_code} - {response.text}")
            assert response.status_code == 200
        except Exception as e:
            print(f"❌ Health check exception: {str(e)}")
            raise

    def test_swagger_docs():
        """Test that Swagger UI and OpenAPI schema are available."""
        print("\nTesting Swagger Documentation...")
        
        # Check OpenAPI JSON
        try:
            response_json = client.get("/openapi.json")
            if response_json.status_code == 200:
                print("✅ OpenAPI Schema available")
            else:
                print(f"❌ OpenAPI Schema failed: {response_json.status_code}")
            assert response_json.status_code == 200
            
            # Check Docs UI
            response_docs = client.get("/docs")
            if response_docs.status_code == 200:
                print("✅ Swagger UI available")
            else:
                print(f"❌ Swagger UI failed: {response_docs.status_code}")
            assert response_docs.status_code == 200
        except Exception as e:
            print(f"❌ Swagger docs exception: {str(e)}")
            raise

    async def test_proxy_logic_metadata():
        """
        Test proxy logic by mocking the MetadataServiceClient.
        Verifies that requests to Gateway are routed to the Service Client.
        """
        print("\nTesting Proxy Logic (Metadata Service)...")
        
        # Mock the metadata client
        mock_metadata_client = MagicMock(spec=MetadataServiceClient)
        mock_metadata_client.get_kpis = AsyncMock(return_value=[{"code": "KPI_001", "name": "Test KPI"}])
        
        # Override the dependency
        app.dependency_overrides[get_metadata_client] = lambda: mock_metadata_client
        
        try:
            # Make request to Gateway with Auth Header
            headers = {"Authorization": "Bearer test_token"}
            response = client.get("/api/v1/metadata/kpis", headers=headers)
            
            # Verify response
            if response.status_code == 200:
                print("✅ Proxy request successful (200 OK)")
                data = response.json()
                if data == [{"code": "KPI_001", "name": "Test KPI"}]:
                    print("✅ Data matches mock return value")
                else:
                    print(f"❌ Data mismatch: {data}")
            else:
                print(f"❌ Proxy request failed: {response.status_code} - {response.text}")
                
            # Verify client method was called
            if mock_metadata_client.get_kpis.called:
                 print("✅ Client method 'get_kpis' was called")
            else:
                 print("❌ Client method 'get_kpis' was NOT called")
                 
            assert response.status_code == 200
            assert data == [{"code": "KPI_001", "name": "Test KPI"}]
            
        finally:
            # Clean up dependency override
            app.dependency_overrides = {}

    if __name__ == "__main__":
        # Manually run tests if executed as script
        try:
            # Re-patch for execution context
            with patch('app.core.redis_client.get_redis_pool', AsyncMock(return_value=mock_redis_pool)), \
                 patch('app.core.redis_client.redis_client_context', side_effect=mock_redis_context), \
                 patch('app.core.pubsub.pubsub_service', mock_pubsub), \
                 patch('app.core.websocket_manager.websocket_manager', mock_ws_manager), \
                 patch('app.services.registry.service_registry', mock_registry), \
                 patch('app.services.health.redis_client_context', side_effect=mock_redis_context), \
                 patch('app.core.cache.CacheService', mock_cache_service), \
                 patch('app.middleware.authentication.CacheService', mock_cache_service), \
                 patch('app.middleware.authorization.CacheService', mock_cache_service):
                
                test_api_gateway_health()
                test_swagger_docs()
                
                # Async test runner for the proxy test
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(test_proxy_logic_metadata())
                loop.close()
            
            print("\nAll API Gateway validation tests passed! 🚀")
        except Exception as e:
            print(f"\nValidation failed with error: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
