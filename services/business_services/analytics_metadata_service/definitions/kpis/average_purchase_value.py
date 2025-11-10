"""
Average Purchase Value KPI

The average amount of money spent by customers per transaction.
"""

AVERAGE_PURCHASE_VALUE = {
    "code": "AVERAGE_PURCHASE_VALUE",
    "name": "Average Purchase Value",
    "description": "The average amount of money spent by customers per transaction.",
    "formula": "Total Revenue / Total Number of Purchases",
    "calculation_formula": "Total Revenue / Total Number of Purchases",
    "category": "Sales Development",
    "is_active": True,
    "kpi_definition": "The average amount of money spent by customers per transaction.",
    "expected_business_insights": "Reflects the value of an average transaction and helps in forecasting revenue.",
    "measurement_approach": "Measures the average amount spent by a customer on a single purchase.",
    "trend_analysis": """
    * The average purchase value may increase over time due to inflation or changes in customer spending habits.
    * A decreasing average purchase value could indicate pricing pressure, changes in product mix, or declining customer satisfaction.
    """,
    "diagnostic_questions": """
    * Are there specific products or categories driving the changes in average purchase value?
    * How does the average purchase value compare with industry benchmarks or historical data?
    """,
    "actionable_tips": """
    * Implement upselling and cross-selling strategies to increase the average purchase value.
    * Offer bundled discounts or loyalty programs to encourage higher spending per transaction.
    * Regularly review and adjust pricing strategies to maintain or increase the average purchase value.
    """,
    "visualization_suggestions": """
    * Line charts showing the average purchase value over time.
    * Pie charts to visualize the distribution of purchase values across different customer segments or product categories.
    """,
    "risk_warnings": """
    * A declining average purchase value may lead to reduced revenue and profitability.
    * An excessively high average purchase value may indicate a lack of customer diversity or potential pricing issues.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track customer purchasing behavior and preferences.
    * Point-of-sale (POS) systems with reporting capabilities to analyze transaction data and identify opportunities for increasing purchase value.
    """,
    "integration_points": """
    * Integrate average purchase value tracking with marketing automation platforms to personalize offers and promotions based on customer spending patterns.
    * Link with inventory management systems to ensure adequate stock levels for high-value items and optimize product mix.
    """,
    "change_impact_analysis": """
    * Increasing the average purchase value can lead to higher revenue and improved customer lifetime value.
    * However, aggressive tactics to raise the average purchase value may negatively impact customer satisfaction and retention.
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Purchase History", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
}
