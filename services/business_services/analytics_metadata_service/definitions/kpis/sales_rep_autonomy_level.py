"""
Sales Rep Autonomy Level

The level of independence and decision-making granted to sales reps as a result of effective training.
"""

SALES_REP_AUTONOMY_LEVEL = {
    "code": "SALES_REP_AUTONOMY_LEVEL",
    "name": "Sales Rep Autonomy Level",
    "description": "The level of independence and decision-making granted to sales reps as a result of effective training.",
    "formula": "Qualitative Assessment or Autonomy Level Rating",
    "calculation_formula": "Qualitative Assessment or Autonomy Level Rating",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Rep Autonomy Level to be added.",
    "trend_analysis": """



    * Increasing sales rep autonomy may indicate improved training effectiveness and confidence in decision-making.
    * Decreasing autonomy could signal a lack of trust in sales reps or ineffective training methods.
    
    
    
    """,
    "diagnostic_questions": """



    * Are sales reps consistently making decisions without needing approval or guidance?
    * How does the level of autonomy impact sales performance and customer satisfaction?
    
    
    
    """,
    "actionable_tips": """



    * Provide ongoing coaching and support to ensure sales reps are equipped to make independent decisions.
    * Establish clear guidelines and boundaries for decision-making to balance autonomy with organizational goals.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales rep autonomy over time.
    * Stacked bar charts comparing autonomy levels across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * Too much autonomy without proper training can lead to poor decision-making and negative customer experiences.
    * Too little autonomy can result in disengaged sales reps and missed opportunities for innovation.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with activity tracking and performance metrics to monitor the impact of autonomy on sales outcomes.
    * Training and development platforms to assess the effectiveness of training programs in building autonomy.
    
    
    
    """,
    "integration_points": """



    * Integrate sales rep autonomy data with performance evaluations to understand the correlation between autonomy and results.
    * Link autonomy levels with customer feedback and satisfaction scores to gauge the impact on customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing autonomy can lead to faster decision-making and more agile responses to customer needs.
    * Decreasing autonomy may result in a more controlled sales process but could stifle creativity and innovation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"], "last_validated": "2025-11-10T13:49:33.478659"},
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
                        664.33,
                        671.36,
                        679.49,
                        754.34,
                        696.79,
                        677.23,
                        711.37,
                        680.35,
                        671.08,
                        711.28,
                        628.97,
                        704.58
                ],
                "unit": "units"
        },
        "current": {
                "value": 704.58,
                "unit": "units",
                "change": 75.61,
                "change_percent": 12.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 687.6,
                "min": 628.97,
                "max": 754.34,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 229.0,
                        "percentage": 32.5
                },
                {
                        "category": "Channel Sales",
                        "value": 130.57,
                        "percentage": 18.5
                },
                {
                        "category": "Online Sales",
                        "value": 94.15,
                        "percentage": 13.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 68.96,
                        "percentage": 9.8
                },
                {
                        "category": "Other",
                        "value": 181.9,
                        "percentage": 25.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.146893",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Rep Autonomy Level"
        }
    },
}
