# =============================================================================
# Circuit Breaker Pattern
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""
Circuit breaker for graceful degradation when multi_agent_service is unavailable.

States:
- CLOSED: Normal operation, requests pass through
- OPEN: Service is unavailable, requests fail fast
- HALF_OPEN: Testing if service has recovered
"""

from datetime import datetime
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class ServiceUnavailable(Exception):
    """Exception raised when service is unavailable."""
    pass


class CircuitBreaker:
    """
    Circuit breaker for multi_agent_service calls.
    
    Implements the circuit breaker pattern to prevent cascading failures
    when the multi_agent_service is unavailable.
    """
    
    def __init__(
        self,
        failure_threshold: int = 3,
        recovery_timeout: int = 60
    ):
        """
        Initialize the circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening circuit
            recovery_timeout: Seconds to wait before testing recovery
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time: Optional[datetime] = None
        self.state = "closed"
    
    @property
    def is_open(self) -> bool:
        """Check if the circuit breaker is open."""
        if self.state == "open":
            if self._recovery_timeout_elapsed():
                self.state = "half_open"
                logger.info("Circuit breaker entering half-open state")
                return False
            return True
        return False
    
    def _recovery_timeout_elapsed(self) -> bool:
        """Check if recovery timeout has elapsed."""
        if self.last_failure_time is None:
            return True
        
        elapsed = (datetime.utcnow() - self.last_failure_time).total_seconds()
        return elapsed >= self.recovery_timeout
    
    def record_failure(self):
        """Record a failure and potentially open the circuit."""
        self.failure_count += 1
        self.last_failure_time = datetime.utcnow()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "open"
            logger.error(
                f"Circuit breaker OPENED after {self.failure_count} failures. "
                f"Will retry after {self.recovery_timeout} seconds."
            )
    
    def record_success(self):
        """Record a success and close the circuit."""
        if self.state == "half_open":
            logger.info("Circuit breaker CLOSED after successful request")
        
        self.failure_count = 0
        self.state = "closed"
        self.last_failure_time = None
    
    def reset(self):
        """Force reset the circuit breaker."""
        self.failure_count = 0
        self.state = "closed"
        self.last_failure_time = None
        logger.info("Circuit breaker manually reset")
    
    def get_status(self) -> dict:
        """Get the current status of the circuit breaker."""
        return {
            "state": self.state,
            "failure_count": self.failure_count,
            "failure_threshold": self.failure_threshold,
            "last_failure_time": self.last_failure_time.isoformat() if self.last_failure_time else None,
            "recovery_timeout": self.recovery_timeout
        }
