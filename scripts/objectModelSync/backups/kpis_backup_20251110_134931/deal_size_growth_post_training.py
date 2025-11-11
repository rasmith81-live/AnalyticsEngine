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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.416308"},
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
                        896.53,
                        822.63,
                        757.69,
                        791.12,
                        854.02,
                        794.28,
                        840.45,
                        811.7,
                        779.14,
                        903.25,
                        810.11,
                        883.02
                ],
                "unit": "units"
        },
        "current": {
                "value": 883.02,
                "unit": "units",
                "change": 72.91,
                "change_percent": 9.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 828.66,
                "min": 757.69,
                "max": 903.25,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 135.94,
                        "percentage": 15.4
                },
                {
                        "category": "Category B",
                        "value": 164.74,
                        "percentage": 18.7
                },
                {
                        "category": "Category C",
                        "value": 121.27,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 51.22,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 409.85,
                        "percentage": 46.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.416308",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Deal Size Growth Post-Training"
        }
    },
}
