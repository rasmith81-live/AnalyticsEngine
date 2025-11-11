"""
Lead-to-Opportunity Ratio

The ratio of leads that are converted into sales opportunities.
"""

LEAD_TO_OPPORTUNITY_RATIO = {
    "code": "LEAD_TO_OPPORTUNITY_RATIO",
    "name": "Lead-to-Opportunity Ratio",
    "description": "The ratio of leads that are converted into sales opportunities.",
    "formula": "Number of Opportunities Created / Number of Qualified Leads * 100",
    "calculation_formula": "Number of Opportunities Created / Number of Qualified Leads * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead-to-Opportunity Ratio to be added.",
    "trend_analysis": """



    * An increasing lead-to-opportunity ratio may indicate improved lead quality or more effective sales strategies.
    * A decreasing ratio could signal issues with lead nurturing or a decline in the overall demand for the product or service.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific lead sources that consistently result in higher conversion rates?
    * How does our lead-to-opportunity ratio compare with industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Implement lead scoring to prioritize high-quality leads for follow-up.
    * Provide additional sales training to improve lead conversion techniques.
    * Regularly review and optimize the lead nurturing process to ensure leads are being effectively moved through the sales funnel.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of lead-to-opportunity ratio over time.
    * Pie charts comparing lead sources and their respective conversion rates.
    
    
    
    """,
    "risk_warnings": """



    * A low lead-to-opportunity ratio may result in wasted resources on low-quality leads.
    * A high ratio could indicate missed opportunities for potential sales growth.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and analyze lead conversion data.
    * Marketing automation tools to streamline lead nurturing processes and improve conversion rates.
    
    
    
    """,
    "integration_points": """



    * Integrate lead-to-opportunity ratio tracking with marketing and sales platforms to align efforts and improve lead quality.
    * Link with customer relationship management systems to ensure a seamless transition from lead to opportunity.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the lead-to-opportunity ratio can lead to increased sales revenue and better overall sales performance.
    * However, a significant change in the ratio may require adjustments in resource allocation and sales strategies.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Expansion Opportunity", "Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.020050"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT"],
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
                        64.68,
                        61.81,
                        60.41,
                        58.57,
                        60.25,
                        58.82,
                        63.51,
                        68.96,
                        71.14,
                        58.66,
                        62.35,
                        71.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.08,
                "unit": "%",
                "change": 8.73,
                "change_percent": 14.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.35,
                "min": 58.57,
                "max": 71.14,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.83,
                        "percentage": 15.2
                },
                {
                        "category": "Segment B",
                        "value": 20.73,
                        "percentage": 29.2
                },
                {
                        "category": "Segment C",
                        "value": 10.3,
                        "percentage": 14.5
                },
                {
                        "category": "Segment D",
                        "value": 3.54,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 25.68,
                        "percentage": 36.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.140717",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Lead-to-Opportunity Ratio"
        }
    },
}
