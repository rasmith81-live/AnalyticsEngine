
import jwt
from datetime import datetime
import sys

secret = "secret"
payload = {
    "sub": "client_1",
    "iat": int(datetime.utcnow().timestamp()),
    "exp": int(datetime.utcnow().timestamp()) + 3600
}

print(f"Payload: {payload}")

try:
    token = jwt.encode(payload, secret, algorithm="HS256")
    print(f"Token type: {type(token)}")
    print(f"Token: {token}")
    
    decoded = jwt.decode(token, secret, algorithms=["HS256"])
    print(f"Decoded: {decoded}")
    print("SUCCESS")
except Exception as e:
    print(f"ERROR: {e}")
