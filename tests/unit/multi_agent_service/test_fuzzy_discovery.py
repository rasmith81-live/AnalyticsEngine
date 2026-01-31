# =============================================================================
# Fuzzy Agent Discovery Unit Tests
# =============================================================================
"""
Unit tests for the FuzzyAgentDiscovery class.

Tests cover:
- Exact matching
- Prefix matching
- Fuzzy/similarity matching
- Multi-term queries
- Agent capability registration
"""

import pytest

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from services.backend_services.multi_agent_service.app.discovery.fuzzy_discovery import (
    FuzzyAgentDiscovery,
    AgentCapability,
    SearchResult,
    get_fuzzy_discovery,
)


class TestFuzzyAgentDiscoverySearch:
    """Tests for fuzzy search functionality."""
    
    def test_exact_match_returns_high_score(self):
        """Verify exact match returns highest score."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("architect")
        
        assert len(results) > 0
        assert results[0].agent_role == "architect"
        assert results[0].score >= 0.9
    
    def test_partial_match_returns_results(self):
        """Verify partial match returns results."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("data")
        
        assert len(results) > 0
        roles = [r.agent_role for r in results]
        assert "data_analyst" in roles or "data_scientist" in roles
    
    def test_fuzzy_match_handles_typos(self):
        """Verify fuzzy matching handles typos."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("develper")  # Typo
        
        assert len(results) > 0
        roles = [r.agent_role for r in results]
        assert "developer" in roles
    
    def test_multi_term_query(self):
        """Verify multi-term queries work."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("inventory analysis")
        
        assert len(results) > 0
        roles = [r.agent_role for r in results]
        assert any(r in roles for r in ["supply_chain_analyst", "data_analyst", "operations_manager"])
    
    def test_empty_query_returns_empty(self):
        """Verify empty query returns empty list."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("")
        assert results == []
    
    def test_no_match_returns_empty(self):
        """Verify no match returns empty list."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("xyznonexistent12345")
        assert results == []
    
    def test_limit_parameter(self):
        """Verify limit parameter restricts results."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("manager", limit=2)
        assert len(results) <= 2
    
    def test_search_by_capability(self):
        """Verify search by capability keyword."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("testing")
        
        assert len(results) > 0
        roles = [r.agent_role for r in results]
        assert "tester" in roles
    
    def test_search_by_tool_name(self):
        """Verify search by tool name."""
        discovery = FuzzyAgentDiscovery()
        results = discovery.search("deploy")
        
        assert len(results) > 0
        roles = [r.agent_role for r in results]
        assert "deployment_specialist" in roles


class TestFuzzyAgentDiscoveryRegistration:
    """Tests for agent registration."""
    
    def test_register_custom_agent(self):
        """Verify custom agent registration."""
        discovery = FuzzyAgentDiscovery()
        
        custom_agent = AgentCapability(
            role="custom_specialist",
            display_name="Custom Specialist",
            description="Handles custom tasks",
            domain_keywords=["custom", "specialized"],
            tools=["custom_tool"],
            capabilities=["custom analysis"],
            aliases=["custom"]
        )
        
        discovery.register_agent(custom_agent)
        
        results = discovery.search("custom")
        assert len(results) > 0
        assert results[0].agent_role == "custom_specialist"
    
    def test_get_agent_info(self):
        """Verify agent info retrieval."""
        discovery = FuzzyAgentDiscovery()
        info = discovery.get_agent_info("architect")
        
        assert info is not None
        assert info["role"] == "architect"
        assert "display_name" in info
        assert "tools" in info
    
    def test_get_agent_info_not_found(self):
        """Verify agent info returns None for unknown."""
        discovery = FuzzyAgentDiscovery()
        info = discovery.get_agent_info("nonexistent")
        assert info is None
    
    def test_list_all_agents(self):
        """Verify listing all agents."""
        discovery = FuzzyAgentDiscovery()
        agents = discovery.list_all_agents()
        
        assert len(agents) >= 10  # At least 10 default agents
        assert all("role" in a and "display_name" in a for a in agents)


class TestFuzzyAgentDiscoveryHelpers:
    """Tests for helper methods."""
    
    def test_find_by_capability(self):
        """Verify find_by_capability helper."""
        discovery = FuzzyAgentDiscovery()
        agents = discovery.find_by_capability("architecture")
        
        assert len(agents) > 0
        assert "architect" in agents
    
    def test_find_by_domain(self):
        """Verify find_by_domain helper."""
        discovery = FuzzyAgentDiscovery()
        agents = discovery.find_by_domain("business")
        
        assert len(agents) > 0
        assert any(a in agents for a in ["business_analyst", "business_strategist"])
    
    def test_suggest_agents(self):
        """Verify suggest_agents for task."""
        discovery = FuzzyAgentDiscovery()
        suggestions = discovery.suggest_agents(
            "Design a REST API for inventory management",
            limit=3
        )
        
        assert len(suggestions) <= 3
        roles = [s.agent_role for s in suggestions]
        assert any(r in roles for r in ["architect", "developer", "supply_chain_analyst"])


class TestAgentCapability:
    """Tests for AgentCapability class."""
    
    def test_get_searchable_terms(self):
        """Verify searchable terms extraction."""
        capability = AgentCapability(
            role="test_agent",
            display_name="Test Agent",
            description="This agent handles testing tasks",
            domain_keywords=["testing", "quality"],
            tools=["run_tests", "analyze_coverage"],
            capabilities=["test automation"],
            aliases=["qa", "quality assurance"]
        )
        
        terms = capability.get_searchable_terms()
        
        assert "test_agent" in terms
        assert "test agent" in terms
        assert "testing" in terms
        assert "quality" in terms
        assert "qa" in terms
        assert "run_tests" in terms or "run tests" in terms


class TestSearchResult:
    """Tests for SearchResult class."""
    
    def test_to_dict(self):
        """Verify SearchResult serialization."""
        result = SearchResult(
            agent_role="architect",
            display_name="Architect",
            score=0.95,
            matched_terms=["architecture", "design"],
            match_type="exact"
        )
        
        d = result.to_dict()
        
        assert d["agent_role"] == "architect"
        assert d["display_name"] == "Architect"
        assert d["score"] == 0.95
        assert d["matched_terms"] == ["architecture", "design"]
        assert d["match_type"] == "exact"


class TestSingletonInstance:
    """Tests for singleton instance."""
    
    def test_get_fuzzy_discovery_returns_same_instance(self):
        """Verify singleton pattern."""
        instance1 = get_fuzzy_discovery()
        instance2 = get_fuzzy_discovery()
        
        assert instance1 is instance2
