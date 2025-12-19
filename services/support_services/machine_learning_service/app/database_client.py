"""
Database Client - HTTP client for communicating with the Database Service.
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional
import aiohttp
from datetime import datetime

from .telemetry import inject_trace_context, trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class DatabaseClient:
    """HTTP client for Database Service communication."""
    
    def __init__(
        self,
        base_url: str,
        service_name: str = "machine_learning_service",
        timeout: int = 30,
        retries: int = 3
    ):
        self.base_url = base_url.rstrip('/')
        self.service_name = service_name
        self.timeout = timeout
        self.retries = retries
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def initialize(self):
        """Initialize the database client."""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={"Content-Type": "application/json"}
        )
        logger.info(f"Database client initialized for {self.base_url}")
    
    async def close(self):
        """Close the database client."""
        if self.session:
            await self.session.close()
        logger.info("Database client closed")
    
    @trace_method(name="database_client_request", kind="CLIENT")
    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Make HTTP request with retry logic."""
        if not self.session:
            raise RuntimeError("Database client not initialized")
        
        url = f"{self.base_url}{endpoint}"
        
        # Add span attributes for the request
        add_span_attributes({
            "db.system": "http",
            "db.operation": method,
            "db.url": url,
            "service.name": self.service_name
        })
        
        # Create headers with trace context
        headers = {"Content-Type": "application/json"}
        if correlation_id:
            headers["X-Correlation-ID"] = correlation_id
        
        # Inject trace context into headers
        headers = inject_trace_context(headers)
        
        for attempt in range(self.retries):
            try:
                async with self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    headers=headers
                ) as response:
                    if response.status in [200, 201]:
                        return await response.json()
                    else:
                        error_text = await response.text()
                        logger.error(f"Database service error {response.status}: {error_text}")
                        
                        if response.status >= 500 and attempt < self.retries - 1:
                            # Retry on server errors
                            await asyncio.sleep(2 ** attempt)
                            continue
                        
                        raise aiohttp.ClientResponseError(
                            request_info=response.request_info,
                            history=response.history,
                            status=response.status,
                            message=error_text
                        )
                        
            except aiohttp.ClientError as e:
                logger.error(f"Database client error (attempt {attempt + 1}): {e}")
                if attempt < self.retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise
        
        raise RuntimeError(f"Failed to complete request after {self.retries} attempts")
    
    async def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Execute a SQL query."""
        return await self._make_request(
            method="POST",
            endpoint="/database/query",
            data={
                "query": query,
                "parameters": parameters,
                "service_name": self.service_name
            },
            correlation_id=correlation_id
        )

    async def get_model(self, model_id: str, correlation_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Get model by ID."""
        # Assuming we have a view or table 'ml_models'
        query = "SELECT * FROM ml_models WHERE id = :model_id"
        result = await self.execute_query(query, {"model_id": model_id}, correlation_id)
        
        if result and result.get("success") and result.get("data") and result["data"].get("rows"):
            rows = result["data"]["rows"]
            if rows:
                return rows[0]
        return None

    async def get_job(self, job_id: str, correlation_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Get training job by ID."""
        # Assuming we have a view or table 'training_jobs'
        query = "SELECT * FROM training_jobs WHERE id = :job_id"
        result = await self.execute_query(query, {"job_id": job_id}, correlation_id)
        
        if result and result.get("success") and result.get("data") and result["data"].get("rows"):
            rows = result["data"]["rows"]
            if rows:
                return rows[0]
        return None

    async def check_health(self) -> Dict[str, Any]:
        """Check database service health."""
        return await self._make_request(
            method="GET",
            endpoint="/health"
        )
