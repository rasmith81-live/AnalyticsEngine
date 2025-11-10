"""
Sales Growth Year-over-Year KPI

The percentage increase in sales compared to the same period in the previous year.
"""

from analytics_models import KPI

SALES_GROWTH_YEAR_OVER_YEAR = KPI(
    name="Sales Growth Year-over-Year",
    code="SALES_GROWTH_YEAR_OVER_YEAR",
    category="Sales Development",
    
    # Core Definition
    description="The percentage increase in sales compared to the same period in the previous year.",
    kpi_definition="The percentage increase in sales compared to the same period in the previous year.",
    expected_business_insights="Indicates business growth and the effectiveness of sales strategies.",
    measurement_approach="Compares the increase in sales over a year to the previous year\'s sales.",
    
    # Formula
    formula="((Sales in Current Year - Sales in Previous Year) / Sales in Previous Year) * 100",
    calculation_formula="((Sales in Current Year - Sales in Previous Year) / Sales in Previous Year) * 100",
    
    # Analysis
    trend_analysis="""
    * Sales growth tends to fluctuate based on economic conditions, industry trends, and competitive landscape.
    * An upward trend in sales growth may indicate successful product launches, effective marketing campaigns, or improved sales strategies.
    * A downward trend could signal market saturation, increased competition, or shifts in consumer preferences.
    """,
    diagnostic_questions="""
    * What factors have contributed to the increase or decrease in sales growth compared to the previous year?
    * Are there specific product lines or customer segments driving the changes in sales growth?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in market research to identify emerging opportunities and customer needs.
    * Enhance sales training and coaching programs to improve the performance of the sales team.
    * Explore new distribution channels or partnerships to expand market reach.
    """,
    visualization_suggestions="""
    * Line charts showing year-over-year sales growth by product category or geographic region.
    * Comparative bar graphs to visualize the performance of different sales teams or individual sales representatives.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Rapid sales growth may strain operational resources and lead to issues with order fulfillment or customer service.
    * A decline in sales growth could impact revenue projections and shareholder confidence.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track sales activities and customer interactions.
    * Business intelligence tools for analyzing sales data and identifying trends or opportunities.
    """,
    integration_points="""
    * Integrate sales growth data with inventory management systems to ensure adequate stock levels to meet demand.
    * Link sales growth metrics with financial reporting systems to assess the impact on overall revenue and profitability.
    """,
    change_impact_analysis="""
    * Increasing sales growth may require additional investment in marketing and sales resources.
    * Declining sales growth could necessitate cost-cutting measures or strategic shifts in product offerings.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
