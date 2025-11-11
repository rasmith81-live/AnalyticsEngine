"""
Proposal Acceptance Rate

The percentage of proposals that are accepted by prospects or clients.
"""

PROPOSAL_ACCEPTANCE_RATE = {
    "code": "PROPOSAL_ACCEPTANCE_RATE",
    "name": "Proposal Acceptance Rate",
    "description": "The percentage of proposals that are accepted by prospects or clients.",
    "formula": "Number of Proposals Accepted / Total Number of Proposals Sent * 100",
    "calculation_formula": "Number of Proposals Accepted / Total Number of Proposals Sent * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Proposal Acceptance Rate to be added.",
    "trend_analysis": """



    * An increasing proposal acceptance rate may indicate improved sales strategies or a growing demand for the product or service.
    * A decreasing rate could signal ineffective sales tactics, changes in market preferences, or increased competition.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales representatives or teams with consistently higher or lower proposal acceptance rates?
    * What factors contribute to the acceptance or rejection of proposals, and how can those be addressed?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training and support to improve the quality and relevance of proposals.
    * Regularly review and update proposal templates and content to align with prospect needs and industry trends.
    * Implement a feedback loop to gather insights from rejected proposals and use that information to refine future proposals.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the proposal acceptance rate over time to identify trends and seasonality.
    * Pie charts comparing acceptance rates by sales representative or by product/service category.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low proposal acceptance rate can lead to missed revenue opportunities and decreased market share.
    * High acceptance rates without corresponding sales conversion may indicate overcommitment or unrealistic proposals.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems like Salesforce or HubSpot to track proposal submissions and acceptance rates.
    * Proposal management software such as PandaDoc or Qwilr to streamline the creation and tracking of proposals.
    
    
    
    """,
    "integration_points": """



    * Integrate proposal acceptance data with sales performance metrics to understand the impact on overall revenue and customer acquisition costs.
    * Link with customer relationship management systems to analyze the correlation between accepted proposals and customer lifetime value.
    
    
    
    """,
    "change_impact_analysis": """



    * An improved proposal acceptance rate can lead to increased revenue and market share, but may also require adjustments in production or service delivery to meet demand.
    * Conversely, a declining acceptance rate may signal the need for product or service innovation, changes in pricing strategy, or adjustments in target markets.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lost Sale", "Partner Agreement", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.287456"},
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
                        72.6,
                        76.14,
                        67.59,
                        82.23,
                        68.38,
                        76.85,
                        78.94,
                        76.24,
                        68.86,
                        65.72,
                        65.02,
                        81.51
                ],
                "unit": "%"
        },
        "current": {
                "value": 81.51,
                "unit": "%",
                "change": 16.49,
                "change_percent": 25.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.34,
                "min": 65.02,
                "max": 82.23,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 25.66,
                        "percentage": 31.5
                },
                {
                        "category": "Segment B",
                        "value": 12.11,
                        "percentage": 14.9
                },
                {
                        "category": "Segment C",
                        "value": 14.97,
                        "percentage": 18.4
                },
                {
                        "category": "Segment D",
                        "value": 6.36,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 22.41,
                        "percentage": 27.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.675006",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Proposal Acceptance Rate"
        }
    },
}
