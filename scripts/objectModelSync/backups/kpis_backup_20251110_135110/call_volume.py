"""
Call Volume

The number of calls made by the inside sales team during a specific time period. It can help identify whether the team is making enough calls to generate leads and close deals.
"""

CALL_VOLUME = {
    "code": "CALL_VOLUME",
    "name": "Call Volume",
    "description": "The number of calls made by the inside sales team during a specific time period. It can help identify whether the team is making enough calls to generate leads and close deals.",
    "formula": "Total Number of Calls Made",
    "calculation_formula": "Total Number of Calls Made",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Call Volume to be added.",
    "trend_analysis": """


    * An increasing call volume may indicate a proactive sales team or a response to increased market opportunities.
    * A decreasing call volume could signal a lack of leads, decreased demand, or potential issues within the sales team.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific times or days when call volume tends to be higher or lower?
    * How does our call volume compare with industry benchmarks or with historical data?
    
    
    """,
    "actionable_tips": """


    * Implement call tracking software to monitor and analyze call volume trends.
    * Provide ongoing training and support to the inside sales team to improve call efficiency and effectiveness.
    * Consider adjusting call scripts or outreach strategies based on analysis of call volume and outcomes.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing call volume over time to identify trends and patterns.
    * Bar graphs comparing call volume by individual sales team members to identify top performers and areas for improvement.
    
    
    """,
    "risk_warnings": """


    * High call volume without corresponding sales may indicate inefficiencies in the sales process or product-market fit issues.
    * Low call volume may lead to missed opportunities and decreased revenue.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) systems like Salesforce or HubSpot to track and analyze call volume and outcomes.
    * Call tracking software such as CallRail or CallTrackingMetrics to monitor and optimize call performance.
    
    
    """,
    "integration_points": """


    * Integrate call volume data with lead management systems to better understand the quality of leads generated from calls.
    * Link call volume with sales performance metrics to identify correlations and opportunities for improvement.
    
    
    """,
    "change_impact_analysis": """


    * Increasing call volume may lead to higher lead generation and sales, but it could also impact the workload and stress levels of the inside sales team.
    * Decreasing call volume may result in missed opportunities and reduced revenue, impacting overall sales performance.
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Deal", "Lead", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.670304"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
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
                        408,
                        441,
                        428,
                        446,
                        440,
                        438,
                        419,
                        431,
                        433,
                        433,
                        435,
                        436
                ],
                "unit": "count"
        },
        "current": {
                "value": 436,
                "unit": "count",
                "change": 1,
                "change_percent": 0.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 432.33,
                "min": 408,
                "max": 446,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 109.9,
                        "percentage": 25.2
                },
                {
                        "category": "Category B",
                        "value": 68.8,
                        "percentage": 15.8
                },
                {
                        "category": "Category C",
                        "value": 55.5,
                        "percentage": 12.7
                },
                {
                        "category": "Category D",
                        "value": 58.66,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 143.14,
                        "percentage": 32.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.065896",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Call Volume"
        }
    },
}
