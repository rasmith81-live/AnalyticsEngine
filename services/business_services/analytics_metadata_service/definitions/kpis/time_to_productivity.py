"""
Time to Productivity

The time it takes for a new sales representative to reach full productivity.
"""

TIME_TO_PRODUCTIVITY = {
    "code": "TIME_TO_PRODUCTIVITY",
    "name": "Time to Productivity",
    "description": "The time it takes for a new sales representative to reach full productivity.",
    "formula": "(Time from Hiring Date to Reaching Performance Benchmark)",
    "calculation_formula": "(Time from Hiring Date to Reaching Performance Benchmark)",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Productivity to be added.",
    "trend_analysis": """



    * Time to productivity may show an initial dip as new sales reps undergo training and onboarding.
    * Over time, the trend should show a steady increase as reps gain experience and build their client base.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific onboarding processes or training programs that have proven to accelerate time to productivity?
    * How does the time to productivity for new reps compare to industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Implement mentorship or shadowing programs to help new reps learn from experienced colleagues.
    * Provide ongoing training and support to ensure reps have the knowledge and tools they need to succeed.
    * Set clear and achievable goals for new reps to track their progress and motivate them to reach full productivity.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average time to productivity for new reps over time.
    * Comparative bar charts displaying the time to productivity for different cohorts of new reps.
    
    
    
    """,
    "risk_warnings": """



    * Extended time to productivity can lead to missed sales opportunities and lower revenue.
    * Rapid time to productivity without proper training can result in lower quality interactions and potential customer dissatisfaction.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track new rep activities and progress.
    * Sales training platforms to provide interactive and ongoing learning opportunities for new reps.
    
    
    
    """,
    "integration_points": """



    * Integrate time to productivity data with sales performance metrics to identify correlations and areas for improvement.
    * Link with HR systems to align onboarding and training processes with the specific needs of the sales team.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving time to productivity can lead to increased sales and revenue, but may also require additional investment in training and support.
    * Conversely, a prolonged time to productivity can strain resources and impact overall team morale and performance.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Benchmark", "Deal", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.719939"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_OPERATIONS"],
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
                        11.7,
                        13.6,
                        14.6,
                        11.5,
                        7.4,
                        13.5,
                        8.9,
                        13.5,
                        9.7,
                        8.4,
                        14.6,
                        10.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 10.1,
                "unit": "days",
                "change": -4.5,
                "change_percent": -30.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 11.46,
                "min": 7.4,
                "max": 14.6,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 1.98,
                        "percentage": 19.6
                },
                {
                        "category": "Product Line B",
                        "value": 2.15,
                        "percentage": 21.3
                },
                {
                        "category": "Product Line C",
                        "value": 2.06,
                        "percentage": 20.4
                },
                {
                        "category": "Services",
                        "value": 0.59,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 3.32,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.783132",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time to Productivity"
        }
    },
}
