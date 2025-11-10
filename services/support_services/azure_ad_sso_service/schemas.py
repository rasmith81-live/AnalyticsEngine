"""
Azure AD SSO Service - Pydantic Schemas

API request/response models for Azure AD SSO service.
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict, EmailStr


# ============================================================================
# AzureADConfig Schemas
# ============================================================================

class AzureADConfigBase(BaseModel):
    """Base schema for AzureADConfig."""
    tenant_id: str = Field(..., min_length=1, max_length=255, description="Azure AD Tenant ID")
    tenant_name: str = Field(..., min_length=1, max_length=255, description="Azure AD Tenant name")
    application_id: str = Field(..., min_length=1, max_length=255, description="Application (Client) ID")
    application_secret: str = Field(..., description="Application secret (will be encrypted)")
    authority_url: str = Field(..., max_length=500, description="Azure AD authority URL")
    redirect_uri: str = Field(..., max_length=500, description="OAuth redirect URI")
    scopes: Optional[Dict[str, Any]] = Field(None, description="OAuth scopes")
    sync_enabled: bool = Field(True, description="Whether sync is enabled")
    sync_frequency_minutes: int = Field(60, ge=1, description="Sync frequency in minutes")
    is_active: bool = Field(True, description="Whether config is active")
    config: Optional[Dict[str, Any]] = Field(None, description="Additional configuration")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class AzureADConfigCreate(AzureADConfigBase):
    """Schema for creating AzureADConfig."""
    client_id: int = Field(..., gt=0, description="Client ID from analytics_models")


class AzureADConfigUpdate(BaseModel):
    """Schema for updating AzureADConfig."""
    tenant_name: Optional[str] = Field(None, min_length=1, max_length=255)
    application_secret: Optional[str] = None
    authority_url: Optional[str] = Field(None, max_length=500)
    redirect_uri: Optional[str] = Field(None, max_length=500)
    scopes: Optional[Dict[str, Any]] = None
    sync_enabled: Optional[bool] = None
    sync_frequency_minutes: Optional[int] = Field(None, ge=1)
    is_active: Optional[bool] = None
    config: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None


class AzureADConfigRead(AzureADConfigBase):
    """Schema for reading AzureADConfig."""
    id: int
    client_id: int
    last_sync_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    # Don't expose the secret in read operations
    application_secret: str = Field("***", description="Secret is masked")
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# AzureADUser Schemas
# ============================================================================

class AzureADUserBase(BaseModel):
    """Base schema for AzureADUser."""
    azure_user_id: str = Field(..., max_length=255, description="Azure AD User Object ID")
    user_principal_name: str = Field(..., max_length=255, description="User Principal Name")
    email: EmailStr = Field(..., description="User email")
    display_name: str = Field(..., max_length=255, description="Display name")
    given_name: Optional[str] = Field(None, max_length=255, description="First name")
    surname: Optional[str] = Field(None, max_length=255, description="Last name")
    job_title: Optional[str] = Field(None, max_length=255, description="Job title")
    department: Optional[str] = Field(None, max_length=255, description="Department")
    is_active: bool = Field(True, description="Whether user is active")
    account_enabled: bool = Field(True, description="Whether account is enabled in Azure AD")
    azure_data: Optional[Dict[str, Any]] = Field(None, description="Full Azure AD user data")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class AzureADUserCreate(AzureADUserBase):
    """Schema for creating AzureADUser."""
    ad_config_id: int = Field(..., gt=0, description="Azure AD Config ID")


class AzureADUserUpdate(BaseModel):
    """Schema for updating AzureADUser."""
    user_principal_name: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = None
    display_name: Optional[str] = Field(None, max_length=255)
    given_name: Optional[str] = Field(None, max_length=255)
    surname: Optional[str] = Field(None, max_length=255)
    job_title: Optional[str] = Field(None, max_length=255)
    department: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None
    account_enabled: Optional[bool] = None
    internal_user_id: Optional[int] = Field(None, gt=0)
    azure_data: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None


class AzureADUserRead(AzureADUserBase):
    """Schema for reading AzureADUser."""
    id: int
    ad_config_id: int
    internal_user_id: Optional[int]
    last_synced_at: datetime
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# AzureADGroup Schemas
# ============================================================================

class AzureADGroupBase(BaseModel):
    """Base schema for AzureADGroup."""
    azure_group_id: str = Field(..., max_length=255, description="Azure AD Group Object ID")
    display_name: str = Field(..., max_length=255, description="Group display name")
    description: Optional[str] = Field(None, description="Group description")
    mail: Optional[str] = Field(None, max_length=255, description="Group email")
    mail_enabled: bool = Field(False, description="Whether mail is enabled")
    security_enabled: bool = Field(True, description="Whether security is enabled")
    member_ids: Optional[Dict[str, Any]] = Field(None, description="Group member IDs")
    azure_data: Optional[Dict[str, Any]] = Field(None, description="Full Azure AD group data")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class AzureADGroupCreate(AzureADGroupBase):
    """Schema for creating AzureADGroup."""
    ad_config_id: int = Field(..., gt=0, description="Azure AD Config ID")


class AzureADGroupUpdate(BaseModel):
    """Schema for updating AzureADGroup."""
    display_name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    mail: Optional[str] = Field(None, max_length=255)
    mail_enabled: Optional[bool] = None
    security_enabled: Optional[bool] = None
    member_ids: Optional[Dict[str, Any]] = None
    azure_data: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None


class AzureADGroupRead(AzureADGroupBase):
    """Schema for reading AzureADGroup."""
    id: int
    ad_config_id: int
    last_synced_at: datetime
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# RoleMapping Schemas
# ============================================================================

class RoleMappingBase(BaseModel):
    """Base schema for RoleMapping."""
    client_role_id: int = Field(..., gt=0, description="ClientRole ID from analytics_models")
    is_active: bool = Field(True, description="Whether mapping is active")
    priority: int = Field(0, description="Priority for role assignment")
    auto_provision: bool = Field(True, description="Auto-assign role when user joins group")
    auto_deprovision: bool = Field(True, description="Auto-remove role when user leaves group")
    config: Optional[Dict[str, Any]] = Field(None, description="Additional configuration")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class RoleMappingCreate(RoleMappingBase):
    """Schema for creating RoleMapping."""
    ad_config_id: int = Field(..., gt=0, description="Azure AD Config ID")
    azure_group_id: int = Field(..., gt=0, description="Azure AD Group ID")


class RoleMappingUpdate(BaseModel):
    """Schema for updating RoleMapping."""
    client_role_id: Optional[int] = Field(None, gt=0)
    is_active: Optional[bool] = None
    priority: Optional[int] = None
    auto_provision: Optional[bool] = None
    auto_deprovision: Optional[bool] = None
    config: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None


class RoleMappingRead(RoleMappingBase):
    """Schema for reading RoleMapping."""
    id: int
    ad_config_id: int
    azure_group_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# SyncLog Schemas
# ============================================================================

class SyncLogBase(BaseModel):
    """Base schema for SyncLog."""
    sync_type: str = Field(..., max_length=50, description="Sync type")
    status: str = Field(..., max_length=50, description="Sync status")
    started_at: datetime = Field(..., description="Sync start time")
    completed_at: Optional[datetime] = Field(None, description="Sync completion time")
    duration_seconds: Optional[float] = Field(None, description="Sync duration")
    users_synced: int = Field(0, ge=0)
    users_added: int = Field(0, ge=0)
    users_updated: int = Field(0, ge=0)
    users_removed: int = Field(0, ge=0)
    groups_synced: int = Field(0, ge=0)
    groups_added: int = Field(0, ge=0)
    groups_updated: int = Field(0, ge=0)
    groups_removed: int = Field(0, ge=0)
    roles_assigned: int = Field(0, ge=0)
    roles_revoked: int = Field(0, ge=0)
    error_message: Optional[str] = Field(None, description="Error message if failed")
    error_details: Optional[Dict[str, Any]] = Field(None, description="Error details")
    log_data: Optional[Dict[str, Any]] = Field(None, description="Detailed log data")


class SyncLogRead(SyncLogBase):
    """Schema for reading SyncLog."""
    id: int
    ad_config_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Authentication Schemas
# ============================================================================

class AuthorizationRequest(BaseModel):
    """Request to get authorization URL."""
    client_id: int = Field(..., gt=0, description="Client ID")
    state: Optional[str] = Field(None, description="State parameter for CSRF protection")
    scopes: Optional[List[str]] = Field(None, description="OAuth scopes to request")


class AuthorizationResponse(BaseModel):
    """Response with authorization URL."""
    authorization_url: str = Field(..., description="Authorization URL to redirect user to")
    state: Optional[str] = Field(None, description="State parameter")


class TokenExchangeRequest(BaseModel):
    """Request to exchange authorization code for tokens."""
    client_id: int = Field(..., gt=0, description="Client ID")
    authorization_code: str = Field(..., description="Authorization code from OAuth callback")


class TokenResponse(BaseModel):
    """Response with tokens."""
    access_token: str = Field(..., description="Access token")
    refresh_token: Optional[str] = Field(None, description="Refresh token")
    id_token: Optional[str] = Field(None, description="ID token")
    expires_in: int = Field(..., description="Token expiration in seconds")
    token_type: str = Field("Bearer", description="Token type")


class UserInfoResponse(BaseModel):
    """Response with user information."""
    user_id: str = Field(..., description="Azure AD User ID")
    user_principal_name: str = Field(..., description="User Principal Name")
    email: str = Field(..., description="Email")
    display_name: str = Field(..., description="Display name")
    given_name: Optional[str] = Field(None, description="First name")
    surname: Optional[str] = Field(None, description="Last name")
    job_title: Optional[str] = Field(None, description="Job title")
    department: Optional[str] = Field(None, description="Department")
    groups: List[Dict[str, Any]] = Field(default_factory=list, description="User groups")


class SyncRequest(BaseModel):
    """Request to trigger synchronization."""
    client_id: int = Field(..., gt=0, description="Client ID")
    sync_type: str = Field("full", description="Sync type: users, groups, roles, full")


class SyncResponse(BaseModel):
    """Response with sync results."""
    sync_log_id: int = Field(..., description="Sync log ID")
    status: str = Field(..., description="Sync status")
    message: str = Field(..., description="Status message")
    statistics: Dict[str, int] = Field(..., description="Sync statistics")
