# =============================================================================
# API Routes for Multi-Agent Service
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""API routes for the multi-agent service."""

from . import agent_routes, blackboard_routes, dashboard_routes, health, registry_routes, template_routes, session_routes

__all__ = ["agent_routes", "blackboard_routes", "dashboard_routes", "health", "registry_routes", "template_routes", "session_routes"]
