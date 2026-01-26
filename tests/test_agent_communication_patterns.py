"""
Agent Communication Patterns Test

Tests the complete agent communication flow:
1. Coordinator delegation to sub-agents
2. Sub-agent peer-to-peer communication
3. Coordinator response synthesis
4. MCP server tool usage
5. External service messaging by sub-agents

Runs against the live conversation_service container.
"""

import asyncio
import json
import logging
import httpx
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
CONVERSATION_SERVICE_URL = "http://localhost:8026"
TEST_TIMEOUT = 300.0  # seconds per request (LLM responses can take 2-3 minutes)


@dataclass
class TestScenario:
    """A test scenario designed to trigger specific agent behaviors."""
    name: str
    message: str
    expected_behaviors: List[str]
    description: str


@dataclass
class CommunicationEvent:
    """Represents a captured communication event."""
    event_type: str  # delegation, peer_consultation, mcp_tool, external_service, synthesis
    source: str
    target: Optional[str]
    details: Dict[str, Any]
    timestamp: str


@dataclass
class TestResult:
    """Results from a single test scenario."""
    scenario_name: str
    success: bool
    response: Optional[str]
    events_captured: List[CommunicationEvent]
    delegation_detected: bool
    peer_communication_detected: bool
    mcp_usage_detected: bool
    external_service_detected: bool
    synthesis_detected: bool
    duration_ms: float
    error: Optional[str] = None


# Test scenarios designed to trigger all communication patterns
TEST_SCENARIOS: List[TestScenario] = [
    TestScenario(
        name="KPI_Design_With_Peer_Collaboration",
        message="""
        We're a B2B SaaS company in supply chain. I need help designing KPIs for:
        - Customer churn prediction
        - Revenue per customer segment
        - Feature adoption rates
        
        Can you analyze what metrics would work best and how they relate to industry 
        standards like SCOR? I want your data scientist and business strategist to 
        collaborate on this.
        """,
        expected_behaviors=[
            "coordinator_delegation",
            "peer_to_peer_consultation",
            "knowledge_graph_mcp_search",
            "coordinator_synthesis"
        ],
        description="Tests delegation to data_scientist and business_strategist with peer consultation"
    ),
    TestScenario(
        name="Technical_Architecture_With_MCP",
        message="""
        I need to understand our current database schema to design a new analytics 
        architecture. Can you look at our existing tables and suggest how to structure
        our data warehouse? We have customer, order, and product data.
        """,
        expected_behaviors=[
            "coordinator_delegation",
            "postgres_mcp_list_tables",
            "postgres_mcp_describe_table",
            "knowledge_graph_mcp_search",
            "coordinator_synthesis"
        ],
        description="Tests MCP PostgreSQL tools for schema introspection"
    ),
    TestScenario(
        name="Competitive_Analysis_With_Web_Search",
        message="""
        Our competitors like Coupa and SAP Ariba are expanding their analytics 
        capabilities. Can you research what they're doing and how we should position 
        ourselves? Use web search to find recent news and analysis.
        """,
        expected_behaviors=[
            "coordinator_delegation",
            "web_search_mcp",
            "peer_to_peer_consultation",
            "coordinator_synthesis"
        ],
        description="Tests web search MCP and competitive analysis agents"
    ),
    TestScenario(
        name="ML_Model_Registration_External_Service",
        message="""
        Based on our churn prediction KPI, I want to register a machine learning 
        model for automated predictions. The data scientist should set up the model 
        specification and register it with our ML service.
        """,
        expected_behaviors=[
            "coordinator_delegation",
            "external_service_ml_registration",
            "coordinator_synthesis"
        ],
        description="Tests external service messaging to ML service"
    ),
    TestScenario(
        name="Multi_Agent_Collaboration",
        message="""
        I need a comprehensive analytics strategy. This should include:
        1. KPI definitions from the business analyst
        2. Data architecture from the architect  
        3. ML opportunities from the data scientist
        4. Governance requirements from the data governance specialist
        
        Have all these specialists collaborate and give me a unified recommendation.
        """,
        expected_behaviors=[
            "coordinator_delegation_multiple",
            "peer_to_peer_consultation",
            "knowledge_graph_mcp_create",
            "coordinator_synthesis"
        ],
        description="Tests multi-agent delegation and peer collaboration"
    ),
    TestScenario(
        name="Ontology_Curation_With_Librarian",
        message="""
        I want to add a new entity called 'SupplierPerformance' to our ontology. 
        It should track supplier delivery metrics, quality scores, and pricing trends.
        The librarian curator should create this and relate it to our existing 
        supply chain entities.
        """,
        expected_behaviors=[
            "coordinator_delegation",
            "knowledge_graph_mcp_create_entity",
            "knowledge_graph_mcp_create_relation",
            "external_service_metadata",
            "coordinator_synthesis"
        ],
        description="Tests librarian curator with knowledge graph MCP and metadata service"
    )
]


class AgentCommunicationTester:
    """Tests agent communication patterns against live service."""
    
    def __init__(self, base_url: str = CONVERSATION_SERVICE_URL):
        self.base_url = base_url
        self.session_id: Optional[str] = None
        self.results: List[TestResult] = []
        self.summary: Dict[str, Any] = {}
    
    async def create_session(self) -> str:
        """Create a new design session via multi-agent API."""
        async with httpx.AsyncClient(timeout=TEST_TIMEOUT) as client:
            response = await client.post(
                f"{self.base_url}/api/v1/agents/design-session",
                json={
                    "user_id": f"test-user-{datetime.utcnow().strftime('%H%M%S')}",
                    "business_description": "Test B2B SaaS Supply Chain Company",
                    "industry": "Technology / Supply Chain"
                }
            )
            response.raise_for_status()
            data = response.json()
            self.session_id = data.get("session_id")
            logger.info(f"Created test session: {self.session_id}")
            return self.session_id
    
    async def send_message(self, message: str) -> Dict[str, Any]:
        """Send a message and get the response with communication details."""
        if not self.session_id:
            await self.create_session()
        
        async with httpx.AsyncClient(timeout=TEST_TIMEOUT) as client:
            response = await client.post(
                f"{self.base_url}/api/v1/agents/sessions/{self.session_id}/message",
                json={"message": message}
            )
            response.raise_for_status()
            return response.json()
    
    async def get_session_artifacts(self) -> Dict[str, Any]:
        """Get session artifacts to analyze what was generated."""
        if not self.session_id:
            return {}
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.get(
                    f"{self.base_url}/api/v1/agents/sessions/{self.session_id}/artifacts"
                )
                if response.status_code == 200:
                    return response.json()
            except Exception as e:
                logger.warning(f"Could not fetch session artifacts: {e}")
        return {}
    
    def analyze_response_for_patterns(
        self, 
        response: Dict[str, Any],
        artifacts: Dict[str, Any]
    ) -> Dict[str, bool]:
        """Analyze response and artifacts for communication patterns."""
        patterns = {
            "delegation_detected": False,
            "peer_communication_detected": False,
            "mcp_usage_detected": False,
            "external_service_detected": False,
            "synthesis_detected": False
        }
        
        response_text = str(response).lower()
        
        # Check for delegation indicators
        delegation_indicators = [
            "delegat", "consult", "specialist", "agent", "analyst",
            "architect", "scientist", "strategist", "curator"
        ]
        patterns["delegation_detected"] = any(
            ind in response_text for ind in delegation_indicators
        )
        
        # Check for peer communication indicators
        peer_indicators = [
            "collaborat", "discuss", "peer", "consult with",
            "working with", "together with"
        ]
        patterns["peer_communication_detected"] = any(
            ind in response_text for ind in peer_indicators
        )
        
        # Check for MCP tool usage indicators
        mcp_indicators = [
            "database", "schema", "table", "knowledge graph",
            "search", "found", "retrieved", "queried", "web search"
        ]
        patterns["mcp_usage_detected"] = any(
            ind in response_text for ind in mcp_indicators
        )
        
        # Check for external service indicators
        external_indicators = [
            "ml service", "model registr", "machine learning",
            "metadata service", "external service"
        ]
        patterns["external_service_detected"] = any(
            ind in response_text for ind in external_indicators
        )
        
        # Check for synthesis indicators (coordinator combining responses)
        synthesis_indicators = [
            "based on", "combining", "synthesiz", "overall",
            "in summary", "together", "comprehensive"
        ]
        patterns["synthesis_detected"] = any(
            ind in response_text for ind in synthesis_indicators
        )
        
        # Also check artifacts and metadata in response
        if "artifacts" in response:
            patterns["mcp_usage_detected"] = True
        if "agents_consulted" in response:
            agents = response.get("agents_consulted", [])
            if len(agents) > 0:
                patterns["delegation_detected"] = True
            if len(agents) > 1:
                patterns["peer_communication_detected"] = True
        
        return patterns
    
    async def run_scenario(self, scenario: TestScenario) -> TestResult:
        """Run a single test scenario."""
        logger.info(f"\n{'='*60}")
        logger.info(f"Running scenario: {scenario.name}")
        logger.info(f"Description: {scenario.description}")
        logger.info(f"{'='*60}")
        
        start_time = datetime.utcnow()
        events: List[CommunicationEvent] = []
        
        try:
            # Send the test message
            response = await self.send_message(scenario.message.strip())
            
            end_time = datetime.utcnow()
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            # Get session artifacts for detailed analysis
            artifacts = await self.get_session_artifacts()
            
            # Analyze patterns
            patterns = self.analyze_response_for_patterns(response, artifacts)
            
            # Extract response content
            response_content = response.get("content") or response.get("response") or str(response)
            
            result = TestResult(
                scenario_name=scenario.name,
                success=True,
                response=response_content[:2000] if isinstance(response_content, str) else str(response_content)[:2000],
                events_captured=events,
                delegation_detected=patterns["delegation_detected"],
                peer_communication_detected=patterns["peer_communication_detected"],
                mcp_usage_detected=patterns["mcp_usage_detected"],
                external_service_detected=patterns["external_service_detected"],
                synthesis_detected=patterns["synthesis_detected"],
                duration_ms=duration_ms
            )
            
            logger.info(f"Scenario completed in {duration_ms:.0f}ms")
            logger.info(f"Patterns detected: {patterns}")
            
        except Exception as e:
            logger.error(f"Scenario failed: {e}")
            result = TestResult(
                scenario_name=scenario.name,
                success=False,
                response=None,
                events_captured=[],
                delegation_detected=False,
                peer_communication_detected=False,
                mcp_usage_detected=False,
                external_service_detected=False,
                synthesis_detected=False,
                duration_ms=0,
                error=str(e)
            )
        
        self.results.append(result)
        return result
    
    async def run_all_scenarios(self) -> None:
        """Run all test scenarios."""
        logger.info("Starting Agent Communication Pattern Tests")
        logger.info(f"Target: {self.base_url}")
        logger.info(f"Scenarios: {len(TEST_SCENARIOS)}")
        
        # Create fresh session
        await self.create_session()
        
        for scenario in TEST_SCENARIOS:
            await self.run_scenario(scenario)
            # Brief pause between scenarios
            await asyncio.sleep(2)
        
        self.generate_summary()
    
    def generate_summary(self) -> Dict[str, Any]:
        """Generate test summary."""
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        
        self.summary = {
            "test_run_id": f"COMM-TEST-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
            "total_scenarios": total,
            "successful_scenarios": successful,
            "failed_scenarios": total - successful,
            "success_rate": (successful / total * 100) if total > 0 else 0,
            "patterns_detected": {
                "delegation": sum(1 for r in self.results if r.delegation_detected),
                "peer_communication": sum(1 for r in self.results if r.peer_communication_detected),
                "mcp_usage": sum(1 for r in self.results if r.mcp_usage_detected),
                "external_service": sum(1 for r in self.results if r.external_service_detected),
                "synthesis": sum(1 for r in self.results if r.synthesis_detected)
            },
            "avg_response_time_ms": sum(r.duration_ms for r in self.results) / total if total > 0 else 0,
            "session_id": self.session_id
        }
        
        return self.summary
    
    def save_results(self, output_dir: Path) -> str:
        """Save test results to files."""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate markdown report
        md_path = output_dir / f"agent_communication_test_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.md"
        
        md_content = f"""# Agent Communication Patterns Test Results

**Test Run ID:** {self.summary.get('test_run_id', 'N/A')}  
**Session ID:** {self.summary.get('session_id', 'N/A')}  
**Timestamp:** {datetime.utcnow().isoformat()}  

---

## Summary

| Metric | Value |
|--------|-------|
| Total Scenarios | {self.summary['total_scenarios']} |
| Successful | {self.summary['successful_scenarios']} |
| Failed | {self.summary['failed_scenarios']} |
| Success Rate | {self.summary['success_rate']:.1f}% |
| Avg Response Time | {self.summary['avg_response_time_ms']:.0f}ms |

## Communication Patterns Detected

| Pattern | Scenarios Detected |
|---------|-------------------|
| Coordinator Delegation | {self.summary['patterns_detected']['delegation']} / {self.summary['total_scenarios']} |
| Peer-to-Peer Communication | {self.summary['patterns_detected']['peer_communication']} / {self.summary['total_scenarios']} |
| MCP Tool Usage | {self.summary['patterns_detected']['mcp_usage']} / {self.summary['total_scenarios']} |
| External Service Messaging | {self.summary['patterns_detected']['external_service']} / {self.summary['total_scenarios']} |
| Coordinator Synthesis | {self.summary['patterns_detected']['synthesis']} / {self.summary['total_scenarios']} |

---

## Scenario Results

"""
        for result in self.results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            md_content += f"""
### {result.scenario_name} - {status}

**Duration:** {result.duration_ms:.0f}ms

**Patterns Detected:**
- Delegation: {'✓' if result.delegation_detected else '✗'}
- Peer Communication: {'✓' if result.peer_communication_detected else '✗'}
- MCP Usage: {'✓' if result.mcp_usage_detected else '✗'}
- External Service: {'✓' if result.external_service_detected else '✗'}
- Synthesis: {'✓' if result.synthesis_detected else '✗'}

"""
            if result.error:
                md_content += f"**Error:** {result.error}\n\n"
            
            if result.response:
                # Truncate long responses
                response_preview = result.response[:1000]
                if len(result.response) > 1000:
                    response_preview += "..."
                md_content += f"""**Response Preview:**
```
{response_preview}
```

"""
            md_content += "---\n"
        
        # Write markdown
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        # Write JSON results
        json_path = output_dir / f"agent_communication_test_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        json_results = {
            "summary": self.summary,
            "results": [
                {
                    "scenario_name": r.scenario_name,
                    "success": r.success,
                    "delegation_detected": r.delegation_detected,
                    "peer_communication_detected": r.peer_communication_detected,
                    "mcp_usage_detected": r.mcp_usage_detected,
                    "external_service_detected": r.external_service_detected,
                    "synthesis_detected": r.synthesis_detected,
                    "duration_ms": r.duration_ms,
                    "error": r.error,
                    "response_length": len(r.response) if r.response else 0
                }
                for r in self.results
            ]
        }
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, indent=2, default=str)
        
        logger.info(f"Results saved to {md_path}")
        return str(md_path)


async def run_tests():
    """Main test runner."""
    tester = AgentCommunicationTester()
    
    try:
        await tester.run_all_scenarios()
    except Exception as e:
        logger.error(f"Test run failed: {e}")
    
    # Save results
    output_dir = Path(__file__).parent.parent / "test_results"
    result_path = tester.save_results(output_dir)
    
    # Print summary
    print("\n" + "="*60)
    print("AGENT COMMUNICATION PATTERNS TEST - SUMMARY")
    print("="*60)
    print(f"Total Scenarios: {tester.summary['total_scenarios']}")
    print(f"Success Rate: {tester.summary['success_rate']:.1f}%")
    print(f"\nPatterns Detected:")
    for pattern, count in tester.summary['patterns_detected'].items():
        print(f"  - {pattern}: {count}/{tester.summary['total_scenarios']}")
    print(f"\nResults saved to: {result_path}")
    print("="*60)
    
    return tester.summary


if __name__ == "__main__":
    results = asyncio.run(run_tests())
