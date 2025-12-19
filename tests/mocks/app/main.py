import logging
import asyncio
from typing import List, Dict, Optional
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
import uuid

from .models import MockExpectation, MockResponse
from .oidc import router as oidc_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Mock Service Container")

# Include OIDC Router
app.include_router(oidc_router)

# Store expectations in memory
expectations: List[MockExpectation] = []

@app.get("/_mock/health")
async def health_check():
    return {"status": "healthy", "expectations_count": len(expectations)}

@app.post("/_mock/expectations")
async def add_expectation(expectation: MockExpectation):
    if not expectation.id:
        expectation.id = str(uuid.uuid4())
    
    # Remove existing with same ID if present
    global expectations
    expectations = [e for e in expectations if e.id != expectation.id]
    
    expectations.append(expectation)
    # Sort by priority (descending)
    expectations.sort(key=lambda x: x.priority, reverse=True)
    
    logger.info(f"Added expectation: {expectation.method} {expectation.path} -> {expectation.response.status_code}")
    return {"id": expectation.id, "status": "added"}

@app.delete("/_mock/expectations")
async def clear_expectations():
    global expectations
    expectations = []
    logger.info("Cleared all expectations")
    return {"status": "cleared"}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"])
async def catch_all(request: Request, path: str):
    method = request.method
    full_path = f"/{path}"
    
    logger.info(f"Received request: {method} {full_path}")
    
    # Find matching expectation
    matched_expectation = None
    for exp in expectations:
        # TODO: Add more sophisticated matching (headers, body, query params, regex path)
        if exp.method.upper() == method.upper() and exp.path == full_path:
            matched_expectation = exp
            break
            
    if matched_expectation:
        response_def = matched_expectation.response
        
        # Simulate delay
        if response_def.delay_ms > 0:
            await asyncio.sleep(response_def.delay_ms / 1000.0)
            
        logger.info(f"Matched expectation {matched_expectation.id}, returning {response_def.status_code}")
        
        return JSONResponse(
            content=response_def.body,
            status_code=response_def.status_code,
            headers=response_def.headers
        )
    
    # Default behavior: 404
    logger.warning(f"No expectation matched for {method} {full_path}")
    return JSONResponse(
        content={"error": "No mock expectation matched", "path": full_path, "method": method},
        status_code=404
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
