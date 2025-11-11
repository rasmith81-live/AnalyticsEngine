"""
Deal Size Growth Post-Training

The increase in the average size of deals closed by sales reps after receiving training.
"""

DEAL_SIZE_GROWTH_POST_TRAINING = {
    "code": "DEAL_SIZE_GROWTH_POST_TRAINING",
    "name": "Deal Size Growth Post-Training",
    "description": "The increase in the average size of deals closed by sales reps after receiving training.",
    "formula": "(Average Deal Size Post-Training - Average Deal Size Pre-Training) / Average Deal Size Pre-Training * 100",
    "calculation_formula": "(Average Deal Size Post-Training - Average Deal Size Pre-Training) / Average Deal Size Pre-Training * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Size Growth Post-Training to be added.",
    "trend_analysis": """



    * An upward trend in deal size growth post-training may indicate that the training is effectively equipping sales reps with the skills and knowledge to close larger deals.
    * A downward trend could suggest that the training is not effectively translating into increased deal sizes, potentially indicating a need for a different training approach or additional support.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific product lines or customer segments that are consistently driving the increase in deal sizes post-training?
    * How do the deal sizes of trained sales reps compare to those who have not received the training, and what insights can be gained from this comparison?
    
    
    
    """,
    "actionable_tips": """



    * Provide ongoing coaching and reinforcement of training materials to ensure that new skills and knowledge are consistently applied in sales interactions.
    * Encourage sales reps to focus on value-based selling and to identify opportunities for upselling or cross-selling during the sales process.
    * Implement a deal review process to identify areas for improvement and share best practices among the sales team.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average deal size over time for trained sales reps compared to untrained reps.
    * Bar graphs comparing the distribution of deal sizes before and after training to visualize any shifts in the size of closed deals.
    
    
    
    """,
    "risk_warnings": """



    * If deal size growth post-training does not materialize, it may indicate a lack of effectiveness in the training program, leading to potential wasted resources and missed revenue opportunities.
    * Relying solely on deal size growth as a KPI may overlook other important aspects of sales performance, such as conversion rates or customer satisfaction.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track deal sizes and analyze the impact of training on sales performance.
    * Sales enablement platforms to provide sales reps with the necessary resources and support to effectively apply their training in real-world sales situations.
    
    
    
    """,
    "integration_points": """



    * Integrate deal size growth post-training with performance management systems to align individual and team goals with the desired increase in deal sizes.
    * Linking this KPI with customer feedback and satisfaction metrics can provide a more comprehensive understanding of the impact of training on overall sales performance.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in deal size growth post-training may positively impact revenue and profitability, but it could also require adjustments in sales strategies and resource allocation.
    * Conversely, a lack of improvement in deal sizes post-training may lead to missed revenue opportunities and could indicate a need for broader sales process improvements.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.915374"},
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
                        61.59,
                        61.34,
                        47.58,
                        51.99,
                        62.29,
                        46.92,
                        48.9,
                        62.98,
                        61.52,
                        54.31,
                        54.88,
                        63.82
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.82,
                "unit": "%",
                "change": 8.94,
                "change_percent": 16.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.51,
                "min": 46.92,
                "max": 63.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.81,
                        "percentage": 24.8
                },
                {
                        "category": "Segment B",
                        "value": 9.31,
                        "percentage": 14.6
                },
                {
                        "category": "Segment C",
                        "value": 10.77,
                        "percentage": 16.9
                },
                {
                        "category": "Segment D",
                        "value": 2.89,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 25.04,
                        "percentage": 39.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.891466",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Deal Size Growth Post-Training"
        }
    },
}
