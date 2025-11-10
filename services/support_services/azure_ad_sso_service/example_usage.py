"""
Azure AD SSO Service - Example Usage

Demonstrates how to set up and use Azure AD SSO integration.
"""

import asyncio
from datetime import datetime

from models import (
    AzureADConfig,
    AzureADUser,
    AzureADGroup,
    RoleMapping,
    SyncLog
)
from auth import AzureADAuthProvider, TokenManager
from sync import AzureADSyncService


# ============================================================================
# Example 1: Initial Setup
# ============================================================================

async def setup_azure_ad_config():
    """Set up Azure AD configuration for a client."""
    
    # Create Azure AD configuration
    config = AzureADConfig(
        client_id=1,  # Reference to Client from analytics_models
        tenant_id="12345678-1234-1234-1234-123456789012",
        tenant_name="Contoso Corporation",
        application_id="87654321-4321-4321-4321-210987654321",
        application_secret="your-secret-here",  # Will be encrypted
        authority_url="https://login.microsoftonline.com/12345678-1234-1234-1234-123456789012",
        redirect_uri="https://analytics.contoso.com/auth/callback",
        scopes={
            "scopes": [
                "openid",
                "profile",
                "email",
                "User.Read",
                "Group.Read.All"
            ]
        },
        sync_enabled=True,
        sync_frequency_minutes=60,
        config={
            "auto_create_users": True,
            "sync_disabled_users": False,
            "default_role_on_first_login": "viewer"
        }
    )
    
    print(f"Created Azure AD Config for client {config.client_id}")
    print(f"Tenant: {config.tenant_name}")
    print(f"Authority: {config.authority_url}")
    
    return config


# ============================================================================
# Example 2: Authentication Flow
# ============================================================================

async def authenticate_user(config: AzureADConfig):
    """Demonstrate OAuth authentication flow."""
    
    # Step 1: Create auth provider
    auth_provider = AzureADAuthProvider(
        tenant_id=config.tenant_id,
        client_id=config.application_id,
        client_secret=config.application_secret,
        redirect_uri=config.redirect_uri
    )
    
    # Step 2: Get authorization URL
    state = "random-csrf-token-12345"
    auth_url = auth_provider.get_authorization_url(state=state)
    
    print("\n" + "=" * 80)
    print("Step 1: Redirect user to authorization URL")
    print("=" * 80)
    print(f"Authorization URL: {auth_url}")
    print("\nUser will be redirected to Azure AD to sign in...")
    
    # Step 3: User signs in and is redirected back with authorization code
    # (In real application, this comes from the callback endpoint)
    authorization_code = "simulated-auth-code-from-callback"
    
    print("\n" + "=" * 80)
    print("Step 2: Exchange authorization code for tokens")
    print("=" * 80)
    
    try:
        # Exchange code for tokens
        tokens = await auth_provider.exchange_code_for_token(authorization_code)
        
        print("✓ Tokens received:")
        print(f"  - Access Token: {tokens['access_token'][:50]}...")
        print(f"  - Refresh Token: {tokens.get('refresh_token', 'N/A')[:50]}...")
        print(f"  - Expires In: {tokens['expires_in']} seconds")
        
        # Step 4: Get user information
        print("\n" + "=" * 80)
        print("Step 3: Get user information")
        print("=" * 80)
        
        user_info = await auth_provider.get_user_info(tokens['access_token'])
        
        print("✓ User Information:")
        print(f"  - User ID: {user_info['id']}")
        print(f"  - UPN: {user_info['userPrincipalName']}")
        print(f"  - Email: {user_info['mail']}")
        print(f"  - Display Name: {user_info['displayName']}")
        print(f"  - Job Title: {user_info.get('jobTitle', 'N/A')}")
        print(f"  - Department: {user_info.get('department', 'N/A')}")
        
        # Step 5: Get user groups
        print("\n" + "=" * 80)
        print("Step 4: Get user groups")
        print("=" * 80)
        
        groups = await auth_provider.get_user_groups(tokens['access_token'])
        
        print(f"✓ User is member of {len(groups)} groups:")
        for group in groups[:5]:  # Show first 5
            print(f"  - {group['displayName']} ({group['id']})")
        
        return tokens, user_info, groups
        
    except Exception as e:
        print(f"✗ Authentication failed: {e}")
        return None, None, None


# ============================================================================
# Example 3: User Synchronization
# ============================================================================

async def sync_users_from_azure_ad(config: AzureADConfig, access_token: str, session):
    """Synchronize users from Azure AD."""
    
    print("\n" + "=" * 80)
    print("Synchronizing Users from Azure AD")
    print("=" * 80)
    
    # Create sync service
    sync_service = AzureADSyncService(config, access_token)
    
    # Sync users
    result = await sync_service.sync_users(session)
    
    print(f"✓ User Sync Complete:")
    print(f"  - Total Synced: {result['synced']}")
    print(f"  - Added: {result['added']}")
    print(f"  - Updated: {result['updated']}")
    print(f"  - Removed: {result['removed']}")
    
    return result


# ============================================================================
# Example 4: Group Synchronization
# ============================================================================

async def sync_groups_from_azure_ad(config: AzureADConfig, access_token: str, session):
    """Synchronize groups from Azure AD."""
    
    print("\n" + "=" * 80)
    print("Synchronizing Groups from Azure AD")
    print("=" * 80)
    
    # Create sync service
    sync_service = AzureADSyncService(config, access_token)
    
    # Sync groups
    result = await sync_service.sync_groups(session)
    
    print(f"✓ Group Sync Complete:")
    print(f"  - Total Synced: {result['synced']}")
    print(f"  - Added: {result['added']}")
    print(f"  - Updated: {result['updated']}")
    print(f"  - Removed: {result['removed']}")
    
    return result


# ============================================================================
# Example 5: Role Mapping
# ============================================================================

async def setup_role_mappings(config: AzureADConfig, session):
    """Set up role mappings between Azure AD groups and ClientRoles."""
    
    print("\n" + "=" * 80)
    print("Setting Up Role Mappings")
    print("=" * 80)
    
    # Example: Map Azure AD groups to ClientRoles
    
    # Mapping 1: Administrators group → Administrator role
    admin_mapping = RoleMapping(
        ad_config_id=config.id,
        azure_group_id=1,  # Azure AD Group ID
        client_role_id=1,  # ClientRole ID from analytics_models
        is_active=True,
        priority=100,
        auto_provision=True,
        auto_deprovision=True,
        config={
            "description": "Full administrative access",
            "requires_mfa": True
        }
    )
    
    print("✓ Created mapping: Administrators → Administrator Role")
    
    # Mapping 2: Sales Team group → Sales Manager role
    sales_mapping = RoleMapping(
        ad_config_id=config.id,
        azure_group_id=2,
        client_role_id=2,
        is_active=True,
        priority=50,
        auto_provision=True,
        auto_deprovision=True,
        config={
            "description": "Sales data access",
            "default_dashboard": "sales_overview"
        }
    )
    
    print("✓ Created mapping: Sales Team → Sales Manager Role")
    
    # Mapping 3: Analysts group → Data Analyst role
    analyst_mapping = RoleMapping(
        ad_config_id=config.id,
        azure_group_id=3,
        client_role_id=3,
        is_active=True,
        priority=30,
        auto_provision=True,
        auto_deprovision=False,  # Don't auto-remove
        config={
            "description": "Read-only data access",
            "can_export": True
        }
    )
    
    print("✓ Created mapping: Analysts → Data Analyst Role")
    
    return [admin_mapping, sales_mapping, analyst_mapping]


# ============================================================================
# Example 6: Full Synchronization
# ============================================================================

async def perform_full_sync(config: AzureADConfig, access_token: str, session):
    """Perform full synchronization of users, groups, and roles."""
    
    print("\n" + "=" * 80)
    print("Performing Full Synchronization")
    print("=" * 80)
    
    # Create sync service
    sync_service = AzureADSyncService(config, access_token)
    
    # Perform full sync
    sync_log = await sync_service.sync_all(session)
    
    print(f"\n✓ Full Sync Complete:")
    print(f"  - Status: {sync_log.status}")
    print(f"  - Duration: {sync_log.duration_seconds:.2f} seconds")
    print(f"\n  Users:")
    print(f"    - Synced: {sync_log.users_synced}")
    print(f"    - Added: {sync_log.users_added}")
    print(f"    - Updated: {sync_log.users_updated}")
    print(f"    - Removed: {sync_log.users_removed}")
    print(f"\n  Groups:")
    print(f"    - Synced: {sync_log.groups_synced}")
    print(f"    - Added: {sync_log.groups_added}")
    print(f"    - Updated: {sync_log.groups_updated}")
    print(f"    - Removed: {sync_log.groups_removed}")
    print(f"\n  Roles:")
    print(f"    - Assigned: {sync_log.roles_assigned}")
    print(f"    - Revoked: {sync_log.roles_revoked}")
    
    if sync_log.error_message:
        print(f"\n  ✗ Error: {sync_log.error_message}")
    
    return sync_log


# ============================================================================
# Example 7: Token Management
# ============================================================================

async def manage_tokens():
    """Demonstrate token management."""
    
    print("\n" + "=" * 80)
    print("Token Management")
    print("=" * 80)
    
    # Create token manager
    token_manager = TokenManager()
    
    # Store tokens for a user
    user_id = "user-123"
    token_manager.store_token(
        user_id=user_id,
        access_token="access-token-value",
        refresh_token="refresh-token-value",
        expires_in=3600  # 1 hour
    )
    
    print(f"✓ Stored tokens for user {user_id}")
    
    # Get token
    access_token = token_manager.get_token(user_id)
    print(f"✓ Retrieved access token: {access_token[:20]}...")
    
    # Check if expired
    is_expired = token_manager.is_token_expired(user_id)
    print(f"✓ Token expired: {is_expired}")
    
    # Get refresh token
    refresh_token = token_manager.get_refresh_token(user_id)
    print(f"✓ Retrieved refresh token: {refresh_token[:20]}...")
    
    # Remove tokens (logout)
    token_manager.remove_token(user_id)
    print(f"✓ Removed tokens for user {user_id}")


# ============================================================================
# Example 8: Complete Workflow
# ============================================================================

async def complete_workflow():
    """Demonstrate complete Azure AD SSO workflow."""
    
    print("=" * 80)
    print("Azure AD SSO Service - Complete Workflow")
    print("=" * 80)
    
    # Step 1: Set up configuration
    config = await setup_azure_ad_config()
    
    # Step 2: Authenticate user (simulated)
    # In real application, this would be triggered by user login
    # tokens, user_info, groups = await authenticate_user(config)
    
    # Step 3: For background sync, use application access token
    # (In real application, get this using client credentials flow)
    app_access_token = "simulated-app-access-token"
    
    # Step 4: Set up role mappings
    # role_mappings = await setup_role_mappings(config, session)
    
    # Step 5: Perform full sync
    # sync_log = await perform_full_sync(config, app_access_token, session)
    
    # Step 6: Manage tokens
    await manage_tokens()
    
    print("\n" + "=" * 80)
    print("Workflow Complete!")
    print("=" * 80)
    print("\nNext Steps:")
    print("1. Configure Azure AD application in Azure Portal")
    print("2. Create AzureADConfig in database")
    print("3. Set up role mappings")
    print("4. Enable automatic synchronization")
    print("5. Test authentication flow")
    print("6. Monitor sync logs")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    # Run complete workflow
    asyncio.run(complete_workflow())
