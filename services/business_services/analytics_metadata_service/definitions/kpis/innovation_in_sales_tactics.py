"""
Innovation in Sales Tactics

The rate at which new and innovative sales tactics are adopted by sales reps post-training.
"""

INNOVATION_IN_SALES_TACTICS = {
    "code": "INNOVATION_IN_SALES_TACTICS",
    "name": "Innovation in Sales Tactics",
    "description": "The rate at which new and innovative sales tactics are adopted by sales reps post-training.",
    "formula": "Qualitative Assessment or Number of Innovative Tactics Adopted Post-Training",
    "calculation_formula": "Qualitative Assessment or Number of Innovative Tactics Adopted Post-Training",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Innovation in Sales Tactics to be added.",
    "trend_analysis": """



    * Increasing adoption of new sales tactics may indicate a positive response to training and coaching.
    * Decreasing adoption rates could signal a need for reevaluation of the training content or delivery methods.
    
    
    
    """,
    "diagnostic_questions": """



    * Are sales reps provided with the necessary resources and support to implement new tactics effectively?
    * How are the innovative tactics being communicated and reinforced within the sales team?
    
    
    
    """,
    "actionable_tips": """



    * Encourage open communication and feedback channels to understand the practical challenges faced by sales reps in adopting new tactics.
    * Provide ongoing reinforcement and coaching to ensure new tactics are integrated into daily sales activities.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the adoption rates of new tactics over time.
    * Comparison bar charts to visualize the effectiveness of different tactics in driving sales performance.
    
    
    
    """,
    "risk_warnings": """



    * Low adoption rates may lead to missed sales opportunities and stagnant performance.
    * Rapid adoption without proper evaluation could lead to ineffective or counterproductive tactics being implemented.
    
    
    
    """,
    "tracking_tools": """



    * Sales performance management software to track and analyze the impact of new tactics on overall sales metrics.
    * Collaboration and communication tools to facilitate knowledge sharing and best practice dissemination among the sales team.
    
    
    
    """,
    "integration_points": """



    * Integrate new tactic adoption data with individual sales performance metrics to identify correlations and best practices.
    * Link with customer relationship management (CRM) systems to understand the impact of new tactics on customer interactions and conversions.
    
    
    
    """,
    "change_impact_analysis": """



    * Successful adoption of innovative tactics can lead to increased sales efficiency and effectiveness.
    * However, poorly executed tactics may result in decreased customer satisfaction and trust.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.974878"},
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
                        335,
                        350,
                        357,
                        370,
                        335,
                        350,
                        330,
                        344,
                        363,
                        339,
                        346,
                        371
                ],
                "unit": "count"
        },
        "current": {
                "value": 371,
                "unit": "count",
                "change": 25,
                "change_percent": 7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 349.17,
                "min": 330,
                "max": 371,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 113.98,
                        "percentage": 30.7
                },
                {
                        "category": "Channel Sales",
                        "value": 61.95,
                        "percentage": 16.7
                },
                {
                        "category": "Online Sales",
                        "value": 56.04,
                        "percentage": 15.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 41.11,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 97.92,
                        "percentage": 26.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.039383",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Innovation in Sales Tactics"
        }
    },
}
