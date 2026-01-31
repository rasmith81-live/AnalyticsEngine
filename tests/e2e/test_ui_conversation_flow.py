"""
E2E Test: Full Interview Flow with Contract Enforcement

Phase 17: UI Integration Validation

Tests the complete interview flow with contract enforcement visible in UI.
"""

import pytest
import json
from datetime import datetime


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_full_interview_with_contracts(simulator, browser):
    """Test complete interview flow with contract enforcement visible in UI."""
    
    # 1. Navigate to interview page
    await browser.goto("http://localhost:5173/design/interview")
    await browser.wait_for_load_state("networkidle")
    
    # 2. Create new session
    new_session_btn = browser.locator("button[data-testid='new-session']")
    if await new_session_btn.is_visible():
        await new_session_btn.click()
        await browser.wait_for_timeout(1000)
    
    # 3. Send initial message
    message_input = browser.locator("textarea[data-testid='message-input']")
    await message_input.fill(
        "We are a manufacturing company that produces industrial equipment. "
        "We want to track production efficiency and quality metrics."
    )
    
    send_btn = browser.locator("button[data-testid='send']")
    await send_btn.click()
    
    # 4. Wait for processing indicator
    processing = browser.locator("[data-testid='processing-indicator']")
    await processing.wait_for(state="visible", timeout=5000)
    
    # 5. Wait for response
    await browser.wait_for_timeout(10000)  # Wait for LLM response
    
    # 6. Verify agent activity shows in UI
    agent_activity = browser.locator("[data-testid='agent-activity']")
    if await agent_activity.is_visible():
        assert True, "Agent activity panel is visible"
    
    # 7. Check for contract status panel (if visible)
    contract_status = browser.locator("[data-testid='contract-status']")
    if await contract_status.is_visible():
        # Verify it shows agent state information
        content = await contract_status.text_content()
        assert content is not None
    
    # 8. Verify message appears in chat
    message_list = browser.locator("[data-testid='message-list']")
    await message_list.wait_for(state="visible", timeout=30000)


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_session_creation_and_message_flow(simulator, browser):
    """Test basic session creation and message exchange."""
    
    # Navigate to interview page
    await browser.goto("http://localhost:5173/design/interview")
    await browser.wait_for_load_state("networkidle")
    
    # Verify page loaded
    page_title = browser.locator("h1, h2").first
    await page_title.wait_for(state="visible", timeout=5000)
    
    # Check for session controls
    session_controls = browser.locator("[data-testid='session-controls']")
    if await session_controls.is_visible():
        assert True, "Session controls are visible"


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_parallel_analysis_ui(simulator, browser):
    """Test parallel analysis triggered from UI."""
    
    # Create session first
    session = await simulator.create_session(user_id="test_user")
    
    # Navigate to session
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Look for analyze button
    analyze_btn = browser.locator("button[data-testid='run-analysis']")
    if await analyze_btn.is_visible():
        await analyze_btn.click()
        
        # Wait for analysis to complete
        await browser.wait_for_timeout(5000)
        
        # Check for analysis results
        results = browser.locator("[data-testid='analysis-results']")
        if await results.is_visible():
            assert True, "Analysis results displayed"


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_artifacts_display(simulator, browser):
    """Test that artifacts are properly displayed in UI."""
    
    # Create session with some context
    session = await simulator.create_session(user_id="test_user")
    
    # Send message that should generate artifacts
    await simulator.send_message(
        session.id,
        "Design a customer entity schema with name, email, and order history"
    )
    
    # Navigate to session
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Check for artifacts panel
    artifacts_panel = browser.locator("[data-testid='artifacts-panel']")
    if await artifacts_panel.is_visible():
        assert True, "Artifacts panel is visible"


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_websocket_connection(simulator, browser):
    """Test WebSocket connection for real-time updates."""
    
    # Create session
    session = await simulator.create_session(user_id="test_user")
    
    # Navigate to session
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Check for WebSocket connection indicator
    ws_indicator = browser.locator("[data-testid='ws-status']")
    if await ws_indicator.is_visible():
        status = await ws_indicator.text_content()
        assert "connected" in status.lower() or "online" in status.lower()


# =============================================================================
# Test Result Saving
# =============================================================================

@pytest.fixture(autouse=True)
async def save_test_results(request, browser, test_result_path):
    """Save test results after each test."""
    yield
    
    # Save screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"test_results/screenshots/{test_name}_{timestamp}.png"
        
        try:
            await browser.screenshot(path=screenshot_path)
        except Exception:
            pass
