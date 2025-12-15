
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

class TimescaleManager:
    """
    Manages TimescaleDB specific features: Hypertables, Compression, Retention, and Continuous Aggregates.
    """

    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def init_extension(self) -> bool:
        """Ensure TimescaleDB extension is enabled."""
        async with self.session_factory() as session:
            try:
                await session.execute(text("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"))
                await session.commit()
                logger.info("TimescaleDB extension verified/enabled.")
                return True
            except Exception as e:
                logger.error(f"Failed to enable TimescaleDB extension: {e}")
                return False

    async def convert_to_hypertable(
        self, 
        table_name: str, 
        time_column: str, 
        chunk_time_interval: str = "7 days",
        if_not_exists: bool = True
    ) -> bool:
        """Convert a standard PostgreSQL table to a TimescaleDB hypertable."""
        async with self.session_factory() as session:
            try:
                # Check if already a hypertable
                check_query = text(
                    "SELECT 1 FROM timescaledb_information.hypertables WHERE hypertable_name = :table_name"
                )
                result = await session.execute(check_query, {"table_name": table_name})
                if result.scalar():
                    if if_not_exists:
                        logger.info(f"Table {table_name} is already a hypertable.")
                        return True
                    else:
                        logger.warning(f"Table {table_name} is already a hypertable.")
                        return False

                # Convert
                cmd = text(
                    f"SELECT create_hypertable(:table_name, :time_column, chunk_time_interval => INTERVAL :chunk_interval, if_not_exists => :if_not_exists)"
                )
                await session.execute(cmd, {
                    "table_name": table_name,
                    "time_column": time_column,
                    "chunk_interval": chunk_time_interval,
                    "if_not_exists": if_not_exists
                })
                await session.commit()
                logger.info(f"Converted {table_name} to hypertable.")
                return True
            except Exception as e:
                logger.error(f"Failed to convert {table_name} to hypertable: {e}")
                await session.rollback()
                raise

    async def set_compression_policy(
        self, 
        table_name: str, 
        compress_after: str = "7 days",
        segment_by: Optional[List[str]] = None,
        order_by: str = "time DESC"
    ) -> bool:
        """Enable compression and set policy."""
        async with self.session_factory() as session:
            try:
                # Enable compression
                segment_clause = f", segmentby => ARRAY[{', '.join(map(repr, segment_by))}]" if segment_by else ""
                alter_cmd = text(f"ALTER TABLE {table_name} SET (timescaledb.compress{segment_clause}, timescaledb.compress_orderby = '{order_by}');")
                
                # Check if compression already enabled to avoid error
                # Ideally we check pg catalogs, but for now try/except pattern for idempotency usually used or specific check
                try:
                    await session.execute(alter_cmd)
                except Exception as e:
                    if "already" in str(e).lower():
                        pass # Already enabled
                    else:
                        raise e

                # Add policy
                policy_cmd = text(f"SELECT add_compression_policy('{table_name}', INTERVAL '{compress_after}', if_not_exists => TRUE);")
                await session.execute(policy_cmd)
                await session.commit()
                logger.info(f"Compression policy set for {table_name} after {compress_after}.")
                return True
            except Exception as e:
                logger.error(f"Failed to set compression policy for {table_name}: {e}")
                await session.rollback()
                raise

    async def set_retention_policy(self, table_name: str, drop_after: str = "1 year") -> bool:
        """Set data retention policy."""
        async with self.session_factory() as session:
            try:
                cmd = text(f"SELECT add_retention_policy('{table_name}', INTERVAL '{drop_after}', if_not_exists => TRUE);")
                await session.execute(cmd)
                await session.commit()
                logger.info(f"Retention policy set for {table_name} drop after {drop_after}.")
                return True
            except Exception as e:
                logger.error(f"Failed to set retention policy for {table_name}: {e}")
                await session.rollback()
                raise

    async def create_continuous_aggregate(
        self, 
        view_name: str, 
        query: str, 
        refresh_interval: Optional[str] = None,
        replace: bool = False
    ) -> bool:
        """
        Create a Continuous Aggregate view.
        
        Args:
            view_name: Name of the materialzed view.
            query: The SELECT query defining the aggregate (must include time_bucket).
            refresh_interval: If provided, adds a refresh policy (e.g., '1 hour').
            replace: If True, drops existing view first.
        """
        async with self.session_factory() as session:
            try:
                if replace:
                    await session.execute(text(f"DROP MATERIALIZED VIEW IF EXISTS {view_name} CASCADE;"))
                
                # Create View
                # Note: WITH (timescaledb.continuous) is the syntax
                create_cmd = text(f"CREATE MATERIALIZED VIEW IF NOT EXISTS {view_name} WITH (timescaledb.continuous) AS {query} WITH NO DATA;")
                await session.execute(create_cmd)
                
                # Add Refresh Policy if requested
                if refresh_interval:
                    policy_cmd = text(
                        f"SELECT add_continuous_aggregate_policy('{view_name}', "
                        f"start_offset => NULL, "
                        f"end_offset => INTERVAL '1 hour', "
                        f"schedule_interval => INTERVAL '{refresh_interval}', "
                        f"if_not_exists => TRUE);"
                    )
                    await session.execute(policy_cmd)
                
                await session.commit()
                logger.info(f"Continuous Aggregate {view_name} created.")
                return True
            except Exception as e:
                logger.error(f"Failed to create Continuous Aggregate {view_name}: {e}")
                await session.rollback()
                raise

    async def refresh_continuous_aggregate(self, view_name: str, start_time: datetime, end_time: datetime) -> bool:
        """Manually refresh a specific range of a continuous aggregate."""
        async with self.session_factory() as session:
            try:
                cmd = text(f"CALL refresh_continuous_aggregate('{view_name}', '{start_time}', '{end_time}');")
                await session.execute(cmd)
                await session.commit()
                return True
            except Exception as e:
                logger.error(f"Failed to refresh CAGG {view_name}: {e}")
                return False
