"""
Sales Skill Assessment Completion Rate

The percentage of sales team members who complete periodic skill assessments.
"""

SALES_SKILL_ASSESSMENT_COMPLETION_RATE = {
    "code": "SALES_SKILL_ASSESSMENT_COMPLETION_RATE",
    "name": "Sales Skill Assessment Completion Rate",
    "description": "The percentage of sales team members who complete periodic skill assessments.",
    "formula": "(Number of Completed Assessments / Total Number of Required Assessments) * 100",
    "calculation_formula": "(Number of Completed Assessments / Total Number of Required Assessments) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Skill Assessment Completion Rate to be added.",
    "trend_analysis": """


    * Increasing completion rates may indicate a focus on continuous learning and development within the sales team.
    * Decreasing completion rates could signal disengagement, lack of motivation, or a need for more engaging assessment methods.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific skills or topics where completion rates are consistently lower?
    * How do completion rates compare across different sales team segments (e.g., new hires vs. tenured employees)?
    
    
    """,
    "actionable_tips": """


    * Offer incentives or recognition for completing assessments to boost motivation.
    * Provide additional resources or training to address areas where completion rates are low.
    * Regularly communicate the importance of skill assessments and how they contribute to individual and team success.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing completion rates over time to identify trends and seasonality.
    * Pie charts to compare completion rates across different assessment topics or categories.
    
    
    """,
    "risk_warnings": """


    * Low completion rates may lead to gaps in knowledge and skills within the sales team, impacting overall performance.
    * Consistently high completion rates without corresponding performance improvements may indicate ineffective or irrelevant assessments.
    
    
    """,
    "tracking_tools": """


    * Learning management systems (LMS) with built-in assessment modules for easy tracking and analysis.
    * Survey and assessment tools that provide real-time feedback and insights into completion rates and engagement.
    
    
    """,
    "integration_points": """


    * Integrate skill assessment data with performance reviews to identify correlations between completion rates and sales results.
    * Link assessment completion with individual development plans and training programs to create a seamless learning experience.
    
    
    """,
    "change_impact_analysis": """


    * Improving completion rates can lead to a more knowledgeable and skilled sales team, potentially impacting sales performance and customer satisfaction.
    * However, an overemphasis on completion rates alone may lead to "checkbox" mentality and superficial learning, affecting the quality of skill development.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.500407"},
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
                        82.35,
                        81.09,
                        84.19,
                        85.1,
                        72.8,
                        81.53,
                        85.68,
                        83.49,
                        82.51,
                        77.31,
                        77.13,
                        72.46
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.46,
                "unit": "%",
                "change": -4.67,
                "change_percent": -6.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 80.47,
                "min": 72.46,
                "max": 85.68,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.85,
                        "percentage": 24.6
                },
                {
                        "category": "Category B",
                        "value": 11.3,
                        "percentage": 15.6
                },
                {
                        "category": "Category C",
                        "value": 6.53,
                        "percentage": 9.0
                },
                {
                        "category": "Category D",
                        "value": 7.57,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 29.21,
                        "percentage": 40.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.614771",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Skill Assessment Completion Rate"
        }
    },
}
