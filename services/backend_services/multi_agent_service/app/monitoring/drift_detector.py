# =============================================================================
# Drift Detector
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Behavioral drift detection at state transitions."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class DriftIndicator(str, Enum):
    """Indicators of behavioral drift."""
    RESPONSE_TIME_ANOMALY = "response_time_anomaly"
    CONFIDENCE_WITHOUT_EVIDENCE = "confidence_without_evidence"
    AVOIDANCE_OF_SPECIFICS = "avoidance_of_specifics"
    REPETITION_OF_PATTERNS = "repetition_of_patterns"
    SCOPE_NARROWING = "scope_narrowing"
    OPTIMISM_BIAS = "optimism_bias"
    STRUGGLE_AVOIDANCE = "struggle_avoidance"
    GATE_RUSHING = "gate_rushing"


class DriftCheckResult(BaseModel):
    """Result of a drift check."""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    transition_from: str
    transition_to: str
    indicators_found: List[DriftIndicator] = Field(default_factory=list)
    drift_score: float = 0.0  # 0.0 = no drift, 1.0 = severe drift
    details: Dict[str, Any] = Field(default_factory=dict)
    agent_role: str
    session_id: str


class DriftDetector:
    """
    Detect behavioral drift at state transitions.
    
    From the article:
    "Drift detection notices when agent behavior starts to degrade—
    subtle signs like overconfidence, avoidance of specifics, or
    rushing through gates."
    
    The 8 drift indicators:
    1. Response time anomaly - Too fast or too slow
    2. Confidence without evidence - Claims without backing
    3. Avoidance of specifics - Vague when should be specific
    4. Repetition of patterns - Same phrases/approaches repeated
    5. Scope narrowing - Quietly reducing scope
    6. Optimism bias - Everything is "almost done"
    7. Struggle avoidance - Not signaling when stuck
    8. Gate rushing - Trying to skip approval steps
    """
    
    # Thresholds for detection
    THRESHOLDS = {
        DriftIndicator.RESPONSE_TIME_ANOMALY: {
            "min_ms": 100,      # Too fast = suspicious
            "max_ms": 60000,    # Too slow = struggling
        },
        DriftIndicator.CONFIDENCE_WITHOUT_EVIDENCE: {
            "confidence_phrases": [
                "definitely", "certainly", "obviously", "clearly",
                "without doubt", "absolutely", "of course"
            ],
            "evidence_phrases": [
                "because", "based on", "according to", "the code shows",
                "the test shows", "I verified", "I checked"
            ]
        },
        DriftIndicator.AVOIDANCE_OF_SPECIFICS: {
            "vague_phrases": [
                "generally", "typically", "usually", "often",
                "might", "could", "possibly", "potentially"
            ]
        },
        DriftIndicator.OPTIMISM_BIAS: {
            "optimism_phrases": [
                "almost done", "just needs", "nearly complete",
                "minor fix", "should be quick", "easy fix"
            ]
        }
    }
    
    # Drift score weights per indicator
    WEIGHTS = {
        DriftIndicator.RESPONSE_TIME_ANOMALY: 0.1,
        DriftIndicator.CONFIDENCE_WITHOUT_EVIDENCE: 0.2,
        DriftIndicator.AVOIDANCE_OF_SPECIFICS: 0.15,
        DriftIndicator.REPETITION_OF_PATTERNS: 0.1,
        DriftIndicator.SCOPE_NARROWING: 0.15,
        DriftIndicator.OPTIMISM_BIAS: 0.1,
        DriftIndicator.STRUGGLE_AVOIDANCE: 0.1,
        DriftIndicator.GATE_RUSHING: 0.1,
    }
    
    # Decay rate for drift score
    DECAY_RATE = 0.1
    
    def __init__(self, agent_role: str, session_id: str):
        self.agent_role = agent_role
        self.session_id = session_id
        self.current_drift_score = 0.0
        self.check_history: List[DriftCheckResult] = []
        self.response_history: List[str] = []
    
    def check_at_transition(
        self,
        from_state: str,
        to_state: str,
        response: str,
        response_time_ms: int
    ) -> DriftCheckResult:
        """
        Check for drift at a state transition.
        
        This is called every time an agent transitions states.
        """
        indicators_found = []
        details = {}
        
        # Check response time
        if self._check_response_time(response_time_ms):
            indicators_found.append(DriftIndicator.RESPONSE_TIME_ANOMALY)
            details["response_time_ms"] = response_time_ms
        
        # Check confidence without evidence
        if self._check_confidence_without_evidence(response):
            indicators_found.append(DriftIndicator.CONFIDENCE_WITHOUT_EVIDENCE)
        
        # Check avoidance of specifics
        if self._check_avoidance_of_specifics(response):
            indicators_found.append(DriftIndicator.AVOIDANCE_OF_SPECIFICS)
        
        # Check repetition of patterns
        if self._check_repetition(response):
            indicators_found.append(DriftIndicator.REPETITION_OF_PATTERNS)
        
        # Check optimism bias
        if self._check_optimism_bias(response):
            indicators_found.append(DriftIndicator.OPTIMISM_BIAS)
        
        # Check gate rushing (skipping states)
        if self._check_gate_rushing(from_state, to_state):
            indicators_found.append(DriftIndicator.GATE_RUSHING)
        
        # Calculate drift score
        drift_score = self._calculate_drift_score(indicators_found)
        
        # Update running score with decay
        self.current_drift_score = (
            self.current_drift_score * (1 - self.DECAY_RATE) +
            drift_score * self.DECAY_RATE * 10  # Weight new findings
        )
        self.current_drift_score = min(1.0, self.current_drift_score)
        
        # Store response for pattern detection
        self.response_history.append(response)
        if len(self.response_history) > 10:
            self.response_history.pop(0)
        
        result = DriftCheckResult(
            transition_from=from_state,
            transition_to=to_state,
            indicators_found=indicators_found,
            drift_score=self.current_drift_score,
            details=details,
            agent_role=self.agent_role,
            session_id=self.session_id
        )
        
        self.check_history.append(result)
        return result
    
    def _check_response_time(self, response_time_ms: int) -> bool:
        """Check for response time anomaly."""
        thresholds = self.THRESHOLDS[DriftIndicator.RESPONSE_TIME_ANOMALY]
        return response_time_ms < thresholds["min_ms"] or response_time_ms > thresholds["max_ms"]
    
    def _check_confidence_without_evidence(self, response: str) -> bool:
        """Check for confidence claims without evidence."""
        thresholds = self.THRESHOLDS[DriftIndicator.CONFIDENCE_WITHOUT_EVIDENCE]
        response_lower = response.lower()
        
        confidence_count = sum(
            1 for phrase in thresholds["confidence_phrases"]
            if phrase in response_lower
        )
        evidence_count = sum(
            1 for phrase in thresholds["evidence_phrases"]
            if phrase in response_lower
        )
        
        # Confidence without corresponding evidence
        return confidence_count > evidence_count + 1
    
    def _check_avoidance_of_specifics(self, response: str) -> bool:
        """Check for avoidance of specific details."""
        thresholds = self.THRESHOLDS[DriftIndicator.AVOIDANCE_OF_SPECIFICS]
        response_lower = response.lower()
        
        vague_count = sum(
            1 for phrase in thresholds["vague_phrases"]
            if phrase in response_lower
        )
        
        # Too many vague phrases relative to response length
        words = len(response.split())
        threshold_ratio = vague_count / max(words, 1)
        return threshold_ratio > 0.02  # More than 2% vague words
    
    def _check_repetition(self, response: str) -> bool:
        """Check for repetition of patterns."""
        if len(self.response_history) < 3:
            return False
        
        # Check for similar phrases across responses
        response_words = set(response.lower().split())
        overlap_count = 0
        
        for prev_response in self.response_history[-3:]:
            prev_words = set(prev_response.lower().split())
            overlap = len(response_words.intersection(prev_words))
            if overlap > len(response_words) * 0.7:  # 70% overlap
                overlap_count += 1
        
        return overlap_count >= 2
    
    def _check_optimism_bias(self, response: str) -> bool:
        """Check for optimism bias."""
        thresholds = self.THRESHOLDS[DriftIndicator.OPTIMISM_BIAS]
        response_lower = response.lower()
        
        optimism_count = sum(
            1 for phrase in thresholds["optimism_phrases"]
            if phrase in response_lower
        )
        
        return optimism_count >= 2
    
    def _check_gate_rushing(self, from_state: str, to_state: str) -> bool:
        """Check for attempts to rush through gates."""
        # These transitions indicate rushing
        rushing_patterns = [
            ("analysis", "done"),
            ("analysis", "execution"),
            ("execution", "done"),
        ]
        return (from_state, to_state) in rushing_patterns
    
    def _calculate_drift_score(self, indicators: List[DriftIndicator]) -> float:
        """Calculate drift score from indicators found."""
        if not indicators:
            return 0.0
        
        score = sum(self.WEIGHTS.get(ind, 0.1) for ind in indicators)
        return min(1.0, score)
    
    def get_drift_status(self) -> str:
        """Get human-readable drift status."""
        if self.current_drift_score < 0.2:
            return "healthy"
        elif self.current_drift_score < 0.4:
            return "minor"
        elif self.current_drift_score < 0.6:
            return "moderate"
        elif self.current_drift_score < 0.8:
            return "significant"
        else:
            return "severe"
    
    def get_announcement(self) -> Optional[str]:
        """Get announcement if drift is concerning."""
        if self.current_drift_score < 0.3:
            return None
        
        return f"""⚠️ BEHAVIORAL DRIFT DETECTED
Drift Score: {self.current_drift_score:.2f}
Status: {self.get_drift_status()}
Recent Indicators: {[i.value for i in self.check_history[-1].indicators_found] if self.check_history else []}
"""
    
    def to_dashboard_data(self) -> Dict[str, Any]:
        """Get data for dashboard display."""
        return {
            "drift_score": self.current_drift_score,
            "status": self.get_drift_status(),
            "recent_indicators": (
                [i.value for i in self.check_history[-1].indicators_found]
                if self.check_history else []
            ),
            "check_count": len(self.check_history)
        }
