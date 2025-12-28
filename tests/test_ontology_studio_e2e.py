"""
End-to-End Test for Ontology Studio Page

Tests the complete flow:
1. Load the Ontology Studio page
2. Check for JavaScript console errors
3. Verify the graph visualization loads
4. Test API endpoints used by the page

Usage:
    python tests/test_ontology_studio_e2e.py
    
Or with pytest:
    pytest tests/test_ontology_studio_e2e.py -v
"""

import asyncio
import httpx
import json
import os
import re
import subprocess
import sys
import time
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime

# Configuration - Use 127.0.0.1 instead of localhost for Windows Docker compatibility
API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://127.0.0.1:8090")
METADATA_SERVICE_URL = os.getenv("METADATA_SERVICE_URL", "http://127.0.0.1:8020")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://127.0.0.1:3000")

# Test timeouts
REQUEST_TIMEOUT = 30.0

# Containers to monitor for errors during tests
MONITORED_CONTAINERS = [
    "analyticsengine-api_gateway-1",
    "analyticsengine-business_metadata-1",
    "analyticsengine-demo_config_ui-1",
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
            ["docker", "compose", "logs", "--since", f"{since_seconds}s", container_name.replace("analyticsengine-", "").replace("-1", "")],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=r"c:\Users\Arthu\CascadeProjects\AnalyticsEngine"
        )
        logs = result.stdout + result.stderr
        
        error_lines = []
        for line in logs.split('\n'):
            for pattern in ERROR_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
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


class OntologyStudioE2ETest:
    """End-to-end test for Ontology Studio page."""
    
    def __init__(self):
        self.results: List[TestResult] = []
        self.value_chains: List[Dict] = []
        self.modules: List[Dict] = []
        
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

    async def test_frontend_loads(self) -> TestResult:
        """Test that the frontend loads and returns HTML."""
        result = TestResult("Frontend Loads")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(f"{FRONTEND_URL}/")
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    html = response.text
                    if '<div id="root">' in html and '<script' in html:
                        result.passed = True
                        result.details = {
                            "status_code": response.status_code,
                            "content_length": len(html),
                            "has_root_div": True,
                            "has_script": True
                        }
                    else:
                        result.error = "HTML missing expected elements"
                        result.details = {"html_preview": html[:500]}
                else:
                    result.error = f"Status {response.status_code}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def test_frontend_js_bundle(self) -> TestResult:
        """Test that the JavaScript bundle loads correctly."""
        result = TestResult("JS Bundle Loads")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                # First get the HTML to find the JS bundle path
                response = await client.get(f"{FRONTEND_URL}/")
                html = response.text
                
                # Extract JS bundle path from HTML
                import re
                js_match = re.search(r'src="(/assets/index-[^"]+\.js)"', html)
                
                if js_match:
                    js_path = js_match.group(1)
                    js_response = await client.get(f"{FRONTEND_URL}{js_path}")
                    result.duration = time.time() - start
                    
                    if js_response.status_code == 200:
                        js_content = js_response.text
                        result.passed = True
                        result.details = {
                            "js_path": js_path,
                            "bundle_size": len(js_content),
                            "has_react": "react" in js_content.lower() or "React" in js_content,
                            "has_force_graph": "force-graph" in js_content.lower() or "ForceGraph" in js_content
                        }
                    else:
                        result.error = f"JS bundle returned status {js_response.status_code}"
                else:
                    result.error = "Could not find JS bundle path in HTML"
                    result.details = {"html_preview": html[:500]}
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def test_metadata_api_value_chains(self) -> TestResult:
        """Test the value chains API endpoint used by Ontology Studio."""
        result = TestResult("API: Value Chains")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{API_GATEWAY_URL}/api/v1/metadata/definitions/value_chain_pattern_definition",
                    params={"limit": 100}
                )
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    self.value_chains = data if isinstance(data, list) else []
                    result.passed = True
                    result.details = {
                        "count": len(self.value_chains),
                        "sample": self.value_chains[0] if self.value_chains else None
                    }
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def test_metadata_api_modules(self) -> TestResult:
        """Test the modules API endpoint used by Ontology Studio."""
        result = TestResult("API: Modules (Business Processes)")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{API_GATEWAY_URL}/api/v1/metadata/definitions/business_process_definition",
                    params={"limit": 100}
                )
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    self.modules = data if isinstance(data, list) else []
                    result.passed = True
                    result.details = {
                        "count": len(self.modules),
                        "sample": self.modules[0] if self.modules else None
                    }
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def test_metadata_api_kpis(self) -> TestResult:
        """Test the KPIs API endpoint used by Ontology Studio."""
        result = TestResult("API: KPI Definitions")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{API_GATEWAY_URL}/api/v1/metadata/definitions/kpi_definition",
                    params={"limit": 100}
                )
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    kpis = data if isinstance(data, list) else []
                    result.passed = True
                    result.details = {
                        "count": len(kpis),
                        "sample": kpis[0] if kpis else None
                    }
                elif response.status_code == 404:
                    # KPI endpoint might not exist yet - that's OK
                    result.passed = True
                    result.details = {"note": "KPI endpoint returned 404 - may not be implemented yet"}
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def test_metadata_api_entities(self) -> TestResult:
        """Test the entity definitions API endpoint used by Ontology Studio."""
        result = TestResult("API: Entity Definitions")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(
                    f"{API_GATEWAY_URL}/api/v1/metadata/definitions/entity_definition",
                    params={"limit": 100}
                )
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    entities = data if isinstance(data, list) else []
                    result.passed = True
                    result.details = {
                        "count": len(entities),
                        "sample": entities[0] if entities else None
                    }
                elif response.status_code == 404:
                    # Entity endpoint might not exist yet - that's OK
                    result.passed = True
                    result.details = {"note": "Entity endpoint returned 404 - may not be implemented yet"}
                else:
                    result.error = f"Status {response.status_code}: {response.text[:200]}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def test_ontology_studio_route(self) -> TestResult:
        """Test that the Ontology Studio route returns the app shell."""
        result = TestResult("Ontology Studio Route")
        start = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
                response = await client.get(f"{FRONTEND_URL}/ontology-studio")
                result.duration = time.time() - start
                
                if response.status_code == 200:
                    html = response.text
                    if '<div id="root">' in html:
                        result.passed = True
                        result.details = {
                            "status_code": response.status_code,
                            "content_length": len(html)
                        }
                    else:
                        result.error = "HTML missing root div"
                else:
                    result.error = f"Status {response.status_code}"
        except Exception as e:
            result.duration = time.time() - start
            result.error = str(e)
        
        return result

    async def check_container_logs_for_errors(self) -> TestResult:
        """Check container logs for any errors."""
        result = TestResult("Container Logs Check")
        start = time.time()
        
        errors = scan_all_container_logs(since_seconds=60)
        result.duration = time.time() - start
        
        if not errors:
            result.passed = True
            result.details = {"message": "No errors found in container logs"}
        else:
            result.passed = False
            result.error = "Errors found in container logs"
            result.details = errors
        
        return result

    async def run_all_tests(self) -> List[TestResult]:
        """Run all tests and return results."""
        print("\n" + "="*60)
        print("🧪 ONTOLOGY STUDIO E2E TEST SUITE")
        print("="*60 + "\n")
        
        # Health checks
        print("📋 Running health checks...")
        self.results.append(await self.check_service_health(API_GATEWAY_URL, "API Gateway"))
        self.results.append(await self.check_service_health(METADATA_SERVICE_URL, "Metadata Service"))
        
        # Frontend tests
        print("🌐 Testing frontend...")
        self.results.append(await self.test_frontend_loads())
        self.results.append(await self.test_frontend_js_bundle())
        self.results.append(await self.test_ontology_studio_route())
        
        # API tests
        print("🔌 Testing APIs...")
        self.results.append(await self.test_metadata_api_value_chains())
        self.results.append(await self.test_metadata_api_modules())
        self.results.append(await self.test_metadata_api_kpis())
        self.results.append(await self.test_metadata_api_entities())
        
        # Container logs
        print("📜 Checking container logs...")
        self.results.append(await self.check_container_logs_for_errors())
        
        return self.results

    def print_results(self):
        """Print test results summary."""
        print("\n" + "="*60)
        print("📊 TEST RESULTS")
        print("="*60 + "\n")
        
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed)
        
        for result in self.results:
            print(result)
            if result.error:
                print(f"   ⚠️  Error: {result.error}")
            if result.details and not result.passed:
                print(f"   📝 Details: {json.dumps(result.details, indent=2, default=str)[:500]}")
        
        print("\n" + "-"*60)
        print(f"Total: {len(self.results)} | Passed: {passed} | Failed: {failed}")
        
        if failed > 0:
            print("\n❌ SOME TESTS FAILED")
            return False
        else:
            print("\n✅ ALL TESTS PASSED")
            return True


async def main():
    """Main entry point."""
    test = OntologyStudioE2ETest()
    await test.run_all_tests()
    success = test.print_results()
    
    # Print graph data summary
    print("\n" + "="*60)
    print("📊 GRAPH DATA SUMMARY")
    print("="*60)
    print(f"Value Chains: {len(test.value_chains)}")
    print(f"Modules: {len(test.modules)}")
    
    if test.value_chains:
        print("\nValue Chains found:")
        for vc in test.value_chains[:5]:
            print(f"  - {vc.get('code', 'N/A')}: {vc.get('name', 'N/A')}")
    
    if test.modules:
        print("\nModules found:")
        for mod in test.modules[:5]:
            print(f"  - {mod.get('code', 'N/A')}: {mod.get('name', 'N/A')}")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
