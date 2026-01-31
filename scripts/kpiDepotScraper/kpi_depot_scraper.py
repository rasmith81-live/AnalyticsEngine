"""
KPI Depot Web Scraper

Playwright-based scraper to collect KPI definitions from kpidepot.com
Uses authenticated browser session to access subscriber content.

Usage:
    python kpi_depot_scraper.py --category supply-chain
    python kpi_depot_scraper.py --all
    python kpi_depot_scraper.py --url https://kpidepot.com/kpi-supply-chain/buying-87
"""

import asyncio
import json
import re
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict, field
import argparse

from playwright.async_api import async_playwright, Browser, Page, BrowserContext


@dataclass
class KPIAttributes:
    """Extended KPI attributes from 'View All KPI Attributes' section."""
    trend_analysis: str = ""
    diagnostic_questions: List[str] = field(default_factory=list)
    actionable_tips: List[str] = field(default_factory=list)
    visualization_suggestions: List[str] = field(default_factory=list)
    risk_warnings: List[str] = field(default_factory=list)
    tools_technologies: List[str] = field(default_factory=list)
    integration_points: List[str] = field(default_factory=list)
    change_impact: str = ""


@dataclass
class KPIDefinition:
    """Complete KPI definition from KPI Depot."""
    name: str
    code: str
    url: str
    category: str
    subcategory: str
    definition: str
    measurement_approach: str
    standard_formula: str
    attributes: KPIAttributes = field(default_factory=KPIAttributes)
    scraped_at: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        return data


class KPIDepotScraper:
    """Scraper for kpidepot.com using Playwright.
    
    Site Structure:
    - Functional categories: /kpi-supply-chain-management, /kpi-corporate-finance, etc.
    - Each category has subcategory pages: /kpi-supply-chain/buying-87, /kpi-supply-chain/sourcing-XX
    - Each subcategory page contains MULTIPLE inline KPIs with full details
    - Each KPI has: name, definition, formula, and expandable attributes section
    """
    
    BASE_URL = "https://kpidepot.com"
    
    # KPI Depot functional categories (15 functions)
    CATEGORIES = {
        "corporate-finance": "/kpi-corporate-finance",
        "corporate-marketing": "/kpi-corporate-marketing",
        "corporate-strategy": "/kpi-corporate-strategy",
        "customer-service": "/kpi-customer-service",
        "data-management": "/kpi-data-management-analysis",
        "general-council": "/kpi-general-council",
        "human-resources": "/kpi-human-resources",
        "information-technology": "/kpi-information-technology",
        "innovation-management": "/kpi-innovation-management",
        "legal": "/kpi-legal",
        "operations-management": "/kpi-operations-management",
        "product-management": "/kpi-product-management",
        "regulatory-compliance": "/kpi-regulatory-compliance",
        "sales-management": "/kpi-sales-management",
        "supply-chain-management": "/kpi-supply-chain",
    }
    
    def __init__(self, output_dir: str = None, headless: bool = False):
        """
        Initialize the scraper.
        
        Args:
            output_dir: Directory to save scraped KPIs (default: scripts/kpiDepotScraper/output)
            headless: Run browser in headless mode (default: False for auth)
        """
        self.output_dir = Path(output_dir) if output_dir else Path(__file__).parent / "output"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.headless = headless
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.scraped_kpis: List[KPIDefinition] = []
        
    async def start_browser(self, use_persistent_context: bool = True):
        """
        Start browser with persistent context for authentication.
        
        Args:
            use_persistent_context: Use persistent browser context to maintain login
        """
        self.playwright = await async_playwright().start()
        
        # User data directory for persistent login
        user_data_dir = self.output_dir / "browser_data"
        user_data_dir.mkdir(parents=True, exist_ok=True)
        
        if use_persistent_context:
            # Launch with persistent context to maintain cookies/session
            self.context = await self.playwright.chromium.launch_persistent_context(
                user_data_dir=str(user_data_dir),
                headless=self.headless,
                viewport={"width": 1920, "height": 1080},
                slow_mo=100,  # Slow down for visibility
            )
            self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()
        else:
            self.browser = await self.playwright.chromium.launch(headless=self.headless)
            self.context = await self.browser.new_context(
                viewport={"width": 1920, "height": 1080}
            )
            self.page = await self.context.new_page()
            
        print(f"✓ Browser started (headless={self.headless})")
        
    async def close_browser(self):
        """Close browser and cleanup."""
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        print("✓ Browser closed")
        
    async def wait_for_login(self, timeout: int = 300):
        """
        Navigate to site and wait for user to login if needed.
        
        Args:
            timeout: Seconds to wait for manual login
        """
        await self.page.goto(self.BASE_URL)
        await self.page.wait_for_load_state("networkidle")
        
        # Check if logged in by looking for subscriber-only elements
        # Adjust selector based on actual site structure
        is_logged_in = await self._check_login_status()
        
        if not is_logged_in:
            print("\n" + "="*60)
            print("⚠ Please log in to your KPI Depot account in the browser window")
            print("  The scraper will continue automatically once logged in.")
            print(f"  Timeout: {timeout} seconds")
            print("="*60 + "\n")
            
            # Wait for login (check periodically)
            start_time = asyncio.get_event_loop().time()
            while not is_logged_in:
                await asyncio.sleep(5)
                is_logged_in = await self._check_login_status()
                
                elapsed = asyncio.get_event_loop().time() - start_time
                if elapsed > timeout:
                    raise TimeoutError("Login timeout exceeded")
                    
        print("✓ Logged in successfully")
        return True
        
    async def _check_login_status(self) -> bool:
        """Check if user is logged in. Adjust selectors based on actual site."""
        try:
            # Look for common logged-in indicators
            # These selectors need to be adjusted based on actual site structure
            logged_in_indicators = [
                'text="My Account"',
                'text="Logout"',
                'text="Log Out"',
                '[data-logged-in="true"]',
                '.user-menu',
                '.account-menu',
            ]
            
            for selector in logged_in_indicators:
                try:
                    element = await self.page.query_selector(selector)
                    if element:
                        return True
                except:
                    continue
                    
            return False
        except:
            return False
            
    async def get_category_kpi_links(self, category: str) -> List[Dict[str, str]]:
        """
        Get all KPI links from a category page.
        
        Args:
            category: Category key from CATEGORIES dict
            
        Returns:
            List of dicts with 'name', 'url', 'subcategory'
        """
        if category not in self.CATEGORIES:
            print(f"✗ Unknown category: {category}")
            return []
            
        category_url = f"{self.BASE_URL}{self.CATEGORIES[category]}"
        print(f"\n📂 Scanning category: {category}")
        print(f"   URL: {category_url}")
        
        await self.page.goto(category_url)
        await self.page.wait_for_load_state("networkidle")
        
        kpi_links = []
        
        # Find all KPI links on the category page
        # Adjust selectors based on actual site structure
        link_selectors = [
            'a[href*="/kpi-"]',  # Links containing /kpi-
            '.kpi-item a',
            '.kpi-link',
            '.kpi-card a',
            'article a',
        ]
        
        for selector in link_selectors:
            try:
                links = await self.page.query_selector_all(selector)
                for link in links:
                    href = await link.get_attribute('href')
                    text = await link.inner_text()
                    
                    if href and text and self._is_kpi_detail_url(href):
                        full_url = href if href.startswith('http') else f"{self.BASE_URL}{href}"
                        
                        # Extract subcategory from URL if present
                        subcategory = self._extract_subcategory(href, category)
                        
                        kpi_links.append({
                            'name': text.strip(),
                            'url': full_url,
                            'subcategory': subcategory
                        })
            except Exception as e:
                continue
                
        # Remove duplicates
        seen_urls = set()
        unique_links = []
        for link in kpi_links:
            if link['url'] not in seen_urls:
                seen_urls.add(link['url'])
                unique_links.append(link)
                
        print(f"   Found {len(unique_links)} KPIs in {category}")
        return unique_links
        
    def _is_kpi_detail_url(self, url: str) -> bool:
        """Check if URL is a KPI detail page (not a category page)."""
        # KPI detail URLs typically have a number suffix like /buying-87
        return bool(re.search(r'-\d+$', url))
        
    def _extract_subcategory(self, url: str, category: str) -> str:
        """Extract subcategory from URL path."""
        # Example: /kpi-supply-chain/buying-87 -> buying
        match = re.search(rf'/kpi-{category}/([a-z-]+)-\d+$', url.lower())
        if match:
            return match.group(1).replace('-', ' ').title()
        return ""
        
    async def scrape_kpi_page(self, url: str, category: str, subcategory: str = "") -> List[KPIDefinition]:
        """
        Scrape ALL inline KPIs from an industry/subcategory page.
        
        Each page contains MULTIPLE KPIs with their definitions, formulas,
        and expandable attribute sections.
        
        Args:
            url: Full URL to industry KPI page
            category: Functional category (e.g., corporate-finance)
            subcategory: Industry name (e.g., Aerospace & Defense)
            
        Returns:
            List of KPIDefinition objects found on the page
        """
        kpis_found = []
        
        try:
            await self.page.goto(url)
            await self.page.wait_for_load_state("networkidle")
            await asyncio.sleep(1)  # Wait for dynamic content
            
            # Get page title for industry name
            page_title = await self._extract_text(['h1'])
            industry = subcategory or page_title.replace(' KPIs', '').strip()
            
            # Find all KPI entries on the page
            # KPIs are typically in containers with "View all KPI attributes" links
            kpi_containers = await self.page.query_selector_all('[onclick*="toggleDetails"], a[href*="javascript:void"]:has-text("View all KPI attributes")')
            
            if not kpi_containers:
                # Try alternative: find by structure - KPI names are often bold/strong followed by definition
                kpi_containers = await self.page.query_selector_all('.kpi-item, .kpi-entry, article, [class*="kpi"]')
            
            # Extract all KPIs using JavaScript for better access to page structure
            kpis_data = await self.page.evaluate('''() => {
                const kpis = [];
                
                // Find all "View all KPI attributes" toggles - each represents a KPI
                const toggleLinks = document.querySelectorAll('a[onclick*="toggleDetails"], a:not([href]):not([onclick])');
                
                // Alternative: Look for KPI name patterns (bold text followed by description)
                // KPI names are typically in strong/b tags or have specific styling
                const allStrong = document.querySelectorAll('strong, b, .kpi-name, h3, h4');
                
                const processedNames = new Set();
                
                allStrong.forEach((el) => {
                    const name = el.innerText.trim();
                    
                    // Skip if already processed, too short, or looks like a section header
                    if (processedNames.has(name) || name.length < 3 || name.length > 100) return;
                    if (name.includes('KPIs') || name.includes('Subscribe') || name.includes('FAQ')) return;
                    
                    // Get the parent container to find definition and other content
                    let container = el.parentElement;
                    let attempts = 0;
                    while (container && attempts < 5) {
                        const text = container.innerText;
                        // Look for container that has meaningful content
                        if (text.length > 200 && text.includes(name)) {
                            break;
                        }
                        container = container.parentElement;
                        attempts++;
                    }
                    
                    if (container) {
                        const containerText = container.innerText;
                        
                        // Extract definition - text immediately following the KPI name
                        const nameIndex = containerText.indexOf(name);
                        if (nameIndex >= 0) {
                            let defStart = nameIndex + name.length;
                            let defText = containerText.substring(defStart, defStart + 500).trim();
                            
                            // Clean up definition
                            const lines = defText.split('\\n').filter(l => l.trim());
                            const definition = lines[0] || '';
                            
                            // Look for formula patterns
                            let formula = '';
                            const formulaMatch = containerText.match(/(?:Formula|Calculation)[:\\s]*([^\\n]+)/i);
                            if (formulaMatch) {
                                formula = formulaMatch[1].trim();
                            }
                            
                            // Look for trend analysis, tips, etc.
                            const hasAttributes = containerText.includes('trend') || 
                                                 containerText.includes('diagnostic') ||
                                                 containerText.includes('actionable') ||
                                                 containerText.includes('visualization');
                            
                            if (definition.length > 10) {
                                processedNames.add(name);
                                kpis.push({
                                    name: name,
                                    definition: definition.substring(0, 500),
                                    formula: formula,
                                    hasAttributes: hasAttributes,
                                    containerIndex: Array.from(document.body.querySelectorAll('*')).indexOf(container)
                                });
                            }
                        }
                    }
                });
                
                return kpis;
            }''')
            
            # Now expand each KPI's attributes and extract full details
            for kpi_data in kpis_data:
                try:
                    # Try to click "View all KPI attributes" for this KPI
                    await self._expand_kpi_attributes(kpi_data.get('name', ''))
                    await asyncio.sleep(0.3)
                    
                    # Extract extended attributes
                    attributes = await self._extract_kpi_attributes_for_name(kpi_data.get('name', ''))
                    
                    kpi = KPIDefinition(
                        name=kpi_data.get('name', ''),
                        code=self._generate_code(kpi_data.get('name', '')),
                        url=url,
                        category=category,
                        subcategory=industry,
                        definition=kpi_data.get('definition', ''),
                        measurement_approach='',
                        standard_formula=kpi_data.get('formula', ''),
                        attributes=attributes,
                        scraped_at=datetime.now().isoformat()
                    )
                    kpis_found.append(kpi)
                    
                except Exception as e:
                    print(f"      ⚠ Error extracting KPI '{kpi_data.get('name', 'unknown')}': {e}")
                    continue
            
            print(f"   ✓ {industry}: {len(kpis_found)} KPIs extracted")
            return kpis_found
            
        except Exception as e:
            print(f"   ✗ Error scraping {url}: {e}")
            return kpis_found
    
    async def _expand_kpi_attributes(self, kpi_name: str):
        """Click the 'View all KPI attributes' link for a specific KPI."""
        try:
            # Find and click the expand link near this KPI
            await self.page.evaluate(f'''(kpiName) => {{
                const links = document.querySelectorAll('a');
                for (const link of links) {{
                    if (link.innerText.includes('View all KPI attributes')) {{
                        // Check if this link is near the KPI name
                        const container = link.closest('div, article, section');
                        if (container && container.innerText.includes(kpiName)) {{
                            link.click();
                            return true;
                        }}
                    }}
                }}
                return false;
            }}''', kpi_name)
        except:
            pass
    
    async def _extract_kpi_attributes_for_name(self, kpi_name: str) -> KPIAttributes:
        """Extract expanded attributes for a specific KPI."""
        attributes = KPIAttributes()
        
        try:
            # Extract attributes from the expanded section
            attrs_data = await self.page.evaluate(f'''(kpiName) => {{
                const result = {{
                    trend_analysis: '',
                    diagnostic_questions: [],
                    actionable_tips: [],
                    visualization_suggestions: [],
                    risk_warnings: [],
                    tools_technologies: [],
                    integration_points: [],
                    change_impact: ''
                }};
                
                // Find container with this KPI
                const allElements = document.body.innerText;
                const kpiIndex = allElements.indexOf(kpiName);
                if (kpiIndex < 0) return result;
                
                // Get text around this KPI
                const context = allElements.substring(kpiIndex, kpiIndex + 5000);
                
                // Parse trend analysis
                const trendMatch = context.match(/(?:trend|increasing|decreasing)[^.]*\\./gi);
                if (trendMatch) result.trend_analysis = trendMatch.join(' ').substring(0, 500);
                
                // Parse diagnostic questions
                const questionMatches = context.match(/[^.?]*\\?/g);
                if (questionMatches) {{
                    result.diagnostic_questions = questionMatches
                        .filter(q => q.length > 20 && q.length < 200)
                        .slice(0, 5);
                }}
                
                // Parse actionable tips (sentences with action verbs)
                const tipPatterns = context.match(/(?:Implement|Provide|Review|Regularly|Consider|Ensure|Develop|Establish)[^.]*\\./gi);
                if (tipPatterns) {{
                    result.actionable_tips = tipPatterns.slice(0, 5);
                }}
                
                // Parse visualization suggestions
                const vizMatch = context.match(/(?:chart|graph|dashboard|visualization|bar|line|heat map)[^.]*\\./gi);
                if (vizMatch) {{
                    result.visualization_suggestions = vizMatch.slice(0, 3);
                }}
                
                // Parse risk warnings
                const riskMatch = context.match(/(?:risk|warning|caution|high.*may|low.*may)[^.]*\\./gi);
                if (riskMatch) {{
                    result.risk_warnings = riskMatch.slice(0, 3);
                }}
                
                // Parse tools & technologies
                const toolMatch = context.match(/(?:software|tool|system|platform|SAP|Oracle|Microsoft)[^.]*\\./gi);
                if (toolMatch) {{
                    result.tools_technologies = toolMatch.slice(0, 3);
                }}
                
                // Parse integration points
                const intMatch = context.match(/(?:integrate|integration|link with|connect)[^.]*\\./gi);
                if (intMatch) {{
                    result.integration_points = intMatch.slice(0, 3);
                }}
                
                // Parse change impact
                const impactMatch = context.match(/(?:impact|change|investment|cost|improvement)[^.]*\\./gi);
                if (impactMatch) result.change_impact = impactMatch.join(' ').substring(0, 500);
                
                return result;
            }}''', kpi_name)
            
            if attrs_data:
                attributes.trend_analysis = attrs_data.get('trend_analysis', '')
                attributes.diagnostic_questions = attrs_data.get('diagnostic_questions', [])
                attributes.actionable_tips = attrs_data.get('actionable_tips', [])
                attributes.visualization_suggestions = attrs_data.get('visualization_suggestions', [])
                attributes.risk_warnings = attrs_data.get('risk_warnings', [])
                attributes.tools_technologies = attrs_data.get('tools_technologies', [])
                attributes.integration_points = attrs_data.get('integration_points', [])
                attributes.change_impact = attrs_data.get('change_impact', '')
                
        except Exception as e:
            pass
            
        return attributes
            
    async def _extract_text(self, selectors: List[str]) -> str:
        """Extract text from first matching selector."""
        for selector in selectors:
            try:
                element = await self.page.query_selector(selector)
                if element:
                    text = await element.inner_text()
                    return text.strip()
            except:
                continue
        return ""
        
    async def _extract_section_content(self, section_keywords: List[str]) -> str:
        """
        Extract content from a section identified by keywords.
        Looks for headings containing keywords and extracts following content.
        """
        for keyword in section_keywords:
            try:
                # Try finding by heading text
                heading_selectors = [
                    f'h2:has-text("{keyword}")',
                    f'h3:has-text("{keyword}")',
                    f'h4:has-text("{keyword}")',
                    f'.section-title:has-text("{keyword}")',
                    f'[class*="{keyword}"]',
                    f'#section-{keyword}',
                ]
                
                for selector in heading_selectors:
                    try:
                        heading = await self.page.query_selector(selector)
                        if heading:
                            # Get the next sibling or parent's next element
                            content = await self.page.evaluate('''(heading) => {
                                let content = "";
                                let next = heading.nextElementSibling;
                                while (next && !next.matches("h1, h2, h3, h4, h5")) {
                                    content += next.innerText + "\\n";
                                    next = next.nextElementSibling;
                                }
                                return content.trim();
                            }''', heading)
                            
                            if content:
                                return content
                    except:
                        continue
                        
                # Try finding by data attribute or class
                content_selectors = [
                    f'[data-section="{keyword}"]',
                    f'.{keyword}-content',
                    f'#{keyword}',
                ]
                
                for selector in content_selectors:
                    try:
                        element = await self.page.query_selector(selector)
                        if element:
                            return (await element.inner_text()).strip()
                    except:
                        continue
                        
            except:
                continue
                
        return ""
        
    async def _extract_all_attributes(self) -> KPIAttributes:
        """
        Click 'View All KPI Attributes' and extract extended attributes.
        """
        attributes = KPIAttributes()
        
        try:
            # Find and click the "View All KPI Attributes" button
            button_selectors = [
                'button:has-text("View All")',
                'button:has-text("View all KPI")',
                'a:has-text("View All")',
                '.view-all-attributes',
                '[data-action="expand-attributes"]',
                'text="View all KPI attributes"',
            ]
            
            for selector in button_selectors:
                try:
                    button = await self.page.query_selector(selector)
                    if button:
                        await button.click()
                        await self.page.wait_for_load_state("networkidle")
                        await asyncio.sleep(0.5)  # Wait for expansion
                        break
                except:
                    continue
                    
            # Extract each attribute section
            attributes.trend_analysis = await self._extract_section_content([
                'trend', 'trend-analysis', 'trends'
            ])
            
            attributes.diagnostic_questions = await self._extract_list_content([
                'diagnostic', 'diagnostic-questions', 'questions'
            ])
            
            attributes.actionable_tips = await self._extract_list_content([
                'actionable', 'tips', 'actionable-tips', 'recommendations'
            ])
            
            attributes.visualization_suggestions = await self._extract_list_content([
                'visualization', 'visualization-suggestions', 'charts', 'visualize'
            ])
            
            attributes.risk_warnings = await self._extract_list_content([
                'risk', 'risk-warnings', 'warnings', 'cautions'
            ])
            
            attributes.tools_technologies = await self._extract_list_content([
                'tools', 'technologies', 'tools-technologies', 'tech'
            ])
            
            attributes.integration_points = await self._extract_list_content([
                'integration', 'integration-points', 'integrations'
            ])
            
            attributes.change_impact = await self._extract_section_content([
                'change', 'change-impact', 'impact'
            ])
            
        except Exception as e:
            print(f"      ⚠ Error extracting attributes: {e}")
            
        return attributes
        
    async def _extract_list_content(self, section_keywords: List[str]) -> List[str]:
        """Extract list items from a section."""
        items = []
        
        for keyword in section_keywords:
            try:
                # Find section and extract list items
                section_selectors = [
                    f'[data-section="{keyword}"] li',
                    f'.{keyword} li',
                    f'#{keyword} li',
                ]
                
                for selector in section_selectors:
                    try:
                        elements = await self.page.query_selector_all(selector)
                        for el in elements:
                            text = await el.inner_text()
                            if text.strip():
                                items.append(text.strip())
                        if items:
                            return items
                    except:
                        continue
                        
                # Try extracting as paragraph and splitting
                content = await self._extract_section_content(section_keywords)
                if content:
                    # Split by newlines or bullet points
                    lines = re.split(r'[\n•●○-]\s*', content)
                    items = [line.strip() for line in lines if line.strip()]
                    if items:
                        return items
                        
            except:
                continue
                
        return items
        
    def _generate_code(self, name: str) -> str:
        """Generate a code identifier from KPI name."""
        # Remove special characters, convert to uppercase with underscores
        code = re.sub(r'[^\w\s-]', '', name)
        code = re.sub(r'[-\s]+', '_', code)
        return code.upper()
        
    async def scrape_category(self, category: str) -> List[KPIDefinition]:
        """
        Scrape all KPIs from a category (all industries within the function).
        
        Args:
            category: Category key from CATEGORIES
            
        Returns:
            List of KPIDefinition objects
        """
        industry_links = await self.get_category_kpi_links(category)
        
        category_kpis = []
        total = len(industry_links)
        
        for i, link in enumerate(industry_links, 1):
            print(f"\n   [{i}/{total}] Industry: {link['name'][:50]}...")
            
            # scrape_kpi_page now returns a LIST of KPIs from each industry page
            kpis = await self.scrape_kpi_page(
                url=link['url'],
                category=category,
                subcategory=link.get('name', '')  # Use industry name as subcategory
            )
            
            if kpis:
                category_kpis.extend(kpis)
                self.scraped_kpis.extend(kpis)
                
            # Small delay between requests to be respectful
            await asyncio.sleep(1)
            
        return category_kpis
        
    async def scrape_all_categories(self) -> List[KPIDefinition]:
        """Scrape KPIs from all known categories."""
        all_kpis = []
        
        for category in self.CATEGORIES:
            kpis = await self.scrape_category(category)
            all_kpis.extend(kpis)
            
        return all_kpis
        
    async def scrape_single_url(self, url: str) -> Optional[KPIDefinition]:
        """
        Scrape a single KPI URL.
        
        Args:
            url: Full URL to KPI page
        """
        # Extract category from URL
        match = re.search(r'/kpi-([a-z-]+)/', url)
        category = match.group(1) if match else "unknown"
        subcategory = self._extract_subcategory(url, category)
        
        return await self.scrape_kpi_page(url, category, subcategory)
        
    def save_results(self, filename: str = None) -> str:
        """
        Save scraped KPIs to JSON file.
        
        Args:
            filename: Output filename (default: kpis_TIMESTAMP.json)
            
        Returns:
            Path to saved file
        """
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"kpis_{timestamp}.json"
            
        output_path = self.output_dir / filename
        
        data = {
            'scraped_at': datetime.now().isoformat(),
            'total_kpis': len(self.scraped_kpis),
            'kpis': [kpi.to_dict() for kpi in self.scraped_kpis]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"\n✓ Saved {len(self.scraped_kpis)} KPIs to {output_path}")
        return str(output_path)
        
    def export_for_processor(self, filename: str = None) -> str:
        """
        Export KPIs in format compatible with kpi_excel_processor.
        
        Args:
            filename: Output filename (default: kpi_depot_export.csv)
            
        Returns:
            Path to saved file
        """
        if not filename:
            filename = "kpi_depot_export.csv"
            
        output_path = self.output_dir / filename
        
        # Create CSV with columns matching kpi_excel_processor expectations
        import csv
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'KPI', 'Definition', 'Standard Formula', 'Category',
                'Subcategory', 'Measurement Approach', 'Trend Analysis',
                'Diagnostic Questions', 'Actionable Tips', 'Visualization Suggestions',
                'Risk Warnings', 'Tools Technologies', 'Integration Points',
                'Change Impact', 'Source URL'
            ])
            writer.writeheader()
            
            for kpi in self.scraped_kpis:
                writer.writerow({
                    'KPI': kpi.name,
                    'Definition': kpi.definition,
                    'Standard Formula': kpi.standard_formula,
                    'Category': kpi.category,
                    'Subcategory': kpi.subcategory,
                    'Measurement Approach': kpi.measurement_approach,
                    'Trend Analysis': kpi.attributes.trend_analysis,
                    'Diagnostic Questions': '; '.join(kpi.attributes.diagnostic_questions),
                    'Actionable Tips': '; '.join(kpi.attributes.actionable_tips),
                    'Visualization Suggestions': '; '.join(kpi.attributes.visualization_suggestions),
                    'Risk Warnings': '; '.join(kpi.attributes.risk_warnings),
                    'Tools Technologies': '; '.join(kpi.attributes.tools_technologies),
                    'Integration Points': '; '.join(kpi.attributes.integration_points),
                    'Change Impact': kpi.attributes.change_impact,
                    'Source URL': kpi.url
                })
                
        print(f"✓ Exported {len(self.scraped_kpis)} KPIs to {output_path}")
        return str(output_path)


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Scrape KPI definitions from kpidepot.com',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python kpi_depot_scraper.py --category supply-chain
  python kpi_depot_scraper.py --all
  python kpi_depot_scraper.py --url https://kpidepot.com/kpi-supply-chain/buying-87
  python kpi_depot_scraper.py --category supply-chain --headless
        """
    )
    
    parser.add_argument(
        '-c', '--category',
        choices=list(KPIDepotScraper.CATEGORIES.keys()),
        help='Scrape specific category'
    )
    
    parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='Scrape all categories'
    )
    
    parser.add_argument(
        '-u', '--url',
        help='Scrape single KPI URL'
    )
    
    parser.add_argument(
        '--headless',
        action='store_true',
        help='Run browser in headless mode (not recommended for first login)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output directory for scraped data'
    )
    
    parser.add_argument(
        '--list-categories',
        action='store_true',
        help='List available categories and exit'
    )
    
    args = parser.parse_args()
    
    if args.list_categories:
        print("\nAvailable KPI categories:")
        for cat, path in KPIDepotScraper.CATEGORIES.items():
            print(f"  - {cat}: {KPIDepotScraper.BASE_URL}{path}")
        return
        
    if not (args.category or args.all or args.url):
        parser.print_help()
        print("\n✗ Please specify --category, --all, or --url")
        sys.exit(1)
        
    scraper = KPIDepotScraper(output_dir=args.output, headless=args.headless)
    
    try:
        await scraper.start_browser()
        await scraper.wait_for_login()
        
        if args.url:
            kpi = await scraper.scrape_single_url(args.url)
            if kpi:
                scraper.scraped_kpis.append(kpi)
        elif args.all:
            await scraper.scrape_all_categories()
        elif args.category:
            await scraper.scrape_category(args.category)
            
        if scraper.scraped_kpis:
            scraper.save_results()
            scraper.export_for_processor()
            
            print(f"\n{'='*60}")
            print(f"✓ Scraping complete!")
            print(f"  Total KPIs: {len(scraper.scraped_kpis)}")
            print(f"  Output: {scraper.output_dir}")
            print(f"{'='*60}")
        else:
            print("\n⚠ No KPIs were scraped")
            
    except KeyboardInterrupt:
        print("\n\n⚠ Scraping interrupted by user")
        if scraper.scraped_kpis:
            print(f"  Saving {len(scraper.scraped_kpis)} KPIs collected so far...")
            scraper.save_results()
            scraper.export_for_processor()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        if scraper.scraped_kpis:
            print(f"  Saving {len(scraper.scraped_kpis)} KPIs collected before error...")
            scraper.save_results()
    finally:
        await scraper.close_browser()


if __name__ == '__main__':
    asyncio.run(main())
