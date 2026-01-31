# =============================================================================
# Delegation Package - Task Delegation Utilities
# Phase 19: Migrated from conversation_service
# =============================================================================
"""
Task delegation utilities including dry-run preview.

Provides:
- Dry-run preview mode for delegation
- Delegation preview builder
"""

from .dry_run import (
    DelegationPreview,
    DelegationPreviewBuilder,
    DryRunExecutor,
    get_preview_builder,
    get_dry_run_executor,
)

__all__ = [
    "DelegationPreview",
    "DelegationPreviewBuilder",
    "DryRunExecutor",
    "get_preview_builder",
    "get_dry_run_executor",
]
