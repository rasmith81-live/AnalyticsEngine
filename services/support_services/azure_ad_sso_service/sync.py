"""
Azure AD SSO Service - Synchronization

Handles synchronization of users, groups, and role mappings from Azure AD.
"""

import httpx
from datetime import datetime
from typing import Dict, List, Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import (
    AzureADConfig,
    AzureADUser,
    AzureADGroup,
    RoleMapping,
    SyncLog
)


class AzureADSyncService:
    """
    Azure AD Synchronization Service
    
    Syncs users, groups, and role mappings from Azure AD to local database.
    """
    
    def __init__(self, ad_config: AzureADConfig, access_token: str):
        """
        Initialize sync service.
        
        Args:
            ad_config: Azure AD configuration
            access_token: Valid access token for Microsoft Graph API
        """
        self.ad_config = ad_config
        self.access_token = access_token
        self.graph_api_base = "https://graph.microsoft.com/v1.0"
        
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    
    async def sync_all(self, session: AsyncSession) -> SyncLog:
        """
        Perform full synchronization of users, groups, and roles.
        
        Args:
            session: Database session
            
        Returns:
            SyncLog with sync results
        """
        sync_log = SyncLog(
            ad_config_id=self.ad_config.id,
            sync_type="full",
            status="in_progress",
            started_at=datetime.utcnow()
        )
        session.add(sync_log)
        await session.flush()
        
        try:
            # Sync users
            users_result = await self.sync_users(session)
            sync_log.users_synced = users_result["synced"]
            sync_log.users_added = users_result["added"]
            sync_log.users_updated = users_result["updated"]
            sync_log.users_removed = users_result["removed"]
            
            # Sync groups
            groups_result = await self.sync_groups(session)
            sync_log.groups_synced = groups_result["synced"]
            sync_log.groups_added = groups_result["added"]
            sync_log.groups_updated = groups_result["updated"]
            sync_log.groups_removed = groups_result["removed"]
            
            # Sync role mappings
            roles_result = await self.sync_role_assignments(session)
            sync_log.roles_assigned = roles_result["assigned"]
            sync_log.roles_revoked = roles_result["revoked"]
            
            # Update status
            sync_log.status = "success"
            sync_log.completed_at = datetime.utcnow()
            sync_log.duration_seconds = (
                sync_log.completed_at - sync_log.started_at
            ).total_seconds()
            
            # Update config last sync time
            self.ad_config.last_sync_at = datetime.utcnow()
            
            await session.commit()
            
        except Exception as e:
            sync_log.status = "failed"
            sync_log.error_message = str(e)
            sync_log.completed_at = datetime.utcnow()
            await session.commit()
            raise
        
        return sync_log
    
    async def sync_users(self, session: AsyncSession) -> Dict[str, int]:
        """
        Sync users from Azure AD.
        
        Args:
            session: Database session
            
        Returns:
            Dictionary with sync statistics
        """
        stats = {"synced": 0, "added": 0, "updated": 0, "removed": 0}
        
        # Fetch users from Azure AD
        azure_users = await self._fetch_azure_users()
        
        # Get existing users
        result = await session.execute(
            select(AzureADUser).where(
                AzureADUser.ad_config_id == self.ad_config.id
            )
        )
        existing_users = {user.azure_user_id: user for user in result.scalars().all()}
        
        # Track synced user IDs
        synced_user_ids = set()
        
        # Process each Azure AD user
        for azure_user in azure_users:
            azure_user_id = azure_user["id"]
            synced_user_ids.add(azure_user_id)
            
            if azure_user_id in existing_users:
                # Update existing user
                user = existing_users[azure_user_id]
                user.user_principal_name = azure_user.get("userPrincipalName", "")
                user.email = azure_user.get("mail") or azure_user.get("userPrincipalName", "")
                user.display_name = azure_user.get("displayName", "")
                user.given_name = azure_user.get("givenName")
                user.surname = azure_user.get("surname")
                user.job_title = azure_user.get("jobTitle")
                user.department = azure_user.get("department")
                user.account_enabled = azure_user.get("accountEnabled", True)
                user.azure_data = azure_user
                user.last_synced_at = datetime.utcnow()
                stats["updated"] += 1
            else:
                # Add new user
                user = AzureADUser(
                    ad_config_id=self.ad_config.id,
                    azure_user_id=azure_user_id,
                    user_principal_name=azure_user.get("userPrincipalName", ""),
                    email=azure_user.get("mail") or azure_user.get("userPrincipalName", ""),
                    display_name=azure_user.get("displayName", ""),
                    given_name=azure_user.get("givenName"),
                    surname=azure_user.get("surname"),
                    job_title=azure_user.get("jobTitle"),
                    department=azure_user.get("department"),
                    account_enabled=azure_user.get("accountEnabled", True),
                    azure_data=azure_user,
                    last_synced_at=datetime.utcnow()
                )
                session.add(user)
                stats["added"] += 1
            
            stats["synced"] += 1
        
        # Mark removed users as inactive
        for azure_user_id, user in existing_users.items():
            if azure_user_id not in synced_user_ids:
                user.is_active = False
                user.account_enabled = False
                stats["removed"] += 1
        
        await session.flush()
        return stats
    
    async def sync_groups(self, session: AsyncSession) -> Dict[str, int]:
        """
        Sync groups from Azure AD.
        
        Args:
            session: Database session
            
        Returns:
            Dictionary with sync statistics
        """
        stats = {"synced": 0, "added": 0, "updated": 0, "removed": 0}
        
        # Fetch groups from Azure AD
        azure_groups = await self._fetch_azure_groups()
        
        # Get existing groups
        result = await session.execute(
            select(AzureADGroup).where(
                AzureADGroup.ad_config_id == self.ad_config.id
            )
        )
        existing_groups = {group.azure_group_id: group for group in result.scalars().all()}
        
        # Track synced group IDs
        synced_group_ids = set()
        
        # Process each Azure AD group
        for azure_group in azure_groups:
            azure_group_id = azure_group["id"]
            synced_group_ids.add(azure_group_id)
            
            # Fetch group members
            members = await self._fetch_group_members(azure_group_id)
            member_ids = {"members": [m["id"] for m in members]}
            
            if azure_group_id in existing_groups:
                # Update existing group
                group = existing_groups[azure_group_id]
                group.display_name = azure_group.get("displayName", "")
                group.description = azure_group.get("description")
                group.mail = azure_group.get("mail")
                group.mail_enabled = azure_group.get("mailEnabled", False)
                group.security_enabled = azure_group.get("securityEnabled", True)
                group.member_ids = member_ids
                group.azure_data = azure_group
                group.last_synced_at = datetime.utcnow()
                stats["updated"] += 1
            else:
                # Add new group
                group = AzureADGroup(
                    ad_config_id=self.ad_config.id,
                    azure_group_id=azure_group_id,
                    display_name=azure_group.get("displayName", ""),
                    description=azure_group.get("description"),
                    mail=azure_group.get("mail"),
                    mail_enabled=azure_group.get("mailEnabled", False),
                    security_enabled=azure_group.get("securityEnabled", True),
                    member_ids=member_ids,
                    azure_data=azure_group,
                    last_synced_at=datetime.utcnow()
                )
                session.add(group)
                stats["added"] += 1
            
            stats["synced"] += 1
        
        # Remove groups that no longer exist
        for azure_group_id, group in existing_groups.items():
            if azure_group_id not in synced_group_ids:
                await session.delete(group)
                stats["removed"] += 1
        
        await session.flush()
        return stats
    
    async def sync_role_assignments(self, session: AsyncSession) -> Dict[str, int]:
        """
        Sync role assignments based on group memberships.
        
        Args:
            session: Database session
            
        Returns:
            Dictionary with sync statistics
        """
        stats = {"assigned": 0, "revoked": 0}
        
        # Get all active role mappings
        result = await session.execute(
            select(RoleMapping).where(
                RoleMapping.ad_config_id == self.ad_config.id,
                RoleMapping.is_active == True
            )
        )
        role_mappings = result.scalars().all()
        
        # Get all users
        result = await session.execute(
            select(AzureADUser).where(
                AzureADUser.ad_config_id == self.ad_config.id,
                AzureADUser.is_active == True
            )
        )
        users = result.scalars().all()
        
        # Get all groups
        result = await session.execute(
            select(AzureADGroup).where(
                AzureADGroup.ad_config_id == self.ad_config.id
            )
        )
        groups = {group.id: group for group in result.scalars().all()}
        
        # Process role assignments
        for mapping in role_mappings:
            if not mapping.auto_provision:
                continue
            
            group = groups.get(mapping.azure_group_id)
            if not group or not group.member_ids:
                continue
            
            member_ids = group.member_ids.get("members", [])
            
            # Assign roles to group members
            for user in users:
                if user.azure_user_id in member_ids:
                    # User should have this role
                    # Here you would call the analytics_models API to assign the role
                    # For now, we'll just track the statistic
                    stats["assigned"] += 1
                else:
                    # User should not have this role
                    if mapping.auto_deprovision:
                        # Here you would call the analytics_models API to revoke the role
                        stats["revoked"] += 1
        
        return stats
    
    async def _fetch_azure_users(self) -> List[Dict[str, Any]]:
        """Fetch all users from Azure AD."""
        users = []
        url = f"{self.graph_api_base}/users"
        
        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                
                users.extend(data.get("value", []))
                url = data.get("@odata.nextLink")  # Pagination
        
        return users
    
    async def _fetch_azure_groups(self) -> List[Dict[str, Any]]:
        """Fetch all groups from Azure AD."""
        groups = []
        url = f"{self.graph_api_base}/groups"
        
        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                
                groups.extend(data.get("value", []))
                url = data.get("@odata.nextLink")  # Pagination
        
        return groups
    
    async def _fetch_group_members(self, group_id: str) -> List[Dict[str, Any]]:
        """Fetch members of a specific group."""
        members = []
        url = f"{self.graph_api_base}/groups/{group_id}/members"
        
        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                
                members.extend(data.get("value", []))
                url = data.get("@odata.nextLink")  # Pagination
        
        return members


async def sync_users(
    ad_config: AzureADConfig,
    access_token: str,
    session: AsyncSession
) -> Dict[str, int]:
    """
    Sync users from Azure AD.
    
    Args:
        ad_config: Azure AD configuration
        access_token: Valid access token
        session: Database session
        
    Returns:
        Sync statistics
    """
    sync_service = AzureADSyncService(ad_config, access_token)
    return await sync_service.sync_users(session)


async def sync_groups(
    ad_config: AzureADConfig,
    access_token: str,
    session: AsyncSession
) -> Dict[str, int]:
    """
    Sync groups from Azure AD.
    
    Args:
        ad_config: Azure AD configuration
        access_token: Valid access token
        session: Database session
        
    Returns:
        Sync statistics
    """
    sync_service = AzureADSyncService(ad_config, access_token)
    return await sync_service.sync_groups(session)


async def sync_role_mappings(
    ad_config: AzureADConfig,
    access_token: str,
    session: AsyncSession
) -> Dict[str, int]:
    """
    Sync role assignments based on group memberships.
    
    Args:
        ad_config: Azure AD configuration
        access_token: Valid access token
        session: Database session
        
    Returns:
        Sync statistics
    """
    sync_service = AzureADSyncService(ad_config, access_token)
    return await sync_service.sync_role_assignments(session)
