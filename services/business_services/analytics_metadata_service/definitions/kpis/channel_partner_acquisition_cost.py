"""
Channel Partner Acquisition Cost

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
    "full_kpi_definition": "Complete definition for Channel Partner Acquisition Cost to be added.",
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
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Onboarding", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.684525"},
    "required_objects": [],
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        255,
                        256,
                        282,
                        272,
                        287,
                        259,
                        259,
                        281,
                        243,
                        248,
                        244,
                        279
                ],
                "unit": "count"
        },
        "current": {
                "value": 279,
                "unit": "count",
                "change": 35,
                "change_percent": 14.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 263.75,
                "min": 243,
                "max": 287,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 48.62,
                        "percentage": 17.4
                },
                {
                        "category": "Segment B",
                        "value": 62.99,
                        "percentage": 22.6
                },
                {
                        "category": "Segment C",
                        "value": 42.45,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 15.14,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 109.8,
                        "percentage": 39.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.443185",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Channel Partner Acquisition Cost"
        }
    },
}
