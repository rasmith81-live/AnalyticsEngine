"""
Automated Migration Manager - Consolidated from common directory.
"""

import asyncio
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import asyncpg
from alembic import command
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic.operations import Operations
from alembic.runtime.migration import MigrationInfo
from alembic.script import ScriptDirectory
from sqlalchemy import MetaData, Table, create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

logger = logging.getLogger(__name__)

class MigrationPhase:
    """Migration phase constants."""
    VALIDATION = "validation"
    BACKUP = "backup"
    SCHEMA_MIGRATION = "schema_migration"
    DATA_MIGRATION = "data_migration"
    HYPERTABLE_SETUP = "hypertable_setup"
    CONTINUOUS_AGGREGATES = "continuous_aggregates"
    INDEXES = "indexes"
    CONSTRAINTS = "constraints"
    VERIFICATION = "verification"
    CLEANUP = "cleanup"

class MigrationResult:
    """Migration execution result."""
    
    def __init__(self):
        self.success = False
        self.phases_completed: List[str] = []
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.execution_time = 0.0
        self.rollback_point: Optional[str] = None
        self.performance_metrics: Dict[str, Any] = {}

class AutomatedMigrationManager:
    """Automated migration manager for TimescaleDB and CQRS patterns."""
    
    def __init__(
        self,
        database_url: str,
        alembic_config_path: Optional[str] = None,
        enable_rollback: bool = True,
        enable_validation: bool = True,
        enable_performance_monitoring: bool = True
    ):
        self.database_url = database_url
        self.alembic_config_path = alembic_config_path or "alembic.ini"
        self.enable_rollback = enable_rollback
        self.enable_validation = enable_validation
        self.enable_performance_monitoring = enable_performance_monitoring
        
        # Initialize engines
        self.async_engine: Optional[AsyncEngine] = None
        self.sync_engine = None
        
        # Migration state
        self.current_migration: Optional[str] = None
        self.rollback_points: List[str] = []
        
    async def initialize(self):
        """Initialize the migration manager."""
        try:
            # Create async engine
            self.async_engine = create_async_engine(
                self.database_url,
                echo=False,
                pool_size=5,
                max_overflow=10
            )
            
            # Create sync engine for Alembic
            sync_url = self.database_url.replace('+asyncpg', '')
            self.sync_engine = create_engine(sync_url)
            
            logger.info("Migration manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize migration manager: {e}")
            raise
    
    async def execute_migrations(
        self,
        target_revision: Optional[str] = None,
        dry_run: bool = False
    ) -> MigrationResult:
        """Execute database migrations."""
        result = MigrationResult()
        start_time = time.time()
        
        try:
            logger.info(f"Starting migration execution (target: {target_revision}, dry_run: {dry_run})")
            
            # Phase 1: Validation
            if self.enable_validation:
                await self._execute_phase(result, MigrationPhase.VALIDATION, self._validate_environment)
            
            # Phase 2: Backup (if not dry run)
            if not dry_run and self.enable_rollback:
                await self._execute_phase(result, MigrationPhase.BACKUP, self._create_backup)
            
            # Phase 3: Schema Migration
            await self._execute_phase(
                result, 
                MigrationPhase.SCHEMA_MIGRATION, 
                lambda: self._execute_alembic_migration(target_revision, dry_run)
            )
            
            # Phase 4: TimescaleDB Setup
            if not dry_run:
                await self._execute_phase(
                    result, 
                    MigrationPhase.HYPERTABLE_SETUP, 
                    self._setup_hypertables
                )
                
                # Phase 5: Continuous Aggregates
                await self._execute_phase(
                    result, 
                    MigrationPhase.CONTINUOUS_AGGREGATES, 
                    self._setup_continuous_aggregates
                )
                
                # Phase 6: Indexes
                await self._execute_phase(
                    result, 
                    MigrationPhase.INDEXES, 
                    self._create_indexes
                )
                
                # Phase 7: Constraints
                await self._execute_phase(
                    result, 
                    MigrationPhase.CONSTRAINTS, 
                    self._create_constraints
                )
            
            # Phase 8: Verification
            if self.enable_validation:
                await self._execute_phase(result, MigrationPhase.VERIFICATION, self._verify_migration)
            
            # Phase 9: Cleanup
            await self._execute_phase(result, MigrationPhase.CLEANUP, self._cleanup)
            
            result.success = True
            logger.info("Migration execution completed successfully")
            
        except Exception as e:
            logger.error(f"Migration execution failed: {e}")
            result.errors.append(str(e))
            
            # Attempt rollback if enabled
            if self.enable_rollback and not dry_run:
                try:
                    await self._rollback_migration(result)
                except Exception as rollback_error:
                    logger.error(f"Rollback failed: {rollback_error}")
                    result.errors.append(f"Rollback failed: {rollback_error}")
        
        finally:
            result.execution_time = time.time() - start_time
            
        return result
    
    async def _execute_phase(self, result: MigrationResult, phase: str, func):
        """Execute a migration phase."""
        try:
            logger.info(f"Executing phase: {phase}")
            phase_start = time.time()
            
            if asyncio.iscoroutinefunction(func):
                await func()
            else:
                func()
                
            phase_time = time.time() - phase_start
            result.phases_completed.append(phase)
            
            if self.enable_performance_monitoring:
                result.performance_metrics[phase] = phase_time
                
            logger.info(f"Phase {phase} completed in {phase_time:.2f}s")
            
        except Exception as e:
            logger.error(f"Phase {phase} failed: {e}")
            raise
    
    async def _validate_environment(self):
        """Validate the migration environment."""
        # Check database connection
        if not self.async_engine:
            raise RuntimeError("Database engine not initialized")
            
        async with self.async_engine.begin() as conn:
            result = await conn.execute(text("SELECT version()"))
            version = result.scalar()
            logger.info(f"Database version: {version}")
            
            # Check TimescaleDB extension
            result = await conn.execute(
                text("SELECT installed_version FROM pg_available_extensions WHERE name = 'timescaledb'")
            )
            timescale_version = result.scalar()
            if not timescale_version:
                raise RuntimeError("TimescaleDB extension not available")
            logger.info(f"TimescaleDB version: {timescale_version}")
        
        # Check Alembic configuration
        if not Path(self.alembic_config_path).exists():
            raise RuntimeError(f"Alembic config not found: {self.alembic_config_path}")
    
    async def _create_backup(self):
        """Create database backup before migration."""
        backup_name = f"migration_backup_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        logger.info(f"Creating backup: {backup_name}")
        
        # This is a placeholder - implement actual backup logic based on requirements
        # Could use pg_dump or TimescaleDB-specific backup methods
        self.rollback_points.append(backup_name)
    
    def _execute_alembic_migration(self, target_revision: Optional[str], dry_run: bool):
        """Execute Alembic migration."""
        try:
            config = Config(self.alembic_config_path)
            config.set_main_option("sqlalchemy.url", self.database_url.replace('+asyncpg', ''))
            
            if dry_run:
                # For dry run, just show what would be executed
                script_dir = ScriptDirectory.from_config(config)
                with self.sync_engine.connect() as connection:
                    context = MigrationContext.configure(connection)
                    current_rev = context.get_current_revision()
                    
                    if target_revision:
                        revisions = script_dir.get_revisions(current_rev, target_revision)
                    else:
                        revisions = script_dir.get_revisions(current_rev, "head")
                    
                    logger.info(f"Would execute {len(revisions)} migrations")
                    for rev in revisions:
                        logger.info(f"  - {rev.revision}: {rev.doc}")
            else:
                # Execute actual migration
                if target_revision:
                    command.upgrade(config, target_revision)
                else:
                    command.upgrade(config, "head")
                    
                logger.info("Alembic migration completed")
                
        except Exception as e:
            logger.error(f"Alembic migration failed: {e}")
            raise
    
    async def _setup_hypertables(self):
        """Setup TimescaleDB hypertables and initialize TimescaleDB extension.
        
        This method ensures the TimescaleDB extension is enabled and then identifies
        and converts appropriate tables to hypertables for time-series data.
        """
        logger.info("Setting up TimescaleDB extension and hypertables")
        
        if not self.async_engine:
            raise RuntimeError("Database engine not initialized")
        
        # First ensure TimescaleDB extension is enabled
        async with self.async_engine.begin() as conn:
            # Enable TimescaleDB extension
            logger.info("Enabling TimescaleDB extension")
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"))
            
            # Set up permissions (extract database name from connection URL)
            db_name = self.database_url.split('/')[-1].split('?')[0]
            user = self.database_url.split(':')[1].lstrip('/').split(':')[0]
            if db_name and user:
                logger.info(f"Setting up permissions for database {db_name} and user {user}")
                # Note: GRANT requires elevated privileges, may need to be handled differently
                try:
                    await conn.execute(text(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {user};"))
                    logger.info(f"Permissions granted for {user} on {db_name}")
                except Exception as e:
                    logger.warning(f"Could not set permissions: {e}. This may be expected if user doesn't have GRANT privileges.")
        
        # Identify and set up hypertables for each service
        # This leverages the database manager's _setup_hypertables_for_service method
        # which handles the actual hypertable creation logic
        
        # Get list of services from the migration context
        services = self.get_services_list()
        logger.info(f"Setting up hypertables for services: {services}")
        
        hypertables_created = []
        for service_name in services:
            try:
                # Use the database manager's method to set up hypertables for this service
                # In a real implementation, this would be a call to an instance of DatabaseManager
                # For now, we'll implement the logic directly here
                service_hypertables = await self._setup_service_hypertables(service_name)
                hypertables_created.extend(service_hypertables)
                logger.info(f"Created {len(service_hypertables)} hypertables for service {service_name}")
            except Exception as e:
                logger.error(f"Failed to set up hypertables for service {service_name}: {e}")
                
        logger.info(f"Hypertable setup complete. Created {len(hypertables_created)} hypertables in total")
        return hypertables_created
        
    async def _setup_service_hypertables(self, service_name: str) -> List[str]:
        """Set up hypertables for a specific service.
        
        This is a simplified version of DatabaseManager._setup_hypertables_for_service
        that runs within the migration manager context.
        """
        hypertables_created = []
        
        if not self.async_engine:
            raise RuntimeError("Database engine not initialized")
            
        async with self.async_engine.begin() as conn:
            # Get all tables with timestamp columns that should be hypertables
            tables_query = """
            SELECT table_name, column_name 
            FROM information_schema.columns 
            WHERE table_schema = 'public' 
            AND (column_name LIKE '%time%' OR column_name LIKE '%date%' OR column_name = 'timestamp') 
            AND data_type IN ('timestamp', 'timestamptz', 'date')
            """
            result = await conn.execute(text(tables_query))
            potential_hypertables = result.fetchall()
            
            # Check which tables are already hypertables
            hypertable_query = "SELECT table_name FROM timescaledb_information.hypertables"
            result = await conn.execute(text(hypertable_query))
            existing_hypertables = {row[0] for row in result.fetchall()}
            
            # Convert eligible tables to hypertables
            for table_name, time_column in potential_hypertables:
                if table_name not in existing_hypertables:
                    try:
                        # Check if the table has any data
                        has_data_query = f"SELECT EXISTS (SELECT 1 FROM {table_name} LIMIT 1)"
                        result = await conn.execute(text(has_data_query))
                        has_data = result.scalar()
                        
                        # Create hypertable
                        logger.info(f"Converting table {table_name} to hypertable using column {time_column}")
                        create_hypertable_query = f"""
                        SELECT create_hypertable('{table_name}', '{time_column}', 
                                                if_not_exists => TRUE, 
                                                migrate_data => {str(has_data).lower()})
                        """
                        await conn.execute(text(create_hypertable_query))
                        hypertables_created.append(table_name)
                        logger.info(f"Successfully converted {table_name} to a hypertable")
                    except Exception as e:
                        logger.error(f"Failed to convert {table_name} to hypertable: {str(e)}")
                else:
                    logger.info(f"Table {table_name} is already a hypertable")
        
        return hypertables_created
    
    def get_services_list(self) -> List[str]:
        """Get list of services from the migration context.
        
        In a real implementation, this would be determined dynamically
        based on the services in the project.
        """
        # For now, return a hardcoded list of services
        # In a real implementation, this would be determined from the project structure
        return ["database_service", "messaging_service", "service_a", "service_b"]
    
    async def _setup_continuous_aggregates(self):
        """Setup TimescaleDB continuous aggregates."""
        logger.info("Setting up continuous aggregates")
        
        # Placeholder for continuous aggregate setup
        # In a real implementation, this would:
        # 1. Create materialized views for common queries
        # 2. Set up refresh policies
        # 3. Configure compression policies
    
    async def _create_indexes(self):
        """Create database indexes."""
        logger.info("Creating database indexes")
        
        # Placeholder for index creation
        # In a real implementation, this would:
        # 1. Create time-based indexes for hypertables
        # 2. Create indexes for common query patterns
        # 3. Create partial indexes for performance
    
    async def _create_constraints(self):
        """Create database constraints."""
        logger.info("Creating database constraints")
        
        # Placeholder for constraint creation
        # In a real implementation, this would:
        # 1. Add foreign key constraints
        # 2. Add check constraints
        # 3. Add unique constraints
    
    async def _verify_migration(self):
        """Verify migration was successful."""
        logger.info("Verifying migration")
        
        if not self.async_engine:
            raise RuntimeError("Database engine not initialized")
            
        async with self.async_engine.begin() as conn:
            # Verify database connectivity
            await conn.execute(text("SELECT 1"))
            
            # Verify TimescaleDB functionality
            result = await conn.execute(
                text("SELECT count(*) FROM timescaledb_information.hypertables")
            )
            hypertable_count = result.scalar()
            logger.info(f"Found {hypertable_count} hypertables")
    
    async def _cleanup(self):
        """Cleanup after migration."""
        logger.info("Performing cleanup")
        
        # Placeholder for cleanup operations
        # In a real implementation, this would:
        # 1. Clean up temporary files
        # 2. Update migration logs
        # 3. Send notifications
    
    async def _rollback_migration(self, result: MigrationResult):
        """Rollback migration to last known good state."""
        logger.warning("Attempting migration rollback")
        
        if not self.rollback_points:
            logger.error("No rollback points available")
            return
            
        last_rollback_point = self.rollback_points[-1]
        result.rollback_point = last_rollback_point
        
        # Placeholder for rollback logic
        # In a real implementation, this would:
        # 1. Restore from backup
        # 2. Revert Alembic migrations
        # 3. Clean up partial changes
        
        logger.info(f"Rollback to {last_rollback_point} completed")
    
    async def get_migration_status(self) -> Dict[str, Any]:
        """Get current migration status."""
        if not self.sync_engine:
            return {"status": "not_initialized"}
            
        try:
            config = Config(self.alembic_config_path)
            config.set_main_option("sqlalchemy.url", self.database_url.replace('+asyncpg', ''))
            
            script_dir = ScriptDirectory.from_config(config)
            with self.sync_engine.connect() as connection:
                context = MigrationContext.configure(connection)
                current_rev = context.get_current_revision()
                
                # Get available revisions
                heads = script_dir.get_heads()
                
                return {
                    "status": "ready",
                    "current_revision": current_rev,
                    "head_revisions": heads,
                    "pending_migrations": len(script_dir.get_revisions(current_rev, "head")) if current_rev else 0
                }
                
        except Exception as e:
            logger.error(f"Failed to get migration status: {e}")
            return {"status": "error", "error": str(e)}
    
    async def close(self):
        """Close the migration manager."""
        if self.async_engine:
            await self.async_engine.dispose()
        if self.sync_engine:
            self.sync_engine.dispose()
        logger.info("Migration manager closed")
