"""
Secure Storage Manager
Handles encryption, decryption, and storage of sensitive artifacts.
"""
import logging
import base64
from typing import List, Optional, Dict, Any
from datetime import datetime
import hashlib

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from app.config import get_settings
from app.base_models import SecureArtifact
from app.telemetry import trace_method, add_span_attributes

logger = logging.getLogger(__name__)

class SecureStorageManager:
    """Manages secure storage of sensitive artifacts using encryption-at-rest."""

    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.settings = get_settings()
        self._fernet = self._get_fernet_instance()

    def _get_fernet_instance(self) -> Fernet:
        """
        Derive a Fernet key from the application secret key.
        Ensures a consistent 32-byte URL-safe base64-encoded key.
        """
        secret = self.settings.secret_key.encode()
        salt = b'secure_storage_salt' # In a real scenario, this might be dynamic or stored
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(secret))
        return Fernet(key)

    def _encrypt(self, value: str) -> str:
        """Encrypt a string value."""
        return self._fernet.encrypt(value.encode()).decode()

    def _decrypt(self, encrypted_value: str) -> str:
        """Decrypt a string value."""
        return self._fernet.decrypt(encrypted_value.encode()).decode()

    @trace_method(name="secure_storage.store_artifact")
    async def store_artifact(self, key: str, value: str, description: Optional[str] = None, category: str = "general") -> SecureArtifact:
        """Store or update a secure artifact."""
        async with self.session_factory() as session:
            async with session.begin():
                # Check if exists
                stmt = select(SecureArtifact).where(SecureArtifact.key == key)
                result = await session.execute(stmt)
                existing = result.scalar_one_or_none()

                encrypted_val = self._encrypt(value)

                if existing:
                    existing.encrypted_value = encrypted_val
                    existing.description = description
                    existing.category = category
                    # Updated_at is handled by mixin
                    artifact = existing
                    logger.info(f"Updated secure artifact: {key}")
                else:
                    artifact = SecureArtifact(
                        key=key,
                        encrypted_value=encrypted_val,
                        description=description,
                        category=category
                    )
                    session.add(artifact)
                    logger.info(f"Created secure artifact: {key}")
                
                await session.commit()
                return artifact

    @trace_method(name="secure_storage.get_artifact")
    async def get_artifact(self, key: str) -> Optional[Dict[str, Any]]:
        """Retrieve and decrypt a secure artifact."""
        async with self.session_factory() as session:
            stmt = select(SecureArtifact).where(SecureArtifact.key == key)
            result = await session.execute(stmt)
            artifact = result.scalar_one_or_none()

            if not artifact:
                return None

            try:
                decrypted_value = self._decrypt(artifact.encrypted_value)
                return {
                    "key": artifact.key,
                    "value": decrypted_value,
                    "description": artifact.description,
                    "category": artifact.category,
                    "created_at": artifact.created_at,
                    "updated_at": artifact.updated_at
                }
            except Exception as e:
                logger.error(f"Failed to decrypt artifact {key}: {e}")
                raise ValueError("Decryption failed")

    @trace_method(name="secure_storage.list_artifacts")
    async def list_artifacts(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """List artifacts (metadata only, no values)."""
        async with self.session_factory() as session:
            stmt = select(SecureArtifact)
            if category:
                stmt = stmt.where(SecureArtifact.category == category)
            
            result = await session.execute(stmt)
            artifacts = result.scalars().all()

            return [{
                "key": a.key,
                "description": a.description,
                "category": a.category,
                "created_at": a.created_at,
                "updated_at": a.updated_at
            } for a in artifacts]

    @trace_method(name="secure_storage.delete_artifact")
    async def delete_artifact(self, key: str) -> bool:
        """Delete a secure artifact."""
        async with self.session_factory() as session:
            async with session.begin():
                stmt = delete(SecureArtifact).where(SecureArtifact.key == key)
                result = await session.execute(stmt)
                await session.commit()
                return result.rowcount > 0

    @trace_method(name="secure_storage.rotate_keys")
    async def rotate_keys(self, new_secret_key: str) -> int:
        """
        Re-encrypt all artifacts with a new key.
        NOTE: This updates the application setting in memory for the duration of the rotation,
        but persistent config update is out of scope here.
        """
        # 1. Initialize new fernet
        old_fernet = self._fernet
        
        # Derive new key
        secret = new_secret_key.encode()
        salt = b'secure_storage_salt'
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
        key = base64.urlsafe_b64encode(kdf.derive(secret))
        new_fernet = Fernet(key)

        rotated_count = 0
        async with self.session_factory() as session:
            async with session.begin():
                # Fetch all artifacts
                result = await session.execute(select(SecureArtifact))
                artifacts = result.scalars().all()

                for artifact in artifacts:
                    try:
                        # Decrypt with old
                        decrypted = old_fernet.decrypt(artifact.encrypted_value.encode()).decode()
                        # Encrypt with new
                        artifact.encrypted_value = new_fernet.encrypt(decrypted.encode()).decode()
                        rotated_count += 1
                    except Exception as e:
                        logger.error(f"Failed to rotate key for artifact {artifact.key}: {e}")
                        # Continue or abort? For now, log and continue, but this might leave partial state
                        # Ideally this should be an all-or-nothing transaction
                
                await session.commit()
        
        # Update current instance
        self.settings.secret_key = new_secret_key
        self._fernet = new_fernet
        
        return rotated_count
