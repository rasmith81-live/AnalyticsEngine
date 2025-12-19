"""
Security utilities for the API Gateway service.
Handles JWT token creation, validation, and user authentication.
"""
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union

import time
import httpx
from jose import jwt, jwk
from jose.utils import base64url_decode
from passlib.context import CryptContext
from pydantic import BaseModel, Field

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWKS Cache
_jwks_cache: Dict[str, Any] = {}
_jwks_cache_expiry: float = 0

# Token models using Pydantic v2
class Token(BaseModel):
    """Token response model."""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field("bearer", description="Token type")

class TokenPayload(BaseModel):
    """Token payload model."""
    sub: Optional[str] = Field(None, description="Subject (user ID)")
    exp: Optional[datetime] = Field(None, description="Expiration time")
    roles: list[str] = Field(default_factory=list, description="User roles")
    # OIDC specific claims
    iss: Optional[str] = Field(None, description="Issuer")
    aud: Optional[Union[str, List[str]]] = Field(None, description="Audience")

def create_access_token(
    subject: Union[str, Any], expires_delta: Optional[timedelta] = None, roles: list[str] = None
) -> str:
    """
    Create a JWT access token.
    
    Args:
        subject: Subject of the token (usually user ID)
        expires_delta: Optional expiration time delta
        roles: List of user roles
        
    Returns:
        JWT token string
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    if roles:
        to_encode["roles"] = roles
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hash.
    
    Args:
        plain_password: Plain text password
        hashed_password: Hashed password
        
    Returns:
        True if the password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hash a password.
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return pwd_context.hash(password)

def decode_token(token: str) -> TokenPayload:
    """
    Decode a JWT token (Legacy HS256).
    
    Args:
        token: JWT token string
        
    Returns:
        Token payload
    """
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return TokenPayload(**payload)

async def get_jwks() -> Dict[str, Any]:
    """Fetch JWKS with caching."""
    global _jwks_cache, _jwks_cache_expiry
    
    now = time.time()
    if _jwks_cache and now < _jwks_cache_expiry:
        return _jwks_cache
        
    if not settings.OIDC_JWKS_URI:
        raise ValueError("OIDC_JWKS_URI is not configured")
        
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.OIDC_JWKS_URI, timeout=10.0)
            response.raise_for_status()
            _jwks_cache = response.json()
            _jwks_cache_expiry = now + 300  # Cache for 5 minutes
            logger.info("Refreshed JWKS cache")
            return _jwks_cache
    except Exception as e:
        logger.error(f"Failed to fetch JWKS: {e}")
        # Return stale cache if available, else raise
        if _jwks_cache:
            return _jwks_cache
        raise

async def verify_token(token: str) -> TokenPayload:
    """
    Verify a token (Supports both HS256 and OIDC/RS256).
    
    Args:
        token: JWT token string
        
    Returns:
        Token payload
    """
    if settings.AUTH_METHOD == "oidc":
        # Get Key ID from header
        try:
            header = jwt.get_unverified_header(token)
            kid = header.get("kid")
            if not kid:
                raise ValueError("Token header missing 'kid'")
                
            jwks = await get_jwks()
            key = None
            for k in jwks.get("keys", []):
                if k.get("kid") == kid:
                    key = k
                    break
            
            if not key:
                raise ValueError(f"Signing key not found for kid={kid}")
                
            # Verify signature
            payload = jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=settings.OIDC_CLIENT_ID,
                issuer=settings.OIDC_ISSUER,
                options={"verify_at_hash": False} # Skip at_hash for now
            )
            return TokenPayload(**payload)
            
        except Exception as e:
            logger.warning(f"OIDC Token validation failed: {e}")
            raise
    else:
        # Fallback to HS256
        return decode_token(token)
