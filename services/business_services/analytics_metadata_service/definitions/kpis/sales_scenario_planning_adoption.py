"""
Sales Scenario Planning Adoption

The adoption rate of scenario planning exercises by the sales team to prepare for different sales situations.
"""

SALES_SCENARIO_PLANNING_ADOPTION = {
    "code": "SALES_SCENARIO_PLANNING_ADOPTION",
    "name": "Sales Scenario Planning Adoption",
    "description": "The adoption rate of scenario planning exercises by the sales team to prepare for different sales situations.",
    "formula": "(Number of Sales Reps Using Scenario Planning / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Using Scenario Planning / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Scenario Planning Adoption to be added.",
    "trend_analysis": """



    * An increasing adoption rate of scenario planning may indicate a proactive and forward-thinking sales team.
    * A decreasing adoption rate could signal a lack of preparation for different sales situations and potential missed opportunities.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales scenarios where the team consistently struggles or feels unprepared?
    * How does the adoption rate of scenario planning compare with the overall sales performance?
    
    
    
    """,
    "actionable_tips": """



    * Provide training and resources to help the sales team understand the importance and benefits of scenario planning.
    * Encourage collaboration and knowledge sharing among the sales team to develop effective strategies for different sales situations.
    * Incorporate scenario planning into regular sales meetings and performance evaluations to reinforce its importance.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the adoption rate of scenario planning over time.
    * Comparison charts displaying the adoption rate across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * Low adoption of scenario planning may lead to missed sales opportunities and ineffective responses to customer needs.
    * Resistance to scenario planning could indicate a cultural or organizational barrier that hinders sales effectiveness.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with built-in scenario planning modules to integrate planning with sales activities.
    * Sales enablement platforms that offer scenario planning templates and best practices for the sales team.
    
    
    
    """,
    "integration_points": """



    * Integrate scenario planning adoption with sales performance metrics to understand its impact on overall sales effectiveness.
    * Link scenario planning with customer relationship management systems to align strategies with customer needs and preferences.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving scenario planning adoption can lead to better sales performance and customer satisfaction, but may require initial investment in training and resources.
    * Low adoption of scenario planning can result in reactive sales strategies, potentially impacting customer relationships and revenue generation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.496212"},
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
                        71.45,
                        77.29,
                        71.58,
                        65.12,
                        77.0,
                        60.93,
                        77.62,
                        70.1,
                        64.26,
                        66.72,
                        74.41,
                        78.0
                ],
                "unit": "%"
        },
        "current": {
                "value": 78.0,
                "unit": "%",
                "change": 3.59,
                "change_percent": 4.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.21,
                "min": 60.93,
                "max": 78.0,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 19.61,
                        "percentage": 25.1
                },
                {
                        "category": "Channel Sales",
                        "value": 9.96,
                        "percentage": 12.8
                },
                {
                        "category": "Online Sales",
                        "value": 11.89,
                        "percentage": 15.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.76,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 28.78,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.194354",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Scenario Planning Adoption"
        }
    },
}
