"""
Sales Onboarding Efficiency

The efficiency of the sales onboarding process, measured by the time it takes for new hires to reach full productivity.
"""

SALES_ONBOARDING_EFFICIENCY = {
    "code": "SALES_ONBOARDING_EFFICIENCY",
    "name": "Sales Onboarding Efficiency",
    "description": "The efficiency of the sales onboarding process, measured by the time it takes for new hires to reach full productivity.",
    "formula": "Time to Reach Full Productivity / Average Onboarding Duration",
    "calculation_formula": "Time to Reach Full Productivity / Average Onboarding Duration",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Onboarding Efficiency to be added.",
    "trend_analysis": """

    * Shortening onboarding times may indicate more effective training and support for new sales hires.
    * An increasing onboarding time could signal issues with training programs, sales processes, or the quality of new hires.
    
    """,
    "diagnostic_questions": """

    * What are the key milestones or checkpoints in our onboarding process, and how are they being measured?
    * Are there specific areas or skills where new hires consistently struggle to reach full productivity?
    
    """,
    "actionable_tips": """

    * Implement mentorship programs to provide ongoing support and guidance for new hires.
    * Regularly review and update training materials and processes to ensure they are relevant and effective.
    * Utilize technology and simulations to provide realistic sales scenarios for new hires to practice and learn from.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average time to full productivity for new hires over time.
    * Comparison bar charts to visualize the onboarding efficiency of different sales teams or regions.
    
    """,
    "risk_warnings": """

    * Extended onboarding times can lead to decreased sales performance and missed opportunities.
    * Rapidly changing market conditions or product offerings may require frequent updates to the onboarding process.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and manage the progress of new hires through the onboarding process.
    * Customer relationship management (CRM) software to monitor the sales performance of new hires after onboarding.
    
    """,
    "integration_points": """

    * Integrate onboarding data with HR systems to identify correlations between onboarding success and hiring practices.
    * Connect onboarding metrics with sales performance data to assess the long-term impact of the onboarding process.
    
    """,
    "change_impact_analysis": """

    * Improving onboarding efficiency can lead to faster revenue generation and increased sales team effectiveness.
    * However, rushing the onboarding process may result in lower quality sales interactions and reduced customer satisfaction.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Onboarding", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.436099"},
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
                        606.4,
                        495.72,
                        481.79,
                        581.8,
                        577.23,
                        489.68,
                        589.3,
                        559.73,
                        514.97,
                        504.01,
                        570.48,
                        548.38
                ],
                "unit": "units"
        },
        "current": {
                "value": 548.38,
                "unit": "units",
                "change": -22.1,
                "change_percent": -3.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 543.29,
                "min": 481.79,
                "max": 606.4,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 171.75,
                        "percentage": 31.3
                },
                {
                        "category": "Category B",
                        "value": 58.91,
                        "percentage": 10.7
                },
                {
                        "category": "Category C",
                        "value": 50.55,
                        "percentage": 9.2
                },
                {
                        "category": "Category D",
                        "value": 65.7,
                        "percentage": 12.0
                },
                {
                        "category": "Other",
                        "value": 201.47,
                        "percentage": 36.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.436099",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Onboarding Efficiency"
        }
    },
}
