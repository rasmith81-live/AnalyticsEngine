# KPI Depot Web Scraper

Playwright-based scraper to collect KPI definitions from [kpidepot.com](https://kpidepot.com) using your authenticated subscription.

## Features

- **Persistent browser session** - Maintains login across runs
- **Category-based scraping** - Scrape by category or all at once
- **Full KPI extraction** - Captures all fields including extended attributes:
  - Definition
  - Measurement Approach
  - Standard Formula
  - Trend Analysis
  - Diagnostic Questions
  - Actionable Tips
  - Visualization Suggestions
  - Risk Warnings
  - Tools & Technologies
  - Integration Points
  - Change Impact

## Prerequisites

- Python 3.9+
- Playwright installed: `pip install playwright`
- Browser binaries: `playwright install chromium`
- Valid KPI Depot subscription

## Usage

### First Run (Login Required)

On first run, a browser window opens for you to log in:

```powershell
python kpi_depot_scraper.py --category supply-chain
```

The browser stores your session in `output/browser_data/` for subsequent runs.

### Scrape by Category

```powershell
# Single category
python kpi_depot_scraper.py --category supply-chain

# List available categories
python kpi_depot_scraper.py --list-categories
```

**Available categories:**
- `corporate-finance` - Corporate Finance
- `corporate-marketing` - Corporate Marketing
- `corporate-strategy` - Corporate Strategy
- `customer-service` - Customer Service
- `data-management` - Data Management & Analysis
- `general-council` - General Council
- `human-resources` - Human Resources
- `information-technology` - Information Technology
- `innovation-management` - Innovation Management
- `legal` - Legal
- `operations-management` - Operations Management
- `product-management` - Product Management
- `regulatory-compliance` - Regulatory Compliance
- `sales-management` - Sales Management
- `supply-chain-management` - Supply Chain Management

### Scrape All Categories

```powershell
python kpi_depot_scraper.py --all
```

### Scrape Single KPI

```powershell
python kpi_depot_scraper.py --url https://kpidepot.com/kpi-supply-chain/buying-87
```

### Headless Mode

After initial login, you can run headless:

```powershell
python kpi_depot_scraper.py --category supply-chain --headless
```

## Output

The scraper produces two output files in the `output/` directory:

### 1. JSON Export (`kpis_TIMESTAMP.json`)

Full structured data for programmatic use:

```json
{
  "scraped_at": "2026-01-27T20:00:00",
  "total_kpis": 50,
  "kpis": [
    {
      "name": "Order Accuracy Rate",
      "code": "ORDER_ACCURACY_RATE",
      "url": "https://kpidepot.com/kpi-supply-chain/buying-87",
      "category": "supply-chain",
      "subcategory": "Buying",
      "definition": "...",
      "measurement_approach": "...",
      "standard_formula": "...",
      "attributes": {
        "trend_analysis": "...",
        "diagnostic_questions": ["..."],
        "actionable_tips": ["..."],
        ...
      }
    }
  ]
}
```

### 2. CSV Export (`kpi_depot_export.csv`)

Compatible with `kpi_excel_processor.py` for direct import:

| KPI | Definition | Standard Formula | Category | ... |
|-----|------------|------------------|----------|-----|

## Integration with AnalyticsEngine

After scraping, import KPIs using the Excel processor:

```powershell
cd ..\kpiExcelProcessor
python kpi_excel_processor.py -f ..\kpiDepotScraper\output\kpi_depot_export.csv -m SOURCING -c SUPPLY_CHAIN
```

## Customization

The scraper uses CSS selectors that may need adjustment if the KPI Depot site structure changes. Key methods to update:

- `_check_login_status()` - Login detection selectors
- `get_category_kpi_links()` - Category page link extraction
- `_extract_section_content()` - Content section parsing
- `_extract_all_attributes()` - Extended attributes button and sections

## Rate Limiting

The scraper includes a 1-second delay between page requests to be respectful to the server. Adjust `asyncio.sleep()` calls if needed.

## Troubleshooting

### Login Not Detected
- Check if login indicator selectors match the site
- Try logging in manually with browser window visible

### Missing Content
- Verify selectors match current site structure
- Check browser console for JavaScript errors
- Some content may require additional button clicks

### Session Expired
- Delete `output/browser_data/` folder
- Run again without `--headless` to re-login
