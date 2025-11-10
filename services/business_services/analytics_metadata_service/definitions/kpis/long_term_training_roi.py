"""
Long-term Training ROI KPI

The return on investment for sales training calculated over a longer period to gauge sustained impact.
"""

from analytics_models import KPI

LONG_TERM_TRAINING_ROI = KPI(
    name="Long-term Training ROI",
    code="LONG_TERM_TRAINING_ROI",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The return on investment for sales training calculated over a longer period to gauge sustained impact.",
    kpi_definition="The return on investment for sales training calculated over a longer period to gauge sustained impact.",
    expected_business_insights="Reflects the sustained value of training in terms of increased sales and performance improvements.",
    measurement_approach="A measure of the return on investment for sales training over an extended period, typically years.",
    
    # Formula
    formula="(Gain from Investment in Training - Cost of Training) / Cost of Training",
    calculation_formula="(Gain from Investment in Training - Cost of Training) / Cost of Training",
    
    # Analysis
    trend_analysis="""
    * Long-term training ROI may show an initial dip as the investment in training takes time to yield results, followed by a gradual increase as the impact of training becomes evident.
    * A declining trend could indicate a need for updated training methods or a shift in market dynamics that require different skill sets.
    """,
    diagnostic_questions="""
    * Are there specific sales teams or individuals that have shown sustained improvement in performance after training?
    * How does the long-term training ROI compare with industry benchmarks or competitors\' performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly assess the relevance of training content and methods to ensure they align with evolving market needs.
    * Provide ongoing coaching and reinforcement to ensure that training outcomes are sustained over the long term.
    * Encourage a culture of continuous learning and skill development to maximize the long-term impact of training.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of training ROI over multiple years.
    * Comparison graphs to visualize the ROI of different training programs or approaches.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low long-term training ROI may indicate a need for a fundamental shift in training strategies or resource allocation.
    * High variability in training ROI over time may point to inconsistent training quality or effectiveness.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and analyze the long-term impact of different training programs.
    * Performance management software to correlate training ROI with individual and team sales performance.
    """,
    integration_points="""
    * Integrate long-term training ROI analysis with HR systems to align training efforts with talent development and retention strategies.
    * Link training ROI data with sales performance metrics to understand the direct impact of training on revenue generation.
    """,
    change_impact_analysis="""
    * Improving long-term training ROI can lead to a more skilled and motivated sales force, potentially increasing overall sales performance and customer satisfaction.
    * Conversely, a declining long-term training ROI may signal a need for significant changes in training approaches to avoid negative impacts on sales effectiveness and employee morale.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
