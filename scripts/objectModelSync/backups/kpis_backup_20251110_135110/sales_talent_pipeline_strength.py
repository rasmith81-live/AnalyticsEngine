"""
Sales Talent Pipeline Strength

The robustness of the internal pipeline for promoting trained and high-performing sales reps to advanced roles.
"""

SALES_TALENT_PIPELINE_STRENGTH = {
    "code": "SALES_TALENT_PIPELINE_STRENGTH",
    "name": "Sales Talent Pipeline Strength",
    "description": "The robustness of the internal pipeline for promoting trained and high-performing sales reps to advanced roles.",
    "formula": "Qualitative Assessment or Readiness Rating",
    "calculation_formula": "Qualitative Assessment or Readiness Rating",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Talent Pipeline Strength to be added.",
    "trend_analysis": """


    * An increasing pipeline strength may indicate successful sales training and development programs.
    * A decreasing pipeline strength could signal issues in retaining and promoting high-performing sales reps.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific stages in the pipeline where attrition rates are higher?
    * How does the pipeline strength compare with industry benchmarks or historical data?
    
    
    """,
    "actionable_tips": """


    * Implement mentorship programs to support the development of sales reps at different pipeline stages.
    * Regularly review and update promotion criteria to ensure alignment with evolving business needs.
    * Provide ongoing training and upskilling opportunities to enhance the readiness of sales reps for advanced roles.
    
    
    """,
    "visualization_suggestions": """


    * Stacked bar charts showing the distribution of sales reps across different pipeline stages.
    * Trend lines to visualize the changes in pipeline strength over time.
    
    
    """,
    "risk_warnings": """


    * Low pipeline strength may lead to talent shortages in advanced sales roles, impacting overall sales performance.
    * High pipeline strength without corresponding promotion opportunities can lead to disengagement and attrition among sales reps.
    
    
    """,
    "tracking_tools": """


    * CRM systems with pipeline tracking capabilities to monitor the progression of sales reps.
    * Performance management software to assess the readiness and potential of sales reps for advancement.
    
    
    """,
    "integration_points": """


    * Integrate pipeline strength data with HR systems to align training and development initiatives with promotion opportunities.
    * Link pipeline strength with sales performance metrics to identify correlations between pipeline health and sales outcomes.
    
    
    """,
    "change_impact_analysis": """


    * Improving pipeline strength can lead to a more robust and sustainable sales organization, but may require additional investment in training and development.
    * A declining pipeline strength can impact the overall talent pool available for critical sales roles, affecting revenue generation and customer relationships.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.502107"},
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
                        939.53,
                        820.67,
                        838.06,
                        871.21,
                        958.6,
                        821.35,
                        952.08,
                        925.96,
                        848.69,
                        948.19,
                        830.28,
                        936.64
                ],
                "unit": "units"
        },
        "current": {
                "value": 936.64,
                "unit": "units",
                "change": 106.36,
                "change_percent": 12.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 890.94,
                "min": 820.67,
                "max": 958.6,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 175.82,
                        "percentage": 18.8
                },
                {
                        "category": "Category B",
                        "value": 262.96,
                        "percentage": 28.1
                },
                {
                        "category": "Category C",
                        "value": 116.13,
                        "percentage": 12.4
                },
                {
                        "category": "Category D",
                        "value": 91.28,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 290.45,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.618483",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Talent Pipeline Strength"
        }
    },
}
