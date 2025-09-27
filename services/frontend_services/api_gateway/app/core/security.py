"""
Security utilities for the API Gateway service.
Handles JWT token creation, validation, and user authentication.
"""
from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel, Field

from app.core.config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    Decode a JWT token.
    
    Args:
        token: JWT token string
        
    Returns:
        Token payload
    """
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return TokenPayload(**payload)
