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
                        61.5,
                        73.19,
                        62.18,
                        59.44,
                        72.02,
                        56.58,
                        66.95,
                        72.4,
                        68.16,
                        63.5,
                        66.52,
                        67.31
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.31,
                "unit": "%",
                "change": 0.79,
                "change_percent": 1.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 65.81,
                "min": 56.58,
                "max": 73.19,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 18.95,
                        "percentage": 28.2
                },
                {
                        "category": "Channel Sales",
                        "value": 9.26,
                        "percentage": 13.8
                },
                {
                        "category": "Online Sales",
                        "value": 11.04,
                        "percentage": 16.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.08,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 23.98,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.202971",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Skill Assessment Completion Rate"
        }
    },
}
