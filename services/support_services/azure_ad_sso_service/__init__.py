"""
Azure AD SSO Service

Manages Single Sign-On integration with Azure Active Directory for client authentication
and role synchronization.
"""

from .models import (
    AzureADConfig,
    AzureADUser,
    AzureADGroup,
    RoleMapping,
    SyncLog
)

from .auth import (
    AzureADAuthProvider,
    validate_token,
    get_user_info,
    refresh_access_token
)

from .sync import (
    AzureADSyncService,
    sync_users,
    sync_groups,
    sync_role_mappings
)

__all__ = [
    # Models
    "AzureADConfig",
    "AzureADUser",
    "AzureADGroup",
    "RoleMapping",
    "SyncLog",
    # Auth
    "AzureADAuthProvider",
    "validate_token",
    "get_user_info",
    "refresh_access_token",
    # Sync
    "AzureADSyncService",
    "sync_users",
    "sync_groups",
    "sync_role_mappings",
]
