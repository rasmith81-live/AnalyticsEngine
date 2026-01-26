"""
Agent Interview Test - Mock CEO Interview to Test All Agents

This test simulates a CEO describing their business in a way that
activates each agent in the multi-agent system.
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

# Configure logging to capture all agent communications
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Mock CEO Interview Script - designed to activate all agents
MOCK_CEO_INTERVIEW = [
    {
        "turn": 1,
        "speaker": "CEO",
        "message": """
        Hi, I'm the CEO of TechFlow Solutions. We're a mid-sized B2B SaaS company 
        specializing in supply chain optimization software. We have about 500 employees 
        and serve manufacturing clients across North America and Europe.
        
        Our main product helps manufacturers track inventory, optimize procurement, 
        and manage supplier relationships. We process millions of transactions daily 
        and our clients expect real-time visibility into their supply chains.
        """,
        "expected_agents": ["coordinator", "business_analyst", "architect"],
        "expected_topics": ["industry identification", "business model", "scale assessment"]
    },
    {
        "turn": 2,
        "speaker": "CEO",
        "message": """
        Our biggest challenge right now is that we can't effectively measure our 
        performance. We need KPIs for:
        - Customer acquisition cost and lifetime value
        - Product adoption and feature usage rates  
        - Support ticket resolution times and customer satisfaction
        - Revenue per customer segment
        - Churn prediction and retention metrics
        
        I also want to benchmark against industry standards like SCOR for our 
        supply chain modules.
        """,
        "expected_agents": ["librarian_curator", "data_analyst", "business_strategist"],
        "expected_topics": ["KPI design", "SCOR framework", "metrics catalog search"]
    },
    {
        "turn": 3,
        "speaker": "CEO",
        "message": """
        From a technical perspective, we have data in multiple systems:
        - Salesforce for CRM
        - NetSuite for financials  
        - Custom PostgreSQL databases for our product data
        - Snowflake for our data warehouse
        
        We need to integrate all of this and build a unified analytics platform.
        Our dev team uses Azure for deployment. What's the best architecture approach?
        """,
        "expected_agents": ["architect", "developer", "deployment_specialist", "data_governance_specialist"],
        "expected_topics": ["data integration", "architecture design", "Azure deployment"]
    },
    {
        "turn": 4,
        "speaker": "CEO",
        "message": """
        I'm also concerned about our competition. Companies like Coupa, SAP Ariba, 
        and Jaggaer are all expanding their analytics capabilities. What are they 
        doing that we should be aware of? And what are the current best practices 
        for supply chain analytics in the industry?
        """,
        "expected_agents": ["competitive_analyst", "librarian_curator", "business_strategist"],
        "expected_topics": ["competitive research", "web search", "industry best practices"]
    },
    {
        "turn": 5,
        "speaker": "CEO",
        "message": """
        Our sales team needs better forecasting tools. They currently use spreadsheets 
        to track their pipeline. Marketing wants to see campaign ROI and attribution.
        And finance needs accurate revenue recognition and cash flow projections.
        
        Can we design something that serves all these departments?
        """,
        "expected_agents": ["sales_manager", "marketing_manager", "accountant", "data_scientist"],
        "expected_topics": ["sales forecasting", "marketing attribution", "financial metrics"]
    },
    {
        "turn": 6,
        "speaker": "CEO",
        "message": """
        For our user interface, we want something modern and intuitive. Our users 
        are busy operations managers who need to quickly see what's happening and 
        take action. Can you suggest a dashboard design approach?
        
        Also, we need to make sure any solution we build is properly tested and 
        documented for our compliance requirements (SOC 2, GDPR).
        """,
        "expected_agents": ["ui_designer", "tester", "documenter", "data_governance_specialist"],
        "expected_topics": ["UI/UX design", "testing strategy", "compliance documentation"]
    },
    {
        "turn": 7,
        "speaker": "CEO",
        "message": """
        One more thing - our operations team manages the actual deployment and 
        monitoring of our systems. They need visibility into system health, 
        performance metrics, and incident management. We follow ITIL practices.
        
        And our project manager wants to know how long this analytics platform 
        will take to build and what the phases should be.
        """,
        "expected_agents": ["operations_manager", "project_manager", "deployment_specialist"],
        "expected_topics": ["ITIL practices", "monitoring", "project planning"]
    }
]


class AgentTestHarness:
    """Test harness for running mock interviews and capturing agent interactions."""
    
    def __init__(self):
        self.test_results: Dict[str, Any] = {
            "test_id": f"AGENT-TEST-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
            "started_at": None,
            "completed_at": None,
            "interview_turns": [],
            "agent_activations": {},
            "coordinator_responses": [],
            "inter_agent_communications": [],
            "mcp_tool_calls": [],
            "errors": [],
            "summary": {}
        }
        self.orchestrator = None
        self.session = None
    
    async def initialize(self):
        """Initialize the orchestrator and create a test session."""
        logger.info("Initializing Agent Test Harness...")
        
        try:
            # Import the orchestrator
            import sys
            sys.path.insert(0, str(Path(__file__).parent.parent / "services" / "business_services" / "conversation_service" / "app"))
            
            from agents.orchestrator import AgentOrchestrator
            
            self.orchestrator = AgentOrchestrator()
            await self.orchestrator.initialize()
            
            # Create a test session
            self.session = await self.orchestrator.create_session(
                user_id="test-ceo-001",
                business_description="TechFlow Solutions - B2B SaaS Supply Chain Optimization",
                industry="Technology / Supply Chain"
            )
            
            logger.info(f"Test session created: {self.session.session_id}")
            self.test_results["started_at"] = datetime.utcnow().isoformat()
            
        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            self.test_results["errors"].append({
                "phase": "initialization",
                "error": str(e)
            })
            raise
    
    async def run_interview(self):
        """Run the mock CEO interview through all turns."""
        logger.info("Starting mock CEO interview...")
        
        for turn_data in MOCK_CEO_INTERVIEW:
            turn_num = turn_data["turn"]
            message = turn_data["message"].strip()
            expected_agents = turn_data["expected_agents"]
            expected_topics = turn_data["expected_topics"]
            
            logger.info(f"\n{'='*60}")
            logger.info(f"TURN {turn_num}: CEO speaking")
            logger.info(f"{'='*60}")
            logger.info(f"Message: {message[:100]}...")
            
            turn_result = {
                "turn": turn_num,
                "input_message": message,
                "expected_agents": expected_agents,
                "expected_topics": expected_topics,
                "activated_agents": [],
                "agent_responses": [],
                "coordinator_decision": None,
                "coordinator_response": None,
                "mcp_tools_used": [],
                "processing_time_ms": 0,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            try:
                start_time = datetime.utcnow()
                
                # Process the message through the orchestrator
                response = await self.orchestrator.process_message(
                    session_id=self.session.session_id,
                    message=message
                )
                
                end_time = datetime.utcnow()
                turn_result["processing_time_ms"] = (end_time - start_time).total_seconds() * 1000
                
                # Capture the response
                if response:
                    turn_result["coordinator_response"] = response.content if hasattr(response, 'content') else str(response)
                    turn_result["activated_agents"] = response.agents_consulted if hasattr(response, 'agents_consulted') else []
                    
                    # Track agent activations
                    for agent in turn_result["activated_agents"]:
                        if agent not in self.test_results["agent_activations"]:
                            self.test_results["agent_activations"][agent] = []
                        self.test_results["agent_activations"][agent].append(turn_num)
                
                logger.info(f"Response received in {turn_result['processing_time_ms']:.0f}ms")
                logger.info(f"Agents activated: {turn_result['activated_agents']}")
                
            except Exception as e:
                logger.error(f"Error processing turn {turn_num}: {e}")
                turn_result["error"] = str(e)
                self.test_results["errors"].append({
                    "phase": f"turn_{turn_num}",
                    "error": str(e)
                })
            
            self.test_results["interview_turns"].append(turn_result)
            
            # Small delay between turns
            await asyncio.sleep(1)
        
        self.test_results["completed_at"] = datetime.utcnow().isoformat()
    
    def generate_summary(self):
        """Generate test summary statistics."""
        total_agents = set()
        for turn in self.test_results["interview_turns"]:
            total_agents.update(turn.get("activated_agents", []))
        
        expected_all_agents = {
            "coordinator", "architect", "business_analyst", "data_analyst",
            "developer", "tester", "documenter", "deployment_specialist",
            "project_manager", "sales_manager", "accountant", 
            "data_governance_specialist", "data_scientist", "marketing_manager",
            "ui_designer", "business_strategist", "operations_manager",
            "librarian_curator", "competitive_analyst"
        }
        
        missing_agents = expected_all_agents - total_agents
        
        self.test_results["summary"] = {
            "total_turns": len(MOCK_CEO_INTERVIEW),
            "total_agents_activated": len(total_agents),
            "agents_activated": list(total_agents),
            "missing_agents": list(missing_agents),
            "coverage_percentage": (len(total_agents) / len(expected_all_agents)) * 100,
            "total_errors": len(self.test_results["errors"]),
            "avg_response_time_ms": sum(
                t.get("processing_time_ms", 0) for t in self.test_results["interview_turns"]
            ) / len(self.test_results["interview_turns"]) if self.test_results["interview_turns"] else 0
        }
    
    def save_results(self, output_path: str):
        """Save test results to markdown file."""
        self.generate_summary()
        
        md_content = f"""# Agent Interview Test Results

**Test ID:** {self.test_results['test_id']}  
**Started:** {self.test_results['started_at']}  
**Completed:** {self.test_results['completed_at']}  

---

## Summary

| Metric | Value |
|--------|-------|
| Total Interview Turns | {self.test_results['summary']['total_turns']} |
| Agents Activated | {self.test_results['summary']['total_agents_activated']} |
| Agent Coverage | {self.test_results['summary']['coverage_percentage']:.1f}% |
| Avg Response Time | {self.test_results['summary']['avg_response_time_ms']:.0f}ms |
| Total Errors | {self.test_results['summary']['total_errors']} |

### Agents Activated
{', '.join(self.test_results['summary']['agents_activated']) or 'None'}

### Missing Agents
{', '.join(self.test_results['summary']['missing_agents']) or 'None - Full Coverage!'}

---

## Interview Transcript

"""
        for turn in self.test_results["interview_turns"]:
            md_content += f"""
### Turn {turn['turn']}

**CEO Input:**
> {turn['input_message'][:500]}{'...' if len(turn['input_message']) > 500 else ''}

**Expected Agents:** {', '.join(turn['expected_agents'])}  
**Activated Agents:** {', '.join(turn.get('activated_agents', [])) or 'None recorded'}  
**Processing Time:** {turn.get('processing_time_ms', 0):.0f}ms  

**Coordinator Response:**
{turn.get('coordinator_response', 'No response recorded') or 'No response recorded'}

---
"""
        
        # Agent activation matrix
        md_content += """
## Agent Activation Matrix

| Agent | Turns Activated |
|-------|-----------------|
"""
        for agent, turns in sorted(self.test_results["agent_activations"].items()):
            md_content += f"| {agent} | {', '.join(map(str, turns))} |\n"
        
        # Errors section
        if self.test_results["errors"]:
            md_content += """
## Errors

| Phase | Error |
|-------|-------|
"""
            for error in self.test_results["errors"]:
                md_content += f"| {error['phase']} | {error['error'][:100]} |\n"
        
        # Raw JSON results
        md_content += f"""
---

## Raw Results (JSON)

```json
{json.dumps(self.test_results, indent=2, default=str)}
```
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        logger.info(f"Results saved to {output_path}")
        return output_path


async def run_test():
    """Main test runner."""
    harness = AgentTestHarness()
    
    try:
        await harness.initialize()
        await harness.run_interview()
    except Exception as e:
        logger.error(f"Test failed: {e}")
    finally:
        output_path = Path(__file__).parent.parent / "agenttestplan.md"
        harness.save_results(str(output_path))
    
    return harness.test_results


if __name__ == "__main__":
    results = asyncio.run(run_test())
    print(f"\nTest completed. Coverage: {results['summary'].get('coverage_percentage', 0):.1f}%")
