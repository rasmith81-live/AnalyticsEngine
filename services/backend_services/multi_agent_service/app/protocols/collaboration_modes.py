# =============================================================================
# Collaboration Modes
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Collaboration modes for human-agent interaction."""

from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime


class CollaborationMode(str, Enum):
    """
    The four collaboration modes from the contract.
    
    - AUTONOMOUS: Agent works independently with normal gates
    - USER_DUCK: Agent thinks aloud, human redirects when off track
    - AGENT_DUCK: Human explains, agent asks clarifying questions
    - PAIRING: Rapid back-and-forth, neither drives exclusively
    """
    AUTONOMOUS = "autonomous"
    USER_DUCK = "user_duck"
    AGENT_DUCK = "agent_duck"
    PAIRING = "pairing"


class CollaborationModeConfig(BaseModel):
    """Configuration for each collaboration mode."""
    mode: CollaborationMode
    description: str
    approval_required: bool
    verbosity: str  # "low", "medium", "high"
    initiative: str  # "agent", "human", "balanced"


# Mode configurations
MODE_CONFIGS: Dict[CollaborationMode, CollaborationModeConfig] = {
    CollaborationMode.AUTONOMOUS: CollaborationModeConfig(
        mode=CollaborationMode.AUTONOMOUS,
        description="Agent works independently, human approves at gates",
        approval_required=True,
        verbosity="low",
        initiative="agent"
    ),
    CollaborationMode.USER_DUCK: CollaborationModeConfig(
        mode=CollaborationMode.USER_DUCK,
        description="Agent thinks aloud, human redirects when off track",
        approval_required=False,
        verbosity="high",
        initiative="agent"
    ),
    CollaborationMode.AGENT_DUCK: CollaborationModeConfig(
        mode=CollaborationMode.AGENT_DUCK,
        description="Human explains, agent asks clarifying questions",
        approval_required=False,
        verbosity="medium",
        initiative="human"
    ),
    CollaborationMode.PAIRING: CollaborationModeConfig(
        mode=CollaborationMode.PAIRING,
        description="Rapid back-and-forth, exploratory",
        approval_required=False,
        verbosity="medium",
        initiative="balanced"
    ),
}


class ModeTransition(BaseModel):
    """Record of a mode transition."""
    from_mode: CollaborationMode
    to_mode: CollaborationMode
    triggered_by: str  # "magic_phrase", "explicit", "automatic"
    timestamp: datetime


class CollaborationModeManager:
    """
    Manages collaboration mode for a session.
    
    Default is AUTONOMOUS but all modes are gated—
    you can't enter a mode without meeting its prerequisites.
    """
    
    def __init__(self, initial_mode: CollaborationMode = CollaborationMode.AUTONOMOUS):
        self.current_mode = initial_mode
        self.transition_history: list[ModeTransition] = []
    
    def get_current_mode(self) -> CollaborationMode:
        """Get the current collaboration mode."""
        return self.current_mode
    
    def get_mode_config(self) -> CollaborationModeConfig:
        """Get the configuration for the current mode."""
        return MODE_CONFIGS[self.current_mode]
    
    def switch_mode(
        self,
        new_mode: CollaborationMode,
        triggered_by: str = "explicit"
    ) -> ModeTransition:
        """
        Switch to a new collaboration mode.
        
        Returns the transition record.
        """
        transition = ModeTransition(
            from_mode=self.current_mode,
            to_mode=new_mode,
            triggered_by=triggered_by,
            timestamp=datetime.utcnow()
        )
        
        self.transition_history.append(transition)
        self.current_mode = new_mode
        
        return transition
    
    def should_request_approval(self) -> bool:
        """Check if approval is required in current mode."""
        return MODE_CONFIGS[self.current_mode].approval_required
    
    def get_verbosity(self) -> str:
        """Get the verbosity level for current mode."""
        return MODE_CONFIGS[self.current_mode].verbosity
    
    def get_initiative(self) -> str:
        """Get who has initiative in current mode."""
        return MODE_CONFIGS[self.current_mode].initiative
    
    def to_prompt_section(self) -> str:
        """Generate the collaboration mode section for system prompt."""
        config = self.get_mode_config()
        return f"""### Collaboration Mode
Current Mode: {self.current_mode.value.upper()}
Description: {config.description}
Verbosity: {config.verbosity}
Initiative: {config.initiative}
Approval Required: {"Yes" if config.approval_required else "No"}
"""
