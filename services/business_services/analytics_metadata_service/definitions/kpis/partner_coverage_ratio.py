"""
Partner Coverage Ratio KPI

The ratio of the number of active channel partners to the total addressable market, indicating the extent of market coverage through partners.
"""

PARTNER_COVERAGE_RATIO = {
    "code": "PARTNER_COVERAGE_RATIO",
    "name": "Partner Coverage Ratio",
    "description": "The ratio of the number of active channel partners to the total addressable market, indicating the extent of market coverage through partners.",
    "formula": "Number of Market Areas or Customer Segments / Number of Active Partners",
    "calculation_formula": "Number of Market Areas or Customer Segments / Number of Active Partners",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The ratio of the number of active channel partners to the total addressable market, indicating the extent of market coverage through partners.",
    "expected_business_insights": "Indicates whether there are sufficient partners to cover the market and informs recruitment strategies.",
    "measurement_approach": "Compares the number of partners to the potential market areas or customer segments they serve.",
    "trend_analysis": """
    * An increasing partner coverage ratio may indicate successful onboarding of new partners or expansion into new markets.
    * A decreasing ratio could signal partner attrition or a lack of focus on partner enablement and support.
    """,
    "diagnostic_questions": """
    * Are there specific regions or segments of the market where we have a low partner coverage ratio?
    * What are the main reasons for partners leaving or becoming inactive, and how can we address these issues?
    """,
    "actionable_tips": """
    * Invest in partner training and enablement programs to ensure partners are equipped to effectively cover the market.
    * Regularly assess the performance and engagement of existing partners to identify areas for improvement or expansion.
    * Implement a structured partner recruitment strategy to fill gaps in market coverage.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of partner coverage ratio over time.
    * Geospatial maps to visualize the distribution of partners across different regions.
    """,
    "risk_warnings": """
    * A low partner coverage ratio may result in missed opportunities and reduced market penetration.
    * Over-reliance on a small number of partners can create vulnerability to market changes or partner turnover.
    """,
    "tracking_tools": """
    * Partner relationship management (PRM) software to track partner performance and engagement.
    * Market analysis tools to identify potential areas for partner expansion based on market demand.
    """,
    "integration_points": """
    * Integrate partner coverage data with sales and marketing systems to align partner efforts with overall go-to-market strategies.
    * Link partner coverage metrics with customer relationship management (CRM) systems to understand the impact on customer reach and engagement.
    """,
    "change_impact_analysis": """
    * Improving partner coverage can lead to increased market share and revenue, but may also require additional resources for partner support and management.
    * A decrease in partner coverage ratio can negatively impact sales performance and market competitiveness.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Market Segment", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
