# =============================================================================
# Hello Diagnostic Runner
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Runner for the Hello diagnostic scenario."""

from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import time

from ..protocols.hello import HelloProtocol, HelloResult, HelloViability


class DiagnosticScenario(BaseModel):
    """A diagnostic scenario to run."""
    scenario_id: str
    name: str
    description: str
    documents: str
    expected_concerns: List[str] = Field(default_factory=list)
    expected_components: List[str] = Field(default_factory=list)


class DiagnosticReport(BaseModel):
    """Report from running diagnostics."""
    session_id: str
    run_at: datetime = Field(default_factory=datetime.utcnow)
    agents_tested: List[str]
    results: Dict[str, HelloResult]
    overall_viability: HelloViability
    recommendations: List[str]
    duration_ms: int


# Default diagnostic scenario
DEFAULT_SCENARIO = DiagnosticScenario(
    scenario_id="hello-001",
    name="AnalyticsEngine System Overview",
    description="Test agent understanding of the AnalyticsEngine architecture",
    documents="""
# AnalyticsEngine Multi-Agent System

## Overview
AnalyticsEngine is a multi-agent system for business analytics with 27 specialized agents.

## Architecture
- Strategy & Analysis Layer: Coordinator, Business Strategist, Business Analyst, etc.
- Technical Design Layer: Architect, Developer, Tester, etc.
- Business Operations Layer: Sales Manager, Marketing Manager, etc.
- Governance Layer: Data Governance Specialist, Process Scenario Modeler

## Key Components
1. Blackboard Architecture: Shared state for agent coordination
2. Behavioral Contracts: Constraints that shape agent behavior
3. Peer Review: Adversarial pairing for quality assurance
4. Skills: Domain-specific contract applications

## Current Challenges
- Replacing pub/sub with blackboard for auditability
- Implementing behavioral contracts for all 27 agents
- Building the agent performance dashboard
""",
    expected_concerns=[
        "coordination complexity",
        "state consistency",
        "scalability",
        "error handling"
    ],
    expected_components=[
        "blackboard",
        "contracts",
        "agents",
        "peer review"
    ]
)


class HelloDiagnosticRunner:
    """
    Runner for the Hello diagnostic scenario.
    
    The Hello diagnostic tests agent viability at the start of a session
    by asking agents to build a mental model from provided documents.
    """
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.protocol = HelloProtocol(session_id)
        self.scenarios: Dict[str, DiagnosticScenario] = {
            DEFAULT_SCENARIO.scenario_id: DEFAULT_SCENARIO
        }
    
    def add_scenario(self, scenario: DiagnosticScenario) -> None:
        """Add a custom diagnostic scenario."""
        self.scenarios[scenario.scenario_id] = scenario
    
    async def run_diagnostic(
        self,
        agent_roles: List[str],
        scenario_id: str = "hello-001",
        agent_invoker: Any = None  # Function to invoke agents
    ) -> DiagnosticReport:
        """
        Run the hello diagnostic for a list of agents.
        
        Args:
            agent_roles: List of agent roles to test
            scenario_id: Which scenario to use
            agent_invoker: Async function to invoke agents
        
        Returns:
            DiagnosticReport with results
        """
        scenario = self.scenarios.get(scenario_id, DEFAULT_SCENARIO)
        results: Dict[str, HelloResult] = {}
        start_time = time.time()
        
        for agent_role in agent_roles:
            # In production, this would invoke the actual agent
            # For now, we simulate the response
            if agent_invoker:
                response, response_time = await self._invoke_agent(
                    agent_role, scenario.documents, agent_invoker
                )
            else:
                response, response_time = self._simulate_response(agent_role)
            
            # Score the response
            result = await self.protocol.run_hello(
                agent_role=agent_role,
                documents=scenario.documents,
                agent_response=response,
                response_time_ms=response_time
            )
            
            results[agent_role] = result
        
        # Calculate overall viability
        overall = self._calculate_overall_viability(list(results.values()))
        
        # Generate recommendations
        recommendations = self._generate_recommendations(results)
        
        duration_ms = int((time.time() - start_time) * 1000)
        
        return DiagnosticReport(
            session_id=self.session_id,
            agents_tested=agent_roles,
            results=results,
            overall_viability=overall,
            recommendations=recommendations,
            duration_ms=duration_ms
        )
    
    async def _invoke_agent(
        self,
        agent_role: str,
        documents: str,
        agent_invoker: Any
    ) -> tuple[str, int]:
        """Invoke an agent and get response with timing."""
        start = time.time()
        
        prompt = HelloProtocol.HELLO_PROMPT.format(documents=documents)
        response = await agent_invoker(agent_role, prompt)
        
        response_time = int((time.time() - start) * 1000)
        return response, response_time
    
    def _simulate_response(self, agent_role: str) -> tuple[str, int]:
        """Simulate an agent response for testing."""
        # This is a placeholder for testing
        response = f"""
As the {agent_role}, I've analyzed the AnalyticsEngine architecture.

## My Understanding

The system uses a multi-agent architecture with 27 specialized agents organized
into 4 layers. The blackboard architecture replaces pub/sub for better auditability.

## Key Components
1. Blackboard - Shared state coordination
2. Behavioral Contracts - Agent constraints
3. Peer Review - Quality assurance through adversarial pairing

## Concerns
I notice potential coordination complexity with 27 agents. State consistency
across the blackboard could be challenging under high load.

## Next Steps
1. First, review the specific contract for my role
2. Then, understand my adversarial pairing
3. Finally, identify integration points
"""
        return response, 500  # Simulated 500ms response time
    
    def _calculate_overall_viability(
        self,
        results: List[HelloResult]
    ) -> HelloViability:
        """Calculate overall viability from individual results."""
        if not results:
            return HelloViability.FAIL
        
        avg_score = sum(r.scores.overall_score() for r in results) / len(results)
        
        if avg_score >= 90:
            return HelloViability.EXCELLENT
        elif avg_score >= 75:
            return HelloViability.GOOD
        elif avg_score >= 60:
            return HelloViability.MARGINAL
        elif avg_score >= 40:
            return HelloViability.POOR
        else:
            return HelloViability.FAIL
    
    def _generate_recommendations(
        self,
        results: Dict[str, HelloResult]
    ) -> List[str]:
        """Generate recommendations from diagnostic results."""
        recommendations = []
        
        # Check for common issues across agents
        low_doc_reading = [
            role for role, result in results.items()
            if result.scores.doc_reading < 70
        ]
        if low_doc_reading:
            recommendations.append(
                f"Agents {low_doc_reading} may not be reading documents carefully. "
                "Consider adding explicit reference requirements."
            )
        
        low_specificity = [
            role for role, result in results.items()
            if result.scores.mental_model_specificity < 70
        ]
        if low_specificity:
            recommendations.append(
                f"Agents {low_specificity} giving generic responses. "
                "Require specific examples and references."
            )
        
        high_sycophancy = [
            role for role, result in results.items()
            if result.scores.anti_sycophancy < 70
        ]
        if high_sycophancy:
            recommendations.append(
                f"Agents {high_sycophancy} showing sycophantic tendencies. "
                "Reinforce contract rules about honest feedback."
            )
        
        if not recommendations:
            recommendations.append("All agents performing within acceptable parameters.")
        
        return recommendations
