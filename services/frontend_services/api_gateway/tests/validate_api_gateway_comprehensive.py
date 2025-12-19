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
    from app.api.dependencies import get_metadata_client, get_calculation_client, get_config_client
    from app.clients.metadata_client import MetadataServiceClient
    from app.clients.calculation_client import CalculationEngineClient
    from app.clients.config_client import DemoConfigServiceClient
    from app.middleware.circuit_breaker import CircuitState

    client = TestClient(app)

    async def test_service_clients():
        """Test interactions with various service clients."""
        print("\nTesting Service Clients...")
        
        # Mock Calculation Client
        mock_calc_client = MagicMock(spec=CalculationEngineClient)
        mock_calc_client.calculate_kpi = AsyncMock(return_value={"result": 100})
        app.dependency_overrides[get_calculation_client] = lambda: mock_calc_client
        
        # Mock Config Client
        mock_config_client = MagicMock(spec=DemoConfigServiceClient)
        mock_config_client.get_client_configs = AsyncMock(return_value=[{"id": "client1"}])
        app.dependency_overrides[get_config_client] = lambda: mock_config_client

        try:
            headers = {"Authorization": "Bearer test_token"}
            
            # Test Calculation Endpoint
            print("- Testing Calculation Client...")
            resp = client.post("/api/v1/calculations/calculate", json={"kpi": "test"}, headers=headers)
            assert resp.status_code == 200
            assert resp.json() == {"result": 100}
            print("  ✅ Calculation request successful")

            # Test Config Endpoint
            print("- Testing Config Client...")
            resp = client.get("/api/v1/config/clients", headers=headers)
            assert resp.status_code == 200
            assert resp.json() == [{"id": "client1"}]
            print("  ✅ Config request successful")
            
        finally:
            app.dependency_overrides = {}

    async def test_circuit_breaker():
        """Test Circuit Breaker Middleware logic."""
        print("\nTesting Circuit Breaker...")
        
        # We need to simulate the redis behavior for circuit breaker
        # State: CLOSED -> OPEN -> HALF_OPEN
        
        # 1. Test CLOSED state (Normal operation)
        # Mock redis get to return CLOSED (None or 'closed')
        mock_redis_pool.get = AsyncMock(return_value=None) 
        
        headers = {"Authorization": "Bearer test_token"}
        resp = client.get("/health") # Health is excluded, so use another endpoint
        # Use a non-existent endpoint or mocked one that would trigger middleware
        # Let's use metadata endpoint again
        
        mock_metadata_client = MagicMock(spec=MetadataServiceClient)
        mock_metadata_client.get_kpis = AsyncMock(return_value=[])
        app.dependency_overrides[get_metadata_client] = lambda: mock_metadata_client

        try:
            resp = client.get("/api/v1/metadata/kpis", headers=headers)
            assert resp.status_code == 200
            print("  ✅ Circuit CLOSED: Request passed")
            
            # 2. Test OPEN state
            # Mock redis get to return OPEN
            mock_redis_pool.get = AsyncMock(side_effect=lambda k: "open" if "state" in k else None)
            # Also need to mock recovery time check to return future time (not yet recoverable)
            # mock_redis_pool.get side_effect needs to handle multiple keys
            
            async def open_state_side_effect(key):
                if "state" in key:
                    return "open"
                if "recovery_time" in key:
                    import time
                    return str(int(time.time()) + 3600) # Future time
                return None
                
            mock_redis_pool.get = AsyncMock(side_effect=open_state_side_effect)
            
            resp = client.get("/api/v1/metadata/kpis", headers=headers)
            if resp.status_code == 503:
                print("  ✅ Circuit OPEN: Request rejected (503)")
            else:
                 print(f"  ❌ Circuit OPEN check failed: {resp.status_code}")
            assert resp.status_code == 503

        finally:
            app.dependency_overrides = {}

    async def test_rate_limiting():
        """Test Rate Limiting Middleware logic."""
        print("\nTesting Rate Limiting...")
        
        headers = {"Authorization": "Bearer test_token"}
        
        # We need to simulate redis incr returning a value > limit
        # Default limit is 100 (from config)
        
        # Mock redis incr to return 101
        original_incr = mock_redis_pool.incr
        mock_redis_pool.incr = AsyncMock(return_value=101)
        
        # Ensure circuit breaker doesn't block us (reset get to None)
        mock_redis_pool.get = AsyncMock(return_value=None)

        try:
            resp = client.get("/api/v1/metadata/kpis", headers=headers)
            if resp.status_code == 429:
                print("  ✅ Rate Limit Exceeded: Request rejected (429)")
            else:
                print(f"  ❌ Rate Limit check failed: {resp.status_code}")
            assert resp.status_code == 429
            
        finally:
            mock_redis_pool.incr = original_incr

    if __name__ == "__main__":
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
                
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                loop.run_until_complete(test_service_clients())
                loop.run_until_complete(test_circuit_breaker())
                loop.run_until_complete(test_rate_limiting())
                
                loop.close()
            
            print("\nAll Comprehensive Gateway validation tests passed! 🚀")
        except Exception as e:
            print(f"\nValidation failed with error: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
