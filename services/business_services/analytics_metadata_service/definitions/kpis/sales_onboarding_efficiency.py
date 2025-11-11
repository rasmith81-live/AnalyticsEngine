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
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Onboarding", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.442484"},
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
                        231.7,
                        293.9,
                        261.44,
                        281.29,
                        273.14,
                        298.97,
                        307.75,
                        285.3,
                        364.76,
                        367.14,
                        240.21,
                        316.14
                ],
                "unit": "units"
        },
        "current": {
                "value": 316.14,
                "unit": "units",
                "change": 75.93,
                "change_percent": 31.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 293.48,
                "min": 231.7,
                "max": 367.14,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 81.8,
                        "percentage": 25.9
                },
                {
                        "category": "Product Line B",
                        "value": 68.13,
                        "percentage": 21.6
                },
                {
                        "category": "Product Line C",
                        "value": 38.6,
                        "percentage": 12.2
                },
                {
                        "category": "Services",
                        "value": 13.95,
                        "percentage": 4.4
                },
                {
                        "category": "Other",
                        "value": 113.66,
                        "percentage": 36.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.041176",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Onboarding Efficiency"
        }
    },
}
