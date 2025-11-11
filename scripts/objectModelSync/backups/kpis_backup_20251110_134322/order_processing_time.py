"""
Order Processing Time KPI

The time it takes to process a customer order from receipt to shipment.
"""

ORDER_PROCESSING_TIME = {
    "code": "ORDER_PROCESSING_TIME",
    "name": "Order Processing Time",
    "description": "The time it takes to process a customer order from receipt to shipment.",
    "formula": "Average Time Taken from Order Receipt to Shipment",
    "calculation_formula": "Average Time Taken from Order Receipt to Shipment",
    "category": "Sales Operations",
    "is_active": True,
    "kpi_definition": "The time it takes to process a customer order from receipt to shipment.",
    "expected_business_insights": "Assesses the efficiency of order fulfillment and identifies bottlenecks in the process.",
    "measurement_approach": "Measures the time taken to process an order from receipt to shipment.",
    "trend_analysis": """
    * Increasing order processing time may indicate inefficiencies in the order fulfillment process or a surge in order volume.
    * Decreasing processing time can signal improved operational workflows, better inventory management, or streamlined order entry processes.
    """,
    "diagnostic_questions": """
    * Are there specific stages in the order processing workflow that are causing delays?
    * How does our order processing time compare with industry benchmarks or customer expectations?
    """,
    "actionable_tips": """
    * Implement automation in order processing to reduce manual handling and errors.
    * Train staff on efficient order processing techniques and time management.
    * Regularly review and optimize the order processing workflow to identify and eliminate bottlenecks.
    """,
    "visualization_suggestions": """
    * Line charts showing order processing time over different time periods to identify trends and fluctuations.
    * Stacked bar charts comparing processing times for different product categories or customer segments.
    """,
    "risk_warnings": """
    * Extended order processing time can lead to delayed shipments, customer dissatisfaction, and potential order cancellations.
    * Consistently long processing times may indicate systemic issues in the sales operations that could impact overall business performance.
    """,
    "tracking_tools": """
    * Order management systems like Salesforce or SAP to streamline and automate order processing.
    * Workflow management tools such as Trello or Asana to optimize and track order processing tasks.
    """,
    "integration_points": """
    * Integrate order processing time data with customer relationship management (CRM) systems to understand the impact on customer satisfaction and retention.
    * Link order processing time with inventory management systems to ensure timely stock replenishment and fulfillment.
    """,
    "change_impact_analysis": """
    * Reducing order processing time can lead to improved customer satisfaction, repeat business, and positive word-of-mouth referrals.
    * However, overly aggressive reductions in processing time may lead to errors, quality issues, or increased operational costs.
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
}
