-- Verify Persistent Storage Tables
-- 
-- This script verifies that the migration created all required tables
-- and indexes correctly.

-- Check if tables exist
SELECT 
    tablename,
    schemaname,
    tableowner
FROM pg_tables
WHERE tablename IN ('connector_profiles', 'client_configs', 'service_proposals')
ORDER BY tablename;

-- Check table structures
\d connector_profiles
\d client_configs
\d service_proposals

-- Check indexes
SELECT
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename IN ('connector_profiles', 'client_configs', 'service_proposals')
ORDER BY tablename, indexname;

-- Check table comments
SELECT 
    c.relname AS table_name,
    pg_catalog.obj_description(c.oid, 'pg_class') AS table_comment
FROM pg_catalog.pg_class c
WHERE c.relname IN ('connector_profiles', 'client_configs', 'service_proposals')
ORDER BY c.relname;

-- Check column comments
SELECT 
    c.table_name,
    c.column_name,
    pgd.description AS column_comment
FROM information_schema.columns c
LEFT JOIN pg_catalog.pg_statio_all_tables st ON c.table_name = st.relname
LEFT JOIN pg_catalog.pg_description pgd ON pgd.objoid = st.relid 
    AND pgd.objsubid = c.ordinal_position
WHERE c.table_name IN ('connector_profiles', 'client_configs', 'service_proposals')
ORDER BY c.table_name, c.ordinal_position;

-- Verify JSONB columns
SELECT 
    table_name,
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_name IN ('connector_profiles', 'client_configs', 'service_proposals')
    AND data_type = 'jsonb'
ORDER BY table_name, column_name;

-- Test insert and select (will be rolled back)
BEGIN;

-- Test connector_profiles
INSERT INTO connector_profiles (id, profile_data)
VALUES ('test-profile-1', '{"name": "Test Connection", "type": "sql", "test_status": "success"}'::jsonb);

SELECT id, profile_data->>'name' AS name, created_at 
FROM connector_profiles 
WHERE id = 'test-profile-1';

-- Test client_configs
INSERT INTO client_configs (client_id, config_data)
VALUES ('test-client-1', '{"client_name": "Test Client", "license_type": "professional"}'::jsonb);

SELECT client_id, config_data->>'client_name' AS name, created_at 
FROM client_configs 
WHERE client_id = 'test-client-1';

-- Test service_proposals
INSERT INTO service_proposals (proposal_id, proposal_data)
VALUES ('test-proposal-1', '{"proposal_type": "implementation", "status": "draft"}'::jsonb);

SELECT proposal_id, proposal_data->>'status' AS status, created_at 
FROM service_proposals 
WHERE proposal_id = 'test-proposal-1';

-- Rollback test data
ROLLBACK;

-- Summary
SELECT 
    'connector_profiles' AS table_name,
    COUNT(*) AS row_count
FROM connector_profiles
UNION ALL
SELECT 
    'client_configs',
    COUNT(*)
FROM client_configs
UNION ALL
SELECT 
    'service_proposals',
    COUNT(*)
FROM service_proposals;
