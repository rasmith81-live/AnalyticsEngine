import logging
import time
from typing import Dict, List, Optional
from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import JSONResponse, RedirectResponse
from jose import jwt, jwk
from pydantic import BaseModel
import uuid
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger(__name__)

router = APIRouter()

# --- Configuration ---
# In a real scenario, these would be configurable per test/env
TENANT_ID = "mock-tenant-id"
ISSUER = f"http://localhost:8099/{TENANT_ID}/v2.0" # Mock service internal URL
# For external access (from other containers), we might need to adjust based on how they reach us.
# But auth.py uses the authority_url passed to it.

# --- Key Generation ---
# Generate a simplified RSA key pair for signing tokens on startup
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Serialize keys to PEM
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Create JWK for the public key
# This is a simplified JWK construction. In production use python-jose[cryptography] or similar helpers.
# However, python-jose jwk.construct can handle PEM
jwk_key = jwk.construct(public_pem.decode('utf-8'), algorithm="RS256")
KEY_ID = "mock-key-id-1"

# --- Models ---

class TokenRequest(BaseModel):
    grant_type: str = Form(...)
    client_id: str = Form(...)
    client_secret: Optional[str] = Form(None)
    code: Optional[str] = Form(None)
    redirect_uri: Optional[str] = Form(None)
    refresh_token: Optional[str] = Form(None)
    scope: Optional[str] = Form(None)

# --- In-Memory Storage ---
auth_codes: Dict[str, Dict] = {} # code -> {client_id, redirect_uri, nonce, ...}

# --- Endpoints ---

@router.get("/{tenant_id}/v2.0/.well-known/openid-configuration")
async def openid_configuration(tenant_id: str, request: Request):
    base_url = str(request.base_url).rstrip("/")
    # Adjust base_url if running in container but accessed via localhost or vice versa
    # For now, rely on request.base_url
    
    return {
        "issuer": f"{base_url}/{tenant_id}/v2.0",
        "authorization_endpoint": f"{base_url}/{tenant_id}/oauth2/v2.0/authorize",
        "token_endpoint": f"{base_url}/{tenant_id}/oauth2/v2.0/token",
        "jwks_uri": f"{base_url}/{tenant_id}/discovery/v2.0/keys",
        "response_types_supported": ["code", "id_token", "token id_token"],
        "subject_types_supported": ["pairwise"],
        "id_token_signing_alg_values_supported": ["RS256"],
        "scopes_supported": ["openid", "profile", "email", "offline_access"],
        "token_endpoint_auth_methods_supported": ["client_secret_post", "client_secret_basic"],
        "claims_supported": ["sub", "iss", "cloud_instance_name", "cloud_instance_host_name", "cloud_graph_host_name", "msgraph_host", "aud", "exp", "iat", "auth_time", "nonce", "email", "name", "tid", "ver", "at_hash", "c_hash", "preferred_username"]
    }

@router.get("/{tenant_id}/discovery/v2.0/keys")
async def jwks(tenant_id: str):
    return {
        "keys": [
            {
                "kty": "RSA",
                "use": "sig",
                "kid": KEY_ID,
                "n": jwk_key.to_dict().get("n"),
                "e": jwk_key.to_dict().get("e"),
                "alg": "RS256"
            }
        ]
    }

@router.get("/{tenant_id}/oauth2/v2.0/authorize")
async def authorize(
    tenant_id: str,
    client_id: str,
    response_type: str,
    redirect_uri: str,
    scope: str,
    state: Optional[str] = None,
    nonce: Optional[str] = None
):
    # Mock auto-login behavior
    # In a real interactive mock, we might show a login page.
    # Here we assume auto-approval for testing.
    
    code = str(uuid.uuid4())
    auth_codes[code] = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "nonce": nonce,
        "tenant_id": tenant_id
    }
    
    # Redirect back with code
    separator = "&" if "?" in redirect_uri else "?"
    location = f"{redirect_uri}{separator}code={code}"
    if state:
        location += f"&state={state}"
        
    logger.info(f"Mock Authorize: Auto-approving for client {client_id}. Redirecting to {location}")
    return RedirectResponse(url=location, status_code=302)

@router.post("/{tenant_id}/oauth2/v2.0/token")
async def token(
    tenant_id: str,
    request: Request
):
    form_data = await request.form()
    grant_type = form_data.get("grant_type")
    client_id = form_data.get("client_id")
    
    if grant_type == "authorization_code":
        code = form_data.get("code")
        stored_auth = auth_codes.get(code)
        
        if not stored_auth:
            raise HTTPException(status_code=400, detail="Invalid authorization code")
        
        # Verify redirect_uri matches
        if stored_auth["redirect_uri"] != form_data.get("redirect_uri"):
             raise HTTPException(status_code=400, detail="Redirect URI mismatch")

        # Generate Tokens
        now = int(time.time())
        
        # ID Token
        id_token_claims = {
            "aud": client_id,
            "iss": f"{str(request.base_url).rstrip('/')}/{tenant_id}/v2.0",
            "iat": now,
            "nbf": now,
            "exp": now + 3600,
            "sub": "mock-user-id",
            "name": "Mock User",
            "preferred_username": "mockuser@example.com",
            "email": "mockuser@example.com",
            "tid": tenant_id,
            "ver": "2.0",
            "nonce": stored_auth.get("nonce", "")
        }
        
        id_token = jwt.encode(
            id_token_claims, 
            private_pem.decode('utf-8'), 
            algorithm="RS256", 
            headers={"kid": KEY_ID}
        )
        
        # Access Token (Simulated)
        access_token_claims = {
            "aud": "https://graph.microsoft.com", # Default audience for Graph
            "iss": f"{str(request.base_url).rstrip('/')}/{tenant_id}/v2.0",
            "iat": now,
            "nbf": now,
            "exp": now + 3600,
            "sub": "mock-user-id",
            "scp": stored_auth.get("scope", "User.Read"),
            "appid": client_id
        }
        
        access_token = jwt.encode(
            access_token_claims,
            private_pem.decode('utf-8'),
            algorithm="RS256",
            headers={"kid": KEY_ID}
        )
        
        # Remove used code
        del auth_codes[code]
        
        return {
            "token_type": "Bearer",
            "scope": stored_auth.get("scope"),
            "expires_in": 3600,
            "ext_expires_in": 3600,
            "access_token": access_token,
            "id_token": id_token,
            "refresh_token": str(uuid.uuid4()) # Mock refresh token
        }
        
    elif grant_type == "refresh_token":
        # Simplified refresh
        now = int(time.time())
        access_token_claims = {
            "aud": "https://graph.microsoft.com",
            "iss": f"{str(request.base_url).rstrip('/')}/{tenant_id}/v2.0",
            "iat": now,
            "nbf": now,
            "exp": now + 3600,
            "sub": "mock-user-id",
            "scp": "User.Read",
            "appid": client_id
        }
        access_token = jwt.encode(
            access_token_claims,
            private_pem.decode('utf-8'),
            algorithm="RS256",
            headers={"kid": KEY_ID}
        )
        return {
            "token_type": "Bearer",
            "scope": "User.Read",
            "expires_in": 3600,
            "ext_expires_in": 3600,
            "access_token": access_token,
            "refresh_token": str(uuid.uuid4())
        }
        
    else:
        raise HTTPException(status_code=400, detail="Unsupported grant_type")

# --- Microsoft Graph Mock Endpoints ---

@router.get("/v1.0/me")
async def get_me(request: Request):
    # Verify token exists (simplified)
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    return {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
        "businessPhones": [],
        "displayName": "Mock User",
        "givenName": "Mock",
        "jobTitle": "Developer",
        "mail": "mockuser@example.com",
        "mobilePhone": None,
        "officeLocation": None,
        "preferredLanguage": "en-US",
        "surname": "User",
        "userPrincipalName": "mockuser@example.com",
        "id": "mock-user-id"
    }

@router.get("/v1.0/me/memberOf")
async def get_member_of(request: Request):
    # Verify token exists (simplified)
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    return {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#directoryObjects",
        "value": [
            {
                "@odata.type": "#microsoft.graph.group",
                "id": "mock-group-id-1",
                "displayName": "Mock Users",
                "description": "All mock users"
            },
            {
                "@odata.type": "#microsoft.graph.group",
                "id": "mock-group-id-admin",
                "displayName": "Mock Admins",
                "description": "Mock Administrators"
            }
        ]
    }
