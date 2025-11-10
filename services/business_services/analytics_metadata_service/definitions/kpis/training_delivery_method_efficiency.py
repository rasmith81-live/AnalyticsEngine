"""
Training Delivery Method Efficiency KPI

An evaluation of the effectiveness of different training delivery methods (e.g., in-person, online, blended learning).
"""

from analytics_models import KPI

TRAINING_DELIVERY_METHOD_EFFICIENCY = KPI(
    name="Training Delivery Method Efficiency",
    code="TRAINING_DELIVERY_METHOD_EFFICIENCY",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="An evaluation of the effectiveness of different training delivery methods (e.g., in-person, online, blended learning).",
    kpi_definition="An evaluation of the effectiveness of different training delivery methods (e.g., in-person, online, blended learning).",
    expected_business_insights="Provides insight into which training modalities are most effective for the sales team, informing future training strategies.",
    measurement_approach="A measure of the effectiveness of different training delivery methods, such as in-person, online, or hybrid formats.",
    
    # Formula
    formula="Efficiency Rating Based on Performance Improvements Post-Training",
    calculation_formula="Efficiency Rating Based on Performance Improvements Post-Training",
    
    # Analysis
    trend_analysis="""
    * Increased utilization of online training methods may indicate a shift towards remote work and virtual learning.
    * A decline in in-person training effectiveness could signal a need for updated content or more engaging delivery methods.
    """,
    diagnostic_questions="""
    * Are certain topics or skills better suited for specific training delivery methods?
    * How do participant feedback and performance metrics differ across different training delivery methods?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Customize training content to fit the delivery method, ensuring it is engaging and interactive.
    * Regularly assess and update online training platforms to incorporate new technologies and learning trends.
    * Provide options for blended learning to cater to different learning styles and preferences.
    """,
    visualization_suggestions="""
    * Line graphs showing the effectiveness of different training delivery methods over time.
    * Comparison charts displaying participant feedback and performance metrics for each delivery method.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on a single delivery method may lead to disengagement and reduced effectiveness of training.
    * Ignoring participant feedback on delivery methods can result in decreased learning outcomes and knowledge retention.
    """,
    tracking_tools="""
    * Learning management systems (LMS) with analytics capabilities to track participant engagement and performance across different delivery methods.
    * Virtual reality (VR) and augmented reality (AR) technologies for immersive online training experiences.
    """,
    integration_points="""
    * Integrate training delivery method data with HR systems to align learning strategies with employee development goals.
    * Link participant feedback from different delivery methods with performance management systems to identify correlations with job performance.
    """,
    change_impact_analysis="""
    * Improving the effectiveness of training delivery methods can lead to better knowledge retention and application in the workplace.
    * However, changes in delivery methods may require additional resources and time for content development and implementation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
