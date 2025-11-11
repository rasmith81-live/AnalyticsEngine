"""
Rep Attrition Rate

The rate at which sales representatives leave the company.
"""

REP_ATTRITION_RATE = {
    "code": "REP_ATTRITION_RATE",
    "name": "Rep Attrition Rate",
    "description": "The rate at which sales representatives leave the company.",
    "formula": "(Number of Sales Reps Who Left / Average Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Who Left / Average Number of Sales Reps) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Rep Attrition Rate to be added.",
    "trend_analysis": """


    * A rising rep attrition rate may indicate dissatisfaction with compensation, work environment, or management.
    * A decreasing rate could signal improved employee engagement, better training, or more effective leadership.
    
    
    """,
    "diagnostic_questions": """


    * Are there common reasons cited by departing sales representatives?
    * How does our rep attrition rate compare with industry benchmarks or turnover rates in similar roles?
    
    
    """,
    "actionable_tips": """


    * Conduct exit interviews to understand the reasons for leaving and address any recurring issues.
    * Invest in ongoing training and development programs to enhance job satisfaction and career growth opportunities for sales representatives.
    * Regularly review and adjust compensation and benefits packages to remain competitive in the market.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend in rep attrition rate over time.
    * Pie charts to compare reasons for leaving among sales representatives.
    
    
    """,
    "risk_warnings": """


    * High rep attrition rates can lead to loss of sales productivity and revenue.
    * Frequent turnover may indicate underlying issues with company culture, management, or job satisfaction.
    
    
    """,
    "tracking_tools": """


    * Employee engagement and feedback platforms like Culture Amp or Officevibe to gather insights and feedback from the sales team.
    * Human resource management systems to track turnover rates and identify patterns or trends.
    
    
    """,
    "integration_points": """


    * Integrate rep attrition rate data with performance reviews and feedback systems to identify potential issues early on.
    * Link with recruitment and onboarding processes to streamline the hiring and training of new sales representatives.
    
    
    """,
    "change_impact_analysis": """


    * Reducing rep attrition can lead to a more stable and productive sales team, positively impacting overall sales performance and customer relationships.
    * However, addressing high attrition rates may require investment in training, benefits, and employee support programs, impacting operational costs.
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.334481"},
    "required_objects": [],
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
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
                        70.2,
                        81.03,
                        73.5,
                        65.25,
                        81.16,
                        75.22,
                        65.25,
                        82.28,
                        76.86,
                        64.84,
                        68.02,
                        81.41
                ],
                "unit": "%"
        },
        "current": {
                "value": 81.41,
                "unit": "%",
                "change": 13.39,
                "change_percent": 19.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.75,
                "min": 64.84,
                "max": 82.28,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.09,
                        "percentage": 18.5
                },
                {
                        "category": "Category B",
                        "value": 20.05,
                        "percentage": 24.6
                },
                {
                        "category": "Category C",
                        "value": 8.93,
                        "percentage": 11.0
                },
                {
                        "category": "Category D",
                        "value": 10.53,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 26.81,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.071883",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Rep Attrition Rate"
        }
    },
}
