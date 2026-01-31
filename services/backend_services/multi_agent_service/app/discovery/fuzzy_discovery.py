# =============================================================================
# Fuzzy Agent Discovery
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2026-01-12-introducing-prompt-library-cli/
# =============================================================================
"""
Fuzzy agent discovery for finding agents by capability keywords.

Provides:
- Fuzzy matching for agent search
- Capability-based agent discovery
- Forgiving search that handles typos and partial matches
"""

from dataclasses import dataclass, field
from difflib import SequenceMatcher
from typing import Any, Dict, List, Optional, Set, Tuple
import logging
import re

logger = logging.getLogger(__name__)


@dataclass
class AgentCapability:
    """Describes an agent's capabilities for discovery."""
    role: str
    display_name: str
    description: str = ""
    domain_keywords: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)
    capabilities: List[str] = field(default_factory=list)
    aliases: List[str] = field(default_factory=list)
    
    def get_searchable_terms(self) -> Set[str]:
        """Get all searchable terms for this agent."""
        terms = set()
        
        terms.add(self.role.lower())
        terms.add(self.display_name.lower())
        
        for alias in self.aliases:
            terms.add(alias.lower())
        
        for keyword in self.domain_keywords:
            terms.add(keyword.lower())
        
        for tool in self.tools:
            terms.add(tool.lower().replace("_", " "))
            terms.update(tool.lower().split("_"))
        
        for cap in self.capabilities:
            terms.add(cap.lower())
            terms.update(cap.lower().split())
        
        if self.description:
            words = re.findall(r'\b\w{4,}\b', self.description.lower())
            terms.update(words)
        
        return terms


@dataclass
class SearchResult:
    """Result of a fuzzy agent search."""
    agent_role: str
    display_name: str
    score: float
    matched_terms: List[str] = field(default_factory=list)
    match_type: str = "fuzzy"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_role": self.agent_role,
            "display_name": self.display_name,
            "score": round(self.score, 3),
            "matched_terms": self.matched_terms,
            "match_type": self.match_type,
        }


class FuzzyAgentDiscovery:
    """
    Fuzzy search for discovering agents by capability.
    
    Supports:
    - Exact matching
    - Prefix matching
    - Fuzzy/similarity matching
    - Multi-term queries
    
    Usage:
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("inventory analysis")
        # Returns: [supply_chain_analyst, data_analyst, operations_manager]
    """
    
    DEFAULT_AGENTS = [
        AgentCapability(
            role="architect",
            display_name="Architect",
            description="Designs system architecture and technical solutions",
            domain_keywords=["architecture", "design", "system", "integration", "patterns"],
            tools=["design_system", "create_diagram", "review_architecture"],
            capabilities=["system design", "technical architecture", "integration planning"],
            aliases=["system architect", "solution architect", "tech architect"]
        ),
        AgentCapability(
            role="developer",
            display_name="Developer",
            description="Implements features and writes code",
            domain_keywords=["code", "implementation", "development", "programming", "software"],
            tools=["write_code", "refactor", "implement_feature", "debug"],
            capabilities=["coding", "implementation", "debugging", "refactoring"],
            aliases=["programmer", "coder", "software engineer", "dev"]
        ),
        AgentCapability(
            role="data_analyst",
            display_name="Data Analyst",
            description="Analyzes data and creates reports",
            domain_keywords=["data", "analytics", "statistics", "reports", "visualization"],
            tools=["analyze_data", "create_report", "query_database", "visualize"],
            capabilities=["data analysis", "reporting", "sql", "visualization"],
            aliases=["analyst", "data specialist"]
        ),
        AgentCapability(
            role="data_scientist",
            display_name="Data Scientist",
            description="Builds ML models and performs advanced analytics",
            domain_keywords=["machine learning", "ml", "ai", "modeling", "prediction"],
            tools=["train_model", "evaluate_model", "feature_engineering"],
            capabilities=["machine learning", "predictive modeling", "statistical analysis"],
            aliases=["ml engineer", "ai specialist"]
        ),
        AgentCapability(
            role="business_analyst",
            display_name="Business Analyst",
            description="Gathers requirements and analyzes business processes",
            domain_keywords=["business", "requirements", "process", "workflow", "stakeholder"],
            tools=["gather_requirements", "create_specification", "analyze_process"],
            capabilities=["requirements gathering", "process analysis", "stakeholder management"],
            aliases=["ba", "requirements analyst"]
        ),
        AgentCapability(
            role="business_strategist",
            display_name="Business Strategist",
            description="Develops business strategy and competitive analysis",
            domain_keywords=["strategy", "competitive", "market", "growth", "planning"],
            tools=["analyze_market", "develop_strategy", "competitive_analysis"],
            capabilities=["strategic planning", "market analysis", "business development"],
            aliases=["strategist", "strategy consultant"]
        ),
        AgentCapability(
            role="tester",
            display_name="Tester",
            description="Tests software and ensures quality",
            domain_keywords=["testing", "quality", "qa", "validation", "verification"],
            tools=["write_tests", "run_tests", "analyze_coverage", "report_bugs"],
            capabilities=["test automation", "quality assurance", "bug reporting"],
            aliases=["qa", "quality analyst", "test engineer"]
        ),
        AgentCapability(
            role="operations_manager",
            display_name="Operations Manager",
            description="Manages operations and process optimization",
            domain_keywords=["operations", "efficiency", "process", "metrics", "kpi"],
            tools=["analyze_operations", "optimize_process", "track_metrics"],
            capabilities=["process optimization", "operations management", "kpi tracking"],
            aliases=["ops manager", "operations lead"]
        ),
        AgentCapability(
            role="supply_chain_analyst",
            display_name="Supply Chain Analyst",
            description="Analyzes supply chain and logistics",
            domain_keywords=["supply chain", "inventory", "logistics", "procurement", "warehouse"],
            tools=["analyze_inventory", "forecast_demand", "optimize_logistics"],
            capabilities=["inventory management", "demand forecasting", "logistics optimization"],
            aliases=["scm analyst", "logistics analyst"]
        ),
        AgentCapability(
            role="deployment_specialist",
            display_name="Deployment Specialist",
            description="Handles deployment and infrastructure",
            domain_keywords=["deployment", "devops", "infrastructure", "ci/cd", "cloud"],
            tools=["deploy_application", "configure_infrastructure", "setup_pipeline"],
            capabilities=["deployment automation", "infrastructure management", "ci/cd"],
            aliases=["devops", "release engineer", "infra specialist"]
        ),
        AgentCapability(
            role="documenter",
            display_name="Documenter",
            description="Creates documentation and knowledge base",
            domain_keywords=["documentation", "writing", "knowledge", "api docs", "guides"],
            tools=["write_documentation", "create_guide", "update_wiki"],
            capabilities=["technical writing", "documentation", "knowledge management"],
            aliases=["technical writer", "doc specialist"]
        ),
        AgentCapability(
            role="project_manager",
            display_name="Project Manager",
            description="Manages projects and coordinates teams",
            domain_keywords=["project", "planning", "timeline", "coordination", "milestones"],
            tools=["create_plan", "track_progress", "manage_resources"],
            capabilities=["project planning", "team coordination", "risk management"],
            aliases=["pm", "project lead", "scrum master"]
        ),
        AgentCapability(
            role="accountant",
            display_name="Accountant",
            description="Handles financial analysis and accounting",
            domain_keywords=["finance", "accounting", "budget", "costs", "revenue"],
            tools=["analyze_financials", "create_budget", "track_expenses"],
            capabilities=["financial analysis", "budgeting", "cost tracking"],
            aliases=["finance analyst", "financial controller"]
        ),
        AgentCapability(
            role="sales_manager",
            display_name="Sales Manager",
            description="Manages sales strategy and customer relationships",
            domain_keywords=["sales", "revenue", "customers", "pipeline", "deals"],
            tools=["analyze_pipeline", "forecast_sales", "manage_accounts"],
            capabilities=["sales strategy", "customer management", "revenue forecasting"],
            aliases=["sales lead", "account manager"]
        ),
        AgentCapability(
            role="marketing_manager",
            display_name="Marketing Manager",
            description="Develops marketing strategy and campaigns",
            domain_keywords=["marketing", "campaigns", "brand", "content", "growth"],
            tools=["plan_campaign", "analyze_performance", "create_content"],
            capabilities=["marketing strategy", "campaign management", "brand development"],
            aliases=["marketing lead", "growth manager"]
        ),
        AgentCapability(
            role="ui_designer",
            display_name="UI Designer",
            description="Designs user interfaces and experiences",
            domain_keywords=["ui", "ux", "design", "interface", "user experience"],
            tools=["design_interface", "create_mockup", "user_research"],
            capabilities=["ui design", "ux design", "prototyping"],
            aliases=["ux designer", "product designer", "interaction designer"]
        ),
        AgentCapability(
            role="competitive_analyst",
            display_name="Competitive Analyst",
            description="Analyzes competitors and market trends",
            domain_keywords=["competitive", "market", "trends", "benchmarking", "industry"],
            tools=["analyze_competitors", "track_trends", "benchmark"],
            capabilities=["competitive analysis", "market research", "trend analysis"],
            aliases=["market analyst", "intelligence analyst"]
        ),
        AgentCapability(
            role="data_governance_specialist",
            display_name="Data Governance Specialist",
            description="Ensures data quality and compliance",
            domain_keywords=["governance", "compliance", "data quality", "privacy", "standards"],
            tools=["audit_data", "enforce_policies", "track_lineage"],
            capabilities=["data governance", "compliance management", "data quality"],
            aliases=["data steward", "compliance officer"]
        ),
        AgentCapability(
            role="librarian_curator",
            display_name="Librarian Curator",
            description="Manages knowledge and information assets",
            domain_keywords=["knowledge", "library", "curation", "taxonomy", "metadata"],
            tools=["organize_knowledge", "curate_content", "maintain_taxonomy"],
            capabilities=["knowledge management", "content curation", "taxonomy design"],
            aliases=["knowledge manager", "information architect"]
        ),
    ]
    
    def __init__(
        self,
        min_score: float = 0.3,
        max_results: int = 10
    ):
        self._agents: Dict[str, AgentCapability] = {}
        self._min_score = min_score
        self._max_results = max_results
        self._term_index: Dict[str, Set[str]] = {}
        
        self._initialize_default_agents()
    
    def _initialize_default_agents(self) -> None:
        """Initialize with default agent capabilities."""
        for agent in self.DEFAULT_AGENTS:
            self.register_agent(agent)
    
    def register_agent(self, agent: AgentCapability) -> None:
        """Register an agent for discovery."""
        self._agents[agent.role] = agent
        
        for term in agent.get_searchable_terms():
            if term not in self._term_index:
                self._term_index[term] = set()
            self._term_index[term].add(agent.role)
        
        logger.debug(f"Registered agent for discovery: {agent.role}")
    
    def search(
        self,
        query: str,
        limit: Optional[int] = None
    ) -> List[SearchResult]:
        """
        Search for agents matching the query.
        
        Args:
            query: Search query (can be multiple words)
            limit: Maximum number of results
            
        Returns:
            List of SearchResult sorted by score descending
        """
        if not query or not query.strip():
            return []
        
        limit = limit or self._max_results
        query_terms = self._tokenize(query)
        
        scores: Dict[str, Tuple[float, List[str], str]] = {}
        
        for agent_role, agent in self._agents.items():
            score, matched, match_type = self._calculate_score(query_terms, agent)
            if score >= self._min_score:
                scores[agent_role] = (score, matched, match_type)
        
        results = []
        for role, (score, matched, match_type) in sorted(
            scores.items(),
            key=lambda x: x[1][0],
            reverse=True
        )[:limit]:
            agent = self._agents[role]
            results.append(SearchResult(
                agent_role=role,
                display_name=agent.display_name,
                score=score,
                matched_terms=matched,
                match_type=match_type
            ))
        
        return results
    
    def _tokenize(self, query: str) -> List[str]:
        """Tokenize query into search terms."""
        query = query.lower().strip()
        query = re.sub(r'[^\w\s]', ' ', query)
        terms = [t for t in query.split() if len(t) >= 2]
        return terms
    
    def _calculate_score(
        self,
        query_terms: List[str],
        agent: AgentCapability
    ) -> Tuple[float, List[str], str]:
        """Calculate match score for an agent."""
        if not query_terms:
            return 0.0, [], "none"
        
        agent_terms = agent.get_searchable_terms()
        matched_terms = []
        total_score = 0.0
        best_match_type = "fuzzy"
        
        for query_term in query_terms:
            term_score, matched, match_type = self._match_term(
                query_term, agent_terms
            )
            if term_score > 0:
                total_score += term_score
                matched_terms.extend(matched)
                if match_type == "exact":
                    best_match_type = "exact"
                elif match_type == "prefix" and best_match_type != "exact":
                    best_match_type = "prefix"
        
        if query_terms:
            final_score = total_score / len(query_terms)
        else:
            final_score = 0.0
        
        return final_score, list(set(matched_terms)), best_match_type
    
    def _match_term(
        self,
        query_term: str,
        agent_terms: Set[str]
    ) -> Tuple[float, List[str], str]:
        """Match a single query term against agent terms."""
        best_score = 0.0
        best_matched = []
        best_type = "none"
        
        for agent_term in agent_terms:
            if query_term == agent_term:
                return 1.0, [agent_term], "exact"
            
            if agent_term.startswith(query_term):
                score = len(query_term) / len(agent_term)
                if score > best_score:
                    best_score = max(score, 0.7)
                    best_matched = [agent_term]
                    best_type = "prefix"
            
            if query_term in agent_term:
                score = len(query_term) / len(agent_term)
                if score > best_score:
                    best_score = max(score, 0.5)
                    best_matched = [agent_term]
                    best_type = "contains"
        
        if best_score < self._min_score:
            for agent_term in agent_terms:
                similarity = SequenceMatcher(
                    None, query_term, agent_term
                ).ratio()
                if similarity > best_score and similarity >= 0.6:
                    best_score = similarity * 0.8
                    best_matched = [agent_term]
                    best_type = "fuzzy"
        
        return best_score, best_matched, best_type
    
    def find_by_capability(self, capability: str) -> List[str]:
        """Find agents that have a specific capability."""
        results = self.search(capability, limit=5)
        return [r.agent_role for r in results]
    
    def find_by_tool(self, tool_name: str) -> List[str]:
        """Find agents that have a specific tool."""
        matching = []
        tool_lower = tool_name.lower().replace("_", " ")
        
        for role, agent in self._agents.items():
            for tool in agent.tools:
                if tool_lower in tool.lower() or tool.lower() in tool_lower:
                    matching.append(role)
                    break
        
        return matching
    
    def find_by_domain(self, domain: str) -> List[str]:
        """Find agents in a specific domain."""
        results = self.search(domain, limit=10)
        return [r.agent_role for r in results if r.score >= 0.5]
    
    def get_agent_info(self, role: str) -> Optional[Dict[str, Any]]:
        """Get detailed info about an agent."""
        agent = self._agents.get(role)
        if not agent:
            return None
        
        return {
            "role": agent.role,
            "display_name": agent.display_name,
            "description": agent.description,
            "domain_keywords": agent.domain_keywords,
            "tools": agent.tools,
            "capabilities": agent.capabilities,
            "aliases": agent.aliases,
        }
    
    def list_all_agents(self) -> List[Dict[str, str]]:
        """List all registered agents."""
        return [
            {"role": a.role, "display_name": a.display_name}
            for a in self._agents.values()
        ]
    
    def suggest_agents(
        self,
        task_description: str,
        limit: int = 3
    ) -> List[SearchResult]:
        """
        Suggest agents for a task based on description.
        
        This is a convenience method that searches and returns
        the top matching agents for a given task.
        """
        return self.search(task_description, limit=limit)


_discovery_instance: Optional[FuzzyAgentDiscovery] = None


def get_fuzzy_discovery() -> FuzzyAgentDiscovery:
    """Get the singleton fuzzy discovery instance."""
    global _discovery_instance
    if _discovery_instance is None:
        _discovery_instance = FuzzyAgentDiscovery()
    return _discovery_instance
