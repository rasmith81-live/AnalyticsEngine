from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class TimescaleManager:
    """
    Manages TimescaleDB specific features:
    - Continuous Aggregates generation
    - Query Routing (Raw vs Aggregate)
    - Retention and Refresh policies
    """
    
    def __init__(self):
        self.aggregates_registry = {} # Cache of known aggregates
    
    def get_optimal_query_source(
        self, 
        table_name: str, 
        time_range: Tuple[datetime, datetime], 
        interval: str
    ) -> Tuple[str, str]:
        """
        Determines the best table/view to query based on time range and interval.
        
        Args:
            table_name: Base hypertable name
            time_range: (start_date, end_date)
            interval: Requested granularity (e.g., '1h', '1d')
            
        Returns:
            Tuple of (source_table_name, time_bucket_interval)
        """
        start_date, end_date = time_range
        duration = end_date - start_date
        
        # Simple heuristic for now
        # If querying > 1 year -> use monthly aggregate
        # If querying > 1 month -> use daily aggregate
        # If querying > 1 week -> use hourly aggregate
        # Else -> use raw table
        
        # Check if aggregates exist (in a real implementation, we'd check metadata/registry)
        # For now, we assume standard naming convention: {table_name}_{interval}_agg
        
        if duration > timedelta(days=365):
            return f"{table_name}_monthly_agg", "1 month"
        elif duration > timedelta(days=30):
            return f"{table_name}_daily_agg", "1 day"
        elif duration > timedelta(days=7):
            return f"{table_name}_hourly_agg", "1 hour"
        else:
            return table_name, interval

    def generate_continuous_aggregate_query(
        self, 
        view_name: str, 
        source_table: str, 
        time_bucket: str, 
        aggregates: List[Dict[str, str]],
        group_by: List[str] = None
    ) -> str:
        """
        Generates SQL to create a Continuous Aggregate View.
        
        Args:
            view_name: Name of the view to create
            source_table: Underlying hypertable
            time_bucket: Bucket interval (e.g., '1 hour')
            aggregates: List of dicts with 'func' and 'column' (e.g., {'func': 'AVG', 'column': 'temperature'})
            group_by: Additional columns to group by
        """
        select_clauses = [f"time_bucket('{time_bucket}', time) AS bucket"]
        
        for agg in aggregates:
            func = agg['func'].upper()
            col = agg['column']
            alias = agg.get('alias', f"{func.lower()}_{col}")
            select_clauses.append(f"{func}({col}) AS {alias}")
            
        group_by_cols = ["bucket"]
        if group_by:
            select_clauses.extend(group_by)
            group_by_cols.extend(group_by)
            
        query = f"""
        CREATE MATERIALIZED VIEW {view_name}
        WITH (timescaledb.continuous) AS
        SELECT {', '.join(select_clauses)}
        FROM {source_table}
        GROUP BY {', '.join(group_by_cols)};
        """
        return query.strip()

    def generate_refresh_policy_query(
        self, 
        view_name: str, 
        start_offset: str, 
        end_offset: str, 
        schedule_interval: str
    ) -> str:
        """
        Generates SQL to add a refresh policy to a Continuous Aggregate.
        """
        query = f"""
        SELECT add_continuous_aggregate_policy('{view_name}',
            start_offset => INTERVAL '{start_offset}',
            end_offset => INTERVAL '{end_offset}',
            schedule_interval => INTERVAL '{schedule_interval}');
        """
        return query.strip()

    def generate_retention_policy_query(self, table_name: str, drop_after: str) -> str:
        """
        Generates SQL to add a retention policy.
        """
        query = f"""
        SELECT add_retention_policy('{table_name}',
            drop_after => INTERVAL '{drop_after}');
        """
        return query.strip()
