"""
Win-Loss Analysis Completion Rate

The percentage of closed deals that are followed by a win-loss analysis to understand the reasons behind the outcome.
"""

WIN_LOSS_ANALYSIS_COMPLETION_RATE = {
    "code": "WIN_LOSS_ANALYSIS_COMPLETION_RATE",
    "name": "Win-Loss Analysis Completion Rate",
    "description": "The percentage of closed deals that are followed by a win-loss analysis to understand the reasons behind the outcome.",
    "formula": "(Number of Completed Win-Loss Analyses / Total Number of Sales Opportunities) * 100",
    "calculation_formula": "(Number of Completed Win-Loss Analyses / Total Number of Sales Opportunities) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Win-Loss Analysis Completion Rate to be added.",
    "trend_analysis": """



    * An increasing win-loss analysis completion rate may indicate a proactive approach to understanding customer needs and market dynamics.
    * A decreasing rate could signal complacency or a lack of emphasis on learning from lost deals.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales teams or individuals with consistently high or low win-loss analysis completion rates?
    * What are the common reasons for not conducting a win-loss analysis after a deal is closed?
    
    
    
    """,
    "actionable_tips": """



    * Implement a standardized process for conducting win-loss analysis after every closed deal.
    * Provide training and resources to sales teams on how to effectively conduct and utilize win-loss analysis.
    * Create incentives for completing win-loss analysis, such as recognition or rewards for valuable insights gained.
    
    
    
    """,
    "visualization_suggestions": """



    * Stacked bar charts comparing win-loss analysis completion rates by sales team or individual.
    * Trend line graphs showing the change in completion rates over time.
    
    
    
    """,
    "risk_warnings": """



    * A low win-loss analysis completion rate may result in missed opportunities for learning and improvement.
    * Not conducting win-loss analysis can lead to a lack of understanding of customer needs and competitive positioning.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) systems with built-in win-loss analysis tracking capabilities.
    * Sales enablement platforms that facilitate and automate the win-loss analysis process.
    
    
    
    """,
    "integration_points": """



    * Integrate win-loss analysis completion data with sales performance metrics to identify correlations between analysis completion and sales success.
    * Link win-loss analysis insights with product development and marketing strategies to align offerings with customer needs and market demands.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the win-loss analysis completion rate can lead to a better understanding of customer preferences and needs, potentially increasing sales effectiveness.
    * However, an increased focus on win-loss analysis may require additional time and resources from sales teams, impacting their overall productivity.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Competitive Analysis", "Deal", "Enablement Feedback", "Enablement Platform", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.812219"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        73.48,
                        64.09,
                        64.18,
                        77.25,
                        73.77,
                        70.67,
                        78.24,
                        61.88,
                        72.79,
                        75.98,
                        63.84,
                        62.25
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.25,
                "unit": "%",
                "change": -1.59,
                "change_percent": -2.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.87,
                "min": 61.88,
                "max": 78.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 16.28,
                        "percentage": 26.2
                },
                {
                        "category": "Channel Sales",
                        "value": 12.98,
                        "percentage": 20.9
                },
                {
                        "category": "Online Sales",
                        "value": 7.24,
                        "percentage": 11.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.98,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 21.77,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.996689",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Win-Loss Analysis Completion Rate"
        }
    },
}
