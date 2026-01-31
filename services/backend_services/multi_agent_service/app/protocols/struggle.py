# =============================================================================
# Struggle Protocol
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Struggle protocol for transforming deception risk into collaboration."""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class StruggleType(str, Enum):
    """Types of struggle signals."""
    BLOCKED = "blocked"
    CONFUSED = "confused"
    CONFLICTING_EVIDENCE = "conflicting_evidence"
    RESOURCE_MISSING = "resource_missing"
    ASSUMPTION_OVERFLOW = "assumption_overflow"
    REPEATED_FAILURE = "repeated_failure"


class StruggleSignal(BaseModel):
    """
    A structured struggle signal.
    
    From the article:
    "The Struggle Protocol transforms a deception risk into a
    collaboration opportunity. When stuck, agents signal with
    structured format."
    """
    signal_type: StruggleType
    what_i_understand: str
    what_i_tried: List[Dict[str, str]] = Field(default_factory=list)
    where_im_stuck: str
    what_would_help: str
    
    agent_role: str
    session_id: str
    task_id: Optional[str] = None
    attempt_count: int = 0
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    resolved: bool = False
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None
    resolved_by: Optional[str] = None


class StruggleProtocol:
    """
    The Struggle Protocol for signaling when stuck.
    
    Key principles:
    1. After N failed attempts, agent MUST signal (not fake progress)
    2. Signal format is structured for efficient human parsing
    3. Signals are logged for pattern analysis
    4. Resolution is tracked for feedback loop
    """
    
    DEFAULT_SIGNAL_AFTER = 2  # Signal after 2 failed attempts
    
    SIGNAL_TEMPLATE = """🚨 SYNC NEEDED — {signal_type}

**What I understand:**
{what_i_understand}

**What I've tried:**
{tried_list}

**Where I'm stuck:**
{where_im_stuck}

**What would help:**
{what_would_help}
"""
    
    def __init__(
        self,
        session_id: str,
        signal_after: int = DEFAULT_SIGNAL_AFTER
    ):
        self.session_id = session_id
        self.signal_after = signal_after
        self.signals: List[StruggleSignal] = []
        self.attempt_counts: Dict[str, int] = {}  # task_id -> count
    
    def record_attempt(self, task_id: str) -> bool:
        """
        Record a failed attempt for a task.
        
        Returns True if a struggle signal should be sent.
        """
        self.attempt_counts[task_id] = self.attempt_counts.get(task_id, 0) + 1
        return self.attempt_counts[task_id] >= self.signal_after
    
    def should_signal(self, task_id: str) -> bool:
        """Check if a struggle signal should be sent for a task."""
        return self.attempt_counts.get(task_id, 0) >= self.signal_after
    
    def create_signal(
        self,
        signal_type: StruggleType,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str,
        agent_role: str,
        task_id: Optional[str] = None
    ) -> StruggleSignal:
        """Create a new struggle signal."""
        signal = StruggleSignal(
            signal_type=signal_type,
            what_i_understand=what_i_understand,
            what_i_tried=what_i_tried,
            where_im_stuck=where_im_stuck,
            what_would_help=what_would_help,
            agent_role=agent_role,
            session_id=self.session_id,
            task_id=task_id,
            attempt_count=self.attempt_counts.get(task_id, 0) if task_id else 0
        )
        
        self.signals.append(signal)
        return signal
    
    def format_signal(self, signal: StruggleSignal) -> str:
        """Format a struggle signal for display."""
        tried_list = "\n".join([
            f"- **{t.get('action', 'Action')}**: {t.get('outcome', 'No outcome recorded')}"
            for t in signal.what_i_tried
        ]) if signal.what_i_tried else "- No attempts recorded"
        
        return self.SIGNAL_TEMPLATE.format(
            signal_type=signal.signal_type.value.upper(),
            what_i_understand=signal.what_i_understand,
            tried_list=tried_list,
            where_im_stuck=signal.where_im_stuck,
            what_would_help=signal.what_would_help
        )
    
    def resolve_signal(
        self,
        signal_id: int,
        resolution: str,
        resolved_by: str
    ) -> Optional[StruggleSignal]:
        """Mark a signal as resolved."""
        if signal_id < len(self.signals):
            signal = self.signals[signal_id]
            signal.resolved = True
            signal.resolved_at = datetime.utcnow()
            signal.resolution = resolution
            signal.resolved_by = resolved_by
            
            # Reset attempt count for the task
            if signal.task_id:
                self.attempt_counts[signal.task_id] = 0
            
            return signal
        return None
    
    def get_unresolved_signals(self) -> List[StruggleSignal]:
        """Get all unresolved signals."""
        return [s for s in self.signals if not s.resolved]
    
    def get_signal_patterns(self) -> Dict[str, int]:
        """Analyze patterns in struggle signals."""
        patterns: Dict[str, int] = {}
        for signal in self.signals:
            key = f"{signal.agent_role}:{signal.signal_type.value}"
            patterns[key] = patterns.get(key, 0) + 1
        return patterns
    
    def to_prompt_section(self) -> str:
        """Generate the struggle protocol section for system prompt."""
        return f"""### Struggle Protocol

After {self.signal_after} failed attempts, you MUST signal struggle.
Do NOT fake progress. Do NOT pretend to understand when confused.

Signal format:
🚨 SYNC NEEDED — [signal_type]

What I understand: [specific, not generic]
What I've tried: [list of action → outcome]
Where I'm stuck: [specific point of confusion]
What would help: [specific request]

This is REQUIRED. Signaling struggle is BETTER than faking progress.
The contract protects you: struggle signals are not failures, deception is.
"""
