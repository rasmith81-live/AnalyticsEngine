"""
Benchmark Examples

Demonstrates how to create comprehensive benchmark data points with full citation
and structured context for various KPIs.
"""

from datetime import datetime
from analytics_models import Benchmark, KPI


# ============================================================================
# Example 1: E-commerce Conversion Rate Benchmarks
# ============================================================================

def create_ecommerce_conversion_benchmarks():
    """Create conversion rate benchmarks for e-commerce."""
    
    # Assume conversion rate KPI exists
    conversion_rate_kpi = KPI(name="Conversion Rate", code="CONV_RATE")
    
    # Industry Average
    avg_benchmark = Benchmark(
        kpi_id=conversion_rate_kpi.id,
        name="E-commerce Conversion Rate - Industry Average",
        code="CONV_RATE_ECOM_AVG_2024",
        description="Average conversion rate for e-commerce websites in 2024",
        
        # Metric
        metric_value=2.86,
        metric_unit="%",
        statistic_type="mean",
        
        # Definition
        metric_definition="Percentage of website visitors who complete a purchase",
        metric_normalization="(Transactions / Total Sessions) * 100",
        metric_filters={
            "device_types": ["desktop", "mobile", "tablet"],
            "traffic_sources": ["all"],
            "excluded": ["bot_traffic", "internal_traffic"]
        },
        
        # Context
        company_size="All",
        industry="E-commerce",
        geography="United States",
        time_period="2024",
        population="E-commerce websites",
        sample_size=1500,
        
        # Source
        source_publisher="Statista",
        source_title="E-commerce Conversion Rates 2024",
        source_year=2024,
        source_url="https://www.statista.com/statistics/ecommerce-conversion-rates/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=92,
        benchmark_category="industry_standard",
        is_featured=True
    )
    
    # Top Performers (75th Percentile)
    top_benchmark = Benchmark(
        kpi_id=conversion_rate_kpi.id,
        name="E-commerce Conversion Rate - Top Performers",
        code="CONV_RATE_ECOM_P75_2024",
        description="Conversion rate for top-performing e-commerce sites (75th percentile)",
        
        # Metric
        metric_value=4.2,
        metric_unit="%",
        statistic_type="percentile",
        percentile=75,
        
        # Definition
        metric_definition="Percentage of website visitors who complete a purchase",
        metric_normalization="(Transactions / Total Sessions) * 100",
        
        # Context
        company_size="All",
        industry="E-commerce",
        geography="United States",
        time_period="2024",
        population="E-commerce websites",
        sample_size=1500,
        
        # Source
        source_publisher="Statista",
        source_title="E-commerce Conversion Rates 2024",
        source_year=2024,
        source_url="https://www.statista.com/statistics/ecommerce-conversion-rates/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=92,
        benchmark_category="best_in_class",
        is_featured=True
    )
    
    return [avg_benchmark, top_benchmark]


# ============================================================================
# Example 2: SaaS Metrics Benchmarks
# ============================================================================

def create_saas_metrics_benchmarks():
    """Create comprehensive SaaS metrics benchmarks."""
    
    # Monthly Churn Rate
    churn_kpi = KPI(name="Monthly Churn Rate", code="CHURN_MONTHLY")
    
    churn_median = Benchmark(
        kpi_id=churn_kpi.id,
        name="SaaS Monthly Churn - Median",
        code="CHURN_SAAS_MEDIAN_2024",
        description="Median monthly churn rate for B2B SaaS companies",
        
        # Metric
        metric_value=5.6,
        metric_unit="%",
        statistic_type="median",
        
        # Definition
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
        geography="Global",
        time_period="2024",
        population="B2B SaaS Companies",
        sample_size=847,
        sample_description="847 B2B SaaS companies with at least 100 paying customers",
        
        # Source
        source_publisher="ChartMogul",
        source_author="ChartMogul Research Team",
        source_title="SaaS Metrics Benchmark Report 2024",
        source_year=2024,
        source_date=datetime(2024, 6, 1),
        source_excerpt="The median monthly churn rate for B2B SaaS companies is 5.6%, with top performers maintaining rates below 3.2%.",
        source_url="https://chartmogul.com/saas-benchmarks-2024/",
        source_download_url="https://chartmogul.com/downloads/saas-benchmarks-2024.pdf",
        source_type="industry_survey",
        source_credibility="high",
        
        # Methodology
        methodology_notes="Data aggregated from ChartMogul customer base. Churn calculated using monthly cohort analysis.",
        caveats="Churn rates vary significantly by ACV, customer segment, and product maturity.",
        
        # Quality
        confidence_level="high",
        data_quality_score=95,
        benchmark_category="industry_standard",
        is_featured=True
    )
    
    # Customer Acquisition Cost (CAC)
    cac_kpi = KPI(name="Customer Acquisition Cost", code="CAC")
    
    cac_benchmark = Benchmark(
        kpi_id=cac_kpi.id,
        name="SaaS CAC - By Company Size",
        code="CAC_SAAS_SMB_2024",
        description="Average customer acquisition cost for SMB SaaS companies",
        
        # Metric
        metric_value=1420,
        metric_unit="$",
        statistic_type="mean",
        
        # Definition
        metric_definition="Total sales and marketing costs divided by number of new customers acquired",
        metric_normalization="(Sales & Marketing Expenses) / New Customers Acquired",
        
        # Context
        company_size="SMB",
        company_size_min=10,
        company_size_max=200,
        company_size_metric="employees",
        industry="SaaS",
        geography="United States",
        time_period="2024",
        population="SMB SaaS Companies",
        sample_size=325,
        
        # Source
        source_publisher="SaaS Capital",
        source_title="SaaS Benchmarks Report 2024",
        source_year=2024,
        source_url="https://www.saas-capital.com/research/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=88,
        benchmark_category="industry_standard",
        is_featured=False
    )
    
    # LTV:CAC Ratio
    ltv_cac_kpi = KPI(name="LTV:CAC Ratio", code="LTV_CAC_RATIO")
    
    ltv_cac_benchmark = Benchmark(
        kpi_id=ltv_cac_kpi.id,
        name="SaaS LTV:CAC Ratio - Healthy Range",
        code="LTV_CAC_HEALTHY_2024",
        description="Healthy LTV:CAC ratio range for SaaS companies",
        
        # Metric (Range)
        metric_value=3.0,  # Target
        metric_value_text="3:1 to 5:1",
        value_min=3.0,
        value_max=5.0,
        metric_unit="ratio",
        statistic_type="range",
        
        # Definition
        metric_definition="Ratio of customer lifetime value to customer acquisition cost",
        metric_normalization="(Average Revenue Per Customer * Gross Margin % / Churn Rate) / CAC",
        
        # Context
        company_size="All",
        industry="SaaS",
        geography="Global",
        time_period="2024",
        
        # Source
        source_publisher="SaaStr",
        source_title="SaaS Metrics That Matter 2024",
        source_year=2024,
        source_excerpt="A healthy LTV:CAC ratio is between 3:1 and 5:1. Below 3:1 indicates high acquisition costs; above 5:1 suggests under-investment in growth.",
        source_url="https://www.saastr.com/saas-metrics/",
        source_type="industry_survey",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=90,
        benchmark_category="industry_standard",
        is_featured=True
    )
    
    return [churn_median, cac_benchmark, ltv_cac_benchmark]


# ============================================================================
# Example 3: Website Performance Benchmarks
# ============================================================================

def create_website_performance_benchmarks():
    """Create website performance benchmarks."""
    
    # Page Load Time
    load_time_kpi = KPI(name="Page Load Time", code="PAGE_LOAD_TIME")
    
    load_time_benchmark = Benchmark(
        kpi_id=load_time_kpi.id,
        name="Page Load Time - Optimal Range",
        code="LOAD_TIME_OPTIMAL_2024",
        description="Optimal page load time for user experience",
        
        # Metric (Range)
        metric_value=2.5,
        metric_value_text="1.0 - 3.0 seconds",
        value_min=1.0,
        value_max=3.0,
        metric_unit="seconds",
        statistic_type="range",
        
        # Definition
        metric_definition="Time from initial request to fully loaded page (DOM complete + all resources)",
        metric_normalization="Measured at 75th percentile of user sessions",
        metric_filters={
            "connection_type": ["3G", "4G", "WiFi"],
            "page_types": ["homepage", "product_pages", "category_pages"]
        },
        
        # Context
        company_size="All",
        industry="Cross-industry",
        geography="Global",
        time_period="2024",
        population="Web pages",
        sample_size=5000,
        
        # Source
        source_publisher="Google",
        source_author="Google Web Performance Team",
        source_title="Web Vitals and Page Experience Report 2024",
        source_year=2024,
        source_date=datetime(2024, 5, 20),
        source_excerpt="Pages loading in under 3 seconds provide optimal user experience. Each additional second increases bounce rate by 32%.",
        source_url="https://web.dev/vitals/",
        source_type="research_report",
        source_credibility="high",
        
        # Methodology
        methodology_notes="Data collected via Chrome User Experience Report (CrUX). Load time measured using Navigation Timing API.",
        caveats="Load times vary by device type, connection speed, and geographic location.",
        
        # Quality
        confidence_level="high",
        data_quality_score=98,
        benchmark_category="industry_standard",
        is_featured=True
    )
    
    # Bounce Rate
    bounce_rate_kpi = KPI(name="Bounce Rate", code="BOUNCE_RATE")
    
    bounce_rate_benchmark = Benchmark(
        kpi_id=bounce_rate_kpi.id,
        name="Bounce Rate - E-commerce Average",
        code="BOUNCE_ECOM_AVG_2024",
        description="Average bounce rate for e-commerce websites",
        
        # Metric
        metric_value=47.2,
        metric_unit="%",
        statistic_type="mean",
        
        # Definition
        metric_definition="Percentage of single-page sessions with no interaction",
        metric_normalization="(Single-Page Sessions / Total Sessions) * 100",
        
        # Context
        industry="E-commerce",
        geography="United States",
        time_period="2024",
        population="E-commerce websites",
        sample_size=2000,
        
        # Source
        source_publisher="Contentsquare",
        source_title="Digital Experience Benchmark Report 2024",
        source_year=2024,
        source_url="https://contentsquare.com/benchmarks/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=91,
        benchmark_category="industry_standard",
        is_featured=False
    )
    
    return [load_time_benchmark, bounce_rate_benchmark]


# ============================================================================
# Example 4: Marketing Benchmarks
# ============================================================================

def create_marketing_benchmarks():
    """Create marketing performance benchmarks."""
    
    # Email Open Rate
    email_open_kpi = KPI(name="Email Open Rate", code="EMAIL_OPEN_RATE")
    
    email_open_b2b = Benchmark(
        kpi_id=email_open_kpi.id,
        name="Email Open Rate - B2B Technology",
        code="EMAIL_OPEN_B2B_TECH_2024",
        description="Average email open rate for B2B technology companies",
        
        # Metric
        metric_value=21.5,
        metric_unit="%",
        statistic_type="mean",
        
        # Definition
        metric_definition="Percentage of delivered emails that were opened",
        metric_normalization="(Unique Opens / Delivered Emails) * 100",
        metric_filters={
            "email_types": ["newsletters", "promotional", "product_updates"],
            "excluded": ["transactional", "password_resets"]
        },
        cohort_rules={
            "list_type": "opted_in",
            "list_health": "cleaned_within_90_days"
        },
        
        # Context
        company_size="SMB to Enterprise",
        industry="B2B Technology",
        geography="United States",
        time_period="2024 H1",
        population="Email campaigns",
        sample_size=2500,
        
        # Source
        source_publisher="Mailchimp",
        source_title="Email Marketing Benchmarks by Industry 2024",
        source_year=2024,
        source_date=datetime(2024, 7, 10),
        source_excerpt="B2B technology companies see an average open rate of 21.5%, above the cross-industry average of 18.0%.",
        source_url="https://mailchimp.com/resources/email-marketing-benchmarks/",
        source_type="industry_survey",
        source_credibility="high",
        
        # Methodology
        methodology_notes="Data aggregated from Mailchimp platform users. Open tracking via pixel.",
        caveats="Open rates affected by Apple Mail Privacy Protection (MPP) which may inflate rates.",
        
        # Quality
        confidence_level="high",
        data_quality_score=90,
        benchmark_category="industry_standard",
        is_featured=False
    )
    
    # Click-Through Rate (CTR)
    ctr_kpi = KPI(name="Email Click-Through Rate", code="EMAIL_CTR")
    
    email_ctr_b2b = Benchmark(
        kpi_id=ctr_kpi.id,
        name="Email CTR - B2B Technology",
        code="EMAIL_CTR_B2B_TECH_2024",
        description="Average email click-through rate for B2B technology",
        
        # Metric
        metric_value=2.6,
        metric_unit="%",
        statistic_type="mean",
        
        # Definition
        metric_definition="Percentage of delivered emails with at least one click",
        metric_normalization="(Unique Clicks / Delivered Emails) * 100",
        
        # Context
        industry="B2B Technology",
        geography="United States",
        time_period="2024 H1",
        population="Email campaigns",
        sample_size=2500,
        
        # Source
        source_publisher="Mailchimp",
        source_title="Email Marketing Benchmarks by Industry 2024",
        source_year=2024,
        source_url="https://mailchimp.com/resources/email-marketing-benchmarks/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=90,
        benchmark_category="industry_standard",
        is_featured=False
    )
    
    # Social Media Engagement Rate
    engagement_kpi = KPI(name="Social Media Engagement Rate", code="SOCIAL_ENGAGEMENT")
    
    social_engagement = Benchmark(
        kpi_id=engagement_kpi.id,
        name="Instagram Engagement Rate - Average",
        code="INSTAGRAM_ENG_AVG_2024",
        description="Average Instagram engagement rate across industries",
        
        # Metric
        metric_value=1.94,
        metric_unit="%",
        statistic_type="mean",
        
        # Definition
        metric_definition="Percentage of followers who engage with posts (likes, comments, shares)",
        metric_normalization="(Total Engagements / Total Followers) * 100",
        
        # Context
        company_size="All",
        industry="Cross-industry",
        geography="Global",
        time_period="2024",
        population="Instagram business accounts",
        sample_size=10000,
        
        # Source
        source_publisher="Hootsuite",
        source_title="Social Media Benchmarks Report 2024",
        source_year=2024,
        source_url="https://www.hootsuite.com/research/social-media-benchmarks",
        source_credibility="high",
        
        # Methodology
        methodology_notes="Data collected from Hootsuite analytics across business accounts.",
        caveats="Engagement rates vary significantly by follower count, content type, and industry.",
        
        # Quality
        confidence_level="medium",
        data_quality_score=85,
        benchmark_category="industry_standard",
        is_featured=False
    )
    
    return [email_open_b2b, email_ctr_b2b, social_engagement]


# ============================================================================
# Example 5: Customer Service Benchmarks
# ============================================================================

def create_customer_service_benchmarks():
    """Create customer service benchmarks."""
    
    # First Response Time
    frt_kpi = KPI(name="First Response Time", code="FIRST_RESPONSE_TIME")
    
    frt_benchmark = Benchmark(
        kpi_id=frt_kpi.id,
        name="First Response Time - SaaS Average",
        code="FRT_SAAS_AVG_2024",
        description="Average first response time for SaaS support tickets",
        
        # Metric
        metric_value=12.5,
        metric_unit="hours",
        statistic_type="median",
        
        # Definition
        metric_definition="Time from ticket creation to first agent response",
        metric_normalization="Measured in business hours",
        metric_filters={
            "ticket_priority": ["normal", "high"],
            "channels": ["email", "chat", "portal"],
            "excluded": ["auto_responses"]
        },
        
        # Context
        company_size="SMB to Enterprise",
        industry="SaaS",
        geography="Global",
        time_period="2024",
        population="Support tickets",
        sample_size=50000,
        
        # Source
        source_publisher="Zendesk",
        source_title="Customer Service Benchmark Report 2024",
        source_year=2024,
        source_url="https://www.zendesk.com/benchmark/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=93,
        benchmark_category="industry_standard",
        is_featured=False
    )
    
    # Customer Satisfaction Score (CSAT)
    csat_kpi = KPI(name="Customer Satisfaction Score", code="CSAT")
    
    csat_benchmark = Benchmark(
        kpi_id=csat_kpi.id,
        name="CSAT - SaaS Industry Average",
        code="CSAT_SAAS_AVG_2024",
        description="Average CSAT score for SaaS companies",
        
        # Metric
        metric_value=86,
        metric_unit="score (0-100)",
        statistic_type="mean",
        
        # Definition
        metric_definition="Percentage of customers rating their experience as satisfied or very satisfied",
        metric_normalization="(Satisfied + Very Satisfied) / Total Responses * 100",
        
        # Context
        industry="SaaS",
        geography="Global",
        time_period="2024",
        population="Customer surveys",
        sample_size=100000,
        
        # Source
        source_publisher="Qualtrics",
        source_title="XM Institute Customer Experience Benchmarks 2024",
        source_year=2024,
        source_url="https://www.qualtrics.com/xm-institute/benchmarks/",
        source_credibility="high",
        
        # Quality
        confidence_level="high",
        data_quality_score=94,
        benchmark_category="industry_standard",
        is_featured=True
    )
    
    return [frt_benchmark, csat_benchmark]


# ============================================================================
# Usage Example
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Benchmark Examples")
    print("=" * 80)
    
    # Create various benchmark sets
    ecommerce_benchmarks = create_ecommerce_conversion_benchmarks()
    print(f"\n✓ Created {len(ecommerce_benchmarks)} e-commerce benchmarks")
    
    saas_benchmarks = create_saas_metrics_benchmarks()
    print(f"✓ Created {len(saas_benchmarks)} SaaS benchmarks")
    
    performance_benchmarks = create_website_performance_benchmarks()
    print(f"✓ Created {len(performance_benchmarks)} website performance benchmarks")
    
    marketing_benchmarks = create_marketing_benchmarks()
    print(f"✓ Created {len(marketing_benchmarks)} marketing benchmarks")
    
    service_benchmarks = create_customer_service_benchmarks()
    print(f"✓ Created {len(service_benchmarks)} customer service benchmarks")
    
    total = (len(ecommerce_benchmarks) + len(saas_benchmarks) + 
             len(performance_benchmarks) + len(marketing_benchmarks) + 
             len(service_benchmarks))
    
    print(f"\n{'=' * 80}")
    print(f"Total: {total} benchmarks created with full citation and context")
    print("=" * 80)
