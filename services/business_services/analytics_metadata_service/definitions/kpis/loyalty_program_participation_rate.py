"""
Loyalty Program Participation Rate KPI

The percentage of customers participating in a company’s loyalty or rewards program.
"""

LOYALTY_PROGRAM_PARTICIPATION_RATE = {
    "code": "LOYALTY_PROGRAM_PARTICIPATION_RATE",
    "name": "Loyalty Program Participation Rate",
    "description": "The percentage of customers participating in a company’s loyalty or rewards program.",
    "formula": "(Number of Loyalty Program Members / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Loyalty Program Members / Total Number of Customers) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The percentage of customers participating in a company’s loyalty or rewards program.",
    "expected_business_insights": "Indicates customer interest in loyalty incentives and can guide program improvements.",
    "measurement_approach": "Tracks the percentage of customers who are active members of a loyalty program.",
    "trend_analysis": """
    * An increasing loyalty program participation rate may indicate successful marketing efforts or enhanced program benefits that attract more customers.
    * A decreasing rate could signal dissatisfaction with the program, lack of awareness, or ineffective rewards, leading to potential customer churn.
    """,
    "diagnostic_questions": """
    * What are the primary reasons customers cite for participating or not participating in the loyalty program?
    * How does the participation rate vary across different customer segments or geographic regions?
    """,
    "actionable_tips": """
    * Regularly review and update the loyalty program to ensure it remains attractive and relevant to customers.
    * Personalize rewards and incentives based on individual customer preferences and purchase history.
    * Implement targeted marketing campaigns to promote the benefits of the loyalty program and encourage participation.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend in participation rate over time.
    * Pie charts comparing participation rates across different customer segments.
    """,
    "risk_warnings": """
    * A low participation rate may lead to reduced customer retention and lower overall sales.
    * High participation rates without corresponding increases in customer engagement or satisfaction could indicate a need for program adjustments.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and analyze customer participation data.
    * Marketing automation tools to personalize loyalty program communications and offers.
    """,
    "integration_points": """
    * Integrate participation rate data with customer feedback and satisfaction scores to understand the impact of the loyalty program on overall customer experience.
    * Link participation rates with sales performance metrics to assess the program's influence on purchasing behavior.
    """,
    "change_impact_analysis": """
    * An increase in participation rate may lead to higher customer lifetime value and improved brand advocacy.
    * Conversely, a decrease in participation could result in reduced customer loyalty and advocacy, impacting long-term sales and profitability.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Loyalty Program", "Sales Training Program"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
