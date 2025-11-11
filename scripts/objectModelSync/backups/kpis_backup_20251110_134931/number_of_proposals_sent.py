"""
Number of Proposals Sent

The total number of sales proposals or quotes sent to potential customers.
"""

NUMBER_OF_PROPOSALS_SENT = {
    "code": "NUMBER_OF_PROPOSALS_SENT",
    "name": "Number of Proposals Sent",
    "description": "The total number of sales proposals or quotes sent to potential customers.",
    "formula": "Total Number of Sales Proposals Issued",
    "calculation_formula": "Total Number of Sales Proposals Issued",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Proposals Sent to be added.",
    "trend_analysis": """

    * An increasing number of proposals sent may indicate a proactive sales team or a growing customer base.
    * A decreasing number could signal a lack of lead generation or a shift in sales strategy towards more targeted prospects.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales channels or regions that are driving the majority of proposal requests?
    * How does the conversion rate from proposals to sales compare to historical data or industry benchmarks?
    
    """,
    "actionable_tips": """

    * Implement a CRM system to better track and manage proposal requests and follow-ups.
    * Provide sales training on effective proposal writing and presentation techniques.
    * Regularly review and update proposal templates to ensure they align with the latest product or service offerings.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the monthly or quarterly trend in the number of proposals sent.
    * Pie charts to compare the distribution of proposals across different product lines or customer segments.
    
    """,
    "risk_warnings": """

    * A high number of proposals sent without corresponding sales could indicate a problem with the quality of leads or the effectiveness of the sales team.
    * A low number of proposals may lead to missed opportunities and stagnant sales growth.
    
    """,
    "tracking_tools": """

    * Proposal management software like PandaDoc or Qwilr for creating, sending, and tracking proposals.
    * Data analytics tools to identify patterns in proposal requests and optimize sales strategies.
    
    """,
    "integration_points": """

    * Integrate proposal tracking with the CRM system to streamline lead management and follow-up processes.
    * Link proposal data with marketing automation platforms to align sales and marketing efforts for better lead generation.
    
    """,
    "change_impact_analysis": """

    * An increase in the number of proposals sent may lead to higher workload for the sales team and a need for more efficient processes.
    * A decrease in proposals could impact revenue and market share if not addressed with targeted marketing and sales efforts.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"], "last_validated": "2025-11-10T13:43:23.712843"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        457,
                        470,
                        480,
                        444,
                        489,
                        448,
                        456,
                        447,
                        452,
                        490,
                        492,
                        476
                ],
                "unit": "count"
        },
        "current": {
                "value": 476,
                "unit": "count",
                "change": -16,
                "change_percent": -3.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 466.75,
                "min": 444,
                "max": 492,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 95.8,
                        "percentage": 20.1
                },
                {
                        "category": "Category B",
                        "value": 63.35,
                        "percentage": 13.3
                },
                {
                        "category": "Category C",
                        "value": 87.97,
                        "percentage": 18.5
                },
                {
                        "category": "Category D",
                        "value": 44.86,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 184.02,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.712843",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Number of Proposals Sent"
        }
    },
}
