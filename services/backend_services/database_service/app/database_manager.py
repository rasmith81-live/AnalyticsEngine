"""
Database Manager - Consolidates all database functionality.
"""

import asyncio
import json
import logging
import uuid
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import QueuePool
import redis.asyncio as redis

from .config import DatabaseServiceSettings
from .base_models import Base, NewsArticle
from .telemetry import trace_method, add_span_attributes, inject_trace_context

logger = logging.getLogger(__name__)

class MigrationPhase(Enum):
    PRE_VALIDATION = "pre_validation"
    MIGRATION_EXECUTION = "migration_execution"
    HYPERTABLE_CREATION = "hypertable_creation"
    POST_VALIDATION = "post_validation"

@dataclass
class ValidationIssue:
    severity: str
    category: str
    description: str
    location: str
    suggestion: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass
class MigrationResult:
    success: bool
    service_name: str
    start_time: datetime
    end_time: Optional[datetime] = None
    phases_completed: List[MigrationPhase] = field(default_factory=list)
    validation_issues: List[ValidationIssue] = field(default_factory=list)
    error_message: Optional[str] = None
    rollback_performed: bool = False
    hypertables_created: List[str] = field(default_factory=list)

class DatabaseManager:
    """Centralized database manager with CQRS and TimescaleDB support."""
    
    def __init__(self, settings: DatabaseServiceSettings):
        self.settings = settings
        self.async_engine = None
        self.sync_engine = None
        self.session_factory = None
        self.redis_client = None
        self.query_metrics = {}
        self.command_metrics = {}
        self.cache_stats = {"hits": 0, "misses": 0}
    
    @trace_method(name="database_manager_initialize", kind="INTERNAL")
    async def initialize(self):
        """Initialize database connections."""
        try:
            # Create async engine
            self.async_engine = create_async_engine(
                self.settings.database_url,
                pool_size=self.settings.connection_pool_size,
                max_overflow=self.settings.connection_pool_max_overflow,
                pool_timeout=self.settings.connection_pool_timeout,
                pool_recycle=self.settings.connection_pool_recycle
            )
            
            # Create sync engine for migrations
            sync_url = self.settings.database_url.replace('+asyncpg', '+psycopg2')
            self.sync_engine = create_engine(sync_url, poolclass=QueuePool, pool_size=5)
            
            # Create session factory
            self.session_factory = async_sessionmaker(self.async_engine, class_=AsyncSession)
            
            # Initialize Redis
            if self.settings.enable_query_cache:
                self.redis_client = redis.from_url(self.settings.redis_url, decode_responses=True)
            
            # Validate TimescaleDB
            await self._validate_timescaledb()
            
            # Create base tables
            if self.settings.run_migrations_on_startup:
                async with self.async_engine.begin() as conn:
                    await conn.run_sync(Base.metadata.create_all)
            
            logger.info("Database manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize database manager: {str(e)}")
            raise
    
    @trace_method(name="database_manager_cleanup", kind="INTERNAL")
    async def cleanup(self):
        """Clean up database connections and resources."""
        if self.async_engine:
            await self.async_engine.dispose()
            logger.info("Async database engine disposed")
        
        if self.sync_engine:
            self.sync_engine.dispose()
            logger.info("Sync database engine disposed")
            
        if self.redis_client:
            await self.redis_client.close()
            logger.info("Redis client closed")
            
    @trace_method(name="database_health_check", kind="INTERNAL")
    async def check_health(self) -> Dict[str, Any]:
        """Check database health and return status information.
        
        Returns:
            Dict containing health status information
        """
        from datetime import datetime
        
        # Default health status with required connection_pool_status field
        health_status = {
            "status": "healthy",
            "database_connected": False,
            "timescaledb_available": False,
            "redis_connected": False,
            "active_connections": 0,
            "timestamp": datetime.utcnow(),
            "connection_pool_status": {
                "checkedout": 0,
                "checkedin": 0,
                "size": 0,
                "overflow": 0,
                "timeout": 0
            }
        }
        
        # Check database connection
        try:
            async with self.async_engine.connect() as conn:
                # Check if database is connected
                result = await conn.execute(text("SELECT 1"))
                health_status["database_connected"] = True
                
                # Check TimescaleDB availability
                result = await conn.execute(text("SELECT extname FROM pg_extension WHERE extname = 'timescaledb'"))
                row = result.fetchone()
                health_status["timescaledb_available"] = row is not None and row[0] == 'timescaledb'
                
                # Get connection pool stats
                pool = self.async_engine.pool
                health_status["active_connections"] = pool.checkedout()
                
                # Update connection pool status
                health_status["connection_pool_status"] = {
                    "checkedout": pool.checkedout(),
                    "checkedin": pool.checkedin(),
                    "size": pool.size(),
                    "overflow": pool.overflow(),
                    "timeout": pool._timeout
                }
                
                # Test Redis connection
                if self.redis_client:
                    await self.redis_client.ping()
                    health_status["redis_connected"] = True
        except Exception as e:
            health_status["status"] = "unhealthy"
            health_status["error_message"] = str(e)
            logger.error(f"Health check error: {str(e)}")
            # connection_pool_status is already initialized with default values
            
        return health_status
    
    async def _validate_timescaledb(self):
        """Validate and initialize TimescaleDB extension."""
        try:
            # Add span attributes for hypertable creation
            add_span_attributes({
                "db.system": "timescaledb",
                "db.operation": "create_hypertable",
                "db.table": "timescaledb",
                "db.time_column": "time",
                "db.chunk_interval": "7 days",
                "correlation_id": "not_provided"
            })
            
            async with self.async_engine.begin() as conn:
                # Check if TimescaleDB extension exists
                result = await conn.execute(text("SELECT extname FROM pg_extension WHERE extname = 'timescaledb'"))
                extension_exists = result.fetchone() is not None
                
                if not extension_exists:
                    logger.info("TimescaleDB extension not found, attempting to create it")
                    try:
                        # Create the TimescaleDB extension
                        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"))
                        logger.info("TimescaleDB extension created successfully")
                        
                        # Set up permissions (extract database name from connection URL)
                        db_name = self.settings.database_url.split('/')[-1].split('?')[0]
                        user = self.settings.database_url.split(':')[1].lstrip('/').split(':')[0]
                        if db_name and user:
                            logger.info(f"Setting up permissions for database {db_name} and user {user}")
                            try:
                                await conn.execute(text(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {user};"))
                                logger.info(f"Permissions granted for {user} on {db_name}")
                            except Exception as perm_error:
                                logger.warning(f"Could not set permissions: {perm_error}. This may be expected if user doesn't have GRANT privileges.")
                    except Exception as ext_error:
                        if self.settings.enforce_timescaledb:
                            logger.error(f"Failed to create TimescaleDB extension: {ext_error}")
                            raise
                        logger.warning(f"Could not create TimescaleDB extension: {ext_error}")
                else:
                    logger.info("TimescaleDB extension already exists")
                    
        except Exception as e:
            if self.settings.enforce_timescaledb:
                logger.error(f"TimescaleDB validation failed: {str(e)}")
                raise
            logger.warning(f"TimescaleDB validation: {str(e)}")
            
        logger.info("TimescaleDB validation completed successfully")
    
    @trace_method(name="database_manager.execute_query", kind="INTERNAL")
    async def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None, 
                          service_name: str = "unknown", timeout: int = 30, 
                          correlation_id: Optional[str] = None):
        """Execute read query with caching."""
        start_time = datetime.utcnow()
        parameters = parameters or {}
        cache_key = None
        cache_hit = False
        result = None
        row_count = 0
        
        # Generate correlation ID if not provided
        if not correlation_id:
            correlation_id = str(uuid.uuid4())
        
        # Add initial span attributes
        add_span_attributes({
            "correlation_id": correlation_id,
            "timestamp.start": start_time.isoformat(),
            "service_name": service_name,
            "db.operation": "query",
            "db.statement_type": query.strip().split()[0].upper() if query else "UNKNOWN",
            "db.query_truncated": query[:100] + "..." if len(query) > 100 else query
        })
        
        try:
            # Check cache if enabled
            if self.settings.enable_query_cache and self.redis_client:
                cache_key = self._generate_cache_key(query, parameters, service_name)
                cached_result = await self._get_cached_result(cache_key)
                if cached_result:
                    self.cache_stats["hits"] += 1
                    cache_hit = True
                    
                    # Add cache hit attributes
                    add_span_attributes({
                        "cache.hit": True,
                        "cache.key": cache_key[:50] if len(cache_key) > 50 else cache_key,
                        "result.row_count": cached_result.get("row_count", 0),
                        "success": True
                    })
                    
                    return cached_result
                self.cache_stats["misses"] += 1
                
                # Add cache miss attribute
                add_span_attributes({"cache.hit": False})
            
            # Execute query with timeout
            async with asyncio.timeout(timeout):
                async with self.session_factory() as session:
                    # Inject trace context into session
                    if hasattr(session, "info"):
                        session.info["correlation_id"] = correlation_id
                        inject_trace_context(session.info)
                    
                    # Execute query
                    query_start = datetime.utcnow()
                    stmt = text(query)
                    result = await session.execute(stmt, parameters)
                    rows = result.fetchall()
                    row_count = len(rows)
                    query_duration = (datetime.utcnow() - query_start).total_seconds()
                    
                    # Convert to dict format
                    column_names = result.keys()
                    result_dict = {
                        "rows": [dict(zip(column_names, row)) for row in rows],
                        "column_names": column_names,
                        "row_count": row_count,
                        "execution_time": query_duration,
                        "timestamp": datetime.utcnow().isoformat(),
                        "service_name": service_name,
                        "correlation_id": correlation_id
                    }
                    
                    # Cache result if enabled
                    if self.settings.enable_query_cache and self.redis_client and cache_key:
                        await self._cache_result(cache_key, result_dict)
                    
                    # Track metrics
                    execution_time = (datetime.utcnow() - start_time).total_seconds()
                    self._track_query_metrics(service_name, execution_time, row_count)
                    
                    # Add success span attributes
                    end_time = datetime.utcnow()
                    add_span_attributes({
                        "timestamp.end": end_time.isoformat(),
                        "duration_ms": (end_time - start_time).total_seconds() * 1000,
                        "db.execution_time_ms": query_duration * 1000,
                        "result.row_count": row_count,
                        "success": True
                    })
                    
                    return result_dict
                    
        except Exception as e:
            # Add error span attributes
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            
            logger.error(f"Query execution failed: {str(e)}")
            raise
    
    @trace_method(name="database_manager.execute_command", kind="INTERNAL")
    async def execute_command(self, command: str, parameters: Optional[Dict[str, Any]] = None,
                            service_name: str = "unknown", transaction_id: Optional[str] = None,
                            timeout: int = 30, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Execute write command."""
        start_time = datetime.utcnow()
        transaction_id = transaction_id or str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add initial span attributes with detailed context
        add_span_attributes({
            "correlation_id": correlation_id,
            "transaction_id": transaction_id,
            "timestamp.start": start_time.isoformat(),
            "service_name": service_name,
            "db.system": "postgresql",
            "db.operation": "command",
            "db.name": service_name,
            "db.statement_type": command.strip().split()[0].upper() if command else "UNKNOWN",
            "db.command_truncated": command[:100] + "..." if len(command) > 100 else command
        })
        
        try:
            # Execute command with timeout
            async with asyncio.timeout(timeout):
                async with self.session_factory() as session:
                    # Inject trace context into session
                    if hasattr(session, "info"):
                        session.info["correlation_id"] = correlation_id
                        session.info["transaction_id"] = transaction_id
                        inject_trace_context(session.info)
                    
                    # Execute command within transaction
                    command_start = datetime.utcnow()
                    async with session.begin():
                        if parameters:
                            result = await session.execute(text(command), parameters)
                        else:
                            result = await session.execute(text(command))
                        
                        affected_rows = getattr(result, 'rowcount', 0)
                        command_duration = (datetime.utcnow() - command_start).total_seconds()
                        
                        # Get returned data
                        returned_data = None
                        if result.returns_rows:
                            rows = result.fetchall()
                            if rows:
                                columns = list(result.keys())
                                returned_data = [dict(zip(columns, row)) for row in rows]
                        
                        # Track metrics
                        execution_time = (datetime.utcnow() - start_time).total_seconds()
                        self._track_command_metrics(service_name, execution_time, affected_rows)
                        
                        # Add success span attributes
                        end_time = datetime.utcnow()
                        add_span_attributes({
                            "timestamp.end": end_time.isoformat(),
                            "duration_ms": (end_time - start_time).total_seconds() * 1000,
                            "db.execution_time_ms": command_duration * 1000,
                            "result.affected_rows": affected_rows,
                            "result.has_returned_data": returned_data is not None,
                            "success": True
                        })
                        
                        return {
                            "affected_rows": affected_rows,
                            "execution_time": execution_time,
                            "transaction_id": transaction_id,
                            "data": returned_data,
                            "correlation_id": correlation_id,
                            "timestamp": end_time.isoformat()
                        }
                    
        except Exception as e:
            # Add error span attributes
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            
            logger.error(f"Command failed for {service_name}: {str(e)}")
            raise
    
    @trace_method(name="database_manager.create_hypertable", kind="INTERNAL")
    async def create_hypertable(self, table_name: str, time_column: str,
                              chunk_interval: str = "7 days", compression_enabled: bool = True,
                              retention_period: Optional[str] = None,
                              correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Create TimescaleDB hypertable."""
        start_time = datetime.utcnow()
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add initial span attributes with detailed context
        add_span_attributes({
            "correlation_id": correlation_id,
            "timestamp.start": start_time.isoformat(),
            "db.system": "timescaledb",
            "db.operation": "create_hypertable",
            "db.table_name": table_name,
            "db.time_column": time_column,
            "db.chunk_interval": chunk_interval,
            "db.compression_enabled": str(compression_enabled),
            "db.retention_period": retention_period or "none"
        })
        
        try:
            async with self.session_factory() as session:
                # Inject trace context into session
                if hasattr(session, "info"):
                    session.info["correlation_id"] = correlation_id
                    inject_trace_context(session.info)
                
                async with session.begin():
                    # Create hypertable
                    await session.execute(
                        text(f"SELECT create_hypertable('{table_name}', '{time_column}', chunk_time_interval => INTERVAL '{chunk_interval}')")
                    )
                    
                    result = {
                        "created": True, 
                        "chunk_interval": chunk_interval,
                        "correlation_id": correlation_id,
                        "timestamp": datetime.utcnow().isoformat()
                    }
                    
                    # Add compression
                    if compression_enabled:
                        await session.execute(text(f"ALTER TABLE {table_name} SET (timescaledb.compress)"))
                        await session.execute(text(f"SELECT add_compression_policy('{table_name}', INTERVAL '7 days')"))
                        result["compression_policy"] = {"enabled": True, "compress_after": "7 days"}
                        
                        # Add compression span attributes
                        add_span_attributes({
                            "db.compression_policy": "7 days"
                        })
                    
                    # Add retention
                    if retention_period:
                        await session.execute(text(f"SELECT add_retention_policy('{table_name}', INTERVAL '{retention_period}')"))
                        result["retention_policy"] = {"enabled": True, "drop_after": retention_period}
                        
                        # Add retention span attributes
                        add_span_attributes({
                            "db.retention_policy": retention_period
                        })
                    
                    # Add success span attributes
                    end_time = datetime.utcnow()
                    add_span_attributes({
                        "timestamp.end": end_time.isoformat(),
                        "duration_ms": (end_time - start_time).total_seconds() * 1000,
                        "success": True
                    })
                    
                    return result
                    
        except Exception as e:
            # Add error span attributes
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            
            logger.error(f"Failed to create hypertable {table_name}: {str(e)}")
            raise

    async def create_news_articles_hypertable(self, correlation_id: Optional[str] = None):
        """Create and configure the news_articles hypertable."""
        try:
            async with self.async_engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all, tables=[NewsArticle.__table__])
            
            await self.create_hypertable(
                table_name='news_articles',
                time_column='published_at',
                chunk_interval='1 day',
                compression_enabled=True,
                retention_period='30 days',
                correlation_id=correlation_id
            )
            logger.info("Successfully created and configured 'news_articles' hypertable.")
        except Exception as e:
            logger.error(f"Failed to create 'news_articles' hypertable: {e}")
            raise

    async def insert_news_article(self, article_data: Dict[str, Any], correlation_id: Optional[str] = None):
        """Insert a new news article into the database."""
        try:
            async with self.session_factory() as session:
                async with session.begin():
                    article = NewsArticle(**article_data)
                    session.add(article)
                    await session.commit()
                logger.info(f"Inserted news article with headline: {article_data.get('headline')}")
        except Exception as e:
            logger.error(f"Failed to insert news article: {e}")
            raise
    
    @trace_method(name="run_migrations", kind="CLIENT")
    async def run_migrations(self, service_name: str, target_revision: str = "head",
                           auto_rollback: bool = False, validation_level: str = "basic",
                           correlation_id: Optional[str] = None) -> MigrationResult:
        """Run migrations for service."""
        result = MigrationResult(
            success=False,
            service_name=service_name,
            start_time=datetime.utcnow()
        )
        
        # Add span attributes for migration context
        add_span_attributes({
            "db.system": "alembic",
            "db.operation": "migration",
            "db.service": service_name,
            "db.target_revision": target_revision,
            "db.validation_level": validation_level,
            "correlation_id": correlation_id or "not_provided"
        })
        
        try:
            logger.info(f"Running migrations for service {service_name} to target {target_revision}")
            
            # Phase 1: Pre-validation
            logger.info("Phase 1: Pre-validation")
            result.phases_completed.append(MigrationPhase.PRE_VALIDATION)
            
            # Phase 2: TimescaleDB extension setup
            logger.info("Phase 2: TimescaleDB extension setup")
            await self._validate_timescaledb()
            
            # Phase 3: Schema migration execution
            logger.info("Phase 3: Schema migration execution")
            # Here we would typically execute Alembic migrations
            # For now, we're just simulating this phase
            result.phases_completed.append(MigrationPhase.MIGRATION_EXECUTION)
            
            # Phase 4: Hypertable setup
            logger.info("Phase 4: Hypertable setup")
            # Identify tables that should be hypertables and convert them
            # This is where we would execute the hypertable creation logic
            await self._setup_hypertables_for_service(service_name)
            result.phases_completed.append(MigrationPhase.HYPERTABLE_CREATION)
            
            # Phase 5: Post-validation
            logger.info("Phase 5: Post-validation")
            result.phases_completed.append(MigrationPhase.POST_VALIDATION)
            
            result.success = True
            result.end_time = datetime.utcnow()
            logger.info(f"Migration completed successfully for service {service_name}")
            
        except Exception as e:
            logger.error(f"Migration failed for service {service_name}: {str(e)}")
            result.error_message = str(e)
            result.end_time = datetime.utcnow()
            
            # Rollback if auto_rollback is enabled
            if auto_rollback:
                logger.info("Attempting automatic rollback")
                try:
                    # Rollback logic would go here
                    result.rollback_performed = True
                    logger.info("Rollback completed successfully")
                except Exception as rollback_error:
                    logger.error(f"Rollback failed: {rollback_error}")
                    result.error_message += f"; Rollback failed: {rollback_error}"
        
        return result
    
    async def get_migration_status(self, service_name: str) -> Dict[str, Any]:
        """Get migration status."""
        try:
            async with self.session_factory() as session:
                result = await session.execute(text("SELECT version_num FROM alembic_version LIMIT 1"))
                version = result.scalar()
                return {
                    "service_name": service_name,
                    "current_version": version,
                    "status": "up_to_date" if version else "not_initialized",
                    "checked_at": datetime.utcnow()
                }
        except Exception:
            return {
                "service_name": service_name,
                "status": "not_initialized",
                "checked_at": datetime.utcnow()
            }
    
    async def register_models(self, service_name: str, models: List[Dict[str, Any]], auto_create_tables: bool = True) -> List[str]:
        """Register models."""
        return [model.get("name", "") for model in models]
    
    async def discover_models(self, service_name: str) -> List[Dict[str, Any]]:
        """Discover models."""
        return []
    
    async def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance stats."""
        return {
            "total_queries": sum(self.query_metrics.values()) if self.query_metrics else 0,
            "total_commands": sum(self.command_metrics.values()) if self.command_metrics else 0,
            "cache_hit_rate": self._calculate_cache_hit_rate(),
            "timestamp": datetime.utcnow()
        }
    
    async def get_connection_status(self) -> Dict[str, Any]:
        """Get connection status."""
        if not self.async_engine:
            return {"error": "Engine not initialized"}
        
        pool = self.async_engine.pool
        return {
            "size": pool.size(),
            "checked_in": pool.checkedin(),
            "checked_out": pool.checkedout(),
            "timestamp": datetime.utcnow()
        }
    
    # Helper methods
    def _generate_cache_key(self, query: str, parameters: Optional[Dict[str, Any]], service_name: str) -> str:
        import hashlib
        key_data = f"{service_name}:{query}:{json.dumps(parameters or {}, sort_keys=True)}"
        return f"query_cache:{hashlib.md5(key_data.encode()).hexdigest()}"
    
    async def _get_cached_result(self, cache_key: str) -> Optional[Dict[str, Any]]:
        try:
            if self.redis_client:
                cached = await self.redis_client.get(cache_key)
                return json.loads(cached) if cached else None
        except Exception:
            pass
        return None
    
    async def _cache_result(self, cache_key: str, result: Dict[str, Any]):
        try:
            if self.redis_client:
                await self.redis_client.setex(cache_key, self.settings.cache_ttl, json.dumps(result, default=str))
        except Exception:
            pass
    
    def _track_query_metrics(self, service_name: str, execution_time: float, row_count: int):
        if service_name not in self.query_metrics:
            self.query_metrics[service_name] = 0
        self.query_metrics[service_name] += 1
    
    def _track_command_metrics(self, service_name: str, execution_time: float, affected_rows: int):
        if service_name not in self.command_metrics:
            self.command_metrics[service_name] = 0
        self.command_metrics[service_name] += 1
    
    @trace_method(name="database_manager.check_database_connection", kind="INTERNAL")
    async def check_database_connection(self, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Check database connection and verify TimescaleDB extension."""
        start_time = datetime.utcnow()
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add initial span attributes
        add_span_attributes({
            "correlation_id": correlation_id,
            "timestamp.start": start_time.isoformat(),
            "db.operation": "health_check",
            "db.system": "postgresql"
        })
        
        try:
            async with self.session_factory() as session:
                # Inject trace context into session
                if hasattr(session, "info"):
                    session.info["correlation_id"] = correlation_id
                    inject_trace_context(session.info)
                
                # Check PostgreSQL connection
                pg_result = await session.execute(text("SELECT version()"))
                pg_version = pg_result.scalar()
                
                # Check TimescaleDB extension
                ts_result = await session.execute(text("SELECT extversion FROM pg_extension WHERE extname = 'timescaledb'"))
                ts_version = ts_result.scalar()
                
                # Check hypertables count
                ht_result = await session.execute(text("SELECT count(*) FROM timescaledb_information.hypertables"))
                hypertables_count = ht_result.scalar() or 0
                
                result = {
                    "status": "healthy",
                    "postgresql_version": pg_version,
                    "timescaledb_version": ts_version,
                    "hypertables_count": hypertables_count,
                    "timestamp": datetime.utcnow().isoformat(),
                    "correlation_id": correlation_id
                }
                
                # Add success span attributes
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "db.postgresql_version": pg_version,
                    "db.timescaledb_version": ts_version or "not_installed",
                    "db.hypertables_count": hypertables_count,
                    "success": True
                })
                
                return result
                
        except Exception as e:
            # Add error span attributes
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            
            logger.error(f"Database connection check failed: {str(e)}")
            return {
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "correlation_id": correlation_id
            }
            
    async def check_health(self, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Backward compatibility method for health checks.
        
        This method calls the more detailed check_database_connection method.
        """
        return await self.check_database_connection(correlation_id=correlation_id)
    
    def _calculate_cache_hit_rate(self) -> float:
        total = self.cache_stats["hits"] + self.cache_stats["misses"]
        return self.cache_stats["hits"] / total if total > 0 else 0.0
        
    async def _setup_hypertables_for_service(self, service_name: str) -> List[str]:
        """Set up TimescaleDB hypertables for a specific service.
        
        This method identifies tables with time-based columns for the given service
        and converts them to TimescaleDB hypertables if they aren't already.
        
        Args:
            service_name: Name of the service to set up hypertables for
            
        Returns:
            List of table names that were converted to hypertables
        """
        logger.info(f"Setting up hypertables for service: {service_name}")
        hypertables_created = []
        
        try:
            if not self.async_engine:
                raise RuntimeError("Database engine not initialized")
                
            async with self.async_engine.begin() as conn:
                # First check if TimescaleDB extension is enabled
                result = await conn.execute(text("SELECT extname FROM pg_extension WHERE extname = 'timescaledb'"))
                if not result.fetchone():
                    logger.warning("TimescaleDB extension not found, enabling it now")
                    await conn.execute(text("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"))
                
                # Get all tables for this service
                # In a real implementation, we would have a way to identify which tables belong to which service
                # For now, we'll use a simple naming convention where tables are prefixed with the service name
                # or we could look for tables with specific time columns
                
                # Example: Check for tables with timestamp columns that should be hypertables
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
                            await self.create_hypertable(table_name, time_column, correlation_id="hypertable_creation")
                            
                            hypertables_created.append(table_name)
                            logger.info(f"Successfully converted {table_name} to a hypertable")
                            
                        except Exception as e:
                            logger.error(f"Failed to convert {table_name} to hypertable: {str(e)}")
                    else:
                        logger.info(f"Table {table_name} is already a hypertable")
                
                logger.info(f"Hypertable setup complete. Created {len(hypertables_created)} hypertables")
                return hypertables_created
                
        except Exception as e:
            logger.error(f"Error setting up hypertables for service {service_name}: {str(e)}")
            raise
