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
                        465.56,
                        602.31,
                        495.4,
                        540.65,
                        579.73,
                        474.7,
                        481.71,
                        481.14,
                        506.37,
                        597.11,
                        595.97,
                        559.86
                ],
                "unit": "units"
        },
        "current": {
                "value": 559.86,
                "unit": "units",
                "change": -36.11,
                "change_percent": -6.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 531.71,
                "min": 465.56,
                "max": 602.31,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 109.03,
                        "percentage": 19.5
                },
                {
                        "category": "Channel Sales",
                        "value": 124.24,
                        "percentage": 22.2
                },
                {
                        "category": "Online Sales",
                        "value": 55.97,
                        "percentage": 10.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 40.15,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 230.47,
                        "percentage": 41.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.209646",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Talent Pipeline Strength"
        }
    },
}
