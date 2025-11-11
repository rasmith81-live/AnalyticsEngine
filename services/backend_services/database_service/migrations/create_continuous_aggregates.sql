-- TimescaleDB Continuous Aggregates for Real-Time KPI Streaming
-- Date: November 11, 2025
-- Purpose: Create continuous aggregates for minute, hour, and day level KPI values

-- ============================================================================
-- 1. MINUTE-LEVEL CONTINUOUS AGGREGATE
-- ============================================================================
-- Aggregates KPI values by minute for real-time streaming
CREATE MATERIALIZED VIEW IF NOT EXISTS kpi_values_minute
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 minute', timestamp) AS bucket,
    kpi_code,
    entity_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    SUM(value) AS sum_value,
    COUNT(*) AS data_points,
    STDDEV(value) AS stddev_value
FROM kpi_values
GROUP BY bucket, kpi_code, entity_id
WITH NO DATA;

-- Create refresh policy: refresh every 30 seconds, covering last 2 minutes
SELECT add_continuous_aggregate_policy('kpi_values_minute',
    start_offset => INTERVAL '2 minutes',
    end_offset => INTERVAL '30 seconds',
    schedule_interval => INTERVAL '30 seconds');

-- Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_kpi_values_minute_bucket_kpi 
    ON kpi_values_minute (bucket DESC, kpi_code, entity_id);

-- ============================================================================
-- 2. HOUR-LEVEL CONTINUOUS AGGREGATE
-- ============================================================================
-- Aggregates KPI values by hour for hourly streaming
CREATE MATERIALIZED VIEW IF NOT EXISTS kpi_values_hour
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', timestamp) AS bucket,
    kpi_code,
    entity_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    SUM(value) AS sum_value,
    COUNT(*) AS data_points,
    STDDEV(value) AS stddev_value
FROM kpi_values
GROUP BY bucket, kpi_code, entity_id
WITH NO DATA;

-- Create refresh policy: refresh every 5 minutes, covering last 2 hours
SELECT add_continuous_aggregate_policy('kpi_values_hour',
    start_offset => INTERVAL '2 hours',
    end_offset => INTERVAL '5 minutes',
    schedule_interval => INTERVAL '5 minutes');

-- Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_kpi_values_hour_bucket_kpi 
    ON kpi_values_hour (bucket DESC, kpi_code, entity_id);

-- ============================================================================
-- 3. DAY-LEVEL CONTINUOUS AGGREGATE
-- ============================================================================
-- Aggregates KPI values by day for daily streaming
CREATE MATERIALIZED VIEW IF NOT EXISTS kpi_values_day
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 day', timestamp) AS bucket,
    kpi_code,
    entity_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    SUM(value) AS sum_value,
    COUNT(*) AS data_points,
    STDDEV(value) AS stddev_value
FROM kpi_values
GROUP BY bucket, kpi_code, entity_id
WITH NO DATA;

-- Create refresh policy: refresh every hour, covering last 7 days
SELECT add_continuous_aggregate_policy('kpi_values_day',
    start_offset => INTERVAL '7 days',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');

-- Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_kpi_values_day_bucket_kpi 
    ON kpi_values_day (bucket DESC, kpi_code, entity_id);

-- ============================================================================
-- 4. HELPER FUNCTIONS
-- ============================================================================

-- Function to get latest KPI value for a given period
CREATE OR REPLACE FUNCTION get_latest_kpi_value(
    p_kpi_code TEXT,
    p_entity_id TEXT,
    p_period TEXT DEFAULT 'minute'
)
RETURNS TABLE (
    bucket TIMESTAMPTZ,
    avg_value DOUBLE PRECISION,
    min_value DOUBLE PRECISION,
    max_value DOUBLE PRECISION,
    sum_value DOUBLE PRECISION,
    data_points BIGINT,
    stddev_value DOUBLE PRECISION
) AS $$
BEGIN
    CASE p_period
        WHEN 'minute' THEN
            RETURN QUERY
            SELECT * FROM kpi_values_minute
            WHERE kpi_code = p_kpi_code AND entity_id = p_entity_id
            ORDER BY bucket DESC
            LIMIT 1;
        WHEN 'hour' THEN
            RETURN QUERY
            SELECT * FROM kpi_values_hour
            WHERE kpi_code = p_kpi_code AND entity_id = p_entity_id
            ORDER BY bucket DESC
            LIMIT 1;
        WHEN 'day' THEN
            RETURN QUERY
            SELECT * FROM kpi_values_day
            WHERE kpi_code = p_kpi_code AND entity_id = p_entity_id
            ORDER BY bucket DESC
            LIMIT 1;
        ELSE
            RAISE EXCEPTION 'Invalid period: %. Must be minute, hour, or day', p_period;
    END CASE;
END;
$$ LANGUAGE plpgsql;

-- Function to get KPI values for a time range
CREATE OR REPLACE FUNCTION get_kpi_values_range(
    p_kpi_code TEXT,
    p_entity_id TEXT,
    p_start_time TIMESTAMPTZ,
    p_end_time TIMESTAMPTZ,
    p_period TEXT DEFAULT 'minute'
)
RETURNS TABLE (
    bucket TIMESTAMPTZ,
    avg_value DOUBLE PRECISION,
    min_value DOUBLE PRECISION,
    max_value DOUBLE PRECISION,
    sum_value DOUBLE PRECISION,
    data_points BIGINT,
    stddev_value DOUBLE PRECISION
) AS $$
BEGIN
    CASE p_period
        WHEN 'minute' THEN
            RETURN QUERY
            SELECT * FROM kpi_values_minute
            WHERE kpi_code = p_kpi_code 
              AND entity_id = p_entity_id
              AND bucket >= p_start_time 
              AND bucket <= p_end_time
            ORDER BY bucket ASC;
        WHEN 'hour' THEN
            RETURN QUERY
            SELECT * FROM kpi_values_hour
            WHERE kpi_code = p_kpi_code 
              AND entity_id = p_entity_id
              AND bucket >= p_start_time 
              AND bucket <= p_end_time
            ORDER BY bucket ASC;
        WHEN 'day' THEN
            RETURN QUERY
            SELECT * FROM kpi_values_day
            WHERE kpi_code = p_kpi_code 
              AND entity_id = p_entity_id
              AND bucket >= p_start_time 
              AND bucket <= p_end_time
            ORDER BY bucket ASC;
        ELSE
            RAISE EXCEPTION 'Invalid period: %. Must be minute, hour, or day', p_period;
    END CASE;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- 5. GRANT PERMISSIONS
-- ============================================================================
-- Grant necessary permissions to application user
-- GRANT SELECT ON kpi_values_minute TO app_user;
-- GRANT SELECT ON kpi_values_hour TO app_user;
-- GRANT SELECT ON kpi_values_day TO app_user;
-- GRANT EXECUTE ON FUNCTION get_latest_kpi_value TO app_user;
-- GRANT EXECUTE ON FUNCTION get_kpi_values_range TO app_user;

-- ============================================================================
-- NOTES:
-- ============================================================================
-- 1. Continuous aggregates automatically update as new data arrives
-- 2. Refresh policies ensure data is kept up-to-date
-- 3. Indexes optimize query performance for streaming lookups
-- 4. Helper functions provide convenient access to aggregated data
-- 5. Adjust refresh intervals based on your performance requirements
