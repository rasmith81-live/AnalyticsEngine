"""
Browser-based E2E Test for Ontology Studio Page

Uses Playwright to load the page in a real browser and capture console errors.

Usage:
    python tests/test_ontology_studio_browser.py
    
Requirements:
    pip install playwright
    playwright install chromium
"""

import asyncio
import sys
import json
from typing import List, Dict, Any

try:
    from playwright.async_api import async_playwright, ConsoleMessage, Error
except ImportError:
    print("❌ Playwright not installed. Install with: pip install playwright && playwright install chromium")
    sys.exit(1)

FRONTEND_URL = "http://127.0.0.1:3000"
ONTOLOGY_STUDIO_URL = f"{FRONTEND_URL}/ontology-studio"


class BrowserTestResult:
    def __init__(self):
        self.console_errors: List[str] = []
        self.console_warnings: List[str] = []
        self.console_logs: List[str] = []
        self.page_errors: List[str] = []
        self.network_errors: List[Dict[str, Any]] = []
        self.page_loaded: bool = False
        self.graph_visible: bool = False
        self.screenshot_path: str = ""


async def test_ontology_studio_page():
    """Load the Ontology Studio page and capture all console output."""
    result = BrowserTestResult()
    
    print("\n" + "="*60)
    print("🌐 BROWSER-BASED ONTOLOGY STUDIO TEST")
    print("="*60 + "\n")
    
    async with async_playwright() as p:
        print("🚀 Launching browser...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Capture console messages
        def handle_console(msg: ConsoleMessage):
            text = msg.text
            msg_type = msg.type
            
            if msg_type == "error":
                result.console_errors.append(text)
                print(f"  ❌ Console Error: {text[:200]}")
            elif msg_type == "warning":
                result.console_warnings.append(text)
            else:
                result.console_logs.append(text)
        
        page.on("console", handle_console)
        
        # Capture page errors (uncaught exceptions)
        def handle_page_error(error: Error):
            result.page_errors.append(str(error))
            print(f"  💥 Page Error: {str(error)[:200]}")
        
        page.on("pageerror", handle_page_error)
        
        # Capture failed network requests
        def handle_request_failed(request):
            result.network_errors.append({
                "url": request.url,
                "method": request.method,
                "failure": request.failure
            })
            print(f"  🔴 Network Error: {request.method} {request.url[:100]}")
        
        page.on("requestfailed", handle_request_failed)
        
        try:
            # First load the main page
            print(f"📄 Loading main page: {FRONTEND_URL}")
            await page.goto(FRONTEND_URL, wait_until="networkidle", timeout=30000)
            await asyncio.sleep(2)
            
            # Navigate to Ontology Studio
            print(f"📄 Navigating to Ontology Studio: {ONTOLOGY_STUDIO_URL}")
            await page.goto(ONTOLOGY_STUDIO_URL, wait_until="networkidle", timeout=30000)
            
            # Wait for page to settle
            print("⏳ Waiting for page to render...")
            await asyncio.sleep(5)
            
            result.page_loaded = True
            
            # Check if the page has content
            body_text = await page.inner_text("body")
            
            if "Ontology Studio" in body_text:
                print("✅ Page title 'Ontology Studio' found")
            else:
                print(f"⚠️ Page title not found. Body text: {body_text[:200]}")
            
            # Check for graph container
            try:
                graph_container = await page.query_selector("canvas")
                if graph_container:
                    result.graph_visible = True
                    print("✅ Canvas element found (graph may be rendering)")
                else:
                    print("⚠️ No canvas element found")
            except Exception as e:
                print(f"⚠️ Error checking for canvas: {e}")
            
            # Try to select a value chain filter to see fewer nodes
            try:
                filter_select = await page.query_selector('[id="vc-filter-label"]')
                if filter_select:
                    print("✅ Value chain filter found")
                    # Click on the select to open dropdown
                    select_element = await page.query_selector('.MuiSelect-select')
                    if select_element:
                        await select_element.click()
                        await asyncio.sleep(1)
                        # Select first option (supply_chain)
                        menu_item = await page.query_selector('li[data-value="supply_chain"]')
                        if menu_item:
                            await menu_item.click()
                            await asyncio.sleep(2)
                            print("✅ Filtered by supply_chain value chain")
            except Exception as e:
                print(f"⚠️ Could not test filter: {e}")
            
            # Take screenshot
            screenshot_path = "test_results/ontology_studio_screenshot.png"
            try:
                import os
                os.makedirs("test_results", exist_ok=True)
                await page.screenshot(path=screenshot_path, full_page=True)
                result.screenshot_path = screenshot_path
                print(f"📸 Screenshot saved to: {screenshot_path}")
            except Exception as e:
                print(f"⚠️ Could not save screenshot: {e}")
            
            # Get page HTML for debugging
            html = await page.content()
            html_path = "test_results/ontology_studio_page.html"
            try:
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"📝 HTML saved to: {html_path}")
            except Exception as e:
                print(f"⚠️ Could not save HTML: {e}")
            
        except Exception as e:
            print(f"💥 Error during test: {e}")
            result.page_errors.append(str(e))
        
        await browser.close()
    
    return result


def print_results(result: BrowserTestResult):
    """Print test results summary."""
    print("\n" + "="*60)
    print("📊 BROWSER TEST RESULTS")
    print("="*60 + "\n")
    
    print(f"Page Loaded: {'✅ Yes' if result.page_loaded else '❌ No'}")
    print(f"Graph Visible: {'✅ Yes' if result.graph_visible else '❌ No'}")
    print(f"Console Errors: {len(result.console_errors)}")
    print(f"Console Warnings: {len(result.console_warnings)}")
    print(f"Page Errors: {len(result.page_errors)}")
    print(f"Network Errors: {len(result.network_errors)}")
    
    if result.console_errors:
        print("\n" + "-"*60)
        print("❌ CONSOLE ERRORS:")
        print("-"*60)
        for i, error in enumerate(result.console_errors[:10], 1):
            print(f"{i}. {error[:500]}")
    
    if result.page_errors:
        print("\n" + "-"*60)
        print("💥 PAGE ERRORS (Uncaught Exceptions):")
        print("-"*60)
        for i, error in enumerate(result.page_errors[:10], 1):
            print(f"{i}. {error[:500]}")
    
    if result.network_errors:
        print("\n" + "-"*60)
        print("🔴 NETWORK ERRORS:")
        print("-"*60)
        for i, error in enumerate(result.network_errors[:10], 1):
            print(f"{i}. {error['method']} {error['url'][:100]} - {error.get('failure', 'Unknown')}")
    
    if result.screenshot_path:
        print(f"\n📸 Screenshot: {result.screenshot_path}")
    
    # Determine overall result
    has_critical_errors = len(result.page_errors) > 0 or len(result.console_errors) > 0
    
    if has_critical_errors:
        print("\n❌ TEST FAILED - Console/Page errors detected")
        return False
    elif not result.page_loaded:
        print("\n❌ TEST FAILED - Page did not load")
        return False
    else:
        print("\n✅ TEST PASSED")
        return True


async def main():
    result = await test_ontology_studio_page()
    success = print_results(result)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
