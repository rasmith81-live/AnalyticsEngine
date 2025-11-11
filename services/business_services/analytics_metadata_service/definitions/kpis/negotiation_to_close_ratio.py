"""
Negotiation-to-Close Ratio

The ratio comparing the number of negotiations to the successfully closed deals.
"""

NEGOTIATION_TO_CLOSE_RATIO = {
    "code": "NEGOTIATION_TO_CLOSE_RATIO",
    "name": "Negotiation-to-Close Ratio",
    "description": "The ratio comparing the number of negotiations to the successfully closed deals.",
    "formula": "Number of Deals Closed / Number of Negotiations Conducted * 100",
    "calculation_formula": "Number of Deals Closed / Number of Negotiations Conducted * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Negotiation-to-Close Ratio to be added.",
    "trend_analysis": """



    * An increasing negotiation-to-close ratio may indicate improved sales tactics or a stronger market position.
    * A decreasing ratio could signal challenges in closing deals or increased competition.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that consistently have a higher negotiation-to-close ratio?
    * How does our negotiation-to-close ratio compare with industry benchmarks or with our competitors?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional negotiation training and resources for sales representatives.
    * Regularly review and adjust pricing strategies to ensure competitiveness.
    * Implement customer relationship management (CRM) systems to track and manage negotiations more effectively.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of negotiation-to-close ratio over time.
    * Scatter plots to identify any correlation between negotiation-to-close ratio and sales volume.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low negotiation-to-close ratio may lead to missed revenue opportunities.
    * A high ratio could indicate a lack of negotiation skills or ineffective sales strategies.
    
    
    
    """,
    "tracking_tools": """



    * CRM software with negotiation tracking capabilities, such as Salesforce or HubSpot.
    * Sales performance analytics tools to identify patterns and opportunities for improvement, like Tableau or Power BI.
    
    
    
    """,
    "integration_points": """



    * Integrate negotiation-to-close ratio data with sales forecasting systems to better predict future performance.
    * Link with customer relationship management platforms to understand the impact of negotiations on customer satisfaction and retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the negotiation-to-close ratio can lead to increased revenue and customer satisfaction.
    * However, overly aggressive negotiation tactics may negatively impact customer relationships and long-term loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.067044"},
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
                        63.86,
                        54.21,
                        62.82,
                        64.38,
                        63.04,
                        61.17,
                        66.29,
                        64.91,
                        69.6,
                        55.42,
                        64.38,
                        69.32
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.32,
                "unit": "%",
                "change": 4.94,
                "change_percent": 7.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.28,
                "min": 54.21,
                "max": 69.6,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.51,
                        "percentage": 18.0
                },
                {
                        "category": "Segment B",
                        "value": 18.11,
                        "percentage": 26.1
                },
                {
                        "category": "Segment C",
                        "value": 10.64,
                        "percentage": 15.3
                },
                {
                        "category": "Segment D",
                        "value": 7.71,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 20.35,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.225824",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Negotiation-to-Close Ratio"
        }
    },
}
