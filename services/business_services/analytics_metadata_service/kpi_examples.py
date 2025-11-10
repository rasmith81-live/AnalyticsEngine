"""
Comprehensive KPI Examples

This file demonstrates how to create KPIs with all the detailed fields including
definition, insights, measurement approach, formulas, trend analysis, diagnostic
questions, actionable steps, visualization suggestions, risk warnings, tracking
tools, integration points, and change impact.
"""

from .db_models import KPI
from .schemas import KPICreate


# ============================================================================
# Example 1: Customer Acquisition Cost (CAC) - Complete Definition
# ============================================================================

def example_customer_acquisition_cost_kpi():
    """
    Example: Comprehensive Customer Acquisition Cost KPI with all fields.
    """
    
    cac_kpi = KPI(
        object_model_id=1,  # Assuming customer segment object model
        name="Customer Acquisition Cost",
        code="CAC",
        description="The total cost of acquiring a new customer",
        is_active=True,
        
        # KPI Definition & Context
        kpi_definition=(
            "Customer Acquisition Cost (CAC) measures the total cost of acquiring a new customer, "
            "including all marketing and sales expenses divided by the number of new customers acquired "
            "during a specific period. This metric is crucial for understanding the efficiency of "
            "customer acquisition efforts and ensuring sustainable growth."
        ),
        expected_business_insights=(
            "CAC provides insights into:\n"
            "- Marketing and sales efficiency\n"
            "- Channel effectiveness (which channels deliver customers at lowest cost)\n"
            "- Scalability of customer acquisition strategies\n"
            "- ROI on marketing investments\n"
            "- Comparison with Customer Lifetime Value (CLV) to ensure profitability\n"
            "- Budget allocation optimization across marketing channels"
        ),
        measurement_approach=(
            "To measure CAC:\n"
            "1. Define the measurement period (monthly, quarterly, annually)\n"
            "2. Sum all marketing and sales expenses for the period\n"
            "3. Count the number of new customers acquired in the same period\n"
            "4. Divide total expenses by number of new customers\n"
            "5. Track consistently across periods for trend analysis\n"
            "6. Segment by channel, product, or customer type for deeper insights"
        ),
        
        # Calculation & Measurement
        formula="CAC = Total Marketing & Sales Expenses / Number of New Customers Acquired",
        calculation_formula=(
            "CAC = (Marketing Spend + Sales Salaries + Sales Commissions + "
            "Marketing Software Costs + Creative Costs + Overhead) / New Customers"
        ),
        unit_of_measure="USD",
        target_value=50.0,
        current_value=45.0,
        threshold_warning=60.0,
        threshold_critical=75.0,
        
        # Analysis & Insights
        trend_analysis=(
            "CAC trends typically show:\n"
            "- Seasonal variations (higher during peak marketing periods)\n"
            "- Decreasing CAC over time indicates improving efficiency\n"
            "- Increasing CAC may signal market saturation or increased competition\n"
            "- Sharp increases warrant immediate investigation\n"
            "- Stable CAC with growing customer base indicates scalable acquisition model\n"
            "- CAC should ideally be 1/3 or less of Customer Lifetime Value (CLV)"
        ),
        diagnostic_questions={
            "questions": [
                "What is our current CAC across all channels?",
                "Which acquisition channels have the lowest CAC?",
                "How does our CAC compare to industry benchmarks?",
                "What is the ratio of CAC to Customer Lifetime Value (CLV)?",
                "Are there seasonal patterns in our CAC?",
                "Which customer segments have the highest/lowest CAC?",
                "How long is our payback period (time to recover CAC)?",
                "What percentage of our revenue goes to customer acquisition?",
                "Are we tracking CAC by product line or service offering?",
                "How has CAC trended over the past 12 months?"
            ]
        },
        actionable_steps={
            "operational": [
                "Implement multi-touch attribution to understand channel effectiveness",
                "A/B test landing pages and ad creative to improve conversion rates",
                "Optimize sales funnel to reduce drop-off at each stage",
                "Automate repetitive marketing tasks to reduce labor costs",
                "Implement lead scoring to focus sales efforts on high-quality leads"
            ],
            "strategic": [
                "Shift budget to channels with lowest CAC and highest CLV",
                "Develop referral programs to leverage word-of-mouth acquisition",
                "Invest in content marketing for long-term organic acquisition",
                "Build strategic partnerships for co-marketing opportunities",
                "Focus on customer retention to improve overall unit economics"
            ],
            "tactical": [
                "Pause underperforming ad campaigns immediately",
                "Negotiate better rates with advertising platforms",
                "Retarget website visitors who didn't convert",
                "Optimize ad targeting to reach ideal customer profile",
                "Test new acquisition channels with small budgets"
            ]
        },
        
        # Visualization & Reporting
        visualization_suggestions={
            "primary_charts": [
                {
                    "type": "line_chart",
                    "description": "CAC trend over time with target line",
                    "axes": {"x": "Time Period", "y": "CAC ($)"}
                },
                {
                    "type": "bar_chart",
                    "description": "CAC by acquisition channel",
                    "axes": {"x": "Channel", "y": "CAC ($)"}
                }
            ],
            "secondary_charts": [
                {
                    "type": "combo_chart",
                    "description": "CAC vs CLV ratio over time",
                    "axes": {"x": "Time Period", "y1": "CAC ($)", "y2": "CLV ($)"}
                },
                {
                    "type": "waterfall_chart",
                    "description": "CAC cost breakdown by component",
                    "components": ["Marketing Spend", "Sales Salaries", "Software", "Other"]
                }
            ],
            "dashboard_kpis": [
                "Current CAC",
                "CAC Trend (% change)",
                "CAC:CLV Ratio",
                "Payback Period",
                "Best Performing Channel"
            ]
        },
        risk_warnings={
            "critical_risks": [
                {
                    "condition": "CAC > CLV",
                    "warning": "Unsustainable business model - losing money on each customer",
                    "action": "Immediately review pricing, reduce acquisition costs, or improve retention"
                },
                {
                    "condition": "CAC increasing >20% month-over-month",
                    "warning": "Rapid cost escalation - potential market saturation",
                    "action": "Investigate cause, pause inefficient campaigns, explore new channels"
                }
            ],
            "warning_signs": [
                {
                    "condition": "CAC:CLV ratio > 1:3",
                    "warning": "Marginal profitability - limited room for error",
                    "action": "Focus on improving either CAC or CLV"
                },
                {
                    "condition": "Payback period > 12 months",
                    "warning": "Long time to recover acquisition costs",
                    "action": "Consider strategies to accelerate revenue or reduce CAC"
                }
            ]
        },
        
        # Tools & Integration
        suggested_tracking_tools={
            "analytics_platforms": [
                "Google Analytics 4 - Track conversion paths and attribution",
                "Mixpanel - Analyze user behavior and conversion funnels",
                "Amplitude - Product analytics and user journey tracking"
            ],
            "marketing_tools": [
                "HubSpot - Marketing automation and CAC tracking",
                "Salesforce - CRM with marketing attribution",
                "Segment - Customer data platform for unified tracking"
            ],
            "bi_tools": [
                "Tableau - Visual analytics and dashboards",
                "Looker - Business intelligence and reporting",
                "Power BI - Microsoft's BI platform"
            ],
            "attribution_tools": [
                "Bizible - B2B marketing attribution",
                "Rockerbox - Multi-touch attribution platform",
                "Attribution - Marketing performance measurement"
            ]
        },
        integration_points={
            "data_sources": [
                "Marketing platforms (Google Ads, Facebook Ads, LinkedIn Ads)",
                "CRM system (customer acquisition dates and sources)",
                "Accounting system (marketing and sales expenses)",
                "Analytics platforms (conversion tracking)",
                "Email marketing platforms (campaign costs and conversions)"
            ],
            "dependent_systems": [
                "Financial reporting (P&L impact)",
                "Marketing budget allocation",
                "Sales compensation planning",
                "Product pricing strategy",
                "Customer success (onboarding efficiency)"
            ],
            "api_integrations": [
                "Marketing API endpoints for spend data",
                "CRM API for customer acquisition data",
                "Accounting API for expense tracking",
                "Data warehouse for centralized reporting"
            ]
        },
        
        # Impact & Relationships
        change_impact=(
            "Changes in CAC impact multiple business areas:\n\n"
            "Increasing CAC:\n"
            "- Reduces profit margins if not offset by price increases\n"
            "- Extends payback period, impacting cash flow\n"
            "- May require increased funding or reduced growth targets\n"
            "- Signals need to optimize marketing efficiency or explore new channels\n"
            "- Could indicate market maturation or increased competition\n\n"
            "Decreasing CAC:\n"
            "- Improves unit economics and profitability\n"
            "- Enables faster growth with same budget\n"
            "- Shortens payback period, improving cash flow\n"
            "- May indicate successful optimization or untapped market opportunity\n"
            "- Allows for more aggressive customer acquisition strategies\n\n"
            "Related KPI Impacts:\n"
            "- CLV:CAC Ratio - Direct inverse relationship\n"
            "- Payback Period - Directly proportional to CAC\n"
            "- Marketing ROI - Inversely related to CAC\n"
            "- Customer Growth Rate - Inversely related (lower CAC enables faster growth)\n"
            "- Gross Margin - Affected by CAC as percentage of revenue"
        ),
        source="Industry standard metric - SaaS and e-commerce best practices",
        parent_kpi_id=None,  # This is a base KPI, not derived
        
        # Display and Categorization
        display_order=1,
        category="Customer Acquisition",
        
        # Metadata
        metadata_={
            "industry_benchmarks": {
                "saas": {"low": 30, "average": 100, "high": 300},
                "ecommerce": {"low": 10, "average": 50, "high": 150},
                "b2b": {"low": 200, "average": 500, "high": 1000}
            },
            "update_frequency": "monthly",
            "data_quality_score": 0.95,
            "last_reviewed": "2024-01-15"
        }
    )
    
    return cac_kpi


# ============================================================================
# Example 2: Net Promoter Score (NPS) - Complete Definition
# ============================================================================

def example_net_promoter_score_kpi():
    """
    Example: Comprehensive Net Promoter Score KPI.
    """
    
    nps_kpi = KPI(
        object_model_id=2,
        name="Net Promoter Score",
        code="NPS",
        description="Customer loyalty and satisfaction metric",
        is_active=True,
        
        kpi_definition=(
            "Net Promoter Score (NPS) measures customer loyalty and satisfaction by asking customers "
            "how likely they are to recommend your product or service to others on a scale of 0-10. "
            "Customers are categorized as Promoters (9-10), Passives (7-8), or Detractors (0-6). "
            "NPS is calculated as the percentage of Promoters minus the percentage of Detractors."
        ),
        expected_business_insights=(
            "NPS reveals:\n"
            "- Overall customer satisfaction and loyalty\n"
            "- Word-of-mouth potential and viral growth coefficient\n"
            "- Customer retention likelihood\n"
            "- Product-market fit strength\n"
            "- Competitive positioning\n"
            "- Early warning signs of churn risk"
        ),
        measurement_approach=(
            "To measure NPS:\n"
            "1. Survey customers with the question: 'How likely are you to recommend us to a friend?'\n"
            "2. Use a 0-10 scale for responses\n"
            "3. Categorize responses: Promoters (9-10), Passives (7-8), Detractors (0-6)\n"
            "4. Calculate: % Promoters - % Detractors\n"
            "5. Follow up with open-ended question: 'What is the primary reason for your score?'\n"
            "6. Track by customer segment, product, and time period"
        ),
        
        formula="NPS = % Promoters - % Detractors",
        calculation_formula="NPS = (Number of Promoters / Total Responses) * 100 - (Number of Detractors / Total Responses) * 100",
        unit_of_measure="score",
        target_value=50.0,
        current_value=45.0,
        threshold_warning=30.0,
        threshold_critical=10.0,
        
        trend_analysis=(
            "NPS trends indicate:\n"
            "- Improving NPS shows successful product/service enhancements\n"
            "- Declining NPS signals customer satisfaction issues requiring immediate attention\n"
            "- Stable high NPS (>50) indicates strong product-market fit\n"
            "- Seasonal variations may reflect product usage patterns\n"
            "- Segment-specific trends reveal which customer types are most satisfied"
        ),
        diagnostic_questions={
            "questions": [
                "What is our current NPS and how does it compare to industry benchmarks?",
                "What percentage of our customers are Promoters, Passives, and Detractors?",
                "What are the most common reasons given by Promoters?",
                "What are the most common reasons given by Detractors?",
                "How does NPS vary by customer segment, product, or region?",
                "What is the correlation between NPS and customer retention?",
                "How quickly do we respond to Detractor feedback?",
                "What percentage of Detractors have we successfully converted?",
                "How has NPS changed after recent product updates?",
                "What is our NPS compared to our main competitors?"
            ]
        },
        actionable_steps={
            "operational": [
                "Implement automated NPS surveys at key touchpoints",
                "Create a closed-loop feedback system to follow up with Detractors",
                "Analyze qualitative feedback to identify common themes",
                "Train customer-facing teams on improving customer experience",
                "Set up alerts for individual Detractor responses"
            ],
            "strategic": [
                "Prioritize product improvements based on Detractor feedback",
                "Build a customer advocacy program leveraging Promoters",
                "Invest in customer success to convert Passives to Promoters",
                "Address systemic issues causing customer dissatisfaction",
                "Align company culture around customer-centricity"
            ],
            "tactical": [
                "Personally reach out to Detractors within 24 hours",
                "Ask Promoters for testimonials and referrals",
                "Create case studies featuring Promoter success stories",
                "Offer special incentives to Passives to increase engagement",
                "Share NPS results and feedback across the organization"
            ]
        },
        
        visualization_suggestions={
            "primary_charts": [
                {
                    "type": "gauge_chart",
                    "description": "Current NPS score with color-coded zones",
                    "zones": {"critical": "0-30", "warning": "30-50", "good": "50-70", "excellent": "70-100"}
                },
                {
                    "type": "stacked_bar_chart",
                    "description": "Distribution of Promoters, Passives, and Detractors",
                    "categories": ["Promoters", "Passives", "Detractors"]
                }
            ],
            "secondary_charts": [
                {
                    "type": "line_chart",
                    "description": "NPS trend over time",
                    "axes": {"x": "Time Period", "y": "NPS Score"}
                },
                {
                    "type": "word_cloud",
                    "description": "Common themes from qualitative feedback"
                }
            ]
        },
        risk_warnings={
            "critical_risks": [
                {
                    "condition": "NPS < 0",
                    "warning": "More Detractors than Promoters - severe customer dissatisfaction",
                    "action": "Emergency customer experience review and immediate corrective action"
                },
                {
                    "condition": "NPS declining >10 points in a quarter",
                    "warning": "Rapid deterioration in customer satisfaction",
                    "action": "Investigate recent changes, gather urgent feedback, implement fixes"
                }
            ],
            "warning_signs": [
                {
                    "condition": "Increasing Detractor percentage",
                    "warning": "Growing customer dissatisfaction",
                    "action": "Analyze Detractor feedback and address top issues"
                }
            ]
        },
        
        suggested_tracking_tools={
            "nps_platforms": [
                "Delighted - Simple NPS surveys",
                "Promoter.io - NPS tracking and analysis",
                "Wootric - In-app NPS surveys",
                "SurveyMonkey - Customizable NPS surveys"
            ],
            "customer_success": [
                "Gainsight - Customer success platform with NPS",
                "ChurnZero - Customer success and NPS tracking",
                "Totango - Customer success management"
            ]
        },
        integration_points={
            "data_sources": [
                "Survey platforms",
                "CRM system",
                "Customer support tickets",
                "Product usage data"
            ],
            "dependent_systems": [
                "Customer success workflows",
                "Product development prioritization",
                "Marketing (advocacy programs)",
                "Executive dashboards"
            ]
        },
        
        change_impact=(
            "NPS changes impact:\n"
            "- Customer retention rates (higher NPS = lower churn)\n"
            "- Organic growth through referrals\n"
            "- Customer Lifetime Value\n"
            "- Brand reputation and market perception\n"
            "- Employee morale (customer satisfaction affects team motivation)"
        ),
        source="Fred Reichheld, Bain & Company, 2003",
        parent_kpi_id=None,
        
        display_order=2,
        category="Customer Satisfaction",
        
        metadata_={
            "industry_benchmarks": {
                "saas": {"excellent": 70, "good": 50, "average": 30},
                "retail": {"excellent": 60, "good": 40, "average": 20}
            },
            "survey_frequency": "quarterly",
            "response_rate_target": 0.30
        }
    )
    
    return nps_kpi


# ============================================================================
# Example 3: Derived KPI - Channel-Specific CAC
# ============================================================================

def example_derived_kpi_channel_cac():
    """
    Example: Derived KPI based on parent CAC, customized for specific channel.
    """
    
    google_ads_cac = KPI(
        object_model_id=1,
        name="Google Ads CAC",
        code="GOOGLE_ADS_CAC",
        description="Customer Acquisition Cost specifically for Google Ads channel",
        is_active=True,
        
        kpi_definition=(
            "Google Ads CAC measures the cost to acquire a customer specifically through "
            "Google Ads campaigns. This is a derived metric from the overall CAC, "
            "customized to track the efficiency of paid search advertising."
        ),
        expected_business_insights=(
            "Provides insights into:\n"
            "- Google Ads campaign efficiency vs other channels\n"
            "- Keyword and ad group performance\n"
            "- Quality Score impact on acquisition costs\n"
            "- Optimal bid strategies and budget allocation"
        ),
        measurement_approach=(
            "Calculate by dividing total Google Ads spend by customers acquired "
            "through Google Ads (tracked via UTM parameters and attribution)"
        ),
        
        formula="Google Ads CAC = Total Google Ads Spend / Customers from Google Ads",
        calculation_formula="Google Ads CAC = (Ad Spend + Management Fees) / New Customers (attributed to Google Ads)",
        unit_of_measure="USD",
        target_value=40.0,
        current_value=38.0,
        threshold_warning=50.0,
        threshold_critical=65.0,
        
        trend_analysis="Monitor for auction competition increases and seasonal CPC fluctuations",
        
        source="Derived from parent CAC metric, customized for Google Ads channel",
        parent_kpi_id=1,  # References the main CAC KPI
        
        display_order=10,
        category="Channel-Specific Acquisition",
        
        metadata_={
            "channel": "Google Ads",
            "attribution_model": "last-click",
            "derived_from": "CAC"
        }
    )
    
    return google_ads_cac


# ============================================================================
# Usage Example
# ============================================================================

if __name__ == "__main__":
    """
    Demonstrate creating comprehensive KPIs.
    """
    
    # Create comprehensive CAC KPI
    cac = example_customer_acquisition_cost_kpi()
    print(f"Created KPI: {cac.name}")
    print(f"Formula: {cac.formula}")
    print(f"Current Value: ${cac.current_value}")
    print(f"Target Value: ${cac.target_value}")
    print(f"\nDefinition: {cac.kpi_definition[:100]}...")
    
    # Create NPS KPI
    nps = example_net_promoter_score_kpi()
    print(f"\nCreated KPI: {nps.name}")
    print(f"Formula: {nps.formula}")
    print(f"Source: {nps.source}")
    
    # Create derived KPI
    google_cac = example_derived_kpi_channel_cac()
    print(f"\nCreated Derived KPI: {google_cac.name}")
    print(f"Parent KPI ID: {google_cac.parent_kpi_id}")
    print(f"Source: {google_cac.source}")
