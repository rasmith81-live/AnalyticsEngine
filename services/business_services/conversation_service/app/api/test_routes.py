"""
Test Routes for Agent Interview Testing

Provides API endpoints to run and monitor agent tests.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from datetime import datetime
import asyncio
import json
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/tests", tags=["Agent Tests"])


# Test state storage (in production, use Redis)
_test_state: Dict[str, Any] = {}


class TestRunRequest(BaseModel):
    """Request to start a test run."""
    test_type: str = Field(default="mock_interview", description="Type of test to run")
    stream_results: bool = Field(default=True, description="Stream results in real-time")


class TestStatus(BaseModel):
    """Status of a test run."""
    test_id: str
    status: str
    current_turn: int
    total_turns: int
    agents_activated: List[str]
    errors: List[str]
    started_at: Optional[str]
    completed_at: Optional[str]


# Mock interview script
MOCK_INTERVIEW = [
    {
        "turn": 1,
        "message": "Hi, I'm the CEO of TechFlow Solutions. We're a mid-sized B2B SaaS company specializing in supply chain optimization software. We have about 500 employees and serve manufacturing clients across North America and Europe. Our main product helps manufacturers track inventory, optimize procurement, and manage supplier relationships.",
        "target_agents": ["coordinator", "business_analyst", "architect"]
    },
    {
        "turn": 2,
        "message": "Our biggest challenge is measuring performance. We need KPIs for customer acquisition cost, lifetime value, product adoption rates, support ticket resolution, revenue per segment, and churn prediction. I want to benchmark against SCOR framework. What existing KPI definitions do you have that we could reuse?",
        "target_agents": ["librarian_curator", "data_analyst", "business_strategist"]
    },
    {
        "turn": 3,
        "message": "We have data in Salesforce for CRM, NetSuite for financials, PostgreSQL for product data, and Snowflake for our warehouse. We need to integrate all of this. Our dev team uses Azure. What's the best architecture approach?",
        "target_agents": ["architect", "developer", "deployment_specialist", "data_governance_specialist"]
    },
    {
        "turn": 4,
        "message": "I'm concerned about competition - Coupa, SAP Ariba, and Jaggaer are expanding analytics. What are they doing? Can you research current industry best practices for supply chain analytics?",
        "target_agents": ["competitive_analyst", "librarian_curator", "business_strategist"]
    },
    {
        "turn": 5,
        "message": "Sales needs forecasting tools, marketing wants campaign ROI and attribution, finance needs revenue recognition and cash flow projections. Can we design analytics for all departments? What ML models would help?",
        "target_agents": ["sales_manager", "marketing_manager", "accountant", "data_scientist"]
    },
    {
        "turn": 6,
        "message": "For the UI, we want something modern for busy operations managers. We also need testing and documentation for SOC 2 and GDPR compliance. What's your approach?",
        "target_agents": ["ui_designer", "tester", "documenter", "data_governance_specialist"]
    },
    {
        "turn": 7,
        "message": "Our ops team follows ITIL and needs system health dashboards and incident management. Our project manager needs a timeline - how long will this take and what are the phases?",
        "target_agents": ["operations_manager", "project_manager", "deployment_specialist"]
    }
]


async def run_mock_interview_test(test_id: str):
    """Background task to run the mock interview test."""
    from ..agents.orchestrator import AgentOrchestrator
    
    _test_state[test_id]["status"] = "running"
    _test_state[test_id]["started_at"] = datetime.utcnow().isoformat()
    
    try:
        # Initialize orchestrator
        orchestrator = AgentOrchestrator()
        await orchestrator.initialize()
        
        # Create test session
        session = await orchestrator.create_session(
            user_id=f"test-{test_id}",
            business_description="TechFlow Solutions - B2B SaaS Supply Chain",
            industry="Technology / Supply Chain"
        )
        
        _test_state[test_id]["session_id"] = session.id
        _test_state[test_id]["events"].append({
            "type": "session_created",
            "timestamp": datetime.utcnow().isoformat(),
            "data": {"session_id": session.id}
        })
        
        # Process each turn
        for turn_data in MOCK_INTERVIEW:
            turn_num = turn_data["turn"]
            message = turn_data["message"]
            target_agents = turn_data["target_agents"]
            
            _test_state[test_id]["current_turn"] = turn_num
            _test_state[test_id]["events"].append({
                "type": "turn_started",
                "timestamp": datetime.utcnow().isoformat(),
                "data": {
                    "turn": turn_num,
                    "message_preview": message[:100] + "...",
                    "target_agents": target_agents
                }
            })
            
            try:
                start_time = datetime.utcnow()
                
                # Process message through orchestrator
                response = await orchestrator.process_message(
                    session_id=session.id,
                    message=message
                )
                
                end_time = datetime.utcnow()
                processing_time = (end_time - start_time).total_seconds() * 1000
                
                # Extract response data
                response_text = ""
                activated_agents = []
                
                if response:
                    if hasattr(response, 'content'):
                        response_text = response.content
                    elif isinstance(response, dict):
                        response_text = response.get('content', str(response))
                    else:
                        response_text = str(response)
                    
                    # Extract activated agents from tool_calls (delegate_to_* calls)
                    if hasattr(response, 'tool_calls') and response.tool_calls:
                        for tool_call in response.tool_calls:
                            tool_name = tool_call.get('name', '') if isinstance(tool_call, dict) else getattr(tool_call, 'name', '')
                            if tool_name.startswith('delegate_to_'):
                                agent_name = tool_name.replace('delegate_to_', '')
                                if agent_name not in activated_agents:
                                    activated_agents.append(agent_name)
                    
                    # Also check metadata for agents_consulted
                    if hasattr(response, 'metadata') and response.metadata:
                        consulted = response.metadata.get('agents_consulted', [])
                        for agent in consulted:
                            if agent not in activated_agents:
                                activated_agents.append(agent)
                    
                    # The coordinator itself is always activated
                    if 'coordinator' not in activated_agents:
                        activated_agents.append('coordinator')
                
                # Update state
                for agent in activated_agents:
                    if agent not in _test_state[test_id]["agents_activated"]:
                        _test_state[test_id]["agents_activated"].append(agent)
                
                _test_state[test_id]["turns"].append({
                    "turn": turn_num,
                    "input": message,
                    "target_agents": target_agents,
                    "activated_agents": activated_agents,
                    "response": response_text[:1000] if response_text else "No response",
                    "processing_time_ms": processing_time
                })
                
                _test_state[test_id]["events"].append({
                    "type": "turn_completed",
                    "timestamp": datetime.utcnow().isoformat(),
                    "data": {
                        "turn": turn_num,
                        "activated_agents": activated_agents,
                        "processing_time_ms": processing_time,
                        "response_preview": response_text[:200] if response_text else "No response"
                    }
                })
                
            except Exception as e:
                logger.error(f"Error in turn {turn_num}: {e}")
                _test_state[test_id]["errors"].append(f"Turn {turn_num}: {str(e)}")
                _test_state[test_id]["events"].append({
                    "type": "turn_error",
                    "timestamp": datetime.utcnow().isoformat(),
                    "data": {"turn": turn_num, "error": str(e)}
                })
            
            # Brief delay between turns
            await asyncio.sleep(0.5)
        
        _test_state[test_id]["status"] = "completed"
        _test_state[test_id]["completed_at"] = datetime.utcnow().isoformat()
        
        # Calculate summary
        all_agents = {
            "coordinator", "architect", "business_analyst", "data_analyst",
            "developer", "tester", "documenter", "deployment_specialist",
            "project_manager", "sales_manager", "accountant",
            "data_governance_specialist", "data_scientist", "marketing_manager",
            "ui_designer", "business_strategist", "operations_manager",
            "librarian_curator", "competitive_analyst"
        }
        activated = set(_test_state[test_id]["agents_activated"])
        missing = all_agents - activated
        
        _test_state[test_id]["summary"] = {
            "total_turns": len(MOCK_INTERVIEW),
            "agents_activated": len(activated),
            "total_agents": len(all_agents),
            "coverage_percent": (len(activated) / len(all_agents)) * 100,
            "missing_agents": list(missing),
            "total_errors": len(_test_state[test_id]["errors"])
        }
        
        _test_state[test_id]["events"].append({
            "type": "test_completed",
            "timestamp": datetime.utcnow().isoformat(),
            "data": _test_state[test_id]["summary"]
        })
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        _test_state[test_id]["status"] = "failed"
        _test_state[test_id]["errors"].append(f"Test failed: {str(e)}")
        _test_state[test_id]["events"].append({
            "type": "test_failed",
            "timestamp": datetime.utcnow().isoformat(),
            "data": {"error": str(e)}
        })


@router.post("/run")
async def start_test_run(request: TestRunRequest, background_tasks: BackgroundTasks):
    """Start a new agent test run."""
    test_id = f"TEST-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"
    
    _test_state[test_id] = {
        "test_id": test_id,
        "test_type": request.test_type,
        "status": "initializing",
        "current_turn": 0,
        "total_turns": len(MOCK_INTERVIEW),
        "agents_activated": [],
        "turns": [],
        "events": [],
        "errors": [],
        "started_at": None,
        "completed_at": None,
        "summary": None
    }
    
    # Start test in background
    background_tasks.add_task(run_mock_interview_test, test_id)
    
    return {"test_id": test_id, "status": "started", "stream_url": f"/api/v1/tests/{test_id}/stream"}


@router.get("/{test_id}/status")
async def get_test_status(test_id: str):
    """Get current status of a test run."""
    if test_id not in _test_state:
        raise HTTPException(status_code=404, detail="Test not found")
    
    state = _test_state[test_id]
    return TestStatus(
        test_id=test_id,
        status=state["status"],
        current_turn=state["current_turn"],
        total_turns=state["total_turns"],
        agents_activated=state["agents_activated"],
        errors=state["errors"],
        started_at=state.get("started_at"),
        completed_at=state.get("completed_at")
    )


@router.get("/{test_id}/results")
async def get_test_results(test_id: str):
    """Get full test results."""
    if test_id not in _test_state:
        raise HTTPException(status_code=404, detail="Test not found")
    
    return _test_state[test_id]


@router.get("/{test_id}/stream")
async def stream_test_events(test_id: str):
    """Stream test events as Server-Sent Events."""
    if test_id not in _test_state:
        raise HTTPException(status_code=404, detail="Test not found")
    
    async def event_generator():
        last_event_idx = 0
        
        while True:
            state = _test_state.get(test_id)
            if not state:
                break
            
            # Send new events
            events = state.get("events", [])
            while last_event_idx < len(events):
                event = events[last_event_idx]
                yield f"data: {json.dumps(event)}\n\n"
                last_event_idx += 1
            
            # Check if test is complete
            if state["status"] in ["completed", "failed"]:
                yield f"data: {json.dumps({'type': 'stream_end', 'final_status': state['status']})}\n\n"
                break
            
            await asyncio.sleep(0.5)
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )


@router.get("/{test_id}/markdown")
async def get_test_markdown(test_id: str):
    """Get test results as markdown."""
    if test_id not in _test_state:
        raise HTTPException(status_code=404, detail="Test not found")
    
    state = _test_state[test_id]
    
    md = f"""# Agent Interview Test Results

**Test ID:** {state['test_id']}  
**Status:** {state['status']}  
**Started:** {state.get('started_at', 'N/A')}  
**Completed:** {state.get('completed_at', 'N/A')}

---

## Summary

"""
    
    if state.get("summary"):
        summary = state["summary"]
        md += f"""| Metric | Value |
|--------|-------|
| Total Turns | {summary['total_turns']} |
| Agents Activated | {summary['agents_activated']} / {summary['total_agents']} |
| Coverage | {summary['coverage_percent']:.1f}% |
| Errors | {summary['total_errors']} |

### Missing Agents
{', '.join(summary['missing_agents']) if summary['missing_agents'] else 'None - Full Coverage!'}

"""
    
    md += """---

## Interview Transcript

"""
    
    for turn in state.get("turns", []):
        md += f"""### Turn {turn['turn']}

**CEO Input:**
> {turn['input'][:300]}{'...' if len(turn['input']) > 300 else ''}

**Target Agents:** {', '.join(turn['target_agents'])}  
**Activated Agents:** {', '.join(turn['activated_agents']) if turn['activated_agents'] else 'None'}  
**Processing Time:** {turn.get('processing_time_ms', 0):.0f}ms

**Coordinator Response:**
{turn.get('response', 'No response')[:500]}{'...' if len(turn.get('response', '')) > 500 else ''}

---

"""
    
    if state.get("errors"):
        md += """## Errors

"""
        for error in state["errors"]:
            md += f"- {error}\n"
    
    return {"markdown": md}


@router.get("/list")
async def list_tests():
    """List all test runs."""
    return {
        "tests": [
            {
                "test_id": tid,
                "status": state["status"],
                "started_at": state.get("started_at"),
                "completed_at": state.get("completed_at")
            }
            for tid, state in _test_state.items()
        ]
    }
