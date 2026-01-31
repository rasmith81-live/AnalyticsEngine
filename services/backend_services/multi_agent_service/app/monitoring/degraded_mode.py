# =============================================================================
# Degraded Mode Monitor
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Degraded mode monitoring and tier suspension."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

from ..contracts.tier_rules import RuleTier


class DegradedModeLevel(str, Enum):
    """Degraded mode levels."""
    NORMAL = "normal"
    LIGHT = "light"
    MODERATE = "moderate"
    SEVERE = "severe"
    EMERGENCY = "emergency"


class DegradedModeAnnouncement(BaseModel):
    """Announcement when entering/changing degraded mode."""
    level: DegradedModeLevel
    tiers_enforced: List[int]
    tiers_suspended: List[int]
    cause: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class DegradedModeMonitor:
    """
    Monitor for degraded mode with tier suspension.
    
    From the article:
    "When under pressure, agents (like humans) will drop less critical
    constraints first. The tier system formalizes this—under degraded
    mode, Tier 2-3 can be suspended while Tier 0-1 remain active."
    
    Degradation Levels:
    - NORMAL:    All tiers enforced (0, 1, 2, 3)
    - LIGHT:     Tier 3 suspended (0, 1, 2 enforced)
    - MODERATE:  Tier 2-3 suspended (0, 1 enforced)
    - SEVERE:    Tier 2-3 suspended, warnings on Tier 1
    - EMERGENCY: Only Tier 0 enforced
    
    The key: Trade-offs are VISIBLE, not silent.
    """
    
    # Which tiers are enforced at each level
    ENFORCED_TIERS: Dict[DegradedModeLevel, List[int]] = {
        DegradedModeLevel.NORMAL: [0, 1, 2, 3],
        DegradedModeLevel.LIGHT: [0, 1, 2],
        DegradedModeLevel.MODERATE: [0, 1],
        DegradedModeLevel.SEVERE: [0, 1],
        DegradedModeLevel.EMERGENCY: [0],
    }
    
    # Thresholds for entering each level
    THRESHOLDS = {
        DegradedModeLevel.LIGHT: {
            "drift_score": 0.4,
            "error_rate": 0.15,
            "token_usage": 0.70,
        },
        DegradedModeLevel.MODERATE: {
            "drift_score": 0.6,
            "error_rate": 0.25,
            "token_usage": 0.85,
        },
        DegradedModeLevel.SEVERE: {
            "drift_score": 0.8,
            "error_rate": 0.35,
            "token_usage": 0.90,
        },
        DegradedModeLevel.EMERGENCY: {
            "drift_score": 0.9,
            "error_rate": 0.50,
            "token_usage": 0.95,
        },
    }
    
    def __init__(self, agent_role: str, session_id: str):
        self.agent_role = agent_role
        self.session_id = session_id
        self.current_level = DegradedModeLevel.NORMAL
        self.history: List[DegradedModeAnnouncement] = []
        
        # Tracking factors
        self.drift_score = 0.0
        self.error_rate = 0.0
        self.token_usage = 0.0
        self.violation_count = 0
    
    def update_factors(
        self,
        drift_score: Optional[float] = None,
        error_rate: Optional[float] = None,
        token_usage: Optional[float] = None,
        violation_count: Optional[int] = None
    ) -> DegradedModeLevel:
        """Update degradation factors and recalculate level."""
        if drift_score is not None:
            self.drift_score = drift_score
        if error_rate is not None:
            self.error_rate = error_rate
        if token_usage is not None:
            self.token_usage = token_usage
        if violation_count is not None:
            self.violation_count = violation_count
        
        new_level = self._calculate_level()
        
        if new_level != self.current_level:
            self._record_transition(new_level)
            self.current_level = new_level
        
        return self.current_level
    
    def _calculate_level(self) -> DegradedModeLevel:
        """Calculate degradation level from current factors."""
        # Check from most severe to least severe
        for level in [
            DegradedModeLevel.EMERGENCY,
            DegradedModeLevel.SEVERE,
            DegradedModeLevel.MODERATE,
            DegradedModeLevel.LIGHT,
        ]:
            thresholds = self.THRESHOLDS[level]
            if (
                self.drift_score >= thresholds["drift_score"] or
                self.error_rate >= thresholds["error_rate"] or
                self.token_usage >= thresholds["token_usage"]
            ):
                return level
        
        return DegradedModeLevel.NORMAL
    
    def _record_transition(self, new_level: DegradedModeLevel) -> None:
        """Record a transition to a new degradation level."""
        cause_parts = []
        if self.drift_score >= 0.4:
            cause_parts.append(f"drift={self.drift_score:.2f}")
        if self.error_rate >= 0.15:
            cause_parts.append(f"errors={self.error_rate:.0%}")
        if self.token_usage >= 0.70:
            cause_parts.append(f"tokens={self.token_usage:.0%}")
        
        announcement = DegradedModeAnnouncement(
            level=new_level,
            tiers_enforced=self.ENFORCED_TIERS[new_level],
            tiers_suspended=self._get_suspended_tiers(new_level),
            cause=" | ".join(cause_parts) if cause_parts else "unknown"
        )
        
        self.history.append(announcement)
    
    def _get_suspended_tiers(self, level: DegradedModeLevel) -> List[int]:
        """Get which tiers are suspended at a given level."""
        enforced = set(self.ENFORCED_TIERS[level])
        all_tiers = {0, 1, 2, 3}
        return sorted(all_tiers - enforced)
    
    def get_enforced_tiers(self) -> List[int]:
        """Get currently enforced tiers."""
        return self.ENFORCED_TIERS[self.current_level]
    
    def get_suspended_tiers(self) -> List[int]:
        """Get currently suspended tiers."""
        return self._get_suspended_tiers(self.current_level)
    
    def is_tier_enforced(self, tier: int) -> bool:
        """Check if a specific tier is currently enforced."""
        return tier in self.get_enforced_tiers()
    
    def get_announcement(self) -> Optional[str]:
        """Get announcement string if in degraded mode."""
        if self.current_level == DegradedModeLevel.NORMAL:
            return None
        
        enforced = self.get_enforced_tiers()
        suspended = self.get_suspended_tiers()
        
        return f"""⚠️ DEGRADED MODE — Level: {self.current_level.value.upper()}
Enforcing: Tier {', '.join(map(str, enforced))}
Suspended: Tier {', '.join(map(str, suspended))}

Cause: drift={self.drift_score:.2f} | errors={self.error_rate:.0%} | tokens={self.token_usage:.0%}

This trade-off is now VISIBLE. You know what's being sacrificed.
"""
    
    def to_prompt_section(self) -> str:
        """Generate degraded mode section for system prompt."""
        if self.current_level == DegradedModeLevel.NORMAL:
            return """### Degraded Mode Status
Status: NORMAL — All tiers enforced
"""
        
        enforced = self.get_enforced_tiers()
        suspended = self.get_suspended_tiers()
        
        tier_status = []
        for tier in range(4):
            if tier in enforced:
                tier_status.append(f"Tier {tier}: ✓ ENFORCED")
            else:
                tier_status.append(f"Tier {tier}: ⏸ SUSPENDED")
        
        return f"""### Degraded Mode Status
Level: {self.current_level.value.upper()}
{chr(10).join(tier_status)}

⚠️ Some rules are suspended due to system pressure.
Focus on Tier 0-1 rules. Tier 2-3 can be deferred.
"""
    
    def to_dashboard_data(self) -> Dict[str, Any]:
        """Get data for dashboard display."""
        return {
            "level": self.current_level.value,
            "tiers_enforced": self.get_enforced_tiers(),
            "tiers_suspended": self.get_suspended_tiers(),
            "factors": {
                "drift_score": self.drift_score,
                "error_rate": self.error_rate,
                "token_usage": self.token_usage,
                "violation_count": self.violation_count
            },
            "transition_count": len(self.history)
        }
