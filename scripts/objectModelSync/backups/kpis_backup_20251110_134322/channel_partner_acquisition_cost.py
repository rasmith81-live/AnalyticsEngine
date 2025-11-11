"""
Channel Partner Acquisition Cost KPI

The total cost associated with acquiring a new channel partner, including recruitment, training, and onboarding expenses.
"""

CHANNEL_PARTNER_ACQUISITION_COST = {
    "code": "CHANNEL_PARTNER_ACQUISITION_COST",
    "name": "Channel Partner Acquisition Cost",
    "description": "The total cost associated with acquiring a new channel partner, including recruitment, training, and onboarding expenses.",
    "formula": "Total Costs of Acquiring New Partners / Total Number of New Partners Acquired",
    "calculation_formula": "Total Costs of Acquiring New Partners / Total Number of New Partners Acquired",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The total cost associated with acquiring a new channel partner, including recruitment, training, and onboarding expenses.",
    "expected_business_insights": "Allows for evaluation of investment efficiency in acquiring new partners and informs budget allocation.",
    "measurement_approach": "Includes costs related to marketing, sales, and onboarding new channel partners.",
    "trend_analysis": """
    * Increasing channel partner acquisition costs may indicate higher recruitment or training expenses, or a more competitive market for new partners.
    * Decreasing costs could signal improved efficiency in onboarding processes or a shift towards lower-cost recruitment channels.
    """,
    "diagnostic_questions": """
    * Are there specific regions or industries where the cost of acquiring channel partners is significantly higher?
    * What is the average time and resources required to fully onboard a new channel partner?
    """,
    "actionable_tips": """
    * Invest in targeted recruitment strategies to attract partners with lower acquisition costs.
    * Implement more efficient training programs to reduce onboarding expenses.
    * Explore partnerships with industry associations or trade groups to access potential partners at a lower cost.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of channel partner acquisition costs over time.
    * Comparison bar charts to visualize the variance in acquisition costs across different regions or industries.
    """,
    "risk_warnings": """
    * High acquisition costs can impact the overall profitability of the channel sales program.
    * Significant fluctuations in acquisition costs may indicate instability in the partner network or market conditions.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems to track and analyze the effectiveness of different recruitment channels.
    * Learning Management Systems (LMS) for efficient and cost-effective training of new channel partners.
    """,
    "integration_points": """
    * Integrate channel partner acquisition cost data with sales performance metrics to assess the ROI of different partner acquisition strategies.
    * Link acquisition cost information with financial systems to accurately calculate the overall cost of sales.
    """,
    "change_impact_analysis": """
    * Reducing acquisition costs may lead to increased profitability, but could also impact the quality and commitment of new partners.
    * Higher acquisition costs may require adjustments in pricing strategies or sales targets to maintain profitability.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Onboarding", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
