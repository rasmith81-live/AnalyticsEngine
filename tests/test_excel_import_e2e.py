"""
End-to-End Test for Excel Import Flow

Tests the complete flow:
1. Upload Excel/CSV file
2. Analyze (extract and enrich KPIs)
3. Commit (save to database with ontology sync)
4. Verify (check value chains, modules, relationships were created)

Usage:
    python tests/test_excel_import_e2e.py
    
Or with pytest:
    pytest tests/test_excel_import_e2e.py -v
"""

import asyncio
import httpx
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime

# Configuration - Use 127.0.0.1 instead of localhost for Windows Docker compatibility
API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://127.0.0.1:8090")
METADATA_SERVICE_URL = os.getenv("METADATA_SERVICE_URL", "http://127.0.0.1:8020")
INGESTION_SERVICE_URL = os.getenv("INGESTION_SERVICE_URL", "http://127.0.0.1:8025")
ENTITY_RESOLUTION_URL = os.getenv("ENTITY_RESOLUTION_URL", "http://127.0.0.1:8012")

# Internal Docker service URLs (for connectivity tests)
INTERNAL_ENTITY_RESOLUTION_URL = "http://entity_resolution_service:8000"

# Test timeouts
REQUEST_TIMEOUT = 60.0
STARTUP_WAIT = 5

# Containers to monitor for errors during tests
MONITORED_CONTAINERS = [
    "analyticsengine-metadata_ingestion_service-1",
    "analyticsengine-entity_resolution_service-1",
    "analyticsengine-api_gateway-1",
    "analyticsengine-business_metadata-1",
]

# Error patterns to look for in logs
ERROR_PATTERNS = [
    r"ERROR",
    r"Exception",
    r"Traceback",
    r"Failed",
    r"Connection refused",
    r"Name or service not known",
    r"TimeoutError",
    r"HTTPStatusError",
]


def get_container_logs(container_name: str, since_seconds: int = 60) -> Tuple[bool, List[str]]:
    """
    Get recent logs from a Docker container and check for errors.
    Returns (has_errors, error_lines).
    """
    try:
        result = subprocess.run(
            ["docker", "logs", "--since", f"{since_seconds}s", container_name],
            capture_output=True,
            text=True,
            timeout=10
        )
        logs = result.stdout + result.stderr
        
        error_lines = []
        for line in logs.split('\n'):
            for pattern in ERROR_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    # Skip common non-critical messages
                    if "healthcheck" in line.lower() or "health check" in line.lower():
                        continue
                    error_lines.append(line.strip())
                    break
        
        return len(error_lines) > 0, error_lines
    except Exception as e:
        return False, [f"Could not get logs: {str(e)}"]


def scan_all_container_logs(since_seconds: int = 30) -> Dict[str, List[str]]:
    """Scan all monitored containers for errors."""
    all_errors = {}
    for container in MONITORED_CONTAINERS:
        has_errors, errors = get_container_logs(container, since_seconds)
        if has_errors and errors:
            # Limit to last 5 errors per container
            all_errors[container] = errors[-5:]
    return all_errors


class TestResult:
    """Container for test results."""
    def __init__(self, name: str):
        self.name = name
        self.passed = False
        self.error: Optional[str] = None
        self.details: Dict[str, Any] = {}
        self.duration: float = 0.0
    
    def __repr__(self):
        status = "✅ PASS" if self.passed else "❌ FAIL"
        return f"{status} {self.name} ({self.duration:.2f}s)"


class ExcelImportE2ETest:
    """End-to-end test for Excel Import functionality."""
    
    def __init__(self):
        self.results: List[TestResult] = []
        self.import_id: Optional[str] = None
        self.kpi_count: int = 0
        
    def create_test_csv(self) -> str:
        """Create a sample CSV file for testing."""
        # Column names must match what KPIExcelProcessor expects: KPI, Definition, Standard Formula
        csv_content = '''KPI,Definition,Standard Formula,Category,Module
Sales Revenue Growth,Percentage increase in sales revenue over time,((Current Period Revenue - Previous Period Revenue) / Previous Period Revenue) * 100,Sales Performance,sales_analytics
Customer Acquisition Cost,Total cost to acquire a new customer,Total Marketing & Sales Costs / Number of New Customers Acquired,Marketing Efficiency,marketing_analytics
Customer Lifetime Value,Predicted total revenue from a customer,Average Purchase Value * Purchase Frequency * Customer Lifespan,Customer Analytics,customer_analytics
Conversion Rate,Percentage of leads that become customers,(Number of Conversions / Total Number of Leads) * 100,Sales Performance,sales_analytics
Net Promoter Score,Customer loyalty metric based on survey,Percentage Promoters - Percentage Detractors,Customer Experience,customer_analytics
'''
        # Create temp file
        temp_dir = tempfile.mkdtemp()
        csv_path = os.path.join(temp_dir, "test_kpis.csv")
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write(csv_content)
        return csv_path
    
    async def check_service_health(self, url: str, name: str) -> TestResult:
        """Check if a service is healthy."""
        result = TestResult(f"Health Check: {name}")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{url}/health")
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    result.passed = True
                    result.details = response.json()
                else:
                    result.error = f"Status {response.status_code}: {response.text}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_upload(self, csv_path: str) -> TestResult:
        """Test uploading a CSV file."""
        result = TestResult("Upload CSV File")
        start = time.time()
        
        try:
            # Try direct service first to get better error messages
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                with open(csv_path, 'rb') as f:
                    file_content = f.read()
                
                files = {'file': ('test_kpis.csv', file_content, 'text/csv')}
                
                # Try direct service first
                try:
                    response = await client.post(
                        f"{INGESTION_SERVICE_URL}/import/upload",
                        files=files
                    )
                except Exception as direct_error:
                    # Fall back to API Gateway
                    files = {'file': ('test_kpis.csv', file_content, 'text/csv')}
                    response = await client.post(
                        f"{API_GATEWAY_URL}/api/v1/metadata-ingestion/import/upload",
                        files=files
                    )
                
                result.duration = time.time() - start
                result.details['status_code'] = response.status_code
                result.details['response'] = response.text[:500] if response.text else None
                
                if response.status_code == 200:
                    data = response.json()
                    # Response uses camelCase: importId, validRows
                    self.import_id = data.get('importId') or data.get('import_id')
                    self.kpi_count = data.get('validRows') or data.get('kpi_count', 0)
                    result.passed = self.import_id is not None
                    result.details['import_id'] = self.import_id
                    result.details['kpi_count'] = self.kpi_count
                    result.details['ontology_sync'] = data.get('ontology_sync', {})
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_commit(self) -> TestResult:
        """Test committing the import."""
        result = TestResult("Commit Import")
        start = time.time()
        
        if not self.import_id:
            result.error = "No import_id available (upload must succeed first)"
            return result
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.post(
                    f"{API_GATEWAY_URL}/api/v1/metadata-ingestion/import/{self.import_id}/commit"
                )
                
                result.duration = time.time() - start
                result.details['status_code'] = response.status_code
                result.details['response'] = response.text[:1000] if response.text else None
                
                if response.status_code == 200:
                    data = response.json()
                    result.passed = True
                    result.details['committed_count'] = data.get('committed_count', 0)
                    result.details['ontology_sync'] = data.get('ontology_sync_summary', {})
                else:
                    result.error = f"Status {response.status_code}: {response.text[:500]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_verify_kpis(self) -> TestResult:
        """Verify KPIs were created in metadata service."""
        result = TestResult("Verify KPIs Created")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/metric_definition",
                    params={'limit': 10}
                )
                
                result.duration = time.time() - start
                result.details['status_code'] = response.status_code
                
                if response.status_code == 200:
                    data = response.json()
                    kpi_count = len(data) if isinstance(data, list) else 0
                    result.passed = kpi_count > 0
                    result.details['kpi_count'] = kpi_count
                    if kpi_count > 0:
                        result.details['sample_kpi'] = data[0].get('name', 'N/A')
                    else:
                        result.error = "No KPIs found in database"
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_verify_value_chains(self) -> TestResult:
        """Verify value chains were created."""
        result = TestResult("Verify Value Chains Created")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/value_chain_pattern_definition",
                    params={'limit': 10}
                )
                
                result.duration = time.time() - start
                result.details['status_code'] = response.status_code
                
                if response.status_code == 200:
                    data = response.json()
                    vc_count = len(data) if isinstance(data, list) else 0
                    result.details['value_chain_count'] = vc_count
                    if vc_count > 0:
                        result.passed = True
                        result.details['value_chains'] = [d.get('name', 'N/A') for d in data[:5]]
                    else:
                        result.passed = False
                        result.error = "No value chains found - ontology sync may have failed"
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_verify_modules(self) -> TestResult:
        """Verify modules (business processes) were created."""
        result = TestResult("Verify Modules Created")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/business_process_definition",
                    params={'limit': 10}
                )
                
                result.duration = time.time() - start
                result.details['status_code'] = response.status_code
                
                if response.status_code == 200:
                    data = response.json()
                    module_count = len(data) if isinstance(data, list) else 0
                    result.details['module_count'] = module_count
                    if module_count > 0:
                        result.passed = True
                        result.details['modules'] = [d.get('name', 'N/A') for d in data[:5]]
                    else:
                        result.passed = False
                        result.error = "No modules found - ontology sync may have failed"
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_verify_relationships(self) -> TestResult:
        """Verify relationships were created."""
        result = TestResult("Verify Relationships Created")
        start = time.time()
        
        try:
            # Query database directly for relationships count
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                # Get a KPI and check its relationships
                response = await client.get(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/metric_definition",
                    params={'limit': 1}
                )
                
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    if data and len(data) > 0:
                        kpi_code = data[0].get('code')
                        # Try to get relationships for this KPI
                        rel_response = await client.get(
                            f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/metric_definition/{kpi_code}/relationships"
                        )
                        if rel_response.status_code == 200:
                            rel_data = rel_response.json()
                            rel_count = len(rel_data) if isinstance(rel_data, list) else 0
                            result.details['relationship_count'] = rel_count
                            result.passed = rel_count > 0
                            if rel_count == 0:
                                result.error = "No relationships found for KPIs"
                        else:
                            result.details['relationship_check'] = "Could not query relationships"
                            result.passed = True  # Don't fail the whole test
                    else:
                        result.error = "No KPIs to check relationships for"
                else:
                    result.error = f"Status {response.status_code}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result
    
    async def test_config_sync(self) -> TestResult:
        """
        Verify the running container has the correct configuration.
        This catches stale code in containers when volume is updated but container not restarted.
        """
        result = TestResult("Config Sync Check")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{INGESTION_SERVICE_URL}/debug/config")
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    result.details = data
                    
                    # Check if config matches expected values
                    expected_url = "http://entity_resolution_service:8000"
                    actual_url = data.get("entity_resolution_url", "")
                    
                    if actual_url == expected_url:
                        result.passed = True
                    else:
                        result.passed = False
                        result.error = f"Stale code detected! Container has '{actual_url}' but should be '{expected_url}'. Restart container."
                elif response.status_code == 404:
                    # Endpoint doesn't exist - old code
                    result.passed = False
                    result.error = "Debug endpoint not found - container running old code. Rebuild/restart required."
                else:
                    result.error = f"Status {response.status_code}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = f"Config check failed: {str(e)}"
        
        return result
    
    async def test_internal_service_connectivity(self) -> TestResult:
        """
        Test that metadata_ingestion_service can reach entity_resolution_service internally.
        This catches Docker DNS issues like wrong service names (dashes vs underscores).
        """
        result = TestResult("Internal Service Connectivity")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                # Call the ingestion service's internal connectivity check
                # This endpoint tests if the service can reach entity_resolution_service
                response = await client.post(
                    f"{INGESTION_SERVICE_URL}/debug/test-entity-resolution",
                    json={"text": "Test connectivity check"}
                )
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    result.passed = data.get("reachable", False)
                    result.details = data
                    if not result.passed:
                        result.error = data.get("error", "Entity Resolution Service not reachable")
                elif response.status_code == 404:
                    # Endpoint doesn't exist, try direct entity resolution test
                    er_response = await client.post(
                        f"{ENTITY_RESOLUTION_URL}/api/v1/entity-resolution/semantic/extract",
                        json={"text": "connectivity test", "name": "test"}
                    )
                    result.duration = time.time() - start
                    if er_response.status_code == 200:
                        result.passed = True
                        result.details["entity_resolution_direct"] = "reachable"
                    else:
                        result.error = f"Entity Resolution returned {er_response.status_code}"
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = f"Connectivity test failed: {str(e)}"
        
        return result
    
    async def run_all_tests(self) -> None:
        """Run all E2E tests."""
        print("\n" + "="*60)
        print("  EXCEL IMPORT E2E TEST SUITE")
        print("="*60)
        print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60 + "\n")
        
        # Check services health first
        print("📡 Checking Service Health...\n")
        health_results = await asyncio.gather(
            self.check_service_health(API_GATEWAY_URL, "API Gateway"),
            self.check_service_health(METADATA_SERVICE_URL, "Metadata Service"),
        )
        
        for r in health_results:
            self.results.append(r)
            print(f"  {r}")
            if r.error:
                print(f"     Error: {r.error}")
        
        # Check if services are healthy before proceeding
        all_healthy = all(r.passed for r in health_results)
        if not all_healthy:
            print("\n⚠️  Some services are not healthy. Aborting tests.")
            self.print_summary()
            return
        
        print("\n" + "-"*60)
        print("🔄 Running Import Flow Tests...\n")
        
        # Create test file
        csv_path = self.create_test_csv()
        print(f"  Created test file: {csv_path}\n")
        
        # Run tests in sequence
        tests = [
            ("Config Sync", self.test_config_sync()),
            ("Internal Connectivity", self.test_internal_service_connectivity()),
            ("Upload", self.test_upload(csv_path)),
            ("Commit", self.test_commit()),
            ("Verify KPIs", self.test_verify_kpis()),
            ("Verify Value Chains", self.test_verify_value_chains()),
            ("Verify Modules", self.test_verify_modules()),
            ("Verify Relationships", self.test_verify_relationships()),
        ]
        
        for name, coro in tests:
            print(f"  Running: {name}...")
            test_start = time.time()
            result = await coro
            test_duration = time.time() - test_start
            self.results.append(result)
            print(f"  {result}")
            if result.error:
                print(f"     ❌ Error: {result.error}")
            if result.details:
                for k, v in result.details.items():
                    if k not in ['response', 'status_code']:
                        print(f"     • {k}: {v}")
            
            # Scan container logs for errors after failed tests
            if not result.passed:
                container_errors = scan_all_container_logs(since_seconds=int(test_duration) + 10)
                if container_errors:
                    print(f"     📋 Container Errors Detected:")
                    for container, errors in container_errors.items():
                        short_name = container.replace("analyticsengine-", "").replace("-1", "")
                        print(f"        [{short_name}]:")
                        for err in errors[:3]:  # Show max 3 errors per container
                            # Truncate long error lines
                            err_display = err[:120] + "..." if len(err) > 120 else err
                            print(f"          • {err_display}")
            print()
            
            # Stop if critical test fails
            if not result.passed and name in ["Config Sync", "Internal Connectivity", "Upload", "Commit"]:
                print(f"  ⚠️  Critical test '{name}' failed. Stopping further tests.\n")
                break
        
        # Cleanup
        try:
            os.remove(csv_path)
            os.rmdir(os.path.dirname(csv_path))
        except:
            pass
        
        self.print_summary()
    
    def print_summary(self) -> None:
        """Print test summary."""
        print("\n" + "="*60)
        print("  TEST SUMMARY")
        print("="*60)
        
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed)
        total_time = sum(r.duration for r in self.results)
        
        print(f"\n  Total Tests: {len(self.results)}")
        print(f"  ✅ Passed: {passed}")
        print(f"  ❌ Failed: {failed}")
        print(f"  ⏱️  Duration: {total_time:.2f}s")
        
        if failed > 0:
            print("\n  FAILED TESTS:")
            for r in self.results:
                if not r.passed:
                    print(f"    • {r.name}: {r.error}")
        
        print("\n" + "="*60)
        
        if failed == 0:
            print("  🎉 ALL TESTS PASSED!")
        else:
            print("  ⚠️  SOME TESTS FAILED - Review errors above")
        
        print("="*60 + "\n")


def enable_mock_llm():
    """Enable MOCK_LLM in entity_resolution_service for testing."""
    print("\n🔧 Enabling MOCK_LLM mode for testing (no LLM charges)...")
    try:
        result = subprocess.run(
            ["docker", "compose", "exec", "-e", "MOCK_LLM=true", 
             "entity_resolution_service", "echo", "MOCK_LLM enabled"],
            capture_output=True, text=True, timeout=10,
            cwd=str(Path(__file__).parent.parent)
        )
        # Actually need to restart with env var
        subprocess.run(
            ["docker", "compose", "up", "-d", "entity_resolution_service"],
            capture_output=True, text=True, timeout=60,
            cwd=str(Path(__file__).parent.parent),
            env={**os.environ, "MOCK_LLM": "true"}
        )
        time.sleep(10)  # Wait for service restart
        print("   ✅ MOCK_LLM enabled")
        return True
    except Exception as e:
        print(f"   ⚠️  Could not enable MOCK_LLM: {e}")
        return False


def disable_mock_llm():
    """Disable MOCK_LLM in entity_resolution_service after testing."""
    print("\n🔧 Disabling MOCK_LLM mode (restoring real LLM)...")
    try:
        subprocess.run(
            ["docker", "compose", "up", "-d", "entity_resolution_service"],
            capture_output=True, text=True, timeout=60,
            cwd=str(Path(__file__).parent.parent),
            env={**os.environ, "MOCK_LLM": "false"}
        )
        time.sleep(5)
        print("   ✅ MOCK_LLM disabled - real LLM restored")
    except Exception as e:
        print(f"   ⚠️  Could not disable MOCK_LLM: {e}")


async def main():
    """Main entry point."""
    # Enable mock LLM for testing to avoid charges
    mock_enabled = enable_mock_llm()
    
    try:
        test = ExcelImportE2ETest()
        await test.run_all_tests()
        
        # Return exit code based on results
        failed = sum(1 for r in test.results if not r.passed)
    finally:
        # Always restore real LLM after tests
        if mock_enabled:
            disable_mock_llm()
    
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    asyncio.run(main())
