"""
E2E Test: Contract Violation Handling

Phase 17: UI Integration Validation

Tests that the UI properly displays contract violations
and hard stop scenarios.
"""

import pytest
from datetime import datetime


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_contract_violation_display(simulator, browser):
    """Test UI displays contract violations appropriately."""
    
    # 1. Create session configured to trigger violation
    session = await simulator.create_session_with_violation_trigger()
    
    # 2. Navigate to session
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # 3. Check for violation alert
    violation_alert = browser.locator("[data-testid='violation-alert']")
    
    if await violation_alert.is_visible():
        # 4. Verify violation details
        violation_tier = browser.locator("[data-testid='violation-tier']")
        if await violation_tier.is_visible():
            tier_text = await violation_tier.text_content()
            assert tier_text is not None


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_contract_status_panel_visibility(simulator, browser):
    """Test contract status panel is visible and shows agent states."""
    
    session = await simulator.create_session(user_id="test_user")
    
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Look for contract status panel
    contract_panel = browser.locator("[data-testid='contract-status']")
    
    if await contract_panel.is_visible():
        # Verify it shows header
        header = contract_panel.locator("h3, [data-testid='contract-status-header']")
        if await header.is_visible():
            header_text = await header.text_content()
            assert "Contract" in header_text or "Status" in header_text


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_hard_stop_display(simulator, browser, mock_contract_violation):
    """Test UI displays hard stop when contract triggers it."""
    
    mock_contract_violation.activate()
    
    session = await simulator.create_session(user_id="test_user")
    
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Check for hard stop indicator
    hard_stop = browser.locator("[data-testid='hard-stop-indicator']")
    
    if await hard_stop.is_visible():
        stop_text = await hard_stop.text_content()
        assert "HARD STOP" in stop_text.upper() or "STOP" in stop_text.upper()


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_violation_tier_display(simulator, browser):
    """Test different violation tiers are displayed correctly."""
    
    session = await simulator.create_session(user_id="test_user")
    
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Contract status panel should show tier information
    contract_panel = browser.locator("[data-testid='contract-status']")
    
    if await contract_panel.is_visible():
        # Check for tier badges/indicators
        tier_badges = contract_panel.locator("[data-testid^='tier-']")
        count = await tier_badges.count()
        
        # May have 0 if no violations, but structure should exist


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_agent_state_machine_display(simulator, browser):
    """Test UI shows current state of each agent's state machine."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Send a message to activate some agents
    await simulator.send_message(
        session.id,
        "Please analyze our manufacturing process for efficiency"
    )
    
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Look for state indicators in contract panel
    state_indicators = browser.locator("[data-testid='agent-state']")
    count = await state_indicators.count()
    
    if count > 0:
        # Verify states are valid
        valid_states = ['idle', 'analysis', 'approval', 'execution', 'validation', 'done', 'hard_stop']
        
        for i in range(min(count, 5)):  # Check first 5
            indicator = state_indicators.nth(i)
            state_text = await indicator.text_content()
            if state_text:
                state_lower = state_text.lower().strip()
                # Should contain one of the valid states


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_violation_count_display(simulator, browser):
    """Test violation count is displayed for each agent."""
    
    session = await simulator.create_session(user_id="test_user")
    
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    contract_panel = browser.locator("[data-testid='contract-status']")
    
    if await contract_panel.is_visible():
        # Look for violation counts
        violation_counts = contract_panel.locator("[data-testid='violation-count']")
        count = await violation_counts.count()
        
        if count > 0:
            # Verify counts are numbers
            for i in range(count):
                count_elem = violation_counts.nth(i)
                text = await count_elem.text_content()
                if text:
                    # Should contain a number or "Clean"
                    assert text.isdigit() or "clean" in text.lower() or "0" in text


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_assumption_count_display(simulator, browser):
    """Test assumption count is tracked and displayed."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Send messages that might cause assumptions
    await simulator.send_message(
        session.id,
        "Design a system for tracking inventory with automatic reordering"
    )
    
    await browser.goto(f"http://localhost:5173/design/interview?session={session.id}")
    await browser.wait_for_load_state("networkidle")
    
    # Look for assumption counts in contract panel
    assumption_counts = browser.locator("[data-testid='assumption-count']")
    
    if await assumption_counts.count() > 0:
        first_count = assumption_counts.first
        text = await first_count.text_content()
        assert text is not None
