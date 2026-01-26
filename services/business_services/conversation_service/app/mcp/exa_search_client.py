"""
Exa Search MCP Client for AI-powered web search.

Exa provides semantic search capabilities optimized for AI agents,
supporting natural language queries and structured results.
"""

from __future__ import annotations

import logging
import time
import asyncio
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from collections import defaultdict

import httpx
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class ExaSearchResult(BaseModel):
    """A single search result from Exa."""
    title: str
    url: str
    text: Optional[str] = None
    highlights: List[str] = Field(default_factory=list)
    score: float = 0.0
    published_date: Optional[str] = None
    author: Optional[str] = None


class ExaSearchResponse(BaseModel):
    """Response from Exa search."""
    success: bool
    results: List[ExaSearchResult] = Field(default_factory=list)
    query: str = ""
    total_results: int = 0
    execution_time_ms: float = 0.0
    error: Optional[str] = None
    cached: bool = False


class ExaContentsResponse(BaseModel):
    """Response from Exa contents extraction."""
    success: bool
    url: str
    title: Optional[str] = None
    text: Optional[str] = None
    highlights: List[str] = Field(default_factory=list)
    error: Optional[str] = None


class RateLimiter:
    """Simple rate limiter for API calls."""
    
    def __init__(self, max_requests: int, period_seconds: int = 60):
        self.max_requests = max_requests
        self.period_seconds = period_seconds
        self.requests: List[float] = []
    
    async def acquire(self) -> None:
        """Wait until a request can be made within rate limits."""
        now = time.time()
        cutoff = now - self.period_seconds
        
        # Remove old requests
        self.requests = [t for t in self.requests if t > cutoff]
        
        if len(self.requests) >= self.max_requests:
            # Wait for the oldest request to expire
            wait_time = self.requests[0] - cutoff
            if wait_time > 0:
                logger.debug(f"Rate limit reached, waiting {wait_time:.2f}s")
                await asyncio.sleep(wait_time)
        
        self.requests.append(now)


class SimpleCache:
    """Simple in-memory cache for search results."""
    
    def __init__(self, ttl_seconds: int = 3600):
        self.cache: Dict[str, tuple[Any, datetime]] = {}
        self.ttl = timedelta(seconds=ttl_seconds)
    
    def get(self, key: str) -> Optional[Any]:
        """Get a cached value if it exists and hasn't expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if datetime.utcnow() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value: Any) -> None:
        """Cache a value."""
        self.cache[key] = (value, datetime.utcnow())
    
    def clear(self) -> None:
        """Clear the cache."""
        self.cache.clear()


class ExaSearchClient:
    """
    Client for Exa Search API.
    
    Exa provides AI-native search with semantic understanding,
    ideal for agent-driven research and competitive analysis.
    """
    
    EXA_API_BASE = "https://api.exa.ai"
    
    def __init__(
        self,
        api_key: str,
        rate_limit: int = 10,
        cache_ttl: int = 3600,
        timeout: float = 30.0
    ):
        """
        Initialize the Exa search client.
        
        Args:
            api_key: Exa API key
            rate_limit: Max requests per minute
            cache_ttl: Cache TTL in seconds
            timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.timeout = timeout
        self.rate_limiter = RateLimiter(rate_limit, 60)
        self.cache = SimpleCache(cache_ttl)
        self._client: Optional[httpx.AsyncClient] = None
    
    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the HTTP client."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=self.timeout,
                headers={
                    "x-api-key": self.api_key,
                    "Content-Type": "application/json"
                }
            )
        return self._client
    
    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()
    
    def get_tools(self) -> List[Dict[str, Any]]:
        """Get tool schemas for this client."""
        return [
            {
                "name": "search_web",
                "description": "Search the web using Exa's semantic search for relevant documents and articles",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Natural language search query"
                        },
                        "num_results": {
                            "type": "integer",
                            "description": "Number of results to return (max 10)",
                            "default": 5,
                            "maximum": 10
                        },
                        "use_autoprompt": {
                            "type": "boolean",
                            "description": "Let Exa optimize the query for better results",
                            "default": True
                        },
                        "include_domains": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Only include results from these domains"
                        },
                        "exclude_domains": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Exclude results from these domains"
                        },
                        "start_published_date": {
                            "type": "string",
                            "description": "Filter to content published after this date (YYYY-MM-DD)"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "search_news",
                "description": "Search for recent news articles on a topic",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "News search query"
                        },
                        "num_results": {
                            "type": "integer",
                            "description": "Number of results to return",
                            "default": 5,
                            "maximum": 10
                        },
                        "days_back": {
                            "type": "integer",
                            "description": "Only include news from the last N days",
                            "default": 7
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "search_companies",
                "description": "Search for information about companies and organizations",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Company search query (e.g., 'real-time analytics startups')"
                        },
                        "num_results": {
                            "type": "integer",
                            "description": "Number of results to return",
                            "default": 5,
                            "maximum": 10
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "find_similar",
                "description": "Find web pages similar to a given URL",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL to find similar pages for"
                        },
                        "num_results": {
                            "type": "integer",
                            "description": "Number of similar pages to return",
                            "default": 5,
                            "maximum": 10
                        }
                    },
                    "required": ["url"]
                }
            },
            {
                "name": "get_contents",
                "description": "Extract the full text content from a URL",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL to extract content from"
                        }
                    },
                    "required": ["url"]
                }
            }
        ]
    
    async def execute(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an Exa tool."""
        if tool_name == "search_web":
            return await self.search_web(**params)
        elif tool_name == "search_news":
            return await self.search_news(**params)
        elif tool_name == "search_companies":
            return await self.search_companies(**params)
        elif tool_name == "find_similar":
            return await self.find_similar(**params)
        elif tool_name == "get_contents":
            return await self.get_contents(**params)
        else:
            return {"success": False, "error": f"Unknown tool: {tool_name}"}
    
    async def search_web(
        self,
        query: str,
        num_results: int = 5,
        use_autoprompt: bool = True,
        include_domains: List[str] = None,
        exclude_domains: List[str] = None,
        start_published_date: str = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Perform a semantic web search.
        
        Args:
            query: Natural language search query
            num_results: Number of results to return
            use_autoprompt: Let Exa optimize the query
            include_domains: Only include these domains
            exclude_domains: Exclude these domains
            start_published_date: Filter by publish date
            
        Returns:
            Search results
        """
        start_time = time.time()
        
        # Check cache
        cache_key = f"search:{query}:{num_results}"
        cached = self.cache.get(cache_key)
        if cached:
            cached["cached"] = True
            return cached
        
        # Rate limit
        await self.rate_limiter.acquire()
        
        try:
            client = await self._get_client()
            
            payload = {
                "query": query,
                "numResults": min(num_results, 10),
                "useAutoprompt": use_autoprompt,
                "type": "neural",
                "contents": {
                    "text": {"maxCharacters": 1000},
                    "highlights": True
                }
            }
            
            if include_domains:
                payload["includeDomains"] = include_domains
            if exclude_domains:
                payload["excludeDomains"] = exclude_domains
            if start_published_date:
                payload["startPublishedDate"] = start_published_date
            
            response = await client.post(
                f"{self.EXA_API_BASE}/search",
                json=payload
            )
            response.raise_for_status()
            data = response.json()
            
            results = [
                ExaSearchResult(
                    title=r.get("title", ""),
                    url=r.get("url", ""),
                    text=r.get("text", ""),
                    highlights=r.get("highlights", []),
                    score=r.get("score", 0.0),
                    published_date=r.get("publishedDate"),
                    author=r.get("author")
                ).model_dump()
                for r in data.get("results", [])
            ]
            
            result = {
                "success": True,
                "results": results,
                "query": query,
                "total_results": len(results),
                "execution_time_ms": (time.time() - start_time) * 1000,
                "cached": False
            }
            
            # Cache the result
            self.cache.set(cache_key, result)
            
            return result
            
        except httpx.HTTPStatusError as e:
            logger.error(f"Exa search failed: {e.response.status_code} - {e.response.text}")
            return {
                "success": False,
                "error": f"Exa API error: {e.response.status_code}",
                "results": [],
                "query": query,
                "execution_time_ms": (time.time() - start_time) * 1000
            }
        except Exception as e:
            logger.error(f"Exa search failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "results": [],
                "query": query,
                "execution_time_ms": (time.time() - start_time) * 1000
            }
    
    async def search_news(
        self,
        query: str,
        num_results: int = 5,
        days_back: int = 7,
        **kwargs
    ) -> Dict[str, Any]:
        """Search for recent news articles."""
        # Calculate the start date
        start_date = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y-%m-%d")
        
        return await self.search_web(
            query=query,
            num_results=num_results,
            start_published_date=start_date,
            include_domains=[
                "reuters.com", "bloomberg.com", "techcrunch.com",
                "wsj.com", "nytimes.com", "theverge.com",
                "arstechnica.com", "wired.com", "forbes.com"
            ]
        )
    
    async def search_companies(
        self,
        query: str,
        num_results: int = 5,
        **kwargs
    ) -> Dict[str, Any]:
        """Search for company information."""
        # Enhance query for company search
        enhanced_query = f"company {query}"
        
        return await self.search_web(
            query=enhanced_query,
            num_results=num_results,
            include_domains=[
                "crunchbase.com", "linkedin.com", "g2.com",
                "capterra.com", "gartner.com", "forrester.com",
                "producthunt.com"
            ]
        )
    
    async def find_similar(
        self,
        url: str,
        num_results: int = 5,
        **kwargs
    ) -> Dict[str, Any]:
        """Find pages similar to a given URL."""
        start_time = time.time()
        
        await self.rate_limiter.acquire()
        
        try:
            client = await self._get_client()
            
            response = await client.post(
                f"{self.EXA_API_BASE}/findSimilar",
                json={
                    "url": url,
                    "numResults": min(num_results, 10),
                    "contents": {
                        "text": {"maxCharacters": 500},
                        "highlights": True
                    }
                }
            )
            response.raise_for_status()
            data = response.json()
            
            results = [
                ExaSearchResult(
                    title=r.get("title", ""),
                    url=r.get("url", ""),
                    text=r.get("text", ""),
                    highlights=r.get("highlights", []),
                    score=r.get("score", 0.0)
                ).model_dump()
                for r in data.get("results", [])
            ]
            
            return {
                "success": True,
                "results": results,
                "source_url": url,
                "total_results": len(results),
                "execution_time_ms": (time.time() - start_time) * 1000
            }
            
        except Exception as e:
            logger.error(f"Exa find_similar failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "results": [],
                "source_url": url,
                "execution_time_ms": (time.time() - start_time) * 1000
            }
    
    async def get_contents(
        self,
        url: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Extract content from a URL."""
        start_time = time.time()
        
        await self.rate_limiter.acquire()
        
        try:
            client = await self._get_client()
            
            response = await client.post(
                f"{self.EXA_API_BASE}/contents",
                json={
                    "ids": [url],
                    "text": {"maxCharacters": 5000},
                    "highlights": True
                }
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get("results"):
                result = data["results"][0]
                return {
                    "success": True,
                    "url": url,
                    "title": result.get("title"),
                    "text": result.get("text"),
                    "highlights": result.get("highlights", []),
                    "execution_time_ms": (time.time() - start_time) * 1000
                }
            else:
                return {
                    "success": False,
                    "error": "No content returned",
                    "url": url,
                    "execution_time_ms": (time.time() - start_time) * 1000
                }
            
        except Exception as e:
            logger.error(f"Exa get_contents failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "url": url,
                "execution_time_ms": (time.time() - start_time) * 1000
            }
