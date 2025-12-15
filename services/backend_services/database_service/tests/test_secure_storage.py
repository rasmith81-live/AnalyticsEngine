
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
from datetime import datetime

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.secure_storage_manager import SecureStorageManager
from app.models import SecureArtifactResponse
from app.base_models import SecureArtifact
from app.main import app, get_secure_storage_manager
from fastapi.testclient import TestClient

@pytest.fixture
def mock_session_factory():
    # Create the session mock
    session_mock = AsyncMock()
    
    # Mock begin() - In SQLAlchemy AsyncSession, begin() is a sync method that returns an async context manager
    trans_cm = AsyncMock()
    trans_cm.__aenter__.return_value = session_mock
    trans_cm.__aexit__.return_value = None
    session_mock.begin = MagicMock(return_value=trans_cm)
    
    # Mock execute result
    result_mock = MagicMock()
    session_mock.execute.return_value = result_mock
    
    # Mock synchronous methods
    session_mock.add = MagicMock()
    
    # Factory context manager (async with session_factory() as session:)
    factory_cm = AsyncMock()
    factory_cm.__aenter__.return_value = session_mock
    factory_cm.__aexit__.return_value = None
    
    # The factory itself is synchronous but returns the async context manager
    factory = MagicMock(return_value=factory_cm)
    return factory

@pytest.fixture
def secure_manager(mock_session_factory):
    # Patch settings to have a fixed secret key
    with patch("app.secure_storage_manager.get_settings") as mock_settings:
        mock_settings.return_value.secret_key = "test-secret-key-123"
        manager = SecureStorageManager(mock_session_factory)
        return manager

@pytest.fixture
def client(secure_manager):
    app.dependency_overrides[get_secure_storage_manager] = lambda: secure_manager
    
    # Do not use context manager for TestClient to avoid triggering lifespan events
    # which would attempt to connect to the database.
    client = TestClient(app)
    yield client
    
    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_encryption_decryption(secure_manager):
    """Test internal encryption and decryption helpers."""
    original = "sensitive-data-123"
    encrypted = secure_manager._encrypt(original)
    
    assert encrypted != original
    decrypted = secure_manager._decrypt(encrypted)
    assert decrypted == original

@pytest.mark.asyncio
async def test_store_new_artifact(secure_manager, mock_session_factory):
    """Test storing a new artifact."""
    session = mock_session_factory.return_value.__aenter__.return_value
    
    # Mock finding existing artifact (None)
    result_mock = MagicMock()
    result_mock.scalar_one_or_none.return_value = None
    session.execute.return_value = result_mock
    
    # Store
    artifact = await secure_manager.store_artifact(
        key="api_key",
        value="12345",
        description="Test API Key",
        category="credentials"
    )
    
    # Verify session.add called
    session.add.assert_called_once()
    saved_artifact = session.add.call_args[0][0]
    
    print(f"Saved artifact: {saved_artifact}")
    print(f"Key: {saved_artifact.key}")
    print(f"Encrypted Value: {saved_artifact.encrypted_value}")
    
    assert isinstance(saved_artifact, SecureArtifact), "Not a SecureArtifact instance"
    assert saved_artifact.key == "api_key", f"Key mismatch: {saved_artifact.key}"
    assert saved_artifact.encrypted_value != "12345", "Value was not encrypted"
    
    decrypted = secure_manager._decrypt(saved_artifact.encrypted_value)
    assert decrypted == "12345", f"Decryption mismatch: {decrypted}"

@pytest.mark.asyncio
async def test_delete_artifact(secure_manager, mock_session_factory):
    """Test deleting an artifact."""
    session = mock_session_factory.return_value.__aenter__.return_value
    
    # Mock result
    result_mock = MagicMock()
    result_mock.rowcount = 1
    session.execute.return_value = result_mock
    
    deleted = await secure_manager.delete_artifact("api_key")
    
    assert deleted is True
    session.execute.assert_called()
    # Check that delete statement was executed
    # We can't easily check the exact statement content with MagicMock on execute unless we inspect call args deeply, 
    # but we verify execute was called.

@pytest.mark.asyncio
async def test_get_artifact(secure_manager, mock_session_factory):
    """Test retrieving and decrypting an artifact."""
    session = mock_session_factory.return_value.__aenter__.return_value
    
    # Mock db artifact
    db_artifact = SecureArtifact(
        key="api_key",
        encrypted_value=secure_manager._encrypt("secret-value"),
        description="desc",
        category="cat",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    result_mock = MagicMock()
    result_mock.scalar_one_or_none.return_value = db_artifact
    session.execute.return_value = result_mock
    
    # Retrieve
    result = await secure_manager.get_artifact("api_key")
    
    assert result is not None
    assert result["key"] == "api_key"
    assert result["value"] == "secret-value"

@pytest.mark.asyncio
async def test_list_artifacts(secure_manager, mock_session_factory):
    """Test listing artifacts (metadata only)."""
    session = mock_session_factory.return_value.__aenter__.return_value
    
    # Mock db artifacts
    artifacts = [
        SecureArtifact(key="k1", encrypted_value="e1", category="c1"),
        SecureArtifact(key="k2", encrypted_value="e2", category="c2")
    ]
    
    result_mock = MagicMock()
    result_mock.scalars.return_value.all.return_value = artifacts
    session.execute.return_value = result_mock
    
    # List
    results = await secure_manager.list_artifacts()
    
    assert len(results) == 2
    assert "value" not in results[0] # Should not return decrypted value
    assert results[0]["key"] == "k1"

@pytest.mark.asyncio
async def test_key_rotation(secure_manager, mock_session_factory):
    """Test key rotation logic."""
    session = mock_session_factory.return_value.__aenter__.return_value
    
    # Setup artifact with OLD key
    old_secret = "test-secret-key-123"
    new_secret = "new-super-secret-key-999"
    
    # Ensure manager uses old key initially
    secure_manager.settings.secret_key = old_secret
    secure_manager._fernet = secure_manager._get_fernet_instance()
    
    original_value = "my-secret-data"
    encrypted_with_old = secure_manager._encrypt(original_value)
    
    artifact = SecureArtifact(key="k1", encrypted_value=encrypted_with_old)
    
    # Mock fetching
    result_mock = MagicMock()
    result_mock.scalars.return_value.all.return_value = [artifact]
    session.execute.return_value = result_mock
    
    # Rotate
    count = await secure_manager.rotate_keys(new_secret)
    
    assert count == 1
    # Artifact should now be encrypted with NEW key
    # Current manager should also be updated
    assert secure_manager.settings.secret_key == new_secret
    
    # Verify we can decrypt with new manager state
    decrypted = secure_manager._decrypt(artifact.encrypted_value)
    assert decrypted == original_value

# API Tests

def test_api_store_artifact(client, secure_manager):
    """Test POST /secure/artifacts"""
    # Mock manager response
    secure_manager.store_artifact = AsyncMock(return_value=SecureArtifact(
        key="api_key_1",
        encrypted_value="enc_val",
        description="Test Key",
        category="api",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    ))
    
    response = client.post("/secure/artifacts", json={
        "key": "api_key_1",
        "value": "super_secret",
        "description": "Test Key",
        "category": "api"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["key"] == "api_key_1"
    assert "value" not in data # Should not return value in store response
    secure_manager.store_artifact.assert_called_once()

def test_api_get_artifact(client, secure_manager):
    """Test GET /secure/artifacts/{key}"""
    # Mock manager response
    secure_manager.get_artifact = AsyncMock(return_value={
        "key": "api_key_1",
        "value": "super_secret",
        "description": "Test Key",
        "category": "api",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    })
    
    response = client.get("/secure/artifacts/api_key_1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["key"] == "api_key_1"
    assert data["value"] == "super_secret"
    secure_manager.get_artifact.assert_called_once_with("api_key_1")

def test_api_get_artifact_not_found(client, secure_manager):
    """Test GET /secure/artifacts/{key} not found"""
    secure_manager.get_artifact = AsyncMock(return_value=None)
    
    response = client.get("/secure/artifacts/missing_key")
    
    assert response.status_code == 404

def test_api_list_artifacts(client, secure_manager):
    """Test GET /secure/artifacts"""
    secure_manager.list_artifacts = AsyncMock(return_value=[
        {
            "key": "k1",
            "description": "d1",
            "category": "c1",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
    ])
    
    response = client.get("/secure/artifacts")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["key"] == "k1"

def test_api_delete_artifact(client, secure_manager):
    """Test DELETE /secure/artifacts/{key}"""
    secure_manager.delete_artifact = AsyncMock(return_value=True)
    
    response = client.delete("/secure/artifacts/k1")
    
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_api_rotate_keys(client, secure_manager):
    """Test POST /secure/rotate-keys"""
    secure_manager.rotate_keys = AsyncMock(return_value=5)
    
    response = client.post("/secure/rotate-keys", params={"new_secret_key": "new_secret"})
    
    assert response.status_code == 200
    assert response.json()["rotated_count"] == 5
