"""
Product Knowledge Test Scores KPI

Average scores on product knowledge tests taken by sales reps after training.
"""

from analytics_models import KPI

PRODUCT_KNOWLEDGE_TEST_SCORES = KPI(
    name="Product Knowledge Test Scores",
    code="PRODUCT_KNOWLEDGE_TEST_SCORES",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="Average scores on product knowledge tests taken by sales reps after training.",
    kpi_definition="Average scores on product knowledge tests taken by sales reps after training.",
    expected_business_insights="Indicates the effectiveness of product training and reps\' readiness to adequately present and sell products.",
    measurement_approach="Scores achieved by sales reps on tests designed to assess their understanding of the products they sell.",
    
    # Formula
    formula="Average of Product Knowledge Test Scores",
    calculation_formula="Average of Product Knowledge Test Scores",
    
    # Analysis
    trend_analysis="""
    * Increasing average scores may indicate improved training effectiveness or better product understanding among sales reps.
    * Decreasing scores could signal a need for updated training materials or a lack of product knowledge retention.
    """,
    diagnostic_questions="""
    * Are there specific product areas where sales reps consistently score lower on the knowledge tests?
    * How do the average scores compare with the performance of top-performing sales reps?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update training materials to reflect new product features or changes.
    * Implement regular refresher training sessions to reinforce product knowledge and ensure retention.
    * Encourage a culture of continuous learning and knowledge sharing among sales reps.
    """,
    visualization_suggestions="""
    * Line charts showing average scores over time to identify trends in knowledge retention.
    * Comparison bar charts to visualize differences in scores across different product categories or sales teams.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low average scores may lead to decreased sales performance and missed opportunities.
    * Inaccurate product knowledge can result in customer dissatisfaction and lost sales.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and manage training materials and assessments.
    * Knowledge management platforms to facilitate easy access to product information for sales reps.
    """,
    integration_points="""
    * Integrate product knowledge test results with individual performance evaluations to identify areas for improvement.
    * Link training and assessment data with customer feedback to understand the impact of product knowledge on customer satisfaction.
    """,
    change_impact_analysis="""
    * Improving product knowledge can lead to increased customer confidence and higher sales conversion rates.
    * Conversely, a decline in average scores may result in decreased customer trust and satisfaction, impacting sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Knowledge Base", "Partner Training", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
