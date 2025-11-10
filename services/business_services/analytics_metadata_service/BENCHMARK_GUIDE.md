# KPI Benchmark Guide

## Overview

The **Benchmark** model provides comprehensive industry benchmark data points for KPIs with full citation and structured context. Each benchmark represents a specific data point from research studies, industry reports, or authoritative sources that provide context for KPI performance evaluation.

---

## Key Features

✅ **Full Citation Support** - Complete source attribution with publisher, author, title, year, URLs  
✅ **Structured Context** - Company size, industry, geography, time period, population  
✅ **Exact Metric Information** - Value, unit, statistic type (mean, median, percentile)  
✅ **Metric Definition** - How the metric is defined, normalized, and filtered  
✅ **Sample Details** - Sample size, description, and methodology notes  
✅ **Quality Indicators** - Confidence level, data quality score, verification tracking  
✅ **Flexible Categorization** - Tags, categories, featured status  

---

## Database Model

### Core Fields

#### **Identification**
- `id` - Primary key
- `kpi_id` - Foreign key to KPI
- `name` - Benchmark name
- `code` - Unique benchmark code
- `description` - Detailed description
- `is_active` - Active status

#### **Exact Metric Information**
- `metric_value` - Numeric benchmark value
- `metric_value_text` - Text representation (for ranges or non-numeric)
- `metric_unit` - Unit of measure (%, $, seconds, count, etc.)
- `statistic_type` - Type: mean, median, mode, percentile, range
- `percentile` - Percentile value (0-100) if applicable
- `value_min` - Minimum value in range
- `value_max` - Maximum value in range

#### **Metric Definition & Attributes**
- `metric_definition` - How the metric is defined and calculated
- `metric_normalization` - How normalized (per user, per session, etc.)
- `metric_filters` - Filters applied (JSON)
- `cohort_rules` - Cohort or segment rules (JSON)

#### **Context & Segmentation**

**Company Size:**
- `company_size` - Size category (SMB, Mid-Market, Enterprise)
- `company_size_min` - Minimum size
- `company_size_max` - Maximum size
- `company_size_metric` - Size metric (employees, revenue, customers)

**Time Period:**
- `time_period` - Period as reported (Q1 2024, 2023 Annual)
- `time_period_start` - Start date
- `time_period_end` - End date

**Population:**
- `population` - What was measured (landing pages, sessions, users)
- `population_size` - Size of population

**Industry:**
- `industry` - Industry or sector
- `industry_tags` - Array of industry tags (JSON)

**Geography:**
- `geography` - Geographic scope
- `country` - Specific country
- `region` - Region (North America, EMEA, etc.)

**Sample:**
- `sample_size` - Number of observations
- `sample_description` - Description of sample

#### **Source Details & Citation**

**Publisher/Author:**
- `source_publisher` - Publisher or organization
- `source_author` - Author(s)
- `source_title` - Title of report/study

**Year & Date:**
- `source_year` - Publication year
- `source_date` - Exact publication date

**Source Content:**
- `source_excerpt` - Relevant excerpt or quote
- `source_url` - URL to source
- `source_download_url` - Download URL for PDF/whitepaper
- `source_doi` - Digital Object Identifier (for academic sources)

**Source Quality:**
- `source_type` - Type: research_report, whitepaper, academic_study, etc.
- `source_credibility` - Credibility: high, medium, low

#### **Methodology & Comments**
- `methodology_notes` - Research methodology notes
- `caveats` - Important caveats or limitations
- `special_coverage` - Special coverage areas
- `comments` - Additional comments

#### **Quality & Validation**
- `confidence_level` - Confidence: high, medium, low
- `data_quality_score` - Quality score (0-100)
- `last_verified_at` - Last verification date
- `verified_by` - Who verified

#### **Categorization & Display**
- `benchmark_category` - Category: industry_standard, best_in_class, average, poor_performance
- `display_order` - Display order for sorting
- `is_featured` - Feature prominently
- `tags` - Tags for categorization (JSON)
- `metadata_` - Additional metadata (JSON)

---

## Usage Examples

### Example 1: E-commerce Conversion Rate Benchmark

```python
from analytics_models import Benchmark, KPI

# Assume we have a Conversion Rate KPI
conversion_rate_kpi = KPI(name="Conversion Rate", code="CONV_RATE")

# Create benchmark from industry report
ecommerce_benchmark = Benchmark(
    kpi_id=conversion_rate_kpi.id,
    name="E-commerce Conversion Rate - Industry Average",
    code="CONV_RATE_ECOM_AVG_2024",
    description="Average conversion rate for e-commerce websites in 2024",
    
    # Exact Metric
    metric_value=2.86,
    metric_unit="%",
    statistic_type="mean",
    
    # Metric Definition
    metric_definition="Percentage of website visitors who complete a purchase",
    metric_normalization="Transactions / Total Sessions * 100",
    metric_filters={
        "device_types": ["desktop", "mobile", "tablet"],
        "traffic_sources": ["all"],
        "excluded": ["bot_traffic", "internal_traffic"]
    },
    
    # Context
    company_size="All",
    industry="E-commerce",
    industry_tags={"industries": ["retail", "online_shopping", "consumer_goods"]},
    geography="United States",
    country="United States",
    region="North America",
    
    # Time Period
    time_period="Q1-Q4 2024",
    time_period_start=datetime(2024, 1, 1),
    time_period_end=datetime(2024, 12, 31),
    
    # Population
    population="E-commerce websites",
    population_size=5000000,
    
    # Sample
    sample_size=1500,
    sample_description="1,500 e-commerce websites across various product categories",
    
    # Source Citation
    source_publisher="Statista",
    source_author="Statista Research Department",
    source_title="E-commerce Conversion Rates in the United States 2024",
    source_year=2024,
    source_date=datetime(2024, 3, 15),
    source_excerpt="The average conversion rate for e-commerce websites in the United States was 2.86% in 2024, with mobile conversion rates at 1.82% and desktop at 3.91%.",
    source_url="https://www.statista.com/statistics/ecommerce-conversion-rates/",
    source_type="industry_survey",
    source_credibility="high",
    
    # Methodology
    methodology_notes="Data collected via web analytics platforms from participating e-commerce sites. Conversion defined as completed transaction with payment confirmation.",
    caveats="Conversion rates vary significantly by product category, price point, and traffic source. Mobile rates typically lower than desktop.",
    
    # Quality
    confidence_level="high",
    data_quality_score=92,
    last_verified_at=datetime(2024, 10, 1),
    verified_by="Data Analytics Team",
    
    # Categorization
    benchmark_category="industry_standard",
    display_order=1,
    is_featured=True,
    tags={"tags": ["conversion", "ecommerce", "2024", "us_market"]}
)
```

### Example 2: SaaS Churn Rate Benchmark (Percentile)

```python
# SaaS Monthly Churn Rate - 75th Percentile (Best Performers)
saas_churn_p75 = Benchmark(
    kpi_id=churn_rate_kpi.id,
    name="SaaS Monthly Churn Rate - 75th Percentile",
    code="CHURN_SAAS_P75_2024",
    description="Monthly churn rate for top-performing SaaS companies (75th percentile)",
    
    # Exact Metric
    metric_value=3.2,
    metric_unit="%",
    statistic_type="percentile",
    percentile=75,
    
    # Metric Definition
    metric_definition="Percentage of customers who cancel subscription in a given month",
    metric_normalization="(Churned Customers / Total Customers at Start of Month) * 100",
    cohort_rules={
        "cohort_type": "monthly",
        "minimum_tenure": "1_month",
        "excluded_cohorts": ["trial_users", "free_tier"]
    },
    
    # Context
    company_size="SMB to Enterprise",
    company_size_min=10,
    company_size_max=5000,
    company_size_metric="employees",
    
    industry="SaaS",
    industry_tags={"industries": ["software", "b2b_saas", "subscription"]},
    
    geography="Global",
    region="Global",
    
    # Time Period
    time_period="2024 Annual",
    time_period_start=datetime(2024, 1, 1),
    time_period_end=datetime(2024, 12, 31),
    
    # Population
    population="B2B SaaS Companies",
    population_size=250000,
    
    # Sample
    sample_size=847,
    sample_description="847 B2B SaaS companies with at least 100 paying customers",
    
    # Source Citation
    source_publisher="ChartMogul",
    source_author="ChartMogul Research Team",
    source_title="SaaS Metrics Benchmark Report 2024",
    source_year=2024,
    source_date=datetime(2024, 6, 1),
    source_excerpt="The 75th percentile of SaaS companies maintain a monthly churn rate of 3.2% or lower, while the median is 5.6%.",
    source_url="https://chartmogul.com/saas-benchmarks-2024/",
    source_download_url="https://chartmogul.com/downloads/saas-benchmarks-2024.pdf",
    source_type="industry_survey",
    source_credibility="high",
    
    # Methodology
    methodology_notes="Data aggregated from ChartMogul customer base. Churn calculated using monthly cohort analysis. Only companies with >100 customers included.",
    caveats="Churn rates vary significantly by ACV, customer segment, and product maturity. Early-stage companies typically have higher churn.",
    special_coverage="Report includes separate benchmarks for different ACV bands and customer segments",
    
    # Quality
    confidence_level="high",
    data_quality_score=95,
    last_verified_at=datetime(2024, 9, 15),
    verified_by="SaaS Metrics Team",
    
    # Categorization
    benchmark_category="best_in_class",
    display_order=2,
    is_featured=True,
    tags={"tags": ["churn", "saas", "b2b", "retention", "best_performers"]}
)
```

### Example 3: Website Load Time Benchmark (Range)

```python
# Website Load Time - Acceptable Range
load_time_benchmark = Benchmark(
    kpi_id=page_load_time_kpi.id,
    name="Website Load Time - Acceptable Range",
    code="LOAD_TIME_ACCEPTABLE_2024",
    description="Acceptable page load time range for optimal user experience",
    
    # Exact Metric (Range)
    metric_value=2.5,  # Target/median
    metric_value_text="1.0 - 3.0 seconds",
    value_min=1.0,
    value_max=3.0,
    metric_unit="seconds",
    statistic_type="range",
    
    # Metric Definition
    metric_definition="Time from initial request to fully loaded page (DOM complete + all resources)",
    metric_normalization="Measured at 75th percentile of user sessions",
    metric_filters={
        "connection_type": ["3G", "4G", "WiFi"],
        "page_types": ["homepage", "product_pages", "category_pages"],
        "excluded": ["admin_pages", "checkout_pages"]
    },
    
    # Context
    company_size="All",
    industry="Cross-industry",
    industry_tags={"industries": ["web", "digital", "online_services"]},
    
    geography="Global",
    region="Global",
    
    # Time Period
    time_period="2024",
    time_period_start=datetime(2024, 1, 1),
    time_period_end=datetime(2024, 12, 31),
    
    # Population
    population="Web pages",
    population_size=10000000,
    
    # Sample
    sample_size=5000,
    sample_description="5,000 high-traffic websites across various industries",
    
    # Source Citation
    source_publisher="Google",
    source_author="Google Web Performance Team",
    source_title="Web Vitals and Page Experience Report 2024",
    source_year=2024,
    source_date=datetime(2024, 5, 20),
    source_excerpt="Pages loading in under 3 seconds provide optimal user experience. Each additional second of load time increases bounce rate by 32%.",
    source_url="https://web.dev/vitals/",
    source_type="research_report",
    source_credibility="high",
    
    # Methodology
    methodology_notes="Data collected via Chrome User Experience Report (CrUX). Load time measured using Navigation Timing API.",
    caveats="Load times vary by device type, connection speed, and geographic location. Mobile typically 2-3x slower than desktop.",
    special_coverage="Report includes Core Web Vitals (LCP, FID, CLS) and their impact on SEO rankings",
    
    # Quality
    confidence_level="high",
    data_quality_score=98,
    last_verified_at=datetime(2024, 10, 15),
    verified_by="Web Performance Team",
    
    # Categorization
    benchmark_category="industry_standard",
    display_order=1,
    is_featured=True,
    tags={"tags": ["performance", "load_time", "web_vitals", "ux"]}
)
```

### Example 4: Email Open Rate Benchmark (Segmented)

```python
# Email Open Rate - B2B Technology Sector
email_open_rate_b2b_tech = Benchmark(
    kpi_id=email_open_rate_kpi.id,
    name="Email Open Rate - B2B Technology",
    code="EMAIL_OPEN_B2B_TECH_2024",
    description="Average email open rate for B2B technology companies",
    
    # Exact Metric
    metric_value=21.5,
    metric_unit="%",
    statistic_type="mean",
    
    # Metric Definition
    metric_definition="Percentage of delivered emails that were opened by recipients",
    metric_normalization="(Unique Opens / Delivered Emails) * 100",
    metric_filters={
        "email_types": ["newsletters", "promotional", "product_updates"],
        "excluded": ["transactional", "password_resets", "receipts"]
    },
    cohort_rules={
        "list_type": "opted_in",
        "list_health": "cleaned_within_90_days",
        "excluded": ["purchased_lists", "unengaged_subscribers"]
    },
    
    # Context
    company_size="SMB to Enterprise",
    company_size_min=50,
    company_size_max=10000,
    company_size_metric="employees",
    
    industry="B2B Technology",
    industry_tags={"industries": ["software", "saas", "it_services", "tech_hardware"]},
    
    geography="United States",
    country="United States",
    region="North America",
    
    # Time Period
    time_period="2024 H1",
    time_period_start=datetime(2024, 1, 1),
    time_period_end=datetime(2024, 6, 30),
    
    # Population
    population="Email campaigns",
    population_size=15000000,
    
    # Sample
    sample_size=2500,
    sample_description="2,500 B2B technology companies sending regular email campaigns",
    
    # Source Citation
    source_publisher="Mailchimp",
    source_author="Mailchimp Benchmark Team",
    source_title="Email Marketing Benchmarks by Industry 2024",
    source_year=2024,
    source_date=datetime(2024, 7, 10),
    source_excerpt="B2B technology companies see an average open rate of 21.5%, which is above the cross-industry average of 18.0%.",
    source_url="https://mailchimp.com/resources/email-marketing-benchmarks/",
    source_type="industry_survey",
    source_credibility="high",
    
    # Methodology
    methodology_notes="Data aggregated from Mailchimp platform users. Open tracking via pixel. Mobile vs desktop opens tracked separately.",
    caveats="Open rates affected by Apple Mail Privacy Protection (MPP) which may inflate rates. Subject line, send time, and list quality significantly impact results.",
    special_coverage="Report includes benchmarks for click rates, unsubscribe rates, and bounce rates by industry",
    
    # Quality
    confidence_level="high",
    data_quality_score=90,
    last_verified_at=datetime(2024, 9, 1),
    verified_by="Email Marketing Team",
    
    # Categorization
    benchmark_category="industry_standard",
    display_order=3,
    is_featured=False,
    tags={"tags": ["email", "open_rate", "b2b", "technology", "marketing"]}
)
```

---

## Benchmark Categories

### **industry_standard**
Represents typical performance across the industry. Most companies fall within this range.

### **best_in_class**
Top performers (typically 75th-90th percentile). Aspirational targets for high-performing organizations.

### **average**
Median or mean performance. Represents the "middle of the pack."

### **poor_performance**
Below-average performance (typically bottom 25th percentile). Indicates need for improvement.

---

## Statistic Types

### **mean**
Average value across all observations. Sensitive to outliers.

### **median**
Middle value when sorted. More robust to outliers than mean.

### **percentile**
Value at a specific percentile (e.g., 75th percentile = top 25% of performers).

### **range**
Acceptable or typical range of values (min to max).

### **mode**
Most frequently occurring value.

---

## Source Types

- **research_report** - Formal research study or report
- **whitepaper** - Industry whitepaper or guide
- **academic_study** - Peer-reviewed academic research
- **industry_survey** - Survey of industry participants
- **case_study** - Individual case study or analysis
- **vendor_report** - Report from software vendor or platform
- **government_data** - Government statistics or data
- **proprietary_research** - Internal or proprietary research

---

## Best Practices

### 1. **Always Include Full Citation**
- Publisher/author
- Title
- Year
- URL or DOI
- Source excerpt for context

### 2. **Provide Context**
- Industry, geography, company size
- Time period
- Sample size and description
- Methodology notes

### 3. **Define the Metric Clearly**
- Exact definition
- Normalization method
- Filters and cohort rules
- Any caveats or limitations

### 4. **Verify and Update Regularly**
- Set `last_verified_at` when reviewing
- Update benchmarks annually or when new data available
- Mark outdated benchmarks as inactive

### 5. **Use Appropriate Statistic Types**
- Mean for normally distributed data
- Median for skewed distributions
- Percentiles for performance tiers
- Ranges for acceptable bounds

### 6. **Tag Appropriately**
- Use tags for easy filtering
- Include year, industry, geography
- Add relevant keywords

---

## Query Examples

### Get All Benchmarks for a KPI

```python
benchmarks = session.query(Benchmark).filter(
    Benchmark.kpi_id == kpi.id,
    Benchmark.is_active == True
).order_by(Benchmark.display_order).all()
```

### Get Featured Benchmarks

```python
featured = session.query(Benchmark).filter(
    Benchmark.is_featured == True,
    Benchmark.is_active == True
).all()
```

### Get Benchmarks by Industry

```python
saas_benchmarks = session.query(Benchmark).filter(
    Benchmark.industry.like('%SaaS%'),
    Benchmark.is_active == True
).all()
```

### Get Recent Benchmarks

```python
from datetime import datetime, timedelta

recent = session.query(Benchmark).filter(
    Benchmark.source_year >= 2023,
    Benchmark.is_active == True
).order_by(Benchmark.source_year.desc()).all()
```

### Get Best-in-Class Benchmarks

```python
best_in_class = session.query(Benchmark).filter(
    Benchmark.benchmark_category == 'best_in_class',
    Benchmark.is_active == True
).all()
```

---

## API Endpoints (Suggested)

```
GET    /kpis/{kpi_id}/benchmarks          - List benchmarks for KPI
POST   /kpis/{kpi_id}/benchmarks          - Create benchmark
GET    /benchmarks/{id}                   - Get benchmark
PUT    /benchmarks/{id}                   - Update benchmark
DELETE /benchmarks/{id}                   - Delete benchmark
GET    /benchmarks/featured               - Get featured benchmarks
GET    /benchmarks/search                 - Search benchmarks
```

---

## Conclusion

The Benchmark model provides a comprehensive, citation-backed system for storing and managing KPI benchmark data. With full source attribution, structured context, and quality indicators, it enables data-driven performance evaluation and goal setting.
