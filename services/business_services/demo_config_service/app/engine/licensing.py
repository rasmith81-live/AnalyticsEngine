
"""
License Management Engine
Handles generation and validation of cryptographic license keys.
"""
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime
import jwt
import hashlib

class LicenseKeyGenerator:
    """Generates signed license keys."""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        
    def generate_key(
        self,
        client_id: str,
        modules: List[str],
        expiration_date: datetime
    ) -> str:
        """
        Generate a signed license key (JWT).
        
        Args:
            client_id: Client identifier
            modules: List of enabled modules
            expiration_date: License expiration
            
        Returns:
            Signed JWT string acting as license key
        """
        payload = {
            "sub": client_id,
            "modules": modules,
            "exp": int(expiration_date.timestamp()),
            "iat": int(datetime.utcnow().timestamp()) - 60,  # Backdate 60s to ensure validity
            "iss": "AnalyticsEngine"
        }
        
        # Use HS256 for symmetric signing
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return token

class LicenseValidator:
    """Validates license keys."""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        
    def validate_key(self, key: str) -> Tuple[bool, Dict[str, Any]]:
        """
        Validate a license key.
        
        Args:
            key: License key string
            
        Returns:
            Tuple of (is_valid, claims)
        """
        try:
            claims = jwt.decode(
                key,
                self.secret_key,
                algorithms=["HS256"],
                options={"verify_exp": True, "verify_iat": False},
                leeway=10
            )
            
            # Map 'sub' back to client_id for convenience
            claims["client_id"] = claims["sub"]
            
            return True, claims
            
        except jwt.ExpiredSignatureError:
            return False, {"error": "License expired"}
        except jwt.InvalidTokenError as e:
            return False, {"error": f"Invalid license key: {str(e)}"}
