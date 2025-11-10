"""
Sales Training Material Update Frequency KPI

The frequency at which sales training materials are updated to reflect the latest products, services, and selling techniques.
"""

SALES_TRAINING_MATERIAL_UPDATE_FREQUENCY = {
    "code": "SALES_TRAINING_MATERIAL_UPDATE_FREQUENCY",
    "name": "Sales Training Material Update Frequency",
    "description": "The frequency at which sales training materials are updated to reflect the latest products, services, and selling techniques.",
    "formula": "Number of Updates per Time Period",
    "calculation_formula": "Number of Updates per Time Period",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The frequency at which sales training materials are updated to reflect the latest products, services, and selling techniques.",
    "expected_business_insights": "Ensures that sales reps are receiving current and relevant information, reflecting changes in the market and product offerings.",
    "measurement_approach": "Measures how often sales training materials are reviewed and updated.",
    "trend_analysis": """
    * Increasing frequency of updates may indicate a proactive approach to keeping sales teams informed about the latest offerings and market trends.
    * Conversely, a decreasing update frequency could signal complacency or a lack of emphasis on continuous improvement in sales training.
    """,
    "diagnostic_questions": """
    * Are the updates to sales training materials aligned with the launch of new products or services?
    * How do sales representatives perceive the relevance and effectiveness of the current training materials?
    """,
    "actionable_tips": """
    * Establish a regular review schedule to ensure sales training materials are updated in a timely manner.
    * Solicit feedback from the sales team to identify areas where training materials need improvement or updates.
    """,
    "visualization_suggestions": """
    * Line charts showing the frequency of updates over time.
    * Comparison charts to illustrate the correlation between update frequency and sales performance metrics.
    """,
    "risk_warnings": """
    * Outdated sales training materials may lead to misinformed sales pitches and lost opportunities.
    * Infrequent updates could result in a disconnect between the sales team and the current market landscape.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) with version control capabilities to track and manage updates to training materials.
    * Content management systems (CMS) for centralized storage and easy access to sales training materials.
    """,
    "integration_points": """
    * Integrate update frequency data with sales performance metrics to assess the impact of updated materials on sales outcomes.
    * Link training material updates with product development and marketing calendars to ensure alignment with new launches and campaigns.
    """,
    "change_impact_analysis": """
    * Improving the update frequency can enhance sales team productivity and effectiveness in engaging with customers.
    * However, frequent updates may also require additional resources and time commitment from the sales enablement and product teams.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Partner Training", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
