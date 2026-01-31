# =============================================================================
# Session Continuity Protocol
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Session continuity for durable memory across sessions."""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
import json


class SessionMemory(BaseModel):
    """Memory entry for session continuity."""
    key: str
    value: Any
    category: str  # "decision", "context", "artifact", "preference"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    created_by: str  # Agent role
    importance: int = 1  # 1-5, higher = more important


class SessionContext(BaseModel):
    """Full session context for continuity."""
    session_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_active: datetime = Field(default_factory=datetime.utcnow)
    
    # Memory entries
    memories: Dict[str, SessionMemory] = Field(default_factory=dict)
    
    # Key decisions made
    decisions: List[Dict[str, Any]] = Field(default_factory=list)
    
    # Active tasks
    active_tasks: List[str] = Field(default_factory=list)
    
    # Collaboration mode history
    mode_history: List[Dict[str, Any]] = Field(default_factory=list)
    
    # Agent states
    agent_states: Dict[str, str] = Field(default_factory=dict)


class SessionContinuityProtocol:
    """
    Protocol for maintaining session continuity.
    
    From the article:
    "Session Continuity: Durable memory that persists across sessions.
    The agent can recall decisions, context, and preferences."
    
    Key features:
    1. Remember key decisions and their rationale
    2. Persist context across session breaks
    3. Track what was tried and what worked
    4. Enable resumption after interruption
    """
    
    def __init__(self, session_id: str):
        self.context = SessionContext(session_id=session_id)
    
    def remember(
        self,
        key: str,
        value: Any,
        category: str,
        agent_role: str,
        importance: int = 1
    ) -> SessionMemory:
        """
        Store a memory for later recall.
        
        Categories:
        - decision: A decision that was made
        - context: Background context
        - artifact: An artifact reference
        - preference: User or agent preference
        """
        memory = SessionMemory(
            key=key,
            value=value,
            category=category,
            created_by=agent_role,
            importance=importance
        )
        
        self.context.memories[key] = memory
        self.context.last_active = datetime.utcnow()
        
        return memory
    
    def recall(self, key: str) -> Optional[Any]:
        """Recall a stored memory by key."""
        memory = self.context.memories.get(key)
        return memory.value if memory else None
    
    def recall_by_category(self, category: str) -> List[SessionMemory]:
        """Recall all memories of a given category."""
        return [m for m in self.context.memories.values() if m.category == category]
    
    def recall_important(self, min_importance: int = 3) -> List[SessionMemory]:
        """Recall memories with importance >= threshold."""
        return [m for m in self.context.memories.values() if m.importance >= min_importance]
    
    def record_decision(
        self,
        decision: str,
        rationale: str,
        agent_role: str,
        alternatives_considered: List[str] = None
    ) -> Dict[str, Any]:
        """Record a key decision for future reference."""
        record = {
            "decision": decision,
            "rationale": rationale,
            "agent_role": agent_role,
            "alternatives_considered": alternatives_considered or [],
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self.context.decisions.append(record)
        
        # Also store as memory
        self.remember(
            key=f"decision_{len(self.context.decisions)}",
            value=record,
            category="decision",
            agent_role=agent_role,
            importance=4
        )
        
        return record
    
    def get_decisions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent decisions."""
        return self.context.decisions[-limit:]
    
    def update_agent_state(self, agent_role: str, state: str) -> None:
        """Update the stored state for an agent."""
        self.context.agent_states[agent_role] = state
        self.context.last_active = datetime.utcnow()
    
    def get_agent_state(self, agent_role: str) -> Optional[str]:
        """Get the stored state for an agent."""
        return self.context.agent_states.get(agent_role)
    
    def get_resumption_prompt(self) -> str:
        """
        Generate a prompt section for session resumption.
        
        This helps agents pick up where they left off.
        """
        lines = ["### Session Continuity", ""]
        
        # Recent decisions
        decisions = self.get_decisions(5)
        if decisions:
            lines.append("**Recent Decisions:**")
            for d in decisions:
                lines.append(f"- {d['decision']} (by {d['agent_role']})")
            lines.append("")
        
        # Important memories
        important = self.recall_important(3)
        if important:
            lines.append("**Key Context:**")
            for m in important[:5]:
                lines.append(f"- [{m.category}] {m.key}: {m.value}")
            lines.append("")
        
        # Agent states
        if self.context.agent_states:
            lines.append("**Agent States:**")
            for agent, state in self.context.agent_states.items():
                lines.append(f"- {agent}: {state}")
        
        return "\n".join(lines)
    
    def export(self) -> str:
        """Export session context as JSON for persistence."""
        return self.context.model_dump_json(indent=2)
    
    @classmethod
    def import_context(cls, json_str: str) -> "SessionContinuityProtocol":
        """Import session context from JSON."""
        context = SessionContext.model_validate_json(json_str)
        protocol = cls(context.session_id)
        protocol.context = context
        return protocol
