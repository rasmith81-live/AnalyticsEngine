"""
Proposal-to-Negotiation Ratio

The ratio of proposals given to the number of negotiations started with potential customers.
"""

PROPOSAL_TO_NEGOTIATION_RATIO = {
    "code": "PROPOSAL_TO_NEGOTIATION_RATIO",
    "name": "Proposal-to-Negotiation Ratio",
    "description": "The ratio of proposals given to the number of negotiations started with potential customers.",
    "formula": "Number of Negotiations / Number of Proposals Sent * 100",
    "calculation_formula": "Number of Negotiations / Number of Proposals Sent * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Proposal-to-Negotiation Ratio to be added.",
    "trend_analysis": """



    * An increasing proposal-to-negotiation ratio may indicate that the sales team is becoming more effective at qualifying potential customers before entering negotiations.
    * A decreasing ratio could signal that the sales team is struggling to move potential customers from the proposal stage to negotiation, possibly due to ineffective proposals or lack of follow-up.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific factors that tend to result in successful negotiations after a proposal is given?
    * What feedback have potential customers provided about the proposals, and how can we use that feedback to improve our approach?
    
    
    
    """,
    "actionable_tips": """



    * Provide sales training to improve the quality and effectiveness of proposals.
    * Implement a follow-up process to ensure that proposals are not left unaddressed and to gather feedback for improvement.
    * Analyze successful negotiations to identify common factors and incorporate them into the proposal process.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of the ratio over time to identify any consistent patterns or changes.
    * Stacked bar charts comparing the ratio across different sales representatives or regions to identify potential areas for improvement.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low proposal-to-negotiation ratio may indicate a need for more targeted lead generation or a review of the qualification process.
    * A high ratio could lead to missed opportunities if potential customers are not being effectively moved towards negotiation.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track the status of proposals and negotiations with potential customers.
    * Sales enablement platforms to create and manage high-quality, effective proposals.
    
    
    
    """,
    "integration_points": """



    * Integrate the proposal-to-negotiation ratio with lead generation and qualification processes to ensure a consistent and effective sales pipeline.
    * Link the ratio with customer feedback systems to gather insights on the effectiveness of proposals and areas for improvement.
    
    
    
    """,
    "change_impact_analysis": """



    * An improved proposal-to-negotiation ratio can lead to more efficient use of sales resources and potentially higher conversion rates.
    * However, a significant change in the ratio may require adjustments in sales strategies and resource allocation, potentially impacting short-term sales performance.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Proposal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.291137"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        63.64,
                        52.76,
                        68.67,
                        56.0,
                        62.95,
                        68.69,
                        64.9,
                        67.06,
                        62.56,
                        62.66,
                        52.05,
                        62.44
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.44,
                "unit": "%",
                "change": 10.39,
                "change_percent": 20.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 62.03,
                "min": 52.05,
                "max": 68.69,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.12,
                        "percentage": 22.6
                },
                {
                        "category": "Segment B",
                        "value": 13.06,
                        "percentage": 20.9
                },
                {
                        "category": "Segment C",
                        "value": 5.48,
                        "percentage": 8.8
                },
                {
                        "category": "Segment D",
                        "value": 4.01,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 25.77,
                        "percentage": 41.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.682968",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Proposal-to-Negotiation Ratio"
        }
    },
}
