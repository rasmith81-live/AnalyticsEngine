"""
Deal Size Growth Post-Training KPI

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
    "kpi_definition": "The increase in the average size of deals closed by sales reps after receiving training.",
    "expected_business_insights": "Indicates whether training is leading to more effective sales strategies and higher-value sales.",
    "measurement_approach": "The change in average deal size secured by sales reps after completing training.",
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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
