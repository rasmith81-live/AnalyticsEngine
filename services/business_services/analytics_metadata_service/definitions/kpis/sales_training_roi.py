"""
Sales Training ROI

The return on investment for sales training, assessing the effectiveness of training programs in improving sales performance.
"""

SALES_TRAINING_ROI = {
    "code": "SALES_TRAINING_ROI",
    "name": "Sales Training ROI",
    "description": "The return on investment for sales training, assessing the effectiveness of training programs in improving sales performance.",
    "formula": "(Increase in Sales Revenue - Cost of Training) / Cost of Training * 100",
    "calculation_formula": "(Increase in Sales Revenue - Cost of Training) / Cost of Training * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Training ROI to be added.",
    "trend_analysis": """



    * An increasing sales training ROI may indicate the effectiveness of new training programs or improved adoption of training by the sales team.
    * A decreasing ROI could signal a need to reassess the training content or delivery methods, as well as potential issues with sales team engagement.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales training programs or modules that are consistently rated as more effective by the sales team?
    * How does the sales training ROI compare with industry benchmarks or with the performance of top-performing sales teams?
    
    
    
    """,
    "actionable_tips": """



    * Regularly gather feedback from the sales team to identify areas for improvement in the training programs.
    * Customize training content to address specific sales challenges or market conditions that the team is facing.
    * Invest in coaching and mentorship programs to reinforce and apply the knowledge gained from sales training.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales training ROI over time.
    * Comparison charts to visualize the ROI of different training programs or initiatives.
    
    
    
    """,
    "risk_warnings": """



    * A low sales training ROI may lead to decreased sales performance and missed revenue targets.
    * An inconsistent or declining ROI could indicate a need for a more strategic approach to sales training and development.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track participation and engagement with training materials.
    * Sales performance analytics tools to correlate training effectiveness with actual sales results.
    
    
    
    """,
    "integration_points": """



    * Integrate sales training ROI data with individual sales performance metrics to identify correlations and opportunities for targeted training interventions.
    * Link training ROI with customer satisfaction and retention metrics to understand the impact of training on customer relationships.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving sales training ROI can lead to increased sales productivity and revenue generation.
    * Conversely, a declining ROI may result in decreased motivation and confidence among the sales team, impacting overall sales performance.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.537898"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
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
                        60.19,
                        49.94,
                        61.96,
                        66.81,
                        51.13,
                        57.89,
                        66.45,
                        51.93,
                        67.34,
                        54.85,
                        65.1,
                        54.05
                ],
                "unit": "%"
        },
        "current": {
                "value": 54.05,
                "unit": "%",
                "change": -11.05,
                "change_percent": -17.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 58.97,
                "min": 49.94,
                "max": 67.34,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 10.92,
                        "percentage": 20.2
                },
                {
                        "category": "Channel Sales",
                        "value": 7.34,
                        "percentage": 13.6
                },
                {
                        "category": "Online Sales",
                        "value": 6.94,
                        "percentage": 12.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.83,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 23.02,
                        "percentage": 42.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.294885",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Training ROI"
        }
    },
}
