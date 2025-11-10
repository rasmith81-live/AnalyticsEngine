# Azure AD SSO Service

## Overview

The Azure AD SSO Service provides **Single Sign-On** integration with Azure Active Directory (Azure AD) for client authentication and role synchronization. It handles OAuth/OIDC authentication, user/group synchronization, and automatic role mapping based on Azure AD group memberships.

---

## Features

✅ **OAuth 2.0 / OpenID Connect Authentication**  
✅ **Single Sign-On (SSO)** with Azure AD  
✅ **Automatic User Synchronization** from Azure AD  
✅ **Group Synchronization** with member tracking  
✅ **Automatic Role Mapping** based on group memberships  
✅ **Token Management** with refresh support  
✅ **Audit Logging** for all sync operations  
✅ **Multi-Tenant Support** (one config per client)  

---

## Architecture

```
Client Organization
  │
  └── Azure AD Tenant
       │
       ├── Users (synced to AzureADUser)
       ├── Groups (synced to AzureADGroup)
       └── Group Memberships
            │
            └── Role Mappings (AzureADGroup → ClientRole)
                 │
                 └── Automatic Role Assignment
```

---

## Database Models

### 1. AzureADConfig
**Purpose**: Stores Azure AD tenant configuration for a client

**Key Fields**:
- `client_id` - Reference to Client from analytics_models
- `tenant_id` - Azure AD Tenant ID (GUID)
- `application_id` - Azure AD Application (Client) ID
- `application_secret` - Encrypted application secret
- `authority_url` - Azure AD authority URL
- `redirect_uri` - OAuth redirect URI
- `sync_enabled` - Whether sync is enabled
- `sync_frequency_minutes` - Sync frequency
- `last_sync_at` - Last successful sync timestamp

### 2. AzureADUser
**Purpose**: Stores synchronized users from Azure AD

**Key Fields**:
- `azure_user_id` - Azure AD User Object ID
- `user_principal_name` - UPN (username@domain.com)
- `email` - User email
- `display_name`, `given_name`, `surname` - Name fields
- `job_title`, `department` - Organization info
- `account_enabled` - Whether account is enabled in Azure AD
- `internal_user_id` - Link to internal user table
- `last_synced_at` - Last sync timestamp

### 3. AzureADGroup
**Purpose**: Stores synchronized groups from Azure AD

**Key Fields**:
- `azure_group_id` - Azure AD Group Object ID
- `display_name` - Group name
- `description` - Group description
- `member_ids` - JSON array of member user IDs
- `security_enabled` - Whether it's a security group
- `last_synced_at` - Last sync timestamp

### 4. RoleMapping
**Purpose**: Maps Azure AD groups to ClientRoles

**Key Fields**:
- `azure_group_id` - Azure AD Group
- `client_role_id` - ClientRole from analytics_models
- `auto_provision` - Auto-assign role when user joins group
- `auto_deprovision` - Auto-remove role when user leaves group
- `priority` - Priority for role assignment

### 5. SyncLog
**Purpose**: Audit log for synchronization operations

**Key Fields**:
- `sync_type` - Type: users, groups, roles, full
- `status` - Status: success, failed, partial
- `users_synced`, `users_added`, `users_updated`, `users_removed`
- `groups_synced`, `groups_added`, `groups_updated`, `groups_removed`
- `roles_assigned`, `roles_revoked`
- `error_message`, `error_details`

---

## Setup Guide

### Step 1: Register Application in Azure AD

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to **Azure Active Directory** → **App registrations**
3. Click **New registration**
4. Configure:
   - **Name**: "AnalyticsEngine SSO"
   - **Supported account types**: "Accounts in this organizational directory only"
   - **Redirect URI**: `https://your-app.com/auth/callback`
5. Click **Register**

### Step 2: Configure Application

1. Go to **Certificates & secrets**
2. Click **New client secret**
3. Save the secret value (you won't see it again!)
4. Go to **API permissions**
5. Add permissions:
   - Microsoft Graph → Delegated permissions:
     - `openid`
     - `profile`
     - `email`
     - `User.Read`
     - `Group.Read.All`
   - Microsoft Graph → Application permissions:
     - `User.Read.All`
     - `Group.Read.All`
6. Click **Grant admin consent**

### Step 3: Get Configuration Values

From the Azure AD app registration, collect:
- **Tenant ID**: Found in Overview
- **Application (Client) ID**: Found in Overview
- **Client Secret**: The value you saved earlier
- **Authority URL**: `https://login.microsoftonline.com/{tenant-id}`

### Step 4: Create AzureADConfig

```python
from azure_ad_sso_service import AzureADConfig

config = AzureADConfig(
    client_id=1,  # Your client ID from analytics_models
    tenant_id="12345678-1234-1234-1234-123456789012",
    tenant_name="Contoso",
    application_id="87654321-4321-4321-4321-210987654321",
    application_secret="your-secret-here",
    authority_url="https://login.microsoftonline.com/12345678-1234-1234-1234-123456789012",
    redirect_uri="https://your-app.com/auth/callback",
    scopes={
        "scopes": ["openid", "profile", "email", "User.Read", "Group.Read.All"]
    },
    sync_enabled=True,
    sync_frequency_minutes=60
)
```

---

## Authentication Flow

### 1. Initiate Login

```python
from azure_ad_sso_service.auth import AzureADAuthProvider

# Create auth provider
auth_provider = AzureADAuthProvider(
    tenant_id=config.tenant_id,
    client_id=config.application_id,
    client_secret=config.application_secret,
    redirect_uri=config.redirect_uri
)

# Get authorization URL
auth_url = auth_provider.get_authorization_url(state="random-state-value")

# Redirect user to auth_url
```

### 2. Handle Callback

```python
# User is redirected back with authorization code
authorization_code = request.query_params.get("code")

# Exchange code for tokens
tokens = await auth_provider.exchange_code_for_token(authorization_code)

# tokens contains:
# - access_token
# - refresh_token
# - id_token
# - expires_in
```

### 3. Get User Information

```python
# Get user info from Microsoft Graph
user_info = await auth_provider.get_user_info(tokens["access_token"])

# user_info contains:
# - id (Azure AD User ID)
# - userPrincipalName
# - mail
# - displayName
# - givenName
# - surname
# - jobTitle
# - department
```

### 4. Get User Groups

```python
# Get user's group memberships
groups = await auth_provider.get_user_groups(tokens["access_token"])

# groups is a list of group objects
```

### 5. Validate Token

```python
# Validate JWT token
decoded_token = await auth_provider.validate_token(tokens["id_token"])

# decoded_token contains claims
```

---

## Synchronization

### Manual Sync

```python
from azure_ad_sso_service.sync import AzureADSyncService

# Create sync service
sync_service = AzureADSyncService(config, access_token)

# Perform full sync
sync_log = await sync_service.sync_all(session)

print(f"Sync Status: {sync_log.status}")
print(f"Users Synced: {sync_log.users_synced}")
print(f"Groups Synced: {sync_log.groups_synced}")
print(f"Roles Assigned: {sync_log.roles_assigned}")
```

### Sync Individual Components

```python
# Sync only users
users_result = await sync_service.sync_users(session)

# Sync only groups
groups_result = await sync_service.sync_groups(session)

# Sync only role assignments
roles_result = await sync_service.sync_role_assignments(session)
```

### Automated Sync

Configure automatic synchronization:

```python
config.sync_enabled = True
config.sync_frequency_minutes = 60  # Sync every hour
```

Implement a background task:

```python
import asyncio
from datetime import datetime, timedelta

async def auto_sync_task():
    while True:
        # Get all active configs
        configs = await get_active_configs()
        
        for config in configs:
            if not config.sync_enabled:
                continue
            
            # Check if sync is due
            if config.last_sync_at:
                next_sync = config.last_sync_at + timedelta(
                    minutes=config.sync_frequency_minutes
                )
                if datetime.utcnow() < next_sync:
                    continue
            
            # Perform sync
            try:
                # Get access token (using client credentials flow)
                access_token = await get_app_access_token(config)
                
                sync_service = AzureADSyncService(config, access_token)
                await sync_service.sync_all(session)
            except Exception as e:
                print(f"Sync failed for client {config.client_id}: {e}")
        
        # Wait before next check
        await asyncio.sleep(300)  # Check every 5 minutes
```

---

## Role Mapping

### Create Role Mapping

```python
from azure_ad_sso_service import RoleMapping

# Map Azure AD group to ClientRole
mapping = RoleMapping(
    ad_config_id=config.id,
    azure_group_id=azure_group.id,  # Azure AD Group from sync
    client_role_id=admin_role.id,   # ClientRole from analytics_models
    auto_provision=True,
    auto_deprovision=True,
    priority=10
)
```

### How It Works

1. **User joins Azure AD group** → Sync detects membership
2. **RoleMapping exists** → Role is automatically assigned
3. **User leaves Azure AD group** → Role is automatically revoked (if auto_deprovision=True)

### Example Scenario

```python
# Azure AD Groups
sales_group = AzureADGroup(display_name="Sales Team")
finance_group = AzureADGroup(display_name="Finance Team")
admin_group = AzureADGroup(display_name="Administrators")

# ClientRoles from analytics_models
sales_role = ClientRole(name="Sales Manager")
finance_role = ClientRole(name="Finance Analyst")
admin_role = ClientRole(name="Administrator")

# Create mappings
RoleMapping(
    azure_group_id=sales_group.id,
    client_role_id=sales_role.id,
    auto_provision=True
)

RoleMapping(
    azure_group_id=finance_group.id,
    client_role_id=finance_role.id,
    auto_provision=True
)

RoleMapping(
    azure_group_id=admin_group.id,
    client_role_id=admin_role.id,
    auto_provision=True,
    priority=100  # Higher priority
)

# When sync runs:
# - Users in "Sales Team" get "Sales Manager" role
# - Users in "Finance Team" get "Finance Analyst" role
# - Users in "Administrators" get "Administrator" role
```

---

## API Endpoints (Suggested)

### Authentication Endpoints

```
GET    /auth/azure/login/{client_id}          - Get authorization URL
GET    /auth/azure/callback                   - OAuth callback handler
POST   /auth/azure/token                      - Exchange code for token
POST   /auth/azure/refresh                    - Refresh access token
GET    /auth/azure/userinfo                   - Get user information
GET    /auth/azure/logout                     - Logout URL
```

### Configuration Endpoints

```
POST   /azure-ad/configs                      - Create Azure AD config
GET    /azure-ad/configs                      - List configs
GET    /azure-ad/configs/{id}                 - Get config
PUT    /azure-ad/configs/{id}                 - Update config
DELETE /azure-ad/configs/{id}                 - Delete config
```

### Sync Endpoints

```
POST   /azure-ad/sync                         - Trigger sync
GET    /azure-ad/sync/logs                    - List sync logs
GET    /azure-ad/sync/logs/{id}               - Get sync log
GET    /azure-ad/sync/status/{client_id}      - Get sync status
```

### User/Group Endpoints

```
GET    /azure-ad/users                        - List synced users
GET    /azure-ad/users/{id}                   - Get user
GET    /azure-ad/groups                       - List synced groups
GET    /azure-ad/groups/{id}                  - Get group
GET    /azure-ad/groups/{id}/members          - Get group members
```

### Role Mapping Endpoints

```
POST   /azure-ad/role-mappings                - Create role mapping
GET    /azure-ad/role-mappings                - List role mappings
GET    /azure-ad/role-mappings/{id}           - Get role mapping
PUT    /azure-ad/role-mappings/{id}           - Update role mapping
DELETE /azure-ad/role-mappings/{id}           - Delete role mapping
```

---

## Security Considerations

### 1. Secret Storage
- **Never store secrets in plain text**
- Use encryption for `application_secret`
- Consider using Azure Key Vault

### 2. Token Management
- Store tokens securely (encrypted)
- Implement token refresh logic
- Clear tokens on logout

### 3. CSRF Protection
- Always use `state` parameter in OAuth flow
- Validate state on callback

### 4. Token Validation
- Always validate JWT tokens
- Check expiration
- Verify issuer and audience

### 5. Permissions
- Request minimum necessary permissions
- Use delegated permissions for user context
- Use application permissions for background sync

---

## Troubleshooting

### Common Issues

#### 1. "Invalid client secret"
- Verify secret is correct
- Check if secret has expired
- Generate new secret in Azure Portal

#### 2. "Insufficient privileges"
- Check API permissions in Azure AD
- Ensure admin consent is granted
- Verify user has necessary permissions

#### 3. "Token validation failed"
- Check tenant ID is correct
- Verify application ID matches
- Ensure token hasn't expired

#### 4. "Sync fails"
- Check access token is valid
- Verify Graph API permissions
- Check network connectivity

---

## Best Practices

### 1. Sync Frequency
- Don't sync too frequently (respect rate limits)
- Recommended: 30-60 minutes for production
- Use webhooks for real-time updates (if available)

### 2. Error Handling
- Log all sync errors
- Implement retry logic with exponential backoff
- Alert administrators on repeated failures

### 3. Monitoring
- Track sync success rate
- Monitor sync duration
- Alert on sync failures

### 4. Testing
- Test with test Azure AD tenant first
- Verify role mappings before production
- Test token refresh logic

### 5. Documentation
- Document all role mappings
- Keep Azure AD group names consistent
- Document sync schedule

---

## Dependencies

```
httpx>=0.24.0
pyjwt[crypto]>=2.8.0
cryptography>=41.0.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
```

---

## Conclusion

The Azure AD SSO Service provides comprehensive Single Sign-On integration with automatic user/group synchronization and role mapping. It enables seamless authentication and authorization for multi-tenant analytics applications.
