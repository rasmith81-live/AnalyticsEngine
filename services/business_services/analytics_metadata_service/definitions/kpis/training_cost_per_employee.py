"""
Training Cost Per Employee

The average cost incurred by the company for training each sales representative.
"""

TRAINING_COST_PER_EMPLOYEE = {
    "code": "TRAINING_COST_PER_EMPLOYEE",
    "name": "Training Cost Per Employee",
    "description": "The average cost incurred by the company for training each sales representative.",
    "formula": "Total Training Costs / Number of Sales Reps Trained",
    "calculation_formula": "Total Training Costs / Number of Sales Reps Trained",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Cost Per Employee to be added.",
    "trend_analysis": """



    * Training cost per employee may increase over time due to inflation, higher demand for specialized training, or the need for more advanced training materials.
    * A decreasing trend could indicate more cost-effective training methods, improved training efficiency, or a reduction in the need for external training resources.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific training programs or materials that are driving up the cost per employee?
    * How does the cost per employee compare with industry benchmarks or with the performance of top-performing sales representatives?
    
    
    
    """,
    "actionable_tips": """



    * Invest in digital training resources and e-learning platforms to reduce the cost of physical training materials and external trainers.
    * Implement mentorship programs to provide on-the-job training at a lower cost.
    * Regularly review and update training programs to ensure they remain relevant and cost-effective.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of training cost per employee over time.
    * Comparison bar charts to visualize the cost per employee for different training programs or sales teams.
    
    
    
    """,
    "risk_warnings": """



    * High training costs per employee may impact the company's overall profitability and competitiveness.
    * Excessive training costs without a corresponding increase in sales performance could indicate inefficiencies in the training process.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track and manage training costs and materials.
    * Cost analysis software to identify areas of high training costs and potential cost-saving opportunities.
    
    
    
    """,
    "integration_points": """



    * Integrate training cost data with sales performance metrics to assess the effectiveness of training programs.
    * Link training cost information with HR systems to analyze the impact of training on employee retention and performance.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing training costs may lead to lower overall expenses, but could also impact the quality and effectiveness of training programs.
    * Increased training costs may indicate a strategic investment in developing a highly skilled sales force, potentially leading to improved sales performance in the long run.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.734952"},
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
                        339,
                        364,
                        340,
                        348,
                        359,
                        351,
                        373,
                        386,
                        388,
                        377,
                        373,
                        375
                ],
                "unit": "count"
        },
        "current": {
                "value": 375,
                "unit": "count",
                "change": 2,
                "change_percent": 0.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 364.42,
                "min": 339,
                "max": 388,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 90.34,
                        "percentage": 24.1
                },
                {
                        "category": "Channel Sales",
                        "value": 66.77,
                        "percentage": 17.8
                },
                {
                        "category": "Online Sales",
                        "value": 51.14,
                        "percentage": 13.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 43.7,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 123.05,
                        "percentage": 32.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.831640",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Training Cost Per Employee"
        }
    },
}
