"""
Outbound Call Conversion Rate

The percentage of outbound calls that result in a desired action, such as a meeting or sale.
"""

OUTBOUND_CALL_CONVERSION_RATE = {
    "code": "OUTBOUND_CALL_CONVERSION_RATE",
    "name": "Outbound Call Conversion Rate",
    "description": "The percentage of outbound calls that result in a desired action, such as a meeting or sale.",
    "formula": "(Number of Successful Sales / Number of Outbound Calls) * 100",
    "calculation_formula": "(Number of Successful Sales / Number of Outbound Calls) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Outbound Call Conversion Rate to be added.",
    "trend_analysis": """



    * An increasing outbound call conversion rate may indicate improved sales pitch effectiveness or better lead quality.
    * A decreasing rate could signal issues with the sales process, such as ineffective follow-up or poor targeting of prospects.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific market segments or customer profiles that have a higher conversion rate?
    * How does our outbound call conversion rate compare with industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training to improve communication and persuasion skills.
    * Refine lead qualification criteria to ensure better targeting of potential customers.
    * Implement a structured follow-up process to increase the likelihood of conversion.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of outbound call conversion rates over time.
    * Pie charts to compare conversion rates across different sales teams or territories.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low conversion rate can lead to wasted resources and decreased morale among sales teams.
    * A high conversion rate without corresponding sales growth may indicate a need for better lead quality assessment.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze call outcomes.
    * Sales enablement tools to provide sales teams with the necessary resources and content for effective calls.
    
    
    
    """,
    "integration_points": """



    * Integrate outbound call conversion data with lead generation systems to identify the most promising leads.
    * Link conversion rate analysis with customer relationship management systems to track the entire sales process from call to close.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the outbound call conversion rate can lead to increased sales revenue and customer acquisition.
    * However, a focus solely on increasing conversion rates may lead to overlooking the quality of customer interactions and long-term customer satisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Lead", "Lost Sale", "Meeting", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["COLD_CALL_CONVERSION_RATE"], "last_validated": "2025-11-10T13:49:33.134120"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT"],
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
                        59.26,
                        74.31,
                        62.33,
                        72.14,
                        65.88,
                        61.03,
                        64.75,
                        66.91,
                        62.19,
                        63.3,
                        69.85,
                        56.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.71,
                "unit": "%",
                "change": -13.14,
                "change_percent": -18.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 64.89,
                "min": 56.71,
                "max": 74.31,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 14.97,
                        "percentage": 26.4
                },
                {
                        "category": "Channel Sales",
                        "value": 11.08,
                        "percentage": 19.5
                },
                {
                        "category": "Online Sales",
                        "value": 5.5,
                        "percentage": 9.7
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.47,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 19.69,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.346180",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Outbound Call Conversion Rate"
        }
    },
}
