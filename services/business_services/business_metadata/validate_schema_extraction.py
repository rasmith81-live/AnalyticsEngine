"""
Validation tests for Schema Extraction (Phase 4)

Tests the SchemaExtractor service, EntityEventHandler, and schema extraction API.
"""

import asyncio
import json
from pathlib import Path
import tempfile
import shutil

from services.schema_extractor import SchemaExtractor
from services.schema_metrics import SchemaMetrics
from ontology_models import EntityDefinition, TableSchemaDefinition, ColumnDefinition


def test_schema_extractor_basic():
    """Test basic schema extraction from EntityDefinition."""
    print("\n=== Test 1: Basic Schema Extraction ===")
    
    # Create test entity with table schema
    entity = EntityDefinition(
        id="test-entity-1",
        code="TEST_ENTITY",
        name="Test Entity",
        description="Test entity for validation",
        module_code="TEST_MODULE",
        table_schema=TableSchemaDefinition(
            table_name="test_entities",
            class_name="TestEntity",
            columns=[
                ColumnDefinition(
                    name="id",
                    type="String",
                    primary_key=True,
                    nullable=False
                ),
                ColumnDefinition(
                    name="name",
                    type="String",
                    nullable=False
                ),
                ColumnDefinition(
                    name="created_at",
                    type="DateTime",
                    nullable=False
                )
            ]
        )
    )
    
    # Create temporary directory for schemas
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Initialize extractor
        extractor = SchemaExtractor(output_dir=temp_path)
        
        # Extract schema
        schema = asyncio.run(extractor.extract_schema_from_entity(entity))
        
        # Validate schema structure
        assert schema["table_name"] == "test_entities", "Table name mismatch"
        assert schema["class_name"] == "TestEntity", "Class name mismatch"
        assert len(schema["columns"]) == 3, f"Expected 3 columns, got {len(schema['columns'])}"
        assert schema["_metadata"]["entity_code"] == "TEST_ENTITY", "Entity code mismatch"
        assert schema["_metadata"]["module"] == "TEST_MODULE", "Module code mismatch"
        
        # Validate columns
        id_col = next(c for c in schema["columns"] if c["name"] == "id")
        assert id_col["primary_key"] == True, "ID should be primary key"
        assert id_col["nullable"] == False, "ID should not be nullable"
        
        print("✅ Basic schema extraction successful")
        print(f"   - Table: {schema['table_name']}")
        print(f"   - Columns: {len(schema['columns'])}")
        print(f"   - Entity: {schema['_metadata']['entity_code']}")


def test_schema_json_file_generation():
    """Test JSON file generation from schema."""
    print("\n=== Test 2: JSON File Generation ===")
    
    # Create test entity
    entity = EntityDefinition(
        id="test-entity-2",
        code="SCOR_PROCESS",
        name="SCOR Process",
        description="SCOR process entity",
        module_code="ASCM_SCOR",
        table_schema=TableSchemaDefinition(
            table_name="scor_processes",
            class_name="SCORProcess",
            columns=[
                ColumnDefinition(name="id", type="String", primary_key=True),
                ColumnDefinition(name="process_code", type="String", nullable=False),
                ColumnDefinition(name="description", type="Text")
            ]
        )
    )
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        extractor = SchemaExtractor(output_dir=temp_path)
        
        # Extract and save schema
        schema = asyncio.run(extractor.extract_schema_from_entity(entity))
        output_file = asyncio.run(extractor.save_schema_to_json(schema, "scor_process"))
        
        # Verify file exists
        assert output_file.exists(), f"Schema file not created: {output_file}"
        
        # Verify file contents
        with open(output_file, 'r') as f:
            loaded_schema = json.load(f)
        
        assert loaded_schema["table_name"] == "scor_processes", "Table name mismatch in JSON"
        assert loaded_schema["class_name"] == "SCORProcess", "Class name mismatch in JSON"
        assert len(loaded_schema["columns"]) == 3, "Column count mismatch in JSON"
        
        print("✅ JSON file generation successful")
        print(f"   - File: {output_file.name}")
        print(f"   - Size: {output_file.stat().st_size} bytes")


def test_schema_metrics_tracking():
    """Test metrics tracking for schema operations."""
    print("\n=== Test 3: Schema Metrics Tracking ===")
    
    # Initialize metrics (without ObservabilityClient for testing)
    metrics = SchemaMetrics(observability_client=None)
    
    # Create test entity
    entity = EntityDefinition(
        id="test-entity-3",
        code="TEST_METRIC",
        name="Test Metric Entity",
        module_code="TEST",
        table_schema=TableSchemaDefinition(
            table_name="test_metrics",
            class_name="TestMetric",
            columns=[
                ColumnDefinition(name="id", type="String", primary_key=True)
            ]
        )
    )
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        extractor = SchemaExtractor(output_dir=temp_path, metrics_service=metrics)
        
        # Extract schema (metrics should be tracked)
        schema = asyncio.run(extractor.extract_schema_from_entity(entity))
        
        # Get metrics summary
        summary = metrics.get_metrics_summary()
        
        assert summary["total_extractions"] >= 1, "Extraction not tracked"
        assert summary["successful_extractions"] >= 1, "Success not tracked"
        assert summary["success_rate_percent"] == 100.0, "Success rate should be 100%"
        
        print("✅ Metrics tracking successful")
        print(f"   - Total extractions: {summary['total_extractions']}")
        print(f"   - Success rate: {summary['success_rate_percent']}%")
        print(f"   - Avg duration: {summary['average_duration_ms']:.2f}ms")


def test_schema_extraction_error_handling():
    """Test error handling for invalid entities."""
    print("\n=== Test 4: Error Handling ===")
    
    # Create entity without table_schema
    entity_no_schema = EntityDefinition(
        id="test-entity-4",
        code="NO_SCHEMA",
        name="Entity Without Schema",
        module_code="TEST"
    )
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        metrics = SchemaMetrics(observability_client=None)
        extractor = SchemaExtractor(output_dir=temp_path, metrics_service=metrics)
        
        # Attempt extraction (should fail)
        try:
            schema = asyncio.run(extractor.extract_schema_from_entity(entity_no_schema))
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "does not have table_schema" in str(e), "Wrong error message"
            print("✅ Error handling successful")
            print(f"   - Caught expected error: {str(e)[:50]}...")
        
        # Verify metrics tracked the failure
        summary = metrics.get_metrics_summary()
        assert summary["failed_extractions"] >= 1, "Failure not tracked"
        print(f"   - Failed extractions tracked: {summary['failed_extractions']}")


def test_bulk_extraction():
    """Test bulk schema extraction."""
    print("\n=== Test 5: Bulk Extraction ===")
    
    # Create multiple test entities
    entities = [
        EntityDefinition(
            id=f"test-entity-{i}",
            code=f"ENTITY_{i}",
            name=f"Entity {i}",
            module_code="TEST",
            table_schema=TableSchemaDefinition(
                table_name=f"entity_{i}",
                class_name=f"Entity{i}",
                columns=[
                    ColumnDefinition(name="id", type="String", primary_key=True)
                ]
            )
        )
        for i in range(5)
    ]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        metrics = SchemaMetrics(observability_client=None)
        extractor = SchemaExtractor(output_dir=temp_path, metrics_service=metrics)
        
        # Extract all schemas
        results = []
        for entity in entities:
            try:
                schema = asyncio.run(extractor.extract_schema_from_entity(entity))
                filename = entity.code.lower()
                output_file = asyncio.run(extractor.save_schema_to_json(schema, filename))
                results.append({
                    "success": True,
                    "entity_code": entity.code,
                    "output_file": str(output_file)
                })
            except Exception as e:
                results.append({
                    "success": False,
                    "entity_code": entity.code,
                    "error": str(e)
                })
        
        # Generate summary
        summary = extractor.get_extraction_summary(results)
        
        assert summary["total_entities"] == 5, "Should process 5 entities"
        assert summary["successful_extractions"] == 5, "All should succeed"
        assert summary["failed_extractions"] == 0, "None should fail"
        assert summary["success_rate"] == 100.0, "Success rate should be 100%"
        
        # Verify all files created
        schema_files = list(temp_path.glob("*.json"))
        assert len(schema_files) == 5, f"Expected 5 files, got {len(schema_files)}"
        
        print("✅ Bulk extraction successful")
        print(f"   - Entities processed: {summary['total_entities']}")
        print(f"   - Success rate: {summary['success_rate']}%")
        print(f"   - Files created: {len(schema_files)}")


def test_metrics_health_reporting():
    """Test health status reporting based on metrics."""
    print("\n=== Test 6: Health Reporting ===")
    
    metrics = SchemaMetrics(observability_client=None)
    
    # Simulate successful extractions
    for i in range(10):
        asyncio.run(metrics.record_extraction_start(f"entity_{i}"))
        asyncio.run(metrics.record_extraction_complete(
            operation_id=f"op_{i}",
            entity_code=f"entity_{i}",
            duration_ms=50.0,
            success=True
        ))
    
    # Get health report
    health = asyncio.run(metrics.report_health())
    
    assert health["status"] == "healthy", "Should be healthy with 100% success"
    assert health["metrics"]["success_rate_percent"] == 100.0, "Success rate should be 100%"
    
    print("✅ Health reporting successful")
    print(f"   - Status: {health['status']}")
    print(f"   - Success rate: {health['metrics']['success_rate_percent']}%")
    print(f"   - Total extractions: {health['metrics']['total_extractions']}")


def run_all_tests():
    """Run all validation tests."""
    print("=" * 60)
    print("SCHEMA EXTRACTION VALIDATION TESTS (Phase 4)")
    print("=" * 60)
    
    tests = [
        ("Basic Schema Extraction", test_schema_extractor_basic),
        ("JSON File Generation", test_schema_json_file_generation),
        ("Metrics Tracking", test_schema_metrics_tracking),
        ("Error Handling", test_schema_extraction_error_handling),
        ("Bulk Extraction", test_bulk_extraction),
        ("Health Reporting", test_metrics_health_reporting)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"\n❌ {test_name} FAILED")
            print(f"   Error: {str(e)}")
            failed += 1
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total tests: {len(tests)}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    print(f"Success rate: {(passed / len(tests) * 100):.1f}%")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
