"""
Average Time to Onboard New Sales Reps

The average time it takes to get new sales reps up to speed and productive. A shorter time indicates better training and coaching.
"""

AVERAGE_TIME_TO_ONBOARD_NEW_SALES_REPS = {
    "code": "AVERAGE_TIME_TO_ONBOARD_NEW_SALES_REPS",
    "name": "Average Time to Onboard New Sales Reps",
    "description": "The average time it takes to get new sales reps up to speed and productive. A shorter time indicates better training and coaching.",
    "formula": "Sum of Onboarding Duration for all New Sales Reps / Number of New Sales Reps",
    "calculation_formula": "Sum of Onboarding Duration for all New Sales Reps / Number of New Sales Reps",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Time to Onboard New Sales Reps to be added.",
    "trend_analysis": """



    * Decreasing average time to onboard new sales reps may indicate more effective training and coaching programs.
    * An increasing time to productivity could signal issues with training content, onboarding processes, or coaching effectiveness.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas or topics where new sales reps consistently struggle during onboarding?
    * How does the average onboarding time compare with industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Implement mentorship programs to provide new reps with ongoing support and guidance.
    * Utilize interactive and scenario-based training methods to improve retention and application of knowledge.
    * Regularly review and update training materials to ensure relevance and effectiveness.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average onboarding time over different quarters or years.
    * Comparison bar graphs displaying the onboarding time for different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * Extended onboarding times can lead to decreased sales productivity and missed revenue targets.
    * Prolonged onboarding may indicate a need for reevaluation of training and coaching strategies to prevent turnover or dissatisfaction among new reps.
    
    
    
    """,
    "tracking_tools": """



    * Utilize learning management systems (LMS) to track and analyze the progress of new reps during onboarding.
    * Implement sales enablement platforms to provide access to training materials, resources, and best practices for new reps.
    
    
    
    """,
    "integration_points": """



    * Integrate onboarding time data with performance management systems to assess the impact of training on sales results.
    * Link onboarding metrics with HR systems to identify correlations between onboarding success and employee retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the average onboarding time can lead to increased sales efficiency and effectiveness.
    * However, rapid onboarding may also lead to gaps in knowledge and skill development, impacting long-term sales performance.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer Onboarding", "Deal", "Lead", "Opportunity", "Partner Training", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.661777"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        333,
                        373,
                        369,
                        350,
                        361,
                        380,
                        356,
                        372,
                        351,
                        381,
                        353,
                        371
                ],
                "unit": "count"
        },
        "current": {
                "value": 371,
                "unit": "count",
                "change": 18,
                "change_percent": 5.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 362.5,
                "min": 333,
                "max": 381,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 65.17,
                        "percentage": 17.6
                },
                {
                        "category": "Channel Sales",
                        "value": 97.37,
                        "percentage": 26.2
                },
                {
                        "category": "Online Sales",
                        "value": 49.03,
                        "percentage": 13.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 34.88,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 124.55,
                        "percentage": 33.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.398509",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Time to Onboard New Sales Reps"
        }
    },
}
