# =============================================================================
# Magic Phrases
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Magic phrases for steering agent behavior without breaking flow."""

from typing import Dict, Optional, Callable, Any
from enum import Enum
from pydantic import BaseModel


class MagicPhraseAction(str, Enum):
    """Actions triggered by magic phrases."""
    PROCEED = "proceed"
    SWITCH_MODE = "switch_mode"
    EXPLAIN = "explain"
    STOP = "stop"
    RESET = "reset"
    FAST_FORWARD = "fast_forward"
    ADJUST_DETAIL = "adjust_detail"


class MagicPhrase(BaseModel):
    """Definition of a magic phrase."""
    phrase: str
    aliases: list[str]
    action: MagicPhraseAction
    description: str
    parameters: Dict[str, Any] = {}


# The magic phrases from the contract
MAGIC_PHRASES: list[MagicPhrase] = [
    MagicPhrase(
        phrase="P",
        aliases=["Proceed", "proceed", "p", "go", "Go"],
        action=MagicPhraseAction.PROCEED,
        description="Approve and execute the pending action"
    ),
    MagicPhrase(
        phrase="Let's pair",
        aliases=["pair", "pairing", "pair mode"],
        action=MagicPhraseAction.SWITCH_MODE,
        description="Switch to Pairing collaboration mode",
        parameters={"mode": "pairing"}
    ),
    MagicPhrase(
        phrase="Let me be your UserDuck",
        aliases=["userduck", "user duck", "be my duck"],
        action=MagicPhraseAction.SWITCH_MODE,
        description="Switch to UserDuck mode (agent thinks aloud)",
        parameters={"mode": "user_duck"}
    ),
    MagicPhrase(
        phrase="Walk me through",
        aliases=["explain", "step by step", "step-by-step"],
        action=MagicPhraseAction.EXPLAIN,
        description="Explain step-by-step"
    ),
    MagicPhrase(
        phrase="Stop",
        aliases=["halt", "STOP", "stop now"],
        action=MagicPhraseAction.STOP,
        description="Halt current action immediately"
    ),
    MagicPhrase(
        phrase="Reset",
        aliases=["RESET", "start over", "clear"],
        action=MagicPhraseAction.RESET,
        description="Trigger RESET semantics"
    ),
    MagicPhrase(
        phrase="Fast forward",
        aliases=["skip", "skip to results", "ff"],
        action=MagicPhraseAction.FAST_FORWARD,
        description="Skip to results"
    ),
    MagicPhrase(
        phrase="More detail",
        aliases=["elaborate", "expand", "more"],
        action=MagicPhraseAction.ADJUST_DETAIL,
        description="Increase explanation depth",
        parameters={"direction": "increase"}
    ),
    MagicPhrase(
        phrase="Less detail",
        aliases=["brief", "shorter", "less", "summarize"],
        action=MagicPhraseAction.ADJUST_DETAIL,
        description="Decrease explanation depth",
        parameters={"direction": "decrease"}
    ),
]


class MagicPhraseHandler:
    """
    Handler for detecting and processing magic phrases.
    
    From the article:
    "Magic phrases are short commands for steering without breaking flow.
    They reduce friction in the human-agent pairing experience."
    """
    
    def __init__(self):
        self.phrases = MAGIC_PHRASES
        self._build_lookup()
    
    def _build_lookup(self) -> None:
        """Build lookup table for quick phrase detection."""
        self._lookup: Dict[str, MagicPhrase] = {}
        for phrase in self.phrases:
            self._lookup[phrase.phrase.lower()] = phrase
            for alias in phrase.aliases:
                self._lookup[alias.lower()] = phrase
    
    def detect(self, message: str) -> Optional[MagicPhrase]:
        """
        Detect if a message contains a magic phrase.
        
        Returns the MagicPhrase if found, None otherwise.
        """
        message_lower = message.strip().lower()
        
        # Check for exact match first
        if message_lower in self._lookup:
            return self._lookup[message_lower]
        
        # Check if message starts with a magic phrase
        for key, phrase in self._lookup.items():
            if message_lower.startswith(key):
                return phrase
        
        return None
    
    def handle(
        self,
        message: str,
        mode_manager: Any = None,
        contract: Any = None
    ) -> Optional[Dict[str, Any]]:
        """
        Handle a magic phrase if present.
        
        Returns a dict describing the action taken, or None if no phrase detected.
        """
        phrase = self.detect(message)
        if not phrase:
            return None
        
        result = {
            "phrase": phrase.phrase,
            "action": phrase.action.value,
            "description": phrase.description
        }
        
        if phrase.action == MagicPhraseAction.PROCEED:
            # Approve pending action
            result["effect"] = "Approved pending action"
            
        elif phrase.action == MagicPhraseAction.SWITCH_MODE:
            if mode_manager:
                mode = phrase.parameters.get("mode", "autonomous")
                # mode_manager.switch_mode(mode)
                result["effect"] = f"Switched to {mode} mode"
            
        elif phrase.action == MagicPhraseAction.STOP:
            result["effect"] = "Halted current action"
            
        elif phrase.action == MagicPhraseAction.RESET:
            if contract:
                # contract.force_reset()
                result["effect"] = "Triggered RESET semantics"
            
        elif phrase.action == MagicPhraseAction.FAST_FORWARD:
            result["effect"] = "Skipping to results"
            
        elif phrase.action == MagicPhraseAction.ADJUST_DETAIL:
            direction = phrase.parameters.get("direction", "increase")
            result["effect"] = f"Adjusted detail level: {direction}"
            
        elif phrase.action == MagicPhraseAction.EXPLAIN:
            result["effect"] = "Will explain step-by-step"
        
        return result
    
    def get_phrases_prompt(self) -> str:
        """Generate the magic phrases section for system prompt."""
        lines = ["### Magic Phrases", ""]
        lines.append("The user may use these shortcuts to steer without breaking flow:")
        lines.append("")
        
        for phrase in self.phrases:
            aliases = ", ".join([f'"{a}"' for a in phrase.aliases[:2]])
            lines.append(f"- **\"{phrase.phrase}\"** ({aliases}): {phrase.description}")
        
        return "\n".join(lines)
