"""
Opportunity Win Rate

The percentage of sales opportunities that are converted into actual sales.
"""

OPPORTUNITY_WIN_RATE = {
    "code": "OPPORTUNITY_WIN_RATE",
    "name": "Opportunity Win Rate",
    "description": "The percentage of sales opportunities that are converted into actual sales.",
    "formula": "(Total Number of Won Opportunities / Total Number of Opportunities) * 100",
    "calculation_formula": "(Total Number of Won Opportunities / Total Number of Opportunities) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Opportunity Win Rate to be added.",
    "trend_analysis": """



    * An increasing opportunity win rate may indicate improved sales strategies or a growing market demand.
    * A decreasing rate could signal ineffective sales processes or increased competition.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors contribute to the successful conversion of sales opportunities?
    * Are there specific stages in the sales pipeline where opportunities are frequently lost?
    
    
    
    """,
    "actionable_tips": """



    * Provide ongoing sales training and coaching to improve sales team performance.
    * Implement a lead scoring system to prioritize high-quality opportunities.
    * Regularly review and refine the sales process to identify and address bottlenecks.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of opportunity win rates over time.
    * Pie charts comparing win rates across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low opportunity win rate may indicate a need for significant changes in sales strategy or personnel.
    * High win rates without corresponding revenue growth could signal overcommitment or discounting.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and analyze sales opportunities and outcomes.
    * Sales enablement platforms to provide sales teams with the necessary tools and resources to improve win rates.
    
    
    
    """,
    "integration_points": """



    * Integrate opportunity win rate data with marketing analytics to understand the quality of leads generated.
    * Link win rates with customer feedback systems to identify areas for improvement in the sales process.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in opportunity win rate can lead to higher revenue and improved sales team morale.
    * However, a focus solely on win rate may neglect the importance of customer satisfaction and long-term relationships.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Expansion Opportunity", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["OPPORTUNITY_TO_SALE_RATIO"], "last_validated": "2025-11-10T13:49:33.110911"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"],
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
                        47.78,
                        61.36,
                        53.18,
                        51.28,
                        53.65,
                        59.07,
                        54.35,
                        56.09,
                        59.18,
                        60.66,
                        65.72,
                        62.9
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.9,
                "unit": "%",
                "change": -2.82,
                "change_percent": -4.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 57.1,
                "min": 47.78,
                "max": 65.72,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.24,
                        "percentage": 33.8
                },
                {
                        "category": "Segment B",
                        "value": 10.92,
                        "percentage": 17.4
                },
                {
                        "category": "Segment C",
                        "value": 9.01,
                        "percentage": 14.3
                },
                {
                        "category": "Segment D",
                        "value": 4.03,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 17.7,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.299480",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Opportunity Win Rate"
        }
    },
}
