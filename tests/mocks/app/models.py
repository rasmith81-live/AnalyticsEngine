from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field

class MockResponse(BaseModel):
    status_code: int = 200
    headers: Dict[str, str] = {}
    body: Optional[Union[Dict[str, Any], str, list]] = None
    delay_ms: int = 0

class MockExpectation(BaseModel):
    id: Optional[str] = None
    method: str
    path: str
    response: MockResponse
    priority: int = 10
