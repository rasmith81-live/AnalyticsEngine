"""
Azure AD SSO Service - Authentication

Handles OAuth/OIDC authentication with Azure AD, token validation, and user info retrieval.
"""

import jwt
import httpx
from datetime import datetime, timedelta
from typing import Dict, Optional, Any
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class AzureADAuthProvider:
    """
    Azure AD Authentication Provider
    
    Handles OAuth 2.0 / OpenID Connect authentication flow with Azure AD.
    """
    
    def __init__(
        self,
        tenant_id: str,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        authority_url: Optional[str] = None
    ):
        """
        Initialize Azure AD Auth Provider.
        
        Args:
            tenant_id: Azure AD Tenant ID
            client_id: Application (Client) ID
            client_secret: Application Secret
            redirect_uri: OAuth redirect URI
            authority_url: Optional custom authority URL
        """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        
        # Set authority URL
        if authority_url:
            self.authority_url = authority_url
        else:
            self.authority_url = f"https://login.microsoftonline.com/{tenant_id}"
        
        # OAuth endpoints
        self.authorization_endpoint = f"{self.authority_url}/oauth2/v2.0/authorize"
        self.token_endpoint = f"{self.authority_url}/oauth2/v2.0/token"
        self.jwks_uri = f"{self.authority_url}/discovery/v2.0/keys"
        self.userinfo_endpoint = "https://graph.microsoft.com/v1.0/me"
        
        # Default scopes
        self.default_scopes = [
            "openid",
            "profile",
            "email",
            "User.Read",
            "Group.Read.All"
        ]
    
    def get_authorization_url(
        self,
        state: Optional[str] = None,
        scopes: Optional[list] = None
    ) -> str:
        """
        Generate authorization URL for OAuth flow.
        
        Args:
            state: Optional state parameter for CSRF protection
            scopes: Optional list of scopes to request
            
        Returns:
            Authorization URL
        """
        scopes_str = " ".join(scopes or self.default_scopes)
        
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "response_mode": "query",
            "scope": scopes_str,
        }
        
        if state:
            params["state"] = state
        
        # Build query string
        query_params = "&".join([f"{k}={v}" for k, v in params.items()])
        return f"{self.authorization_endpoint}?{query_params}"
    
    async def exchange_code_for_token(self, authorization_code: str) -> Dict[str, Any]:
        """
        Exchange authorization code for access token.
        
        Args:
            authorization_code: Authorization code from OAuth callback
            
        Returns:
            Token response containing access_token, id_token, refresh_token, etc.
        """
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": authorization_code,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(self.token_endpoint, data=data)
            response.raise_for_status()
            return response.json()
    
    async def refresh_access_token(self, refresh_token: str) -> Dict[str, Any]:
        """
        Refresh access token using refresh token.
        
        Args:
            refresh_token: Refresh token
            
        Returns:
            New token response
        """
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(self.token_endpoint, data=data)
            response.raise_for_status()
            return response.json()
    
    async def get_user_info(self, access_token: str) -> Dict[str, Any]:
        """
        Get user information from Microsoft Graph API.
        
        Args:
            access_token: Access token
            
        Returns:
            User information
        """
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(self.userinfo_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
    
    async def get_user_groups(self, access_token: str) -> list:
        """
        Get user's group memberships from Microsoft Graph API.
        
        Args:
            access_token: Access token
            
        Returns:
            List of groups
        """
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        groups_endpoint = "https://graph.microsoft.com/v1.0/me/memberOf"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(groups_endpoint, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data.get("value", [])
    
    async def validate_token(self, token: str) -> Dict[str, Any]:
        """
        Validate JWT token.
        
        Args:
            token: JWT token to validate
            
        Returns:
            Decoded token claims
            
        Raises:
            jwt.InvalidTokenError: If token is invalid
        """
        # Get signing keys from Azure AD
        async with httpx.AsyncClient() as client:
            response = await client.get(self.jwks_uri)
            response.raise_for_status()
            jwks = response.json()
        
        # Decode token header to get key ID
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        
        # Find matching key
        signing_key = None
        for key in jwks.get("keys", []):
            if key.get("kid") == kid:
                signing_key = key
                break
        
        if not signing_key:
            raise jwt.InvalidTokenError("Unable to find signing key")
        
        # Verify and decode token
        decoded_token = jwt.decode(
            token,
            key=signing_key,
            algorithms=["RS256"],
            audience=self.client_id,
            issuer=f"{self.authority_url}/v2.0"
        )
        
        return decoded_token
    
    async def logout_url(self, post_logout_redirect_uri: Optional[str] = None) -> str:
        """
        Generate logout URL.
        
        Args:
            post_logout_redirect_uri: Optional redirect URI after logout
            
        Returns:
            Logout URL
        """
        logout_endpoint = f"{self.authority_url}/oauth2/v2.0/logout"
        
        if post_logout_redirect_uri:
            return f"{logout_endpoint}?post_logout_redirect_uri={post_logout_redirect_uri}"
        
        return logout_endpoint


async def validate_token(
    token: str,
    tenant_id: str,
    client_id: str
) -> Dict[str, Any]:
    """
    Validate Azure AD JWT token.
    
    Args:
        token: JWT token
        tenant_id: Azure AD Tenant ID
        client_id: Application Client ID
        
    Returns:
        Decoded token claims
    """
    authority_url = f"https://login.microsoftonline.com/{tenant_id}"
    jwks_uri = f"{authority_url}/discovery/v2.0/keys"
    
    # Get signing keys
    async with httpx.AsyncClient() as client:
        response = await client.get(jwks_uri)
        response.raise_for_status()
        jwks = response.json()
    
    # Decode and verify token
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")
    
    signing_key = None
    for key in jwks.get("keys", []):
        if key.get("kid") == kid:
            signing_key = key
            break
    
    if not signing_key:
        raise jwt.InvalidTokenError("Unable to find signing key")
    
    decoded_token = jwt.decode(
        token,
        key=signing_key,
        algorithms=["RS256"],
        audience=client_id,
        issuer=f"{authority_url}/v2.0"
    )
    
    return decoded_token


async def get_user_info(access_token: str) -> Dict[str, Any]:
    """
    Get user information from Microsoft Graph API.
    
    Args:
        access_token: Access token
        
    Returns:
        User information
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    userinfo_endpoint = "https://graph.microsoft.com/v1.0/me"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(userinfo_endpoint, headers=headers)
        response.raise_for_status()
        return response.json()


async def refresh_access_token(
    refresh_token: str,
    tenant_id: str,
    client_id: str,
    client_secret: str
) -> Dict[str, Any]:
    """
    Refresh access token.
    
    Args:
        refresh_token: Refresh token
        tenant_id: Azure AD Tenant ID
        client_id: Application Client ID
        client_secret: Application Secret
        
    Returns:
        New token response
    """
    token_endpoint = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(token_endpoint, data=data)
        response.raise_for_status()
        return response.json()


class TokenManager:
    """
    Manages token storage, validation, and refresh.
    """
    
    def __init__(self):
        self.tokens: Dict[str, Dict[str, Any]] = {}
    
    def store_token(
        self,
        user_id: str,
        access_token: str,
        refresh_token: str,
        expires_in: int
    ):
        """Store tokens for a user."""
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
        
        self.tokens[user_id] = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": expires_at
        }
    
    def get_token(self, user_id: str) -> Optional[str]:
        """Get valid access token for a user."""
        token_data = self.tokens.get(user_id)
        
        if not token_data:
            return None
        
        # Check if token is expired
        if datetime.utcnow() >= token_data["expires_at"]:
            return None
        
        return token_data["access_token"]
    
    def get_refresh_token(self, user_id: str) -> Optional[str]:
        """Get refresh token for a user."""
        token_data = self.tokens.get(user_id)
        return token_data.get("refresh_token") if token_data else None
    
    def remove_token(self, user_id: str):
        """Remove tokens for a user."""
        if user_id in self.tokens:
            del self.tokens[user_id]
    
    def is_token_expired(self, user_id: str) -> bool:
        """Check if token is expired."""
        token_data = self.tokens.get(user_id)
        
        if not token_data:
            return True
        
        return datetime.utcnow() >= token_data["expires_at"]
