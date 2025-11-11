"""
Customer Onboarding Time KPI

The time taken to fully onboard a new customer so they are utilizing the product or service effectively.
"""

CUSTOMER_ONBOARDING_TIME = {
    "code": "CUSTOMER_ONBOARDING_TIME",
    "name": "Customer Onboarding Time",
    "description": "The time taken to fully onboard a new customer so they are utilizing the product or service effectively.",
    "formula": "Average Time Taken From Signup to Achieving First Value Milestone",
    "calculation_formula": "Average Time Taken From Signup to Achieving First Value Milestone",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The time taken to fully onboard a new customer so they are utilizing the product or service effectively.",
    "expected_business_insights": "Assesses the efficiency of the onboarding process and its impact on time-to-value for customers.",
    "measurement_approach": "Tracks the average time taken for a new customer to get up and running with the product or service.",
    "trend_analysis": """
    * Decreasing customer onboarding time may indicate improved onboarding processes or better product usability.
    * An increasing onboarding time could signal issues with training, product complexity, or resource constraints.
    """,
    "diagnostic_questions": """
    * Are there specific steps in the onboarding process that consistently take longer than expected?
    * How does our onboarding time compare with industry benchmarks or best practices?
    """,
    "actionable_tips": """
    * Streamline onboarding processes by creating standardized templates and resources.
    * Invest in training and support resources to help customers get up to speed more quickly.
    * Utilize customer feedback to identify areas of improvement in the onboarding experience.
    """,
    "visualization_suggestions": """
    * Line charts showing the average onboarding time over different time periods.
    * Stacked bar charts comparing onboarding times for different customer segments or product lines.
    """,
    "risk_warnings": """
    * Long onboarding times can lead to customer frustration and potential churn.
    * Rapidly increasing onboarding times may indicate scalability issues with current processes.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track onboarding progress and customer interactions.
    * Learning management systems (LMS) for creating and delivering training materials.
    """,
    "integration_points": """
    * Integrate onboarding time data with customer satisfaction metrics to understand the impact of onboarding on overall customer experience.
    * Link onboarding time with sales performance data to assess the impact of onboarding on customer lifetime value.
    """,
    "change_impact_analysis": """
    * Reducing onboarding time can lead to increased customer satisfaction and potentially higher retention rates.
    * However, rapid onboarding may also lead to lower product adoption and usage if customers feel overwhelmed.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
