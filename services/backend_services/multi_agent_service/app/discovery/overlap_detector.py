# =============================================================================
# Agent Overlap Detector
# Phase 18: Microsoft Best Practices Integration
# Reference: https://developer.microsoft.com/blog/designing-multi-agent-intelligence
# =============================================================================
"""
Detect overlapping capabilities between agents to prevent redundancy.

Analyzes agent tool definitions and system prompts to identify
potential overlap that could cause confusion in routing.
"""

from dataclasses import dataclass
from typing import Dict, List, Set, Tuple, Any, TYPE_CHECKING
import logging
import re
from collections import defaultdict

if TYPE_CHECKING:
    from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


@dataclass
class OverlapWarning:
    """Warning about detected overlap between agents."""
    agent_a: str
    agent_b: str
    overlap_type: str  # tool, domain, capability
    severity: str  # low, medium, high
    details: str
    overlap_score: float  # 0.0 to 1.0
    
    def to_dict(self) -> Dict:
        return {
            "agent_a": self.agent_a,
            "agent_b": self.agent_b,
            "overlap_type": self.overlap_type,
            "severity": self.severity,
            "details": self.details,
            "overlap_score": self.overlap_score,
        }


class AgentOverlapDetector:
    """
    Analyzes agents for capability overlap.
    
    Helps prevent:
    - Redundant agents doing the same work
    - Confusion in intent classification
    - Inefficient routing
    """
    
    # Threshold for warning about overlap
    TOOL_OVERLAP_THRESHOLD = 0.5  # 50% tool overlap
    DOMAIN_OVERLAP_THRESHOLD = 0.7  # 70% domain keyword overlap
    
    def __init__(self):
        self._domain_keywords = self._build_domain_keywords()
    
    def _build_domain_keywords(self) -> Dict[str, Set[str]]:
        """Build domain keyword sets for classification."""
        return {
            "business": {
                "business", "strategy", "market", "revenue", "profit",
                "customer", "sales", "marketing", "stakeholder", "roi"
            },
            "technical": {
                "code", "api", "database", "schema", "architecture",
                "deployment", "infrastructure", "kubernetes", "docker"
            },
            "data": {
                "data", "analytics", "kpi", "metric", "dashboard",
                "visualization", "report", "analysis", "statistics"
            },
            "governance": {
                "governance", "compliance", "policy", "quality",
                "audit", "security", "risk", "regulation"
            },
            "operations": {
                "operations", "process", "workflow", "supply chain",
                "inventory", "logistics", "manufacturing"
            },
        }
    
    def detect_overlaps(
        self,
        agents: Dict[str, "BaseAgent"]
    ) -> List[OverlapWarning]:
        """
        Analyze agents for capability overlap.
        
        Returns list of warnings for significant overlaps.
        """
        warnings = []
        agent_names = list(agents.keys())
        
        # Compare each pair of agents
        for i, name_a in enumerate(agent_names):
            for name_b in agent_names[i + 1:]:
                agent_a = agents[name_a]
                agent_b = agents[name_b]
                
                # Check tool overlap
                tool_warnings = self._check_tool_overlap(
                    name_a, agent_a, name_b, agent_b
                )
                warnings.extend(tool_warnings)
                
                # Check domain overlap via system prompt
                domain_warnings = self._check_domain_overlap(
                    name_a, agent_a, name_b, agent_b
                )
                warnings.extend(domain_warnings)
        
        # Sort by severity and score
        severity_order = {"high": 0, "medium": 1, "low": 2}
        warnings.sort(
            key=lambda w: (severity_order.get(w.severity, 3), -w.overlap_score)
        )
        
        return warnings
    
    def _check_tool_overlap(
        self,
        name_a: str,
        agent_a: "BaseAgent",
        name_b: str,
        agent_b: "BaseAgent"
    ) -> List[OverlapWarning]:
        """Check for overlapping tools between agents."""
        warnings = []
        
        # Get tool names
        tools_a = set(agent_a._tools.keys()) if hasattr(agent_a, '_tools') else set()
        tools_b = set(agent_b._tools.keys()) if hasattr(agent_b, '_tools') else set()
        
        if not tools_a or not tools_b:
            return warnings
        
        # Calculate overlap
        overlap = tools_a.intersection(tools_b)
        total = tools_a.union(tools_b)
        
        if not total:
            return warnings
        
        overlap_score = len(overlap) / len(total)
        
        if overlap_score >= self.TOOL_OVERLAP_THRESHOLD:
            severity = "high" if overlap_score >= 0.7 else "medium"
            warnings.append(OverlapWarning(
                agent_a=name_a,
                agent_b=name_b,
                overlap_type="tool",
                severity=severity,
                details=f"Shared tools: {sorted(overlap)}",
                overlap_score=overlap_score
            ))
        
        return warnings
    
    def _check_domain_overlap(
        self,
        name_a: str,
        agent_a: "BaseAgent",
        name_b: str,
        agent_b: "BaseAgent"
    ) -> List[OverlapWarning]:
        """Check for overlapping domains via system prompt analysis."""
        warnings = []
        
        # Extract domains from agent roles/prompts
        domains_a = self._extract_domains(name_a, agent_a)
        domains_b = self._extract_domains(name_b, agent_b)
        
        if not domains_a or not domains_b:
            return warnings
        
        # Calculate overlap
        overlap = domains_a.intersection(domains_b)
        total = domains_a.union(domains_b)
        
        if not total:
            return warnings
        
        overlap_score = len(overlap) / len(total)
        
        if overlap_score >= self.DOMAIN_OVERLAP_THRESHOLD:
            severity = "high" if overlap_score >= 0.85 else "medium"
            warnings.append(OverlapWarning(
                agent_a=name_a,
                agent_b=name_b,
                overlap_type="domain",
                severity=severity,
                details=f"Shared domains: {sorted(overlap)}",
                overlap_score=overlap_score
            ))
        
        return warnings
    
    def _extract_domains(
        self,
        agent_name: str,
        agent: "BaseAgent"
    ) -> Set[str]:
        """Extract domain keywords from agent."""
        domains = set()
        
        # Check agent name
        name_lower = agent_name.lower()
        for domain, keywords in self._domain_keywords.items():
            if any(kw in name_lower for kw in keywords):
                domains.add(domain)
        
        # Check config role if available
        if hasattr(agent, 'config') and hasattr(agent.config, 'role'):
            role = str(agent.config.role).lower()
            for domain, keywords in self._domain_keywords.items():
                if any(kw in role for kw in keywords):
                    domains.add(domain)
        
        return domains
    
    def get_overlap_report(
        self,
        agents: Dict[str, "BaseAgent"]
    ) -> Dict[str, Any]:
        """
        Generate a full overlap report for all agents.
        """
        warnings = self.detect_overlaps(agents)
        
        # Group by severity
        by_severity = defaultdict(list)
        for w in warnings:
            by_severity[w.severity].append(w.to_dict())
        
        # Calculate overlap matrix
        agent_names = list(agents.keys())
        matrix = {}
        for name in agent_names:
            matrix[name] = {
                other: 0.0 for other in agent_names if other != name
            }
        
        for w in warnings:
            if w.agent_a in matrix and w.agent_b in matrix[w.agent_a]:
                matrix[w.agent_a][w.agent_b] = max(
                    matrix[w.agent_a][w.agent_b],
                    w.overlap_score
                )
            if w.agent_b in matrix and w.agent_a in matrix[w.agent_b]:
                matrix[w.agent_b][w.agent_a] = max(
                    matrix[w.agent_b][w.agent_a],
                    w.overlap_score
                )
        
        return {
            "total_warnings": len(warnings),
            "by_severity": dict(by_severity),
            "overlap_matrix": matrix,
            "recommendations": self._generate_recommendations(warnings)
        }
    
    def _generate_recommendations(
        self,
        warnings: List[OverlapWarning]
    ) -> List[str]:
        """Generate recommendations based on warnings."""
        recommendations = []
        
        high_severity = [w for w in warnings if w.severity == "high"]
        
        if high_severity:
            recommendations.append(
                f"Found {len(high_severity)} high-severity overlaps. "
                "Consider consolidating or clearly differentiating these agents."
            )
        
        tool_overlaps = [w for w in warnings if w.overlap_type == "tool"]
        if tool_overlaps:
            recommendations.append(
                f"Found {len(tool_overlaps)} tool overlaps. "
                "Consider refactoring shared tools into a common module "
                "or assigning tools to specific agents."
            )
        
        domain_overlaps = [w for w in warnings if w.overlap_type == "domain"]
        if domain_overlaps:
            recommendations.append(
                f"Found {len(domain_overlaps)} domain overlaps. "
                "Consider using a supervisor agent pattern to coordinate "
                "agents in the same domain."
            )
        
        if not warnings:
            recommendations.append(
                "No significant overlaps detected. "
                "Agent responsibilities are well-separated."
            )
        
        return recommendations


def detect_agent_overlap(
    agents: Dict[str, "BaseAgent"]
) -> List[OverlapWarning]:
    """
    Convenience function to detect overlaps.
    
    Usage:
        from .overlap_detector import detect_agent_overlap
        warnings = detect_agent_overlap(orchestrator._sub_agents)
    """
    detector = AgentOverlapDetector()
    return detector.detect_overlaps(agents)


def get_overlap_report(
    agents: Dict[str, "BaseAgent"]
) -> Dict[str, Any]:
    """
    Convenience function to get full overlap report.
    """
    detector = AgentOverlapDetector()
    return detector.get_overlap_report(agents)
