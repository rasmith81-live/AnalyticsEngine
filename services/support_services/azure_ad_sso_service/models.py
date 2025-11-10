"""
Azure AD SSO Service - Database Models

SQLAlchemy models for Azure AD configuration, user synchronization, and role mapping.
"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
    Boolean,
    ForeignKey,
    Index,
    JSON,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


class TimestampMixin:
    """Mixin for created_at and updated_at columns."""
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


class AzureADConfig(Base, TimestampMixin):
    """
    AzureADConfig - Azure AD tenant configuration for a client.
    
    Stores Azure AD connection details and SSO configuration for each client.
    """
    __tablename__ = "azure_ad_configs"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        comment="Reference to Client.id from analytics_models"
    )
    
    # Azure AD Tenant Information
    tenant_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Azure AD Tenant ID (GUID)"
    )
    tenant_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Azure AD Tenant name"
    )
    
    # Application Registration Details
    application_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Azure AD Application (Client) ID"
    )
    application_secret: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment="Encrypted application secret"
    )
    
    # OAuth/OIDC Configuration
    authority_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        comment="Azure AD authority URL"
    )
    redirect_uri: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        comment="OAuth redirect URI"
    )
    scopes: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="OAuth scopes requested"
    )
    
    # Sync Configuration
    sync_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="Whether user/group sync is enabled"
    )
    sync_frequency_minutes: Mapped[int] = mapped_column(
        Integer,
        default=60,
        nullable=False,
        comment="Sync frequency in minutes"
    )
    last_sync_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="Last successful sync timestamp"
    )
    
    # Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Additional Azure AD configuration"
    )
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    users: Mapped[List["AzureADUser"]] = relationship(
        "AzureADUser",
        back_populates="ad_config",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    groups: Mapped[List["AzureADGroup"]] = relationship(
        "AzureADGroup",
        back_populates="ad_config",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    role_mappings: Mapped[List["RoleMapping"]] = relationship(
        "RoleMapping",
        back_populates="ad_config",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    sync_logs: Mapped[List["SyncLog"]] = relationship(
        "SyncLog",
        back_populates="ad_config",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_azure_ad_configs_client_id", "client_id"),
        Index("ix_azure_ad_configs_tenant_id", "tenant_id"),
        Index("ix_azure_ad_configs_is_active", "is_active"),
    )
    
    def __repr__(self) -> str:
        return f"<AzureADConfig(id={self.id}, client_id={self.client_id}, tenant_name='{self.tenant_name}')>"


class AzureADUser(Base, TimestampMixin):
    """
    AzureADUser - Synchronized user from Azure AD.
    
    Stores user information synced from Azure AD and links to internal user accounts.
    """
    __tablename__ = "azure_ad_users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ad_config_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("azure_ad_configs.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Azure AD User Information
    azure_user_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Azure AD User Object ID (GUID)"
    )
    user_principal_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="User Principal Name (UPN)"
    )
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    given_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    surname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    job_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    department: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    
    # Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    account_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="Whether account is enabled in Azure AD"
    )
    
    # Internal Mapping
    internal_user_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Reference to internal user table"
    )
    
    # Sync Information
    last_synced_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    
    # Additional Data
    azure_data: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Full Azure AD user data"
    )
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    ad_config: Mapped["AzureADConfig"] = relationship(
        "AzureADConfig",
        back_populates="users"
    )
    
    __table_args__ = (
        Index("ix_azure_ad_users_ad_config_id", "ad_config_id"),
        Index("ix_azure_ad_users_azure_user_id", "azure_user_id"),
        Index("ix_azure_ad_users_user_principal_name", "user_principal_name"),
        Index("ix_azure_ad_users_email", "email"),
        Index("ix_azure_ad_users_is_active", "is_active"),
        Index("ix_azure_ad_users_internal_user_id", "internal_user_id"),
        Index("ix_azure_ad_users_config_azure_id", "ad_config_id", "azure_user_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<AzureADUser(id={self.id}, upn='{self.user_principal_name}', display_name='{self.display_name}')>"


class AzureADGroup(Base, TimestampMixin):
    """
    AzureADGroup - Synchronized group from Azure AD.
    
    Stores group information synced from Azure AD for role mapping.
    """
    __tablename__ = "azure_ad_groups"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ad_config_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("azure_ad_configs.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Azure AD Group Information
    azure_group_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Azure AD Group Object ID (GUID)"
    )
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    mail: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    mail_enabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    security_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Group Members (stored as JSON array of user IDs)
    member_ids: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Array of Azure AD user IDs who are members"
    )
    
    # Sync Information
    last_synced_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    
    # Additional Data
    azure_data: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Full Azure AD group data"
    )
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    ad_config: Mapped["AzureADConfig"] = relationship(
        "AzureADConfig",
        back_populates="groups"
    )
    role_mappings: Mapped[List["RoleMapping"]] = relationship(
        "RoleMapping",
        back_populates="azure_group",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_azure_ad_groups_ad_config_id", "ad_config_id"),
        Index("ix_azure_ad_groups_azure_group_id", "azure_group_id"),
        Index("ix_azure_ad_groups_display_name", "display_name"),
        Index("ix_azure_ad_groups_config_azure_id", "ad_config_id", "azure_group_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<AzureADGroup(id={self.id}, display_name='{self.display_name}')>"


class RoleMapping(Base, TimestampMixin):
    """
    RoleMapping - Maps Azure AD groups to internal ClientRoles.
    
    Defines how Azure AD group memberships translate to internal role assignments.
    """
    __tablename__ = "role_mappings"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ad_config_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("azure_ad_configs.id", ondelete="CASCADE"),
        nullable=False
    )
    azure_group_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("azure_ad_groups.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Internal Role Reference
    client_role_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Reference to ClientRole.id from analytics_models"
    )
    
    # Mapping Configuration
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    priority: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="Priority for role assignment (higher = higher priority)"
    )
    
    # Auto-provisioning
    auto_provision: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="Automatically assign role when user joins group"
    )
    auto_deprovision: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="Automatically remove role when user leaves group"
    )
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Additional mapping configuration"
    )
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    ad_config: Mapped["AzureADConfig"] = relationship(
        "AzureADConfig",
        back_populates="role_mappings"
    )
    azure_group: Mapped["AzureADGroup"] = relationship(
        "AzureADGroup",
        back_populates="role_mappings"
    )
    
    __table_args__ = (
        Index("ix_role_mappings_ad_config_id", "ad_config_id"),
        Index("ix_role_mappings_azure_group_id", "azure_group_id"),
        Index("ix_role_mappings_client_role_id", "client_role_id"),
        Index("ix_role_mappings_is_active", "is_active"),
        Index("ix_role_mappings_group_role", "azure_group_id", "client_role_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<RoleMapping(id={self.id}, azure_group_id={self.azure_group_id}, client_role_id={self.client_role_id})>"


class SyncLog(Base, TimestampMixin):
    """
    SyncLog - Audit log for Azure AD synchronization operations.
    
    Tracks all sync operations, successes, failures, and changes.
    """
    __tablename__ = "sync_logs"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ad_config_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("azure_ad_configs.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Sync Operation Details
    sync_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="Type: users, groups, roles, full"
    )
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="Status: success, failed, partial"
    )
    
    # Timing
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    duration_seconds: Mapped[Optional[float]] = mapped_column(
        nullable=True,
        comment="Sync duration in seconds"
    )
    
    # Statistics
    users_synced: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    users_added: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    users_updated: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    users_removed: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    groups_synced: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    groups_added: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    groups_updated: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    groups_removed: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    roles_assigned: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    roles_revoked: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    # Error Information
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    error_details: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Detailed Log
    log_data: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Detailed sync log data"
    )
    
    # Relationships
    ad_config: Mapped["AzureADConfig"] = relationship(
        "AzureADConfig",
        back_populates="sync_logs"
    )
    
    __table_args__ = (
        Index("ix_sync_logs_ad_config_id", "ad_config_id"),
        Index("ix_sync_logs_sync_type", "sync_type"),
        Index("ix_sync_logs_status", "status"),
        Index("ix_sync_logs_started_at", "started_at"),
    )
    
    def __repr__(self) -> str:
        return f"<SyncLog(id={self.id}, sync_type='{self.sync_type}', status='{self.status}')>"
