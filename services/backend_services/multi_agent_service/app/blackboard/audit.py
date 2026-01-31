# =============================================================================
# Audit Logger for Blackboard Operations
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Audit logging for full traceability of all agent actions."""

from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

from .models import AuditLogEntry

logger = logging.getLogger(__name__)


class AuditLogger:
    """
    Centralized audit logging for all blackboard operations.
    
    Everything visible, everything auditable.
    """
    
    def __init__(self, store=None):
        self.store = store
        self._in_memory_log: List[AuditLogEntry] = []
    
    async def log(
        self,
        session_id: str,
        agent: str,
        action: str,
        entity_type: str,
        entity_id: str,
        previous_state: Optional[Dict[str, Any]] = None,
        new_state: Optional[Dict[str, Any]] = None,
        rules_checked: Optional[List[str]] = None,
        violations: Optional[List[str]] = None
    ) -> AuditLogEntry:
        """Log an operation to the audit trail."""
        entry = AuditLogEntry(
            agent=agent,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            previous_state=previous_state,
            new_state=new_state or {},
            contract_rules_checked=rules_checked or [],
            violations_detected=violations or [],
            session_id=session_id
        )
        
        # Store in memory
        self._in_memory_log.append(entry)
        
        # Persist if store available
        if self.store:
            await self.store.append_audit_entry(
                session_id,
                entry.model_dump(mode="json")
            )
        
        # Log to standard logger
        if violations:
            logger.warning(
                f"Audit: {agent} {action} {entity_type}:{entity_id} "
                f"- VIOLATIONS: {violations}"
            )
        else:
            logger.debug(
                f"Audit: {agent} {action} {entity_type}:{entity_id}"
            )
        
        return entry
    
    def get_entries(
        self,
        session_id: Optional[str] = None,
        agent: Optional[str] = None,
        action: Optional[str] = None,
        entity_type: Optional[str] = None,
        limit: int = 100
    ) -> List[AuditLogEntry]:
        """Query audit log entries with optional filters."""
        entries = self._in_memory_log
        
        if session_id:
            entries = [e for e in entries if e.session_id == session_id]
        if agent:
            entries = [e for e in entries if e.agent == agent]
        if action:
            entries = [e for e in entries if e.action == action]
        if entity_type:
            entries = [e for e in entries if e.entity_type == entity_type]
        
        return entries[-limit:]
    
    def get_violations(
        self,
        session_id: Optional[str] = None,
        agent: Optional[str] = None
    ) -> List[AuditLogEntry]:
        """Get all entries with violations."""
        entries = self._in_memory_log
        
        if session_id:
            entries = [e for e in entries if e.session_id == session_id]
        if agent:
            entries = [e for e in entries if e.agent == agent]
        
        return [e for e in entries if e.violations_detected]
    
    def get_agent_activity(
        self,
        agent: str,
        session_id: Optional[str] = None,
        since: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Get a summary of an agent's activity."""
        entries = [e for e in self._in_memory_log if e.agent == agent]
        
        if session_id:
            entries = [e for e in entries if e.session_id == session_id]
        if since:
            entries = [e for e in entries if e.timestamp >= since]
        
        action_counts: Dict[str, int] = {}
        for entry in entries:
            action_counts[entry.action] = action_counts.get(entry.action, 0) + 1
        
        return {
            "agent": agent,
            "total_actions": len(entries),
            "action_breakdown": action_counts,
            "violations": len([e for e in entries if e.violations_detected]),
            "first_action": entries[0].timestamp.isoformat() if entries else None,
            "last_action": entries[-1].timestamp.isoformat() if entries else None
        }
    
    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Get a summary of all activity in a session."""
        entries = [e for e in self._in_memory_log if e.session_id == session_id]
        
        agent_actions: Dict[str, int] = {}
        for entry in entries:
            agent_actions[entry.agent] = agent_actions.get(entry.agent, 0) + 1
        
        return {
            "session_id": session_id,
            "total_actions": len(entries),
            "agents_involved": list(agent_actions.keys()),
            "agent_action_counts": agent_actions,
            "violations": len([e for e in entries if e.violations_detected]),
            "start_time": entries[0].timestamp.isoformat() if entries else None,
            "end_time": entries[-1].timestamp.isoformat() if entries else None
        }
