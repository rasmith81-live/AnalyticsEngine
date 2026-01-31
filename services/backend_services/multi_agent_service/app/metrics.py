# =============================================================================
# Prometheus Metrics
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Prometheus metrics for multi_agent_service."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# Check if prometheus_client is available
try:
    from prometheus_client import Counter, Histogram, Gauge, Info, generate_latest, CONTENT_TYPE_LATEST
    PROMETHEUS_AVAILABLE = True
except ImportError:
    PROMETHEUS_AVAILABLE = False
    logger.warning("prometheus_client not available - metrics disabled")


# Contract metrics
if PROMETHEUS_AVAILABLE:
    contract_violations = Counter(
        'multi_agent_contract_violations_total',
        'Total contract violations',
        ['agent_role', 'tier', 'rule_id']
    )
    
    state_transitions = Counter(
        'multi_agent_state_transitions_total',
        'Total state transitions',
        ['agent_role', 'from_state', 'to_state', 'allowed']
    )
    
    forbidden_transitions_blocked = Counter(
        'multi_agent_forbidden_transitions_blocked_total',
        'Total forbidden transitions that were blocked',
        ['agent_role', 'from_state', 'to_state']
    )
    
    # Blackboard metrics
    blackboard_tasks = Gauge(
        'multi_agent_blackboard_tasks',
        'Current blackboard tasks by status',
        ['session_id', 'status']
    )
    
    blackboard_artifacts = Counter(
        'multi_agent_blackboard_artifacts_total',
        'Total artifacts submitted',
        ['artifact_type', 'review_status']
    )
    
    blackboard_operations = Counter(
        'multi_agent_blackboard_operations_total',
        'Total blackboard operations',
        ['operation']
    )
    
    # Peer review metrics
    peer_reviews = Counter(
        'multi_agent_peer_reviews_total',
        'Total peer reviews',
        ['creator_role', 'reviewer_role', 'verdict']
    )
    
    self_review_blocked = Counter(
        'multi_agent_self_review_blocked_total',
        'Total self-review attempts blocked',
        ['agent_role']
    )
    
    escalations = Counter(
        'multi_agent_escalations_total',
        'Total escalations (two-failures rule)',
        ['reason']
    )
    
    # Hard stop metrics
    hard_stops = Counter(
        'multi_agent_hard_stops_total',
        'Total hard stop triggers',
        ['agent_role', 'trigger_type']
    )
    
    # Struggle protocol metrics
    struggle_signals = Counter(
        'multi_agent_struggle_signals_total',
        'Total struggle signals',
        ['agent_role', 'signal_type']
    )
    
    # Performance metrics
    agent_processing_time = Histogram(
        'multi_agent_processing_seconds',
        'Agent processing time',
        ['agent_role', 'operation'],
        buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0, 120.0]
    )
    
    blackboard_latency = Histogram(
        'multi_agent_blackboard_latency_seconds',
        'Blackboard operation latency',
        ['operation'],
        buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
    )
    
    # Session metrics
    active_sessions = Gauge(
        'multi_agent_active_sessions',
        'Number of active sessions'
    )
    
    # Service info
    service_info = Info(
        'multi_agent_service',
        'Multi-agent service information'
    )
    
    # Phase 18: Token consumption metrics (Microsoft Best Practices)
    token_consumption_total = Counter(
        'multi_agent_token_consumption_total',
        'Total tokens consumed by agents',
        ['agent_role', 'model', 'token_type']  # token_type: input, output
    )
    
    token_consumption_per_session = Counter(
        'multi_agent_session_token_consumption_total',
        'Tokens consumed per session',
        ['session_id', 'agent_role']
    )
    
    token_cost_estimate = Counter(
        'multi_agent_token_cost_estimate_usd',
        'Estimated cost in USD (multiplied by 1000000 for precision)',
        ['agent_role', 'model']
    )
    
    # Agent versioning metrics
    agent_version_state = Gauge(
        'multi_agent_version_state',
        'Current version state of agents (1=active)',
        ['agent_role', 'version', 'state']
    )
    
    # Dependency tracking metrics
    dependency_changes_detected = Counter(
        'multi_agent_dependency_changes_total',
        'Total dependency changes detected',
        ['agent_role', 'dependency_type']
    )
    
    # Registry metrics
    agent_registrations = Counter(
        'multi_agent_registrations_total',
        'Total agent registrations',
        ['registration_type', 'status']  # type: self, registry-initiated
    )
else:
    contract_violations = None
    state_transitions = None
    forbidden_transitions_blocked = None
    blackboard_tasks = None
    blackboard_artifacts = None
    blackboard_operations = None
    peer_reviews = None
    self_review_blocked = None
    escalations = None
    # Phase 18 metrics
    token_consumption_total = None
    token_consumption_per_session = None
    token_cost_estimate = None
    agent_version_state = None
    dependency_changes_detected = None
    agent_registrations = None
    hard_stops = None
    struggle_signals = None
    agent_processing_time = None
    blackboard_latency = None
    active_sessions = None
    service_info = None


def record_contract_violation(agent_role: str, tier: int, rule_id: str):
    """Record a contract violation."""
    if contract_violations:
        contract_violations.labels(
            agent_role=agent_role,
            tier=str(tier),
            rule_id=rule_id
        ).inc()


def record_state_transition(
    agent_role: str,
    from_state: str,
    to_state: str,
    allowed: bool
):
    """Record a state transition attempt."""
    if state_transitions:
        state_transitions.labels(
            agent_role=agent_role,
            from_state=from_state,
            to_state=to_state,
            allowed=str(allowed).lower()
        ).inc()
    
    if not allowed and forbidden_transitions_blocked:
        forbidden_transitions_blocked.labels(
            agent_role=agent_role,
            from_state=from_state,
            to_state=to_state
        ).inc()


def record_blackboard_operation(operation: str):
    """Record a blackboard operation."""
    if blackboard_operations:
        blackboard_operations.labels(operation=operation).inc()


def record_artifact_submitted(artifact_type: str, review_status: str = "pending"):
    """Record an artifact submission."""
    if blackboard_artifacts:
        blackboard_artifacts.labels(
            artifact_type=artifact_type,
            review_status=review_status
        ).inc()


def record_peer_review(creator_role: str, reviewer_role: str, verdict: str):
    """Record a peer review."""
    if peer_reviews:
        peer_reviews.labels(
            creator_role=creator_role,
            reviewer_role=reviewer_role,
            verdict=verdict
        ).inc()


def record_self_review_blocked(agent_role: str):
    """Record a blocked self-review attempt."""
    if self_review_blocked:
        self_review_blocked.labels(agent_role=agent_role).inc()


def record_escalation(reason: str):
    """Record an escalation."""
    if escalations:
        escalations.labels(reason=reason).inc()


def record_hard_stop(agent_role: str, trigger_type: str):
    """Record a hard stop trigger."""
    if hard_stops:
        hard_stops.labels(
            agent_role=agent_role,
            trigger_type=trigger_type
        ).inc()


def record_struggle_signal(agent_role: str, signal_type: str):
    """Record a struggle signal."""
    if struggle_signals:
        struggle_signals.labels(
            agent_role=agent_role,
            signal_type=signal_type
        ).inc()


def observe_processing_time(agent_role: str, operation: str, duration: float):
    """Observe agent processing time."""
    if agent_processing_time:
        agent_processing_time.labels(
            agent_role=agent_role,
            operation=operation
        ).observe(duration)


def observe_blackboard_latency(operation: str, duration: float):
    """Observe blackboard operation latency."""
    if blackboard_latency:
        blackboard_latency.labels(operation=operation).observe(duration)


def set_active_sessions(count: int):
    """Set the number of active sessions."""
    if active_sessions:
        active_sessions.set(count)


def set_service_info():
    """Set service information."""
    if service_info:
        service_info.info({
            'version': os.getenv('SERVICE_VERSION', '1.0.0'),
            'environment': os.getenv('ENVIRONMENT', 'development'),
            'service_name': 'multi_agent_service'
        })


def get_metrics() -> Optional[bytes]:
    """Get metrics in Prometheus format."""
    if not PROMETHEUS_AVAILABLE:
        return None
    return generate_latest()


def get_metrics_content_type() -> str:
    """Get the content type for metrics."""
    if PROMETHEUS_AVAILABLE:
        return CONTENT_TYPE_LATEST
    return "text/plain"


# =============================================================================
# Phase 18: Token Consumption and Governance Metrics
# =============================================================================

# Token costs per 1M tokens (approximate, update as needed)
TOKEN_COSTS = {
    "claude-opus-4-20250514": {"input": 15.0, "output": 75.0},
    "claude-sonnet-4-20250514": {"input": 3.0, "output": 15.0},
    "gpt-4o": {"input": 2.5, "output": 10.0},
    "gpt-4o-mini": {"input": 0.15, "output": 0.6},
}


def record_token_consumption(
    agent_role: str,
    model: str,
    input_tokens: int,
    output_tokens: int,
    session_id: Optional[str] = None
):
    """
    Record token consumption for an agent.
    
    Args:
        agent_role: Role of the agent
        model: Model used (e.g., claude-opus-4-20250514)
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        session_id: Optional session ID for per-session tracking
    """
    if token_consumption_total:
        token_consumption_total.labels(
            agent_role=agent_role,
            model=model,
            token_type="input"
        ).inc(input_tokens)
        
        token_consumption_total.labels(
            agent_role=agent_role,
            model=model,
            token_type="output"
        ).inc(output_tokens)
    
    if session_id and token_consumption_per_session:
        token_consumption_per_session.labels(
            session_id=session_id,
            agent_role=agent_role
        ).inc(input_tokens + output_tokens)
    
    # Calculate estimated cost
    if token_cost_estimate and model in TOKEN_COSTS:
        costs = TOKEN_COSTS[model]
        input_cost = (input_tokens / 1_000_000) * costs["input"]
        output_cost = (output_tokens / 1_000_000) * costs["output"]
        # Store as micro-dollars for precision
        total_micro_usd = int((input_cost + output_cost) * 1_000_000)
        token_cost_estimate.labels(
            agent_role=agent_role,
            model=model
        ).inc(total_micro_usd)


def record_agent_version_state(agent_role: str, version: str, state: str):
    """Record agent version state."""
    if agent_version_state:
        agent_version_state.labels(
            agent_role=agent_role,
            version=version,
            state=state
        ).set(1)


def record_dependency_change(agent_role: str, dependency_type: str):
    """Record a detected dependency change."""
    if dependency_changes_detected:
        dependency_changes_detected.labels(
            agent_role=agent_role,
            dependency_type=dependency_type
        ).inc()


def record_agent_registration(registration_type: str, status: str):
    """Record an agent registration attempt."""
    if agent_registrations:
        agent_registrations.labels(
            registration_type=registration_type,
            status=status
        ).inc()
