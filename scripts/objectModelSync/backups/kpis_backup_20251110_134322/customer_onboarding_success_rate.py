"""
Customer Onboarding Success Rate KPI

The success rate of bringing new customers up to speed with the product or service.
"""

CUSTOMER_ONBOARDING_SUCCESS_RATE = {
    "code": "CUSTOMER_ONBOARDING_SUCCESS_RATE",
    "name": "Customer Onboarding Success Rate",
    "description": "The success rate of bringing new customers up to speed with the product or service.",
    "formula": "(Number of Customers Successfully Onboarded / Total Number of New Customers) * 100",
    "calculation_formula": "(Number of Customers Successfully Onboarded / Total Number of New Customers) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The success rate of bringing new customers up to speed with the product or service.",
    "expected_business_insights": "Measures the quality and effectiveness of the onboarding process, which can impact long-term customer retention.",
    "measurement_approach": "The percentage of new customers who complete the onboarding process effectively.",
    "trend_analysis": """
    * An increasing customer onboarding success rate may indicate improved training processes or a better understanding of customer needs.
    * A decreasing rate could signal issues with product complexity, ineffective onboarding methods, or a lack of customer support.
    """,
    "diagnostic_questions": """
    * Are there specific aspects of the onboarding process that customers struggle with the most?
    * How does our customer onboarding success rate compare with industry benchmarks or competitors?
    """,
    "actionable_tips": """
    * Implement a comprehensive onboarding program that addresses common customer pain points and provides ongoing support.
    * Utilize customer feedback to continuously improve the onboarding process and make it more user-friendly.
    * Provide clear and accessible resources, such as tutorials and FAQs, to assist customers in getting started with the product or service.
    """,
    "visualization_suggestions": """
    * Line charts showing the customer onboarding success rate over time to identify trends and patterns.
    * Pie charts comparing success rates for different customer segments or product categories.
    """,
    "risk_warnings": """
    * A low customer onboarding success rate can lead to customer frustration, increased support costs, and potential churn.
    * Inadequate onboarding may result in underutilization of the product or service, impacting customer lifetime value.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer onboarding progress and interactions.
    * Learning management systems (LMS) to create and manage onboarding materials and courses.
    """,
    "integration_points": """
    * Integrate customer onboarding success rate with customer satisfaction metrics to understand the impact of onboarding on overall satisfaction.
    * Link onboarding data with sales performance to assess the correlation between successful onboarding and sales outcomes.
    """,
    "change_impact_analysis": """
    * Improving the customer onboarding success rate can lead to higher customer retention and increased lifetime value.
    * However, changes in onboarding processes may require additional resources and time investment, impacting short-term efficiency.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]},
    "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "INSIDE_SALES",
}
