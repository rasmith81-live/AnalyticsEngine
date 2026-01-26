"""
Secrets Manager

Fetches secrets from database_service's secure_storage API with environment fallback.
This provides a unified way to retrieve sensitive credentials for both production
and development environments.

Production: Fetches encrypted secrets from database_service
Development: Falls back to environment variables if secure_storage unavailable
"""

import asyncio
import logging
import os
from typing import Dict, Optional
from datetime import datetime, timedelta

import httpx

logger = logging.getLogger(__name__)


class SecretsManager:
    """
    Manages retrieval of secrets from secure storage with caching and fallback.
    
    Priority order:
    1. Cached value (if not expired)
    2. Secure storage via database_service API
    3. Environment variable fallback
    """
    
    _instance: Optional["SecretsManager"] = None
    _lock = asyncio.Lock()
    
    def __init__(
        self,
        database_service_url: Optional[str] = None,
        cache_ttl_seconds: int = 300,  # 5 minutes
        request_timeout_seconds: float = 5.0
    ):
        self._database_service_url = database_service_url or os.getenv(
            "DATABASE_SERVICE_URL", "http://database_service:8025"
        )
        self._cache_ttl = timedelta(seconds=cache_ttl_seconds)
        self._request_timeout = request_timeout_seconds
        self._cache: Dict[str, Dict] = {}  # key -> {value, expires_at}
        self._initialized = False
    
    @classmethod
    async def get_instance(cls) -> "SecretsManager":
        """Get or create singleton instance."""
        if cls._instance is None:
            async with cls._lock:
                if cls._instance is None:
                    cls._instance = SecretsManager()
        return cls._instance
    
    def _is_cached(self, key: str) -> bool:
        """Check if key is in cache and not expired."""
        if key not in self._cache:
            return False
        return datetime.utcnow() < self._cache[key]["expires_at"]
    
    def _get_cached(self, key: str) -> Optional[str]:
        """Get cached value if valid."""
        if self._is_cached(key):
            return self._cache[key]["value"]
        return None
    
    def _set_cache(self, key: str, value: str) -> None:
        """Cache a value with TTL."""
        self._cache[key] = {
            "value": value,
            "expires_at": datetime.utcnow() + self._cache_ttl
        }
    
    async def _fetch_from_secure_storage(self, key: str) -> Optional[str]:
        """Fetch secret from database_service secure storage API."""
        url = f"{self._database_service_url}/secure/artifacts/{key}"
        
        try:
            async with httpx.AsyncClient(timeout=self._request_timeout) as client:
                response = await client.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    value = data.get("value")
                    if value:
                        logger.info(f"Successfully retrieved secret '{key}' from secure storage")
                        return value
                elif response.status_code == 404:
                    logger.debug(f"Secret '{key}' not found in secure storage")
                else:
                    logger.warning(
                        f"Unexpected response from secure storage for '{key}': "
                        f"status={response.status_code}"
                    )
        except httpx.ConnectError:
            logger.debug(f"Could not connect to database_service for secret '{key}'")
        except httpx.TimeoutException:
            logger.warning(f"Timeout fetching secret '{key}' from secure storage")
        except Exception as e:
            logger.warning(f"Error fetching secret '{key}' from secure storage: {e}")
        
        return None
    
    def _get_env_fallback(self, key: str) -> Optional[str]:
        """Get secret from environment variable."""
        value = os.getenv(key, "")
        if value:
            logger.debug(f"Using environment variable fallback for '{key}'")
            return value
        return None
    
    async def get_secret(self, key: str, use_cache: bool = True) -> Optional[str]:
        """
        Get a secret value.
        
        Args:
            key: Secret key (e.g., "ANTHROPIC_API_KEY")
            use_cache: Whether to use cached value if available
            
        Returns:
            Secret value or None if not found
        """
        # 1. Check cache
        if use_cache:
            cached = self._get_cached(key)
            if cached:
                logger.debug(f"Using cached value for '{key}'")
                return cached
        
        # 2. Try secure storage
        value = await self._fetch_from_secure_storage(key)
        if value:
            self._set_cache(key, value)
            return value
        
        # 3. Fall back to environment
        value = self._get_env_fallback(key)
        if value:
            self._set_cache(key, value)
            return value
        
        logger.warning(f"Secret '{key}' not found in secure storage or environment")
        return None
    
    async def get_secret_sync_wrapper(self, key: str) -> Optional[str]:
        """
        Synchronous wrapper for get_secret.
        Creates event loop if needed (for use in sync contexts).
        """
        try:
            loop = asyncio.get_running_loop()
            return await self.get_secret(key)
        except RuntimeError:
            # No running loop, create one
            return asyncio.run(self.get_secret(key))
    
    def clear_cache(self, key: Optional[str] = None) -> None:
        """Clear cache for a specific key or all keys."""
        if key:
            self._cache.pop(key, None)
        else:
            self._cache.clear()
    
    async def store_secret(self, key: str, value: str, description: Optional[str] = None, category: str = "api_keys") -> bool:
        """
        Store a secret in secure storage.
        
        Args:
            key: Secret key
            value: Secret value
            description: Optional description
            category: Category for organization
            
        Returns:
            True if stored successfully
        """
        url = f"{self._database_service_url}/secure/artifacts"
        payload = {
            "key": key,
            "value": value,
            "description": description,
            "category": category
        }
        
        try:
            async with httpx.AsyncClient(timeout=self._request_timeout) as client:
                response = await client.post(url, json=payload)
                
                if response.status_code == 200:
                    logger.info(f"Successfully stored secret '{key}' in secure storage")
                    self._set_cache(key, value)
                    return True
                else:
                    logger.error(
                        f"Failed to store secret '{key}': status={response.status_code}"
                    )
        except Exception as e:
            logger.error(f"Error storing secret '{key}': {e}")
        
        return False


# Convenience functions for direct use
_secrets_manager: Optional[SecretsManager] = None


async def get_secrets_manager() -> SecretsManager:
    """Get the global secrets manager instance."""
    global _secrets_manager
    if _secrets_manager is None:
        _secrets_manager = await SecretsManager.get_instance()
    return _secrets_manager


async def get_secret(key: str) -> Optional[str]:
    """Convenience function to get a secret."""
    manager = await get_secrets_manager()
    return await manager.get_secret(key)


async def get_anthropic_api_key() -> str:
    """Get the Anthropic API key from secure storage or environment."""
    manager = await get_secrets_manager()
    key = await manager.get_secret("ANTHROPIC_API_KEY")
    return key or ""
