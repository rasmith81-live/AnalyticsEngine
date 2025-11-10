"""
Customer Churn Rate KPI

The percentage of customers who stop doing business with the company over a given period.
"""

CUSTOMER_CHURN_RATE = {
    "code": "CUSTOMER_CHURN_RATE",
    "name": "Customer Churn Rate",
    "description": "The percentage of customers who stop doing business with the company over a given period.",
    "formula": "(Number of Customers Lost During a Period / Number of Customers at the Start of the Period) * 100",
    "calculation_formula": "(Number of Customers Lost During a Period / Number of Customers at the Start of the Period) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The percentage of customers who stop doing business with the company over a given period.",
    "expected_business_insights": "Indicates customer satisfaction and the effectiveness of customer retention strategies.",
    "measurement_approach": "The percentage of customers who stop using a company's product or service over a certain period.",
    "trend_analysis": """
    * An increasing customer churn rate may indicate issues with customer satisfaction, product quality, or customer service.
    * A decreasing rate could signal improved customer retention strategies, product enhancements, or better customer support.
    """,
    "diagnostic_questions": """
    * Are there common reasons why customers are leaving, and can these be addressed?
    * How does our customer churn rate compare to industry benchmarks or our competitors?
    """,
    "actionable_tips": """
    * Implement customer feedback mechanisms to understand the reasons for churn and take corrective actions.
    * Invest in customer success programs to proactively engage with at-risk customers and improve retention.
    * Enhance product or service offerings based on customer feedback and market trends to increase satisfaction and loyalty.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of customer churn rate over time.
    * Pie charts to visualize the reasons for customer churn and their relative impact.
    """,
    "risk_warnings": """
    * High customer churn rates can lead to revenue loss and damage to the company's reputation.
    * Consistently high churn rates may indicate systemic issues that require significant changes in strategy or operations.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer interactions and identify at-risk accounts.
    * Survey tools to gather feedback from departing customers and analyze the root causes of churn.
    """,
    "integration_points": """
    * Integrate customer churn data with sales and marketing systems to identify patterns and develop targeted retention campaigns.
    * Link customer churn metrics with product development and quality assurance processes to address underlying issues.
    """,
    "change_impact_analysis": """
    * Reducing customer churn can lead to increased customer lifetime value and overall revenue growth.
    * However, efforts to reduce churn may require additional resources and investments in customer retention initiatives.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Churn Event", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lost Sale", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Subscription"]},
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
    "module_code": "INSIDE_SALES",
}
