# =============================================================================
# Token Budget Monitor
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Token budget monitoring to prevent context collapse."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class TokenBudgetStatus(str, Enum):
    """Token budget status levels."""
    HEALTHY = "healthy"       # < 50% usage
    CAUTION = "caution"       # 50-70% usage
    WARNING = "warning"       # 70-85% usage
    CRITICAL = "critical"     # 85-95% usage
    COLLAPSE_IMMINENT = "collapse_imminent"  # > 95% usage


class TokenBudgetRecommendation(BaseModel):
    """Recommendation based on token budget status."""
    status: TokenBudgetStatus
    action: str
    priority: int  # 1 = highest


# Recommendations by status level
RECOMMENDATIONS: Dict[TokenBudgetStatus, TokenBudgetRecommendation] = {
    TokenBudgetStatus.HEALTHY: TokenBudgetRecommendation(
        status=TokenBudgetStatus.HEALTHY,
        action="Continue normal operation",
        priority=5
    ),
    TokenBudgetStatus.CAUTION: TokenBudgetRecommendation(
        status=TokenBudgetStatus.CAUTION,
        action="Begin prioritizing essential context. Consider summarizing verbose sections.",
        priority=4
    ),
    TokenBudgetStatus.WARNING: TokenBudgetRecommendation(
        status=TokenBudgetStatus.WARNING,
        action="Compress context aggressively. Focus on current task only. Defer non-essential work.",
        priority=3
    ),
    TokenBudgetStatus.CRITICAL: TokenBudgetRecommendation(
        status=TokenBudgetStatus.CRITICAL,
        action="Emergency context compression. Complete current task and hand off. Prepare for degraded mode.",
        priority=2
    ),
    TokenBudgetStatus.COLLAPSE_IMMINENT: TokenBudgetRecommendation(
        status=TokenBudgetStatus.COLLAPSE_IMMINENT,
        action="STOP. Save state immediately. Signal for session handoff. Context collapse imminent.",
        priority=1
    ),
}


class TokenUsageSnapshot(BaseModel):
    """Snapshot of token usage at a point in time."""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tokens_used: int
    max_tokens: int
    usage_percent: float
    status: TokenBudgetStatus
    agent_role: str
    session_id: str


class TokenBudgetMonitor:
    """
    Monitor token budget and alert before context collapse.
    
    From the article:
    "Token budget warnings allow agents to notice their own degradation
    and announce it visibly rather than silently failing."
    
    Thresholds:
    - HEALTHY:    < 50%  - Normal operation
    - CAUTION:    50-70% - Start compressing
    - WARNING:    70-85% - Prepare for degradation
    - CRITICAL:   85-95% - Imminent collapse
    - COLLAPSE:   > 95%  - Save state immediately
    """
    
    # Threshold percentages
    THRESHOLDS = {
        TokenBudgetStatus.HEALTHY: 0.0,
        TokenBudgetStatus.CAUTION: 0.50,
        TokenBudgetStatus.WARNING: 0.70,
        TokenBudgetStatus.CRITICAL: 0.85,
        TokenBudgetStatus.COLLAPSE_IMMINENT: 0.95,
    }
    
    def __init__(
        self,
        max_tokens: int = 200000,
        agent_role: str = "unknown",
        session_id: str = "unknown"
    ):
        self.max_tokens = max_tokens
        self.agent_role = agent_role
        self.session_id = session_id
        self.current_usage = 0
        self.history: List[TokenUsageSnapshot] = []
        self._last_status = TokenBudgetStatus.HEALTHY
    
    def update_usage(self, tokens_used: int) -> TokenBudgetStatus:
        """Update token usage and return current status."""
        self.current_usage = tokens_used
        status = self.get_status()
        
        # Record snapshot
        snapshot = TokenUsageSnapshot(
            tokens_used=tokens_used,
            max_tokens=self.max_tokens,
            usage_percent=self.get_usage_percent(),
            status=status,
            agent_role=self.agent_role,
            session_id=self.session_id
        )
        self.history.append(snapshot)
        
        # Track status changes
        if status != self._last_status:
            self._last_status = status
        
        return status
    
    def get_usage_percent(self) -> float:
        """Get current usage as a percentage."""
        if self.max_tokens == 0:
            return 0.0
        return self.current_usage / self.max_tokens
    
    def get_status(self) -> TokenBudgetStatus:
        """Get current status based on usage."""
        usage = self.get_usage_percent()
        
        if usage >= self.THRESHOLDS[TokenBudgetStatus.COLLAPSE_IMMINENT]:
            return TokenBudgetStatus.COLLAPSE_IMMINENT
        elif usage >= self.THRESHOLDS[TokenBudgetStatus.CRITICAL]:
            return TokenBudgetStatus.CRITICAL
        elif usage >= self.THRESHOLDS[TokenBudgetStatus.WARNING]:
            return TokenBudgetStatus.WARNING
        elif usage >= self.THRESHOLDS[TokenBudgetStatus.CAUTION]:
            return TokenBudgetStatus.CAUTION
        else:
            return TokenBudgetStatus.HEALTHY
    
    def get_recommendation(self) -> TokenBudgetRecommendation:
        """Get recommendation for current status."""
        return RECOMMENDATIONS[self.get_status()]
    
    def get_remaining_tokens(self) -> int:
        """Get remaining tokens before max."""
        return max(0, self.max_tokens - self.current_usage)
    
    def should_compress(self) -> bool:
        """Check if context compression is recommended."""
        return self.get_status() in [
            TokenBudgetStatus.CAUTION,
            TokenBudgetStatus.WARNING,
            TokenBudgetStatus.CRITICAL,
            TokenBudgetStatus.COLLAPSE_IMMINENT
        ]
    
    def should_halt(self) -> bool:
        """Check if operations should halt."""
        return self.get_status() == TokenBudgetStatus.COLLAPSE_IMMINENT
    
    def get_announcement(self) -> Optional[str]:
        """Get an announcement string if status warrants it."""
        status = self.get_status()
        usage = self.get_usage_percent()
        
        if status == TokenBudgetStatus.HEALTHY:
            return None
        
        recommendation = self.get_recommendation()
        
        return f"""⚠️ TOKEN BUDGET — {status.value.upper()}
Usage: {self.current_usage:,} / {self.max_tokens:,} ({usage:.1%})
Action: {recommendation.action}
"""
    
    def to_prompt_section(self) -> str:
        """Generate token budget section for system prompt."""
        status = self.get_status()
        usage = self.get_usage_percent()
        remaining = self.get_remaining_tokens()
        recommendation = self.get_recommendation()
        
        status_icon = {
            TokenBudgetStatus.HEALTHY: "✓",
            TokenBudgetStatus.CAUTION: "⚡",
            TokenBudgetStatus.WARNING: "⚠️",
            TokenBudgetStatus.CRITICAL: "🔴",
            TokenBudgetStatus.COLLAPSE_IMMINENT: "💀"
        }
        
        return f"""### Token Budget
Status: {status_icon.get(status, '?')} {status.value.upper()}
Usage: {self.current_usage:,} / {self.max_tokens:,} ({usage:.1%})
Remaining: {remaining:,}
Recommendation: {recommendation.action}
"""
    
    def to_dashboard_data(self) -> Dict[str, Any]:
        """Get data for dashboard display."""
        status = self.get_status()
        return {
            "current_usage": self.current_usage,
            "max_tokens": self.max_tokens,
            "usage_percent": self.get_usage_percent() * 100,
            "status": status.value,
            "remaining": self.get_remaining_tokens(),
            "recommendation": self.get_recommendation().action,
            "should_compress": self.should_compress(),
            "should_halt": self.should_halt()
        }
