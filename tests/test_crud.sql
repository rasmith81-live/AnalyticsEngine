-- Test CRUD Operations on New Tables

-- Test 1: Insert into connector_profiles
INSERT INTO connector_profiles (id, profile_data, created_at, updated_at)
VALUES (
    'test-sql-conn-1',
    '{"name": "Production SQL Server", "type": "sql", "connection_string": "Server=prod-db;Database=analytics;", "test_status": "success", "last_tested": "2025-12-21T11:00:00Z"}'::jsonb,
    NOW(),
    NOW()
);

-- Test 2: Insert into client_configs
INSERT INTO client_configs (client_id, config_data, created_at, updated_at)
VALUES (
    'client-acme-corp',
    '{"client_name": "ACME Corporation", "license_type": "enterprise", "modules": ["SCOR", "CRM", "Sales"], "preferences": {"theme": "dark", "notifications": true}}'::jsonb,
    NOW(),
    NOW()
);

-- Test 3: Insert into service_proposals
INSERT INTO service_proposals (proposal_id, proposal_data, created_at)
VALUES (
    'prop-2025-001',
    '{"client_id": "client-acme-corp", "proposal_type": "implementation", "pricing": {"total": 150000, "breakdown": {"consulting": 100000, "implementation": 50000}}, "status": "draft", "timeline": {"start_date": "2025-01-15", "end_date": "2025-06-30"}}'::jsonb,
    NOW()
);

-- Test 4: Read from connector_profiles
SELECT 
    id,
    profile_data->>'name' AS connection_name,
    profile_data->>'type' AS connection_type,
    profile_data->>'test_status' AS status,
    created_at
FROM connector_profiles
WHERE id = 'test-sql-conn-1';

-- Test 5: Read from client_configs
SELECT 
    client_id,
    config_data->>'client_name' AS client_name,
    config_data->>'license_type' AS license,
    config_data->'modules' AS modules,
    created_at
FROM client_configs
WHERE client_id = 'client-acme-corp';

-- Test 6: Read from service_proposals
SELECT 
    proposal_id,
    proposal_data->>'proposal_type' AS type,
    proposal_data->'pricing'->>'total' AS total_price,
    proposal_data->>'status' AS status,
    created_at
FROM service_proposals
WHERE proposal_id = 'prop-2025-001';

-- Test 7: Update connector_profiles
UPDATE connector_profiles
SET 
    profile_data = profile_data || '{"test_status": "verified", "last_tested": "2025-12-21T12:00:00Z"}'::jsonb,
    updated_at = NOW()
WHERE id = 'test-sql-conn-1';

-- Test 8: Verify update
SELECT 
    id,
    profile_data->>'test_status' AS status,
    profile_data->>'last_tested' AS last_tested,
    updated_at
FROM connector_profiles
WHERE id = 'test-sql-conn-1';

-- Test 9: Count records in each table
SELECT 'connector_profiles' AS table_name, COUNT(*) AS record_count FROM connector_profiles
UNION ALL
SELECT 'client_configs', COUNT(*) FROM client_configs
UNION ALL
SELECT 'service_proposals', COUNT(*) FROM service_proposals;

-- Test 10: Verify indexes exist
SELECT 
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename IN ('connector_profiles', 'client_configs', 'service_proposals')
ORDER BY tablename, indexname;
