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
                        75.49,
                        73.41,
                        86.19,
                        88.54,
                        78.87,
                        81.31,
                        71.53,
                        74.3,
                        88.39,
                        84.77,
                        84.2,
                        84.11
                ],
                "unit": "%"
        },
        "current": {
                "value": 84.11,
                "unit": "%",
                "change": -0.09,
                "change_percent": -0.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 80.93,
                "min": 71.53,
                "max": 88.54,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.13,
                        "percentage": 27.5
                },
                {
                        "category": "Category B",
                        "value": 19.15,
                        "percentage": 22.8
                },
                {
                        "category": "Category C",
                        "value": 8.24,
                        "percentage": 9.8
                },
                {
                        "category": "Category D",
                        "value": 9.61,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 23.98,
                        "percentage": 28.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.997432",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Proposal Acceptance Rate"
        }
    },
}
