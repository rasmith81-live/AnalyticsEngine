"""
Admin API endpoints for API key management.
Provides secure storage and verification of API keys.
"""
import logging
from typing import Optional
from pydantic import BaseModel, Field

from fastapi import APIRouter, HTTPException
import httpx

logger = logging.getLogger(__name__)

router = APIRouter()

DATABASE_SERVICE_URL = "http://database_service:8000"
CONVERSATION_SERVICE_URL = "http://conversation_service:8000"


class ApiKeyRequest(BaseModel):
    """Request model for storing an API key."""
    api_key: str = Field(..., description="The API key to store")


class ApiKeyStatusResponse(BaseModel):
    """Response model for API key status."""
    configured: bool = Field(..., description="Whether the API key is configured")
    valid: bool = Field(False, description="Whether the API key is valid")
    message: str = Field("", description="Status message")


class ApiKeySaveResponse(BaseModel):
    """Response model for saving an API key."""
    success: bool = Field(..., description="Whether the save was successful")
    valid: bool = Field(False, description="Whether the API key was verified as valid")
    message: str = Field("", description="Status message")


@router.get("/api-keys/anthropic/status", response_model=ApiKeyStatusResponse)
async def get_anthropic_api_key_status():
    """
    Check if the Anthropic API key is configured and valid.
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{DATABASE_SERVICE_URL}/secure/artifacts/ANTHROPIC_API_KEY"
            )
            
            if response.status_code == 404:
                return ApiKeyStatusResponse(
                    configured=False,
                    valid=False,
                    message="Anthropic API key not configured"
                )
            
            if response.status_code != 200:
                logger.warning(f"Unexpected response from secure storage: {response.status_code}")
                return ApiKeyStatusResponse(
                    configured=False,
                    valid=False,
                    message="Unable to check API key status"
                )
            
            # Key exists, now verify it works
            api_key = response.json().get("value", "")
            if not api_key:
                return ApiKeyStatusResponse(
                    configured=False,
                    valid=False,
                    message="API key value is empty"
                )
            
            # Verify the key with Anthropic
            is_valid = await _verify_anthropic_key(api_key)
            
            return ApiKeyStatusResponse(
                configured=True,
                valid=is_valid,
                message="API key is valid" if is_valid else "API key is configured but failed verification"
            )
            
    except httpx.ConnectError:
        logger.error("Could not connect to database service")
        return ApiKeyStatusResponse(
            configured=False,
            valid=False,
            message="Could not connect to database service"
        )
    except Exception as e:
        logger.error(f"Error checking API key status: {e}")
        return ApiKeyStatusResponse(
            configured=False,
            valid=False,
            message=f"Error: {str(e)}"
        )


@router.post("/api-keys/anthropic", response_model=ApiKeySaveResponse)
async def save_anthropic_api_key(request: ApiKeyRequest):
    """
    Save the Anthropic API key to secure storage and verify it works.
    """
    api_key = request.api_key.strip()
    
    if not api_key:
        raise HTTPException(status_code=400, detail="API key cannot be empty")
    
    if not api_key.startswith("sk-ant-"):
        raise HTTPException(status_code=400, detail="Invalid Anthropic API key format")
    
    try:
        # First verify the key is valid
        is_valid = await _verify_anthropic_key(api_key)
        
        # Store the key in secure storage regardless of validation
        # (user may want to store now and fix issues later)
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                f"{DATABASE_SERVICE_URL}/secure/artifacts",
                json={
                    "key": "ANTHROPIC_API_KEY",
                    "value": api_key,
                    "description": "Anthropic Claude API key for AI conversation features",
                    "category": "api_keys"
                }
            )
            
            if response.status_code != 200:
                logger.error(f"Failed to store API key: {response.status_code} - {response.text}")
                raise HTTPException(
                    status_code=500,
                    detail="Failed to store API key in secure storage"
                )
        
        # Clear the secrets cache in conversation service so it picks up the new key
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                await client.post(f"{CONVERSATION_SERVICE_URL}/admin/clear-secrets-cache")
        except Exception as e:
            logger.warning(f"Could not clear secrets cache: {e}")
        
        return ApiKeySaveResponse(
            success=True,
            valid=is_valid,
            message="API key saved and verified successfully" if is_valid else "API key saved but verification failed"
        )
        
    except HTTPException:
        raise
    except httpx.ConnectError:
        logger.error("Could not connect to database service")
        raise HTTPException(status_code=503, detail="Could not connect to database service")
    except Exception as e:
        logger.error(f"Error saving API key: {e}")
        raise HTTPException(status_code=500, detail=str(e))


async def _verify_anthropic_key(api_key: str) -> bool:
    """
    Verify an Anthropic API key by making a simple API call.
    """
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json"
                },
                json={
                    "model": "claude-3-haiku-20240307",
                    "max_tokens": 10,
                    "messages": [{"role": "user", "content": "Hi"}]
                }
            )
            
            # 200 = success, key is valid
            # 401 = invalid key
            # 400 = bad request (but key might be valid)
            # 429 = rate limited (key is valid but rate limited)
            
            if response.status_code == 200:
                logger.info("Anthropic API key verification successful")
                return True
            elif response.status_code == 401:
                logger.warning("Anthropic API key is invalid (401)")
                return False
            elif response.status_code == 429:
                # Rate limited but key is valid
                logger.info("Anthropic API key valid but rate limited")
                return True
            else:
                logger.warning(f"Anthropic API verification returned {response.status_code}")
                # For other errors, assume key might be valid
                return response.status_code != 401
                
    except Exception as e:
        logger.error(f"Error verifying Anthropic API key: {e}")
        return False
