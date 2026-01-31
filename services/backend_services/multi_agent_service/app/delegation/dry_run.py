# =============================================================================
# Dry-Run Preview Mode for Delegation
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2026-01-12-introducing-prompt-library-cli/
# =============================================================================
"""
Dry-run preview mode for agent delegation.

Provides:
- Preview delegation outcomes before execution
- No side effects in preview mode
- Builds trust through transparency
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class DelegationAction(str, Enum):
    """Types of actions that can occur during delegation."""
    TASK_CREATION = "task_creation"
    AGENT_ASSIGNMENT = "agent_assignment"
    TOOL_INVOCATION = "tool_invocation"
    ARTIFACT_CREATION = "artifact_creation"
    PEER_CONSULTATION = "peer_consultation"
    CONTRACT_CHECK = "contract_check"
    STATE_TRANSITION = "state_transition"


@dataclass
class PredictedAction:
    """A predicted action during delegation preview."""
    action_type: DelegationAction
    description: str
    target: str
    estimated_duration_ms: int = 0
    confidence: float = 0.9
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "action_type": self.action_type.value,
            "description": self.description,
            "target": self.target,
            "estimated_duration_ms": self.estimated_duration_ms,
            "confidence": self.confidence,
            "metadata": self.metadata,
        }


@dataclass
class DelegationPreview:
    """
    Result of a dry-run delegation preview.
    
    Shows what would happen if delegation were executed,
    without actually performing any actions.
    """
    task: str
    target_agent: str
    predicted_actions: List[PredictedAction] = field(default_factory=list)
    estimated_total_duration_ms: int = 0
    estimated_token_usage: int = 0
    contract_warnings: List[str] = field(default_factory=list)
    recommended_reviewers: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    potential_blockers: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "task": self.task,
            "target_agent": self.target_agent,
            "predicted_actions": [a.to_dict() for a in self.predicted_actions],
            "estimated_total_duration_ms": self.estimated_total_duration_ms,
            "estimated_token_usage": self.estimated_token_usage,
            "contract_warnings": self.contract_warnings,
            "recommended_reviewers": self.recommended_reviewers,
            "prerequisites": self.prerequisites,
            "potential_blockers": self.potential_blockers,
            "created_at": self.created_at.isoformat(),
            "action_count": len(self.predicted_actions),
        }


class DelegationPreviewBuilder:
    """
    Builds delegation previews by analyzing task and target agent.
    
    Used to generate dry-run previews before actual delegation.
    """
    
    AGENT_CAPABILITIES = {
        "architect": {
            "tools": ["design_system", "create_diagram", "review_architecture"],
            "domains": ["architecture", "design", "system", "integration"],
            "typical_duration_ms": 5000,
            "token_estimate": 2000,
        },
        "developer": {
            "tools": ["write_code", "refactor", "implement_feature"],
            "domains": ["code", "implementation", "development", "programming"],
            "typical_duration_ms": 8000,
            "token_estimate": 3000,
        },
        "data_analyst": {
            "tools": ["analyze_data", "create_report", "query_database"],
            "domains": ["data", "analytics", "statistics", "reports"],
            "typical_duration_ms": 6000,
            "token_estimate": 2500,
        },
        "business_analyst": {
            "tools": ["gather_requirements", "create_specification", "analyze_process"],
            "domains": ["business", "requirements", "process", "workflow"],
            "typical_duration_ms": 4000,
            "token_estimate": 1800,
        },
        "tester": {
            "tools": ["write_tests", "run_tests", "analyze_coverage"],
            "domains": ["testing", "quality", "validation", "verification"],
            "typical_duration_ms": 5000,
            "token_estimate": 2200,
        },
        "operations_manager": {
            "tools": ["analyze_operations", "optimize_process", "track_metrics"],
            "domains": ["operations", "efficiency", "process", "metrics"],
            "typical_duration_ms": 4500,
            "token_estimate": 1900,
        },
        "supply_chain_analyst": {
            "tools": ["analyze_inventory", "forecast_demand", "optimize_logistics"],
            "domains": ["supply chain", "inventory", "logistics", "procurement"],
            "typical_duration_ms": 5500,
            "token_estimate": 2300,
        },
    }
    
    PEER_REVIEWERS = {
        "architect": ["developer", "business_analyst"],
        "developer": ["architect", "tester"],
        "data_analyst": ["business_analyst", "data_scientist"],
        "business_analyst": ["architect", "operations_manager"],
        "tester": ["developer", "architect"],
        "operations_manager": ["business_analyst", "supply_chain_analyst"],
        "supply_chain_analyst": ["operations_manager", "data_analyst"],
    }
    
    def __init__(self):
        self._custom_capabilities: Dict[str, Dict[str, Any]] = {}
    
    def register_agent_capabilities(
        self,
        agent_role: str,
        capabilities: Dict[str, Any]
    ) -> None:
        """Register custom agent capabilities for preview."""
        self._custom_capabilities[agent_role] = capabilities
        logger.info(f"Registered capabilities for: {agent_role}")
    
    def get_capabilities(self, agent_role: str) -> Dict[str, Any]:
        """Get capabilities for an agent."""
        if agent_role in self._custom_capabilities:
            return self._custom_capabilities[agent_role]
        return self.AGENT_CAPABILITIES.get(agent_role, {
            "tools": [],
            "domains": [],
            "typical_duration_ms": 3000,
            "token_estimate": 1500,
        })
    
    def build_preview(
        self,
        task: str,
        target_agent: str,
        context: Optional[Dict[str, Any]] = None
    ) -> DelegationPreview:
        """
        Build a delegation preview for a task.
        
        Args:
            task: The task description
            target_agent: The target agent role
            context: Optional additional context
            
        Returns:
            DelegationPreview with predicted actions
        """
        context = context or {}
        capabilities = self.get_capabilities(target_agent)
        
        preview = DelegationPreview(
            task=task,
            target_agent=target_agent
        )
        
        preview.predicted_actions.append(PredictedAction(
            action_type=DelegationAction.CONTRACT_CHECK,
            description="Validate contract state allows delegation",
            target="contract_adapter",
            estimated_duration_ms=50,
            confidence=0.99
        ))
        
        preview.predicted_actions.append(PredictedAction(
            action_type=DelegationAction.TASK_CREATION,
            description=f"Create task on blackboard: {task[:50]}...",
            target="blackboard",
            estimated_duration_ms=100,
            confidence=0.95
        ))
        
        preview.predicted_actions.append(PredictedAction(
            action_type=DelegationAction.AGENT_ASSIGNMENT,
            description=f"Assign task to {target_agent}",
            target=target_agent,
            estimated_duration_ms=50,
            confidence=0.95
        ))
        
        task_lower = task.lower()
        matching_tools = []
        for tool in capabilities.get("tools", []):
            tool_keywords = tool.replace("_", " ").split()
            if any(kw in task_lower for kw in tool_keywords):
                matching_tools.append(tool)
        
        if not matching_tools and capabilities.get("tools"):
            matching_tools = [capabilities["tools"][0]]
        
        for tool in matching_tools:
            preview.predicted_actions.append(PredictedAction(
                action_type=DelegationAction.TOOL_INVOCATION,
                description=f"Invoke tool: {tool}",
                target=tool,
                estimated_duration_ms=capabilities.get("typical_duration_ms", 3000),
                confidence=0.85,
                metadata={"tool_name": tool}
            ))
        
        preview.predicted_actions.append(PredictedAction(
            action_type=DelegationAction.ARTIFACT_CREATION,
            description="Create result artifact",
            target="blackboard",
            estimated_duration_ms=100,
            confidence=0.90
        ))
        
        if context.get("requires_review", True):
            reviewers = self.PEER_REVIEWERS.get(target_agent, [])
            if reviewers:
                preview.predicted_actions.append(PredictedAction(
                    action_type=DelegationAction.PEER_CONSULTATION,
                    description=f"Request peer review from {reviewers[0]}",
                    target=reviewers[0],
                    estimated_duration_ms=2000,
                    confidence=0.75
                ))
                preview.recommended_reviewers = reviewers
        
        preview.predicted_actions.append(PredictedAction(
            action_type=DelegationAction.STATE_TRANSITION,
            description="Transition to completed state",
            target="contract_adapter",
            estimated_duration_ms=50,
            confidence=0.95
        ))
        
        preview.estimated_total_duration_ms = sum(
            a.estimated_duration_ms for a in preview.predicted_actions
        )
        preview.estimated_token_usage = capabilities.get("token_estimate", 1500)
        
        preview.contract_warnings = self._check_contract_warnings(
            task, target_agent, context
        )
        preview.prerequisites = self._identify_prerequisites(task, context)
        preview.potential_blockers = self._identify_blockers(
            target_agent, context
        )
        
        return preview
    
    def _check_contract_warnings(
        self,
        task: str,
        target_agent: str,
        context: Dict[str, Any]
    ) -> List[str]:
        """Check for potential contract warnings."""
        warnings = []
        
        if len(task) < 20:
            warnings.append("Task description may be too brief for clear delegation")
        
        if context.get("assumption_count", 0) >= 2:
            warnings.append("Approaching assumption limit (3 max)")
        
        if context.get("failed_attempts", 0) >= 3:
            warnings.append("Multiple failed attempts - consider struggle signal")
        
        capabilities = self.get_capabilities(target_agent)
        domains = capabilities.get("domains", [])
        task_lower = task.lower()
        if not any(d in task_lower for d in domains):
            warnings.append(f"Task may be outside {target_agent}'s primary domain")
        
        return warnings
    
    def _identify_prerequisites(
        self,
        task: str,
        context: Dict[str, Any]
    ) -> List[str]:
        """Identify prerequisites for the task."""
        prerequisites = []
        
        task_lower = task.lower()
        
        if "implement" in task_lower or "code" in task_lower:
            if not context.get("has_design"):
                prerequisites.append("Design or specification document")
        
        if "test" in task_lower:
            if not context.get("has_implementation"):
                prerequisites.append("Implementation to test")
        
        if "deploy" in task_lower:
            if not context.get("has_tests"):
                prerequisites.append("Passing test suite")
        
        if "analyze" in task_lower and "data" in task_lower:
            if not context.get("has_data"):
                prerequisites.append("Data source or dataset")
        
        return prerequisites
    
    def _identify_blockers(
        self,
        target_agent: str,
        context: Dict[str, Any]
    ) -> List[str]:
        """Identify potential blockers."""
        blockers = []
        
        if context.get("agent_busy", {}).get(target_agent):
            blockers.append(f"{target_agent} is currently busy with another task")
        
        if context.get("blackboard_unavailable"):
            blockers.append("Blackboard service is unavailable - degraded mode")
        
        if context.get("contract_state") == "hard_stopped":
            blockers.append("Contract is in hard stop state")
        
        return blockers


class DryRunExecutor:
    """
    Executes delegation with optional dry-run mode.
    
    In dry-run mode, returns preview without side effects.
    """
    
    def __init__(self, preview_builder: Optional[DelegationPreviewBuilder] = None):
        self._preview_builder = preview_builder or DelegationPreviewBuilder()
    
    async def delegate(
        self,
        task: str,
        target_agent: str,
        dry_run: bool = False,
        context: Optional[Dict[str, Any]] = None,
        executor_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """
        Delegate a task with optional dry-run preview.
        
        Args:
            task: The task to delegate
            target_agent: Target agent role
            dry_run: If True, only preview without execution
            context: Additional context for the delegation
            executor_callback: Callback to execute actual delegation
            
        Returns:
            Preview result (if dry_run) or execution result
        """
        context = context or {}
        
        preview = self._preview_builder.build_preview(task, target_agent, context)
        
        if dry_run:
            logger.info(f"Dry-run preview for task: {task[:50]}... -> {target_agent}")
            return {
                "mode": "dry_run",
                "preview": preview.to_dict(),
                "message": "This is a preview. No actions were taken."
            }
        
        if preview.potential_blockers:
            logger.warning(f"Potential blockers detected: {preview.potential_blockers}")
        
        if executor_callback:
            result = await executor_callback(task, target_agent, context)
            return {
                "mode": "executed",
                "result": result,
                "preview_was": preview.to_dict()
            }
        
        return {
            "mode": "executed",
            "message": "Delegation queued (no executor callback provided)",
            "preview_was": preview.to_dict()
        }


_preview_builder_instance: Optional[DelegationPreviewBuilder] = None
_dry_run_executor_instance: Optional[DryRunExecutor] = None


def get_preview_builder() -> DelegationPreviewBuilder:
    """Get the singleton preview builder instance."""
    global _preview_builder_instance
    if _preview_builder_instance is None:
        _preview_builder_instance = DelegationPreviewBuilder()
    return _preview_builder_instance


def get_dry_run_executor() -> DryRunExecutor:
    """Get the singleton dry-run executor instance."""
    global _dry_run_executor_instance
    if _dry_run_executor_instance is None:
        _dry_run_executor_instance = DryRunExecutor()
    return _dry_run_executor_instance
