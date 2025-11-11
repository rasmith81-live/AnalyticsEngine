"""
Revenue per Successful Call

The average revenue generated per successful sales call.
"""

REVENUE_PER_SUCCESSFUL_CALL = {
    "code": "REVENUE_PER_SUCCESSFUL_CALL",
    "name": "Revenue per Successful Call",
    "description": "The average revenue generated per successful sales call.",
    "formula": "Total Revenue from Sales Calls / Total Number of Successful Sales Calls",
    "calculation_formula": "Total Revenue from Sales Calls / Total Number of Successful Sales Calls",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Revenue per Successful Call to be added.",
    "trend_analysis": """

    * Increasing revenue per successful call may indicate improved sales techniques or better targeting of high-value prospects.
    * Decreasing revenue per successful call could signal changes in customer preferences, market saturation, or ineffective sales strategies.
    
    """,
    "diagnostic_questions": """

    * What factors contribute to the success of sales calls that result in high revenue?
    * Are there specific customer segments or industries where revenue per successful call is consistently low, and what can be done to address this?
    
    """,
    "actionable_tips": """

    * Provide additional training and resources to sales teams to enhance their ability to close high-value deals during sales calls.
    * Implement a lead scoring system to prioritize high-potential prospects for sales calls.
    * Regularly review and update sales scripts and pitches to ensure they are effectively communicating the value proposition to potential customers.
    
    """,
    "visualization_suggestions": """

    * Line charts showing revenue per successful call over time to identify trends and seasonality.
    * Pie charts comparing revenue per successful call by sales representative to identify top performers and areas for improvement.
    
    """,
    "risk_warnings": """

    * Low revenue per successful call may lead to decreased motivation and morale among the sales team.
    * Consistently high revenue per successful call from a small number of customers may indicate overreliance on a few key accounts, posing a risk to revenue stability.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and analyze the success of sales calls and customer interactions.
    * Sales enablement platforms to provide sales teams with the necessary resources and content to effectively engage with prospects during calls.
    
    """,
    "integration_points": """

    * Integrate revenue per successful call data with customer relationship management systems to better understand the impact of successful calls on overall customer lifetime value.
    * Link revenue per successful call with sales forecasting and pipeline management to align sales efforts with revenue targets.
    
    """,
    "change_impact_analysis": """

    * Improving revenue per successful call can lead to increased profitability and overall sales performance.
    * Conversely, a decline in revenue per successful call may indicate a need for strategic adjustments in sales tactics and customer targeting.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Customer", "Key Account", "Key Account Manager", "Outbound Call", "Renewal Management", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.118994"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        180,
                        191,
                        157,
                        184,
                        179,
                        168,
                        173,
                        187,
                        167,
                        203,
                        203,
                        179
                ],
                "unit": "count"
        },
        "current": {
                "value": 179,
                "unit": "count",
                "change": -24,
                "change_percent": -11.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 180.92,
                "min": 157,
                "max": 203,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 39.38,
                        "percentage": 22.0
                },
                {
                        "category": "Category B",
                        "value": 26.09,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 23.87,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 9.93,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 79.73,
                        "percentage": 44.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.118994",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Revenue per Successful Call"
        }
    },
}
