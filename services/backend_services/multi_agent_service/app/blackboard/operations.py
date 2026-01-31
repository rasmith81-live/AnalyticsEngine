# =============================================================================
# Blackboard Operations
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Operations for agents to interact with the blackboard."""

from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

from .models import (
    TaskStatus,
    BlackboardTask,
    BlackboardArtifact,
    ApprovalGate,
    StruggleSignalEntry,
    AuditLogEntry,
    AgentBlackboard,
)
from ..contracts.violations import ContractViolation
from ..contracts.tier_rules import RuleTier

logger = logging.getLogger(__name__)


class BlackboardOperations:
    """
    Operations for agents to interact with the blackboard.
    
    All operations are logged and validated against contracts.
    Key principle: No conversation between agents. Read state, do work, write state.
    """
    
    # Adversarial pairing: maps creators to their designated reviewers
    REVIEWER_MAP: Dict[str, str] = {
        # Strategy & Analysis Layer
        "business_strategist": "business_analyst",
        "business_analyst": "business_strategist",
        "data_analyst": "data_scientist",
        "data_scientist": "data_analyst",
        "operations_manager": "data_scientist",
        "mapping_specialist": "architect",
        "document_analyzer": "business_analyst",
        "competitive_analyst": "business_strategist",
        
        # Technical Design Layer
        "architect": "data_governance_specialist",
        "developer": "tester",
        "tester": "developer",
        "documenter": "architect",
        "deployment_specialist": "itil_manager",
        "ui_designer": "tester",
        "itil_manager": "risk_compliance_officer",
        "connection_specialist": "tester",
        
        # Business Operations Layer
        "sales_manager": "accountant",
        "marketing_manager": "data_analyst",
        "accountant": "sales_manager",
        "customer_success_manager": "sales_manager",
        "hr_talent_analyst": "data_governance_specialist",
        "supply_chain_analyst": "risk_compliance_officer",
        "risk_compliance_officer": "itil_manager",
        "project_manager": "operations_manager",
        
        # Governance Layer
        "data_governance_specialist": "architect",
        "process_scenario_modeler": "operations_manager",
        "librarian_curator": "data_governance_specialist",
        
        # Default
        "coordinator": "architect",
    }
    
    def __init__(self, blackboard: AgentBlackboard):
        self.blackboard = blackboard
        self.audit_log: List[AuditLogEntry] = []
    
    async def claim_task(
        self,
        agent_role: str,
        task_id: str
    ) -> BlackboardTask:
        """
        Agent claims an unclaimed task.
        
        Contract rules enforced:
        - Task must be unclaimed
        - Agent must not be in failed_by list (two-failures rule)
        - Dependencies must be satisfied
        """
        task = self.blackboard.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")
        
        if task.status != TaskStatus.UNCLAIMED:
            raise ContractViolation(
                rule="Cannot claim already-claimed task",
                tier=RuleTier.TIER_1,
                context=f"Task {task_id} is {task.status.value}",
                agent_role=agent_role,
                session_id=self.blackboard.session_id
            )
        
        # Check two-failures rule
        if agent_role in task.failed_by:
            raise ContractViolation(
                rule="Cannot claim task previously failed by this agent",
                tier=RuleTier.TIER_1,
                context=f"Agent {agent_role} already failed task {task_id}",
                agent_role=agent_role,
                session_id=self.blackboard.session_id
            )
        
        # Check dependencies
        for dep_id in task.dependencies:
            dep_task = self.blackboard.tasks.get(dep_id)
            if dep_task and dep_task.status != TaskStatus.MERGED:
                raise ContractViolation(
                    rule="Cannot claim task with unsatisfied dependencies",
                    tier=RuleTier.TIER_1,
                    context=f"Dependency {dep_id} is {dep_task.status.value}",
                    agent_role=agent_role,
                    session_id=self.blackboard.session_id
                )
        
        # Claim the task
        previous_state = task.model_dump()
        task.status = TaskStatus.CLAIMED
        task.assigned_to = agent_role
        task.claimed_at = datetime.utcnow()
        
        # Assign reviewer (adversarial pair)
        task.reviewer = self._get_reviewer_for_role(agent_role)
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="claim_task",
            entity_type="task",
            entity_id=task_id,
            previous_state=previous_state,
            new_state=task.model_dump()
        )
        
        self.blackboard.last_modified = datetime.utcnow()
        return task
    
    async def submit_artifact(
        self,
        agent_role: str,
        artifact: BlackboardArtifact
    ) -> BlackboardArtifact:
        """
        Agent submits an artifact for review.
        
        Contract rules enforced:
        - Agent must be assigned to the task
        - Task must be in progress
        """
        task = self.blackboard.tasks.get(artifact.task_id)
        if not task:
            raise ValueError(f"Task {artifact.task_id} not found")
        
        if task.assigned_to != agent_role:
            raise ContractViolation(
                rule="Can only submit artifacts for assigned tasks",
                tier=RuleTier.TIER_1,
                context=f"Task assigned to {task.assigned_to}, not {agent_role}",
                agent_role=agent_role,
                session_id=self.blackboard.session_id
            )
        
        # Store artifact
        self.blackboard.artifacts[artifact.artifact_id] = artifact
        
        # Add to review queue
        self.blackboard.review_queue.append(artifact.artifact_id)
        
        # Update task status
        previous_state = task.model_dump()
        task.status = TaskStatus.READY_FOR_REVIEW
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="submit_artifact",
            entity_type="artifact",
            entity_id=artifact.artifact_id,
            previous_state=None,
            new_state=artifact.model_dump()
        )
        
        self.blackboard.last_modified = datetime.utcnow()
        return artifact
    
    async def review_artifact(
        self,
        reviewer_role: str,
        artifact_id: str,
        approved: bool,
        notes: str
    ) -> BlackboardArtifact:
        """
        Reviewer approves or rejects an artifact.
        
        Contract rules enforced:
        - Reviewer must be assigned reviewer for the task
        - Reviewer cannot be the creator (adversarial constraint)
        """
        artifact = self.blackboard.artifacts.get(artifact_id)
        if not artifact:
            raise ValueError(f"Artifact {artifact_id} not found")
        
        # Adversarial constraint: cannot review own work
        if artifact.created_by == reviewer_role:
            raise ContractViolation(
                rule="Agents cannot review their own work",
                tier=RuleTier.TIER_0,
                context=f"Agent {reviewer_role} created artifact {artifact_id}",
                agent_role=reviewer_role,
                session_id=self.blackboard.session_id
            )
        
        task = self.blackboard.tasks.get(artifact.task_id)
        if task and task.reviewer != reviewer_role:
            raise ContractViolation(
                rule="Only assigned reviewer can review",
                tier=RuleTier.TIER_1,
                context=f"Assigned reviewer is {task.reviewer}, not {reviewer_role}",
                agent_role=reviewer_role,
                session_id=self.blackboard.session_id
            )
        
        # Update artifact
        previous_state = artifact.model_dump()
        artifact.reviewed_by = reviewer_role
        artifact.review_status = "approved" if approved else "rejected"
        artifact.review_notes = notes
        artifact.reviewed_at = datetime.utcnow()
        
        # Update task status
        if task:
            if approved:
                task.status = TaskStatus.APPROVED
            else:
                task.status = TaskStatus.REJECTED
                task.failure_count += 1
                if task.assigned_to and task.assigned_to not in task.failed_by:
                    task.failed_by.append(task.assigned_to)
                task.failure_reasons.append(notes)
        
        # Remove from review queue
        if artifact_id in self.blackboard.review_queue:
            self.blackboard.review_queue.remove(artifact_id)
        
        # Log the operation
        self._log_operation(
            agent=reviewer_role,
            action="review_artifact",
            entity_type="artifact",
            entity_id=artifact_id,
            previous_state=previous_state,
            new_state=artifact.model_dump()
        )
        
        self.blackboard.last_modified = datetime.utcnow()
        return artifact
    
    async def submit_approval_request(
        self,
        agent_role: str,
        gate: ApprovalGate
    ) -> ApprovalGate:
        """
        Agent submits an approval request before executing.
        
        This is the approval gate before any state-changing action.
        """
        gate.requesting_agent = agent_role
        self.blackboard.approval_gates[gate.gate_id] = gate
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="submit_approval_request",
            entity_type="approval_gate",
            entity_id=gate.gate_id,
            previous_state=None,
            new_state=gate.model_dump()
        )
        
        self.blackboard.last_modified = datetime.utcnow()
        return gate
    
    async def signal_struggle(
        self,
        agent_role: str,
        signal: StruggleSignalEntry
    ) -> StruggleSignalEntry:
        """
        Agent signals that they are stuck.
        
        The struggle protocol transforms deception risk into collaboration.
        """
        signal.agent = agent_role
        self.blackboard.struggle_signals[signal.signal_id] = signal
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="signal_struggle",
            entity_type="struggle_signal",
            entity_id=signal.signal_id,
            previous_state=None,
            new_state=signal.model_dump()
        )
        
        logger.info(f"Struggle signal from {agent_role}: {signal.signal_type}")
        
        self.blackboard.last_modified = datetime.utcnow()
        return signal
    
    async def resolve_struggle(
        self,
        resolver_role: str,
        signal_id: str,
        resolution: str
    ) -> StruggleSignalEntry:
        """Resolve a struggle signal."""
        signal = self.blackboard.struggle_signals.get(signal_id)
        if not signal:
            raise ValueError(f"Struggle signal {signal_id} not found")
        
        previous_state = signal.model_dump()
        signal.resolved = True
        signal.resolved_by = resolver_role
        signal.resolution = resolution
        signal.resolved_at = datetime.utcnow()
        
        # Log the operation
        self._log_operation(
            agent=resolver_role,
            action="resolve_struggle",
            entity_type="struggle_signal",
            entity_id=signal_id,
            previous_state=previous_state,
            new_state=signal.model_dump()
        )
        
        self.blackboard.last_modified = datetime.utcnow()
        return signal
    
    async def create_task(
        self,
        creator_role: str,
        task: BlackboardTask
    ) -> BlackboardTask:
        """Create a new task on the blackboard."""
        task.created_by = creator_role
        self.blackboard.tasks[task.task_id] = task
        
        # Log the operation
        self._log_operation(
            agent=creator_role,
            action="create_task",
            entity_type="task",
            entity_id=task.task_id,
            previous_state=None,
            new_state=task.model_dump()
        )
        
        self.blackboard.last_modified = datetime.utcnow()
        return task
    
    def _get_reviewer_for_role(self, creator_role: str) -> str:
        """Map creators to their adversarial reviewers."""
        return self.REVIEWER_MAP.get(creator_role, "coordinator")
    
    def _log_operation(
        self,
        agent: str,
        action: str,
        entity_type: str,
        entity_id: str,
        previous_state: Optional[Dict[str, Any]],
        new_state: Dict[str, Any]
    ) -> None:
        """Log an operation to the audit trail."""
        entry = AuditLogEntry(
            agent=agent,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            previous_state=previous_state,
            new_state=new_state,
            session_id=self.blackboard.session_id
        )
        self.audit_log.append(entry)
    
    def get_audit_log(self) -> List[AuditLogEntry]:
        """Get the full audit log."""
        return self.audit_log.copy()
