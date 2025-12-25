"""
Browser-based E2E Test for KPI Configuration UI

This test uses Playwright to:
1. Launch a headless browser
2. Navigate to the KPI configuration UI
3. Capture console.log, console.error, and network failures
4. Report frontend errors alongside backend errors

Run directly:
    python tests/test_kpi_config_browser_e2e.py
    
Or with pytest:
    pytest tests/test_kpi_config_browser_e2e.py -v
"""

import asyncio
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple

from playwright.async_api import async_playwright, Page, ConsoleMessage, Response, Request

# Configuration
CONFIG_UI_URL = os.getenv("CONFIG_UI_URL", "http://127.0.0.1:3000")
API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://127.0.0.1:8090")
METADATA_SERVICE_URL = os.getenv("METADATA_SERVICE_URL", "http://127.0.0.1:8020")

# Containers to monitor
MONITORED_CONTAINERS = [
    "analyticsengine-api_gateway-1",
    "analyticsengine-business_metadata-1",
    "analyticsengine-demo_config_service-1",
]

# Error patterns for Docker logs
ERROR_PATTERNS = [
    r"ERROR",
    r"Exception",
    r"Traceback",
    r"Failed",
    r"Connection refused",
    r"TimeoutError",
]


@dataclass
class ConsoleEntry:
    """Captured browser console entry."""
    type: str  # 'log', 'error', 'warning', 'info'
    text: str
    timestamp: float
    
    def __str__(self):
        return f"[{self.type.upper()}] {self.text[:150]}"


@dataclass
class NetworkEntry:
    """Captured network request/response."""
    url: str
    method: str
    status: int
    ok: bool
    timestamp: float
    error: Optional[str] = None
    
    def __str__(self):
        status_icon = "✅" if self.ok else "❌"
        return f"{status_icon} {self.method} {self.url} -> {self.status}"


@dataclass
class BrowserTestResult:
    """Container for browser test results."""
    name: str
    passed: bool = False
    error: Optional[str] = None
    duration: float = 0.0
    console_logs: List[ConsoleEntry] = field(default_factory=list)
    console_errors: List[ConsoleEntry] = field(default_factory=list)
    network_failures: List[NetworkEntry] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        icon = "✅" if self.passed else "❌"
        status = "PASS" if self.passed else "FAIL"
        return f"{icon} {status} {self.name} ({self.duration:.2f}s)"


def get_container_logs(container_name: str, since_seconds: int = 60) -> Tuple[bool, List[str]]:
    """Get recent logs from a Docker container and check for errors."""
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
                    if "healthcheck" in line.lower():
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


class KPIConfigBrowserE2ETest:
    """Browser-based E2E test suite for KPI Configuration UI."""
    
    def __init__(self):
        self.results: List[BrowserTestResult] = []
        self.console_entries: List[ConsoleEntry] = []
        self.network_entries: List[NetworkEntry] = []
        self.page: Optional[Page] = None
    
    def _on_console(self, msg: ConsoleMessage):
        """Handle browser console messages."""
        entry = ConsoleEntry(
            type=msg.type,
            text=msg.text,
            timestamp=time.time()
        )
        self.console_entries.append(entry)
        
        # Print errors and important warnings immediately
        if msg.type == "error":
            print(f"     🔴 Console Error: {msg.text[:100]}")
        elif msg.type == "warning" and any(x in msg.text.lower() for x in ["mui", "react", "invalid", "failed", "timeout", "axios"]):
            print(f"     🟡 Console Warning: {msg.text[:100]}")
    
    def _on_response(self, response: Response):
        """Handle network responses."""
        entry = NetworkEntry(
            url=response.url,
            method=response.request.method,
            status=response.status,
            ok=response.ok,
            timestamp=time.time()
        )
        self.network_entries.append(entry)
        
        # Print failed requests immediately
        if not response.ok and response.status >= 400:
            print(f"     🔴 Network Error: {response.request.method} {response.url} -> {response.status}")
    
    def _on_request_failed(self, request: Request):
        """Handle failed network requests (timeouts, connection errors)."""
        failure = request.failure
        error_text = failure if failure else "Unknown failure"
        entry = NetworkEntry(
            url=request.url,
            method=request.method,
            status=0,  # No status for failed requests
            ok=False,
            timestamp=time.time(),
            error=error_text
        )
        self.network_entries.append(entry)
        
        # Print failed requests immediately
        print(f"     🔴 Request Failed: {request.method} {request.url[:80]} - {error_text}")
    
    def _get_recent_console_errors(self, since: float) -> List[ConsoleEntry]:
        """Get console errors since a timestamp."""
        return [e for e in self.console_entries if e.type == "error" and e.timestamp >= since]
    
    def _get_recent_network_failures(self, since: float) -> List[NetworkEntry]:
        """Get network failures since a timestamp."""
        return [e for e in self.network_entries if not e.ok and e.timestamp >= since]
    
    async def test_page_loads(self) -> BrowserTestResult:
        """Test that the config page loads successfully."""
        result = BrowserTestResult(name="Page Loads")
        start = time.time()
        test_start = start
        
        try:
            # Use domcontentloaded instead of networkidle to avoid WebSocket retry delays
            await self.page.goto(CONFIG_UI_URL, wait_until="domcontentloaded", timeout=30000)
            # Wait for React to mount
            await self.page.wait_for_timeout(3000)
            
            # Check for React error boundary
            error_boundary = await self.page.query_selector('[class*="error"], [class*="Error"]')
            if error_boundary:
                error_text = await error_boundary.text_content()
                if "error" in error_text.lower():
                    result.error = f"React error boundary triggered: {error_text[:100]}"
                    result.passed = False
                    return result
            
            # Check page title or main content
            title = await self.page.title()
            result.details["title"] = title
            result.passed = True
            
        except Exception as e:
            result.error = str(e)
            result.passed = False
        
        result.duration = time.time() - start
        result.console_errors = self._get_recent_console_errors(test_start)
        result.network_failures = self._get_recent_network_failures(test_start)
        return result
    
    async def test_kpi_list_loads(self) -> BrowserTestResult:
        """Test that KPIs load in the UI."""
        result = BrowserTestResult(name="KPI List Loads")
        start = time.time()
        test_start = start
        
        try:
            # Wait for KPI data to load - look for common KPI-related elements
            await self.page.wait_for_selector(
                '[data-testid="kpi-list"], [class*="kpi"], [class*="metric"], table, ul',
                timeout=15000
            )
            
            # Try to count loaded items
            kpi_elements = await self.page.query_selector_all(
                '[data-testid*="kpi"], [class*="kpi-item"], [class*="metric-item"], tr, li'
            )
            result.details["element_count"] = len(kpi_elements)
            
            # Check for loading states
            loading = await self.page.query_selector('[class*="loading"], [class*="spinner"]')
            if loading:
                is_visible = await loading.is_visible()
                if is_visible:
                    # Wait a bit more for loading to complete
                    await self.page.wait_for_timeout(3000)
            
            result.passed = True
            
        except Exception as e:
            result.error = str(e)
            result.passed = False
        
        result.duration = time.time() - start
        result.console_errors = self._get_recent_console_errors(test_start)
        result.network_failures = self._get_recent_network_failures(test_start)
        return result
    
    async def test_api_calls_succeed(self) -> BrowserTestResult:
        """Verify that API calls from the frontend succeed."""
        result = BrowserTestResult(name="API Calls Succeed")
        start = time.time()
        
        try:
            # Analyze captured network entries for API calls
            api_calls = [e for e in self.network_entries if "/api/" in e.url]
            failed_calls = [e for e in api_calls if not e.ok]
            
            result.details["total_api_calls"] = len(api_calls)
            result.details["failed_calls"] = len(failed_calls)
            
            if failed_calls:
                result.details["failures"] = [
                    f"{e.method} {e.url} -> {e.status}" for e in failed_calls[:5]
                ]
                result.error = f"{len(failed_calls)} API calls failed"
                result.passed = False
            else:
                result.passed = True
                
        except Exception as e:
            result.error = str(e)
            result.passed = False
        
        result.duration = time.time() - start
        return result
    
    async def test_no_console_errors(self) -> BrowserTestResult:
        """Verify no JavaScript errors or MUI/React warnings in console."""
        result = BrowserTestResult(name="No Console Errors")
        start = time.time()
        
        try:
            # Check both errors AND warnings (MUI often logs as warning)
            errors = [e for e in self.console_entries if e.type == "error"]
            warnings = [e for e in self.console_entries if e.type == "warning"]
            
            # Filter out known benign errors (but NOT network errors - those are real!)
            real_errors = []
            for err in errors:
                text_lower = err.text.lower()
                # Skip ONLY React DevTools, hot reload
                if any(x in text_lower for x in [
                    "devtools", "hot module", "hmr", 
                    "favicon", "manifest.json"
                ]):
                    continue
                # Keep all errors - test should detect them so we can fix them
                real_errors.append(err)
            
            # Check for MUI/React/Axios warnings and errors logged as warnings
            mui_react_warnings = []
            for warn in warnings:
                text_lower = warn.text.lower()
                # Catch MUI, React, Axios, and component-related warnings
                if any(x in text_lower for x in [
                    "mui:", "material-ui", "react", "invalid prop", 
                    "failed prop", "component is changing", "unique key",
                    "cannot update", "memory leak", "deprecated",
                    "axios", "timeout", "econnaborted", "err_connection",
                    "network error", "failed to fetch"
                ]):
                    # Skip expected deprecation warnings
                    if "strict mode" in text_lower:
                        continue
                    mui_react_warnings.append(warn)
            
            result.details["total_errors"] = len(errors)
            result.details["filtered_errors"] = len(real_errors)
            result.details["mui_react_warnings"] = len(mui_react_warnings)
            
            all_issues = real_errors + mui_react_warnings
            if all_issues:
                result.details["issues"] = [e.text[:100] for e in all_issues[:5]]
                result.error = f"{len(real_errors)} errors, {len(mui_react_warnings)} MUI/React warnings"
                result.passed = False
            else:
                result.passed = True
                
        except Exception as e:
            result.error = str(e)
            result.passed = False
        
        result.duration = time.time() - start
        return result
    
    async def test_hard_refresh(self) -> BrowserTestResult:
        """Test hard refresh to force fresh API calls and detect network issues."""
        result = BrowserTestResult(name="Hard Refresh")
        start = time.time()
        test_start = start
        
        try:
            # Clear entries to get fresh count
            pre_refresh_console = len(self.console_entries)
            pre_refresh_network = len(self.network_entries)
            
            # Hard refresh - bypasses cache
            await self.page.reload(wait_until="domcontentloaded")
            # Wait 35 seconds to catch Axios 30s timeouts
            print("     ⏳ Waiting 35s to catch timeout errors...")
            await self.page.wait_for_timeout(35000)
            
            # Count new network entries
            new_network = self.network_entries[pre_refresh_network:]
            new_console = self.console_entries[pre_refresh_console:]
            
            # Frontend calls localhost:8090 (gateway) for API, but SystemMonitorPage checks services directly
            # Exclude /health calls - those are intentional monitoring and may fail intermittently
            api_calls = [e for e in new_network if any(x in e.url for x in [
                "/api/", ":8090"
            ]) and not e.url.endswith(".js") and not e.url.endswith(".css") 
              and "/health" not in e.url]
            failed_network = [e for e in api_calls if not e.ok]
            
            # Check console for AxiosError, timeout, connection errors
            console_errors = []
            for entry in new_console:
                if entry.type != "error":
                    continue
                text_lower = entry.text.lower()
                # Skip WebSocket errors
                if "websocket" in text_lower:
                    continue
                # Catch real errors
                if any(x in text_lower for x in [
                    "axioserror", "timeout", "err_connection", "net::",
                    "error:", "failed", "econnaborted", "econnreset"
                ]):
                    console_errors.append(entry)
            
            result.details["new_requests"] = len(new_network)
            result.details["api_calls"] = len(api_calls)
            result.details["failed_network"] = len(failed_network)
            result.details["console_errors"] = len(console_errors)
            
            all_failures = []
            if failed_network:
                all_failures.extend([
                    f"Network: {e.method} {e.url[-50:]} -> {e.status} {e.error or ''}" 
                    for e in failed_network[:3]
                ])
            if console_errors:
                all_failures.extend([
                    f"Console: {e.text[:80]}" 
                    for e in console_errors[:3]
                ])
            
            if all_failures:
                result.details["failures"] = all_failures
                result.error = f"{len(failed_network)} network failures, {len(console_errors)} console errors"
                result.passed = False
            else:
                result.passed = True
                
        except Exception as e:
            result.error = str(e)
            result.passed = False
        
        result.duration = time.time() - start
        result.console_errors = self._get_recent_console_errors(test_start)
        result.network_failures = self._get_recent_network_failures(test_start)
        return result
    
    async def test_navigation(self) -> BrowserTestResult:
        """Test navigation between pages."""
        result = BrowserTestResult(name="Navigation Works")
        start = time.time()
        test_start = start
        
        try:
            # Try clicking on a KPI item if available
            kpi_link = await self.page.query_selector(
                'a[href*="kpi"], a[href*="metric"], [data-testid*="kpi"] a, button:has-text("View")'
            )
            
            if kpi_link:
                await kpi_link.click()
                await self.page.wait_for_timeout(2000)
                
                # Check URL changed or content updated
                current_url = self.page.url
                result.details["navigated_to"] = current_url
                
                # Go back
                await self.page.go_back()
                await self.page.wait_for_timeout(1000)
                
                result.passed = True
            else:
                result.details["note"] = "No navigation elements found"
                result.passed = True  # Not a failure, just no nav elements
                
        except Exception as e:
            result.error = str(e)
            result.passed = False
        
        result.duration = time.time() - start
        result.console_errors = self._get_recent_console_errors(test_start)
        result.network_failures = self._get_recent_network_failures(test_start)
        return result
    
    async def run_all_tests(self):
        """Run all browser E2E tests."""
        print("\n" + "="*60)
        print("  KPI CONFIGURATION BROWSER E2E TEST SUITE")
        print("="*60)
        print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Target: {CONFIG_UI_URL}")
        print("="*60 + "\n")
        
        async with async_playwright() as p:
            # Launch browser
            print("🌐 Launching browser...")
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1280, "height": 720}
            )
            self.page = await context.new_page()
            
            # Set up listeners
            self.page.on("console", self._on_console)
            self.page.on("response", self._on_response)
            self.page.on("requestfailed", self._on_request_failed)
            
            print("✅ Browser ready\n")
            print("-"*60)
            print("🔄 Running Browser Tests...\n")
            
            # Run tests
            tests = [
                ("Page Load", self.test_page_loads()),
                ("KPI List", self.test_kpi_list_loads()),
                ("Hard Refresh", self.test_hard_refresh()),  # Force fresh API calls
                ("Navigation", self.test_navigation()),
                ("API Calls", self.test_api_calls_succeed()),
                ("Console Errors", self.test_no_console_errors()),
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
                
                # Show console errors
                if result.console_errors:
                    print(f"     📋 Console Errors ({len(result.console_errors)}):")
                    for err in result.console_errors[:3]:
                        print(f"        • {err.text[:80]}...")
                
                # Show network failures
                if result.network_failures:
                    print(f"     📋 Network Failures ({len(result.network_failures)}):")
                    for fail in result.network_failures[:3]:
                        print(f"        • {fail.method} {fail.url[:60]} -> {fail.status}")
                
                # Show details
                if result.details:
                    for k, v in result.details.items():
                        if k not in ['errors', 'failures']:
                            print(f"     • {k}: {v}")
                
                # Scan Docker logs on failure
                if not result.passed:
                    container_errors = scan_all_container_logs(since_seconds=int(test_duration) + 10)
                    if container_errors:
                        print(f"     📋 Container Errors:")
                        for container, errors in container_errors.items():
                            short_name = container.replace("analyticsengine-", "").replace("-1", "")
                            print(f"        [{short_name}]:")
                            for err in errors[:2]:
                                err_display = err[:100] + "..." if len(err) > 100 else err
                                print(f"          • {err_display}")
                
                print()
            
            # Cleanup
            await browser.close()
        
        self.print_summary()
    
    def print_summary(self):
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
        
        # Console/Network summary
        total_console_errors = len([e for e in self.console_entries if e.type == "error"])
        total_network_failures = len([e for e in self.network_entries if not e.ok])
        
        print(f"\n  📊 Browser Metrics:")
        print(f"     • Total Console Errors: {total_console_errors}")
        print(f"     • Total Network Failures: {total_network_failures}")
        print(f"     • Total API Calls Captured: {len([e for e in self.network_entries if '/api/' in e.url])}")
        
        if failed > 0:
            print(f"\n  FAILED TESTS:")
            for r in self.results:
                if not r.passed:
                    print(f"    • {r.name}: {r.error}")
        
        print("\n" + "="*60)
        if failed == 0:
            print("  🎉 ALL TESTS PASSED!")
        else:
            print("  ⚠️  SOME TESTS FAILED - Review errors above")
        print("="*60 + "\n")


async def main():
    """Run the browser E2E tests."""
    test_suite = KPIConfigBrowserE2ETest()
    await test_suite.run_all_tests()
    
    # Exit with appropriate code
    failed = sum(1 for r in test_suite.results if not r.passed)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
