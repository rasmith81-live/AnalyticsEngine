"""
Sales Conversion Rate KPI

The percentage of opportunities that are converted to closed deals.
"""

SALES_CONVERSION_RATE = {
    "code": "SALES_CONVERSION_RATE",
    "name": "Sales Conversion Rate",
    "description": "The percentage of opportunities that are converted to closed deals.",
    "formula": "(Number of Sales / Total Number of Leads) * 100",
    "calculation_formula": "(Number of Sales / Total Number of Leads) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The percentage of opportunities that are converted to closed deals.",
    "expected_business_insights": "Shows the effectiveness of the sales funnel and identifies the quality of leads being generated.",
    "measurement_approach": "Measures the percentage of leads that convert into sales.",
    "trend_analysis": """
    * An increasing sales conversion rate may indicate improved sales strategies or a growing market demand.
    * A decreasing rate could signal ineffective sales processes or a decline in customer interest.
    """,
    "diagnostic_questions": """
    * Are there specific stages in the sales funnel where conversion rates drop significantly?
    * How does our sales conversion rate compare with industry benchmarks or competitor performance?
    """,
    "actionable_tips": """
    * Provide additional sales training and support for the sales team to improve their closing techniques.
    * Implement customer relationship management (CRM) software to better track and manage sales opportunities.
    * Analyze and optimize the sales process to identify and address any bottlenecks or inefficiencies.
    """,
    "visualization_suggestions": """
    * Funnel charts to visualize the conversion rates at each stage of the sales process.
    * Line graphs to track the trend of conversion rates over time.
    """,
    "risk_warnings": """
    * Low sales conversion rates can lead to missed revenue opportunities and reduced profitability.
    * Consistently low conversion rates may indicate a need for a fundamental shift in sales strategy or targeting.
    """,
    "tracking_tools": """
    * CRM systems like Salesforce or HubSpot for tracking and managing sales opportunities.
    * Sales analytics tools to gain insights into the factors affecting conversion rates.
    """,
    "integration_points": """
    * Integrate sales conversion rate data with marketing analytics to understand the impact of marketing efforts on conversion.
    * Link with customer relationship management systems to track the entire customer journey from lead to conversion.
    """,
    "change_impact_analysis": """
    * Improving the sales conversion rate can lead to increased revenue and improved overall sales performance.
    * However, a significant increase in conversion rate may also put pressure on fulfillment and delivery processes, requiring operational adjustments.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_OPERATIONS"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
