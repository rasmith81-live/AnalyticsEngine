-- Test CRUD operations on new tables

-- Test connector_profiles
INSERT INTO connector_profiles (id, profile_data)
VALUES ('test-profile-1', '{"name": "Test SQL Connection", "type": "sql", "test_status": "success"}'::jsonb);

SELECT id, profile_data->>'name' AS name, profile_data->>'type' AS type, created_at 
FROM connector_profiles 
WHERE id = 'test-profile-1';

-- Test client_configs
INSERT INTO client_configs (client_id, config_data)
VALUES ('test-client-1', '{"client_name": "Test Corporation", "license_type": "professional"}'::jsonb);

SELECT client_id, config_data->>'client_name' AS name, config_data->>'license_type' AS license, created_at 
FROM client_configs 
WHERE client_id = 'test-client-1';

-- Test service_proposals
INSERT INTO service_proposals (proposal_id, proposal_data)
VALUES ('test-proposal-1', '{"proposal_type": "implementation", "status": "draft"}'::jsonb);

SELECT proposal_id, proposal_data->>'proposal_type' AS type, proposal_data->>'status' AS status, created_at 
FROM service_proposals 
WHERE proposal_id = 'test-proposal-1';

-- Show all test data
SELECT 'connector_profiles' AS table_name, COUNT(*) AS row_count FROM connector_profiles
UNION ALL
SELECT 'client_configs', COUNT(*) FROM client_configs
UNION ALL
SELECT 'service_proposals', COUNT(*) FROM service_proposals;
