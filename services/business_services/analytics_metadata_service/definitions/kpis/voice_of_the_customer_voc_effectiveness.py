"""
Voice of the Customer (VoC) Effectiveness KPI

The impact of customer feedback on driving business improvements and customer retention strategies.
"""

from analytics_models import KPI

VOICE_OF_THE_CUSTOMER_VOC_EFFECTIVENESS = KPI(
    name="Voice of the Customer (VoC) Effectiveness",
    code="VOICE_OF_THE_CUSTOMER_VOC_EFFECTIVENESS",
    category="Customer Retention",
    
    # Core Definition
    description="The impact of customer feedback on driving business improvements and customer retention strategies.",
    kpi_definition="The impact of customer feedback on driving business improvements and customer retention strategies.",
    expected_business_insights="Assesses how well a company understands and responds to customer needs and expectations.",
    measurement_approach="Evaluates the success of programs designed to collect and analyze customer feedback.",
    
    # Formula
    formula="Comparison of Customer Metrics Before and After VoC Initiatives",
    calculation_formula="Comparison of Customer Metrics Before and After VoC Initiatives",
    
    # Analysis
    trend_analysis="""
    * Increasing effectiveness in using customer feedback to drive business improvements and retention strategies.
    * Decreasing impact of customer feedback on business improvements and retention strategies.
    """,
    diagnostic_questions="""
    * Are there specific areas or aspects of the business where customer feedback has led to significant improvements?
    * How does the customer feedback loop compare with industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular surveys or feedback mechanisms to capture customer sentiment and preferences.
    * Leverage customer feedback to drive product or service enhancements that directly address customer needs and pain points.
    * Establish a cross-functional team dedicated to analyzing and acting on customer feedback to drive business improvements.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer feedback impact over time.
    * Heat maps to identify areas or touchpoints where customer feedback has been most effective.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low effectiveness in using customer feedback may lead to missed opportunities for improvement and customer retention.
    * Ignoring or undervaluing customer feedback can result in customer dissatisfaction and attrition.
    """,
    tracking_tools="""
    * Customer feedback management platforms like Medallia or Qualtrics to systematically capture and analyze customer input.
    * CRM systems with integrated feedback modules to track and act on customer sentiment.
    """,
    integration_points="""
    * Integrate customer feedback analysis with product development processes to ensure customer input directly influences product enhancements.
    * Link customer feedback with sales and marketing systems to align customer retention strategies with customer preferences.
    """,
    change_impact_analysis="""
    * Improving the effectiveness of customer feedback can lead to increased customer satisfaction and loyalty.
    * Decreasing impact of customer feedback may result in reduced customer retention and negative brand perception.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Quarterly Business Review"]
    }
)
