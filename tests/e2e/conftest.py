"""
E2E Test Fixtures

Phase 17: UI Integration Validation

Provides fixtures for:
- Playwright browser automation
- Simulator service integration
- Service mocks for degraded mode testing
"""

import pytest
import asyncio
from typing import AsyncGenerator, Generator
from datetime import datetime

# Playwright imports
try:
    from playwright.async_api import async_playwright, Page, Browser, BrowserContext
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    Page = None
    Browser = None
    BrowserContext = None


# =============================================================================
# Simulator Fixtures
# =============================================================================

@pytest.fixture
async def simulator():
    """
    Provide simulator service for E2E tests.
    
    Per project rules, all tests use the simulator service from
    the Integration Service.
    """
    try:
        from services.business_services.integration_service.simulator import SimulatorService
        
        sim = SimulatorService()
        await sim.initialize()
        yield sim
        await sim.cleanup()
    except ImportError:
        # Fallback to mock simulator if not available
        yield MockSimulator()


class MockSimulator:
    """Mock simulator for when the real simulator is not available."""
    
    async def create_session(self, **kwargs):
        """Create a mock session."""
        from uuid import uuid4
        
        class MockSession:
            id = str(uuid4())
            user_id = kwargs.get("user_id", "test_user")
            status = "active"
        
        return MockSession()
    
    async def send_message(self, session_id: str, message: str):
        """Send a mock message."""
        return {
            "session_id": session_id,
            "agent_role": "coordinator",
            "content": f"Mock response to: {message}",
            "success": True
        }
    
    async def wait_for_artifacts(self, session_id: str, timeout: int = 60):
        """Wait for mock artifacts."""
        return [{"type": "schema", "content": {"mock": True}}]
    
    async def create_session_with_struggle_trigger(self):
        """Create session that will trigger struggle signal."""
        session = await self.create_session()
        self.struggle_trigger_message = "Design a complex quantum computing integration"
        return session
    
    async def create_session_with_violation_trigger(self):
        """Create session that will trigger contract violation."""
        return await self.create_session()
    
    def create_service_mock(self, service: str, behavior: str):
        """Create a service mock."""
        return ServiceMock(service, behavior)


class ServiceMock:
    """Mock for service behavior control."""
    
    def __init__(self, service: str, behavior: str):
        self.service = service
        self.behavior = behavior
        self._active = False
    
    def activate(self):
        """Activate the mock."""
        self._active = True
    
    def deactivate(self):
        """Deactivate the mock."""
        self._active = False


# =============================================================================
# Browser Fixtures
# =============================================================================

@pytest.fixture
async def browser() -> AsyncGenerator:
    """
    Provide Playwright browser for E2E tests.
    
    Runs in headless mode by default.
    """
    if not PLAYWRIGHT_AVAILABLE:
        pytest.skip("Playwright not available")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        page = await context.new_page()
        yield page
        await browser.close()


@pytest.fixture
async def browser_with_trace() -> AsyncGenerator:
    """
    Provide Playwright browser with tracing enabled.
    
    Saves trace to test_results/ for debugging.
    """
    if not PLAYWRIGHT_AVAILABLE:
        pytest.skip("Playwright not available")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        
        # Start tracing
        await context.tracing.start(screenshots=True, snapshots=True)
        
        page = await context.new_page()
        yield page
        
        # Save trace
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_path = f"test_results/e2e_trace_{timestamp}.zip"
        await context.tracing.stop(path=trace_path)
        
        await browser.close()


# =============================================================================
# Service Mock Fixtures
# =============================================================================

@pytest.fixture
async def mock_multi_agent_down(simulator):
    """
    Mock multi_agent_service being unavailable.
    
    Useful for testing degraded mode behavior.
    """
    mock = simulator.create_service_mock(
        service="multi_agent_service",
        behavior="unavailable"
    )
    yield mock
    mock.deactivate()


@pytest.fixture
async def mock_contract_violation(simulator):
    """
    Mock a contract violation scenario.
    """
    mock = simulator.create_service_mock(
        service="multi_agent_service",
        behavior="trigger_violation"
    )
    yield mock
    mock.deactivate()


# =============================================================================
# API Client Fixtures
# =============================================================================

@pytest.fixture
async def multi_agent_client():
    """Provide multi_agent_service client for direct API testing."""
    try:
        from services.business_services.conversation_service.app.agents.multi_agent_client import (
            MultiAgentServiceClient
        )
        
        client = MultiAgentServiceClient()
        yield client
    except ImportError:
        yield None


@pytest.fixture
async def conversation_client():
    """Provide conversation_service client for direct API testing."""
    import httpx
    
    async with httpx.AsyncClient(
        base_url="http://localhost:8026/api/v1",
        timeout=30.0
    ) as client:
        yield client


# =============================================================================
# Test Result Helpers
# =============================================================================

@pytest.fixture
def save_screenshot(browser):
    """Helper to save screenshots to test_results/."""
    async def _save(name: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"test_results/screenshots/{name}_{timestamp}.png"
        await browser.screenshot(path=path)
        return path
    
    return _save


@pytest.fixture
def test_result_path():
    """Get path for test results."""
    def _path(name: str, ext: str = "json"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"test_results/{name}_{timestamp}.{ext}"
    
    return _path
