"""
Sales Certification Rate KPI

The percentage of sales representatives who achieve certification in relevant sales methodologies and product knowledge.
"""

from analytics_models import KPI

SALES_CERTIFICATION_RATE = KPI(
    name="Sales Certification Rate",
    code="SALES_CERTIFICATION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of sales representatives who achieve certification in relevant sales methodologies and product knowledge.",
    kpi_definition="The percentage of sales representatives who achieve certification in relevant sales methodologies and product knowledge.",
    expected_business_insights="Assesses the level of professional development and expertise within the sales team.",
    measurement_approach="Measures the percentage of sales reps who have completed required sales certifications.",
    
    # Formula
    formula="(Number of Certified Sales Reps / Total Number of Sales Reps) * 100",
    calculation_formula="(Number of Certified Sales Reps / Total Number of Sales Reps) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales certification rate may indicate improved training programs or a more knowledgeable sales force.
    * A decreasing rate could signal a need for updated training materials or a shift in product focus.
    """,
    diagnostic_questions="""
    * Are there specific sales methodologies or products where certification rates are consistently low?
    * How does our sales certification rate compare with industry benchmarks or competitor performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update and refresh training materials to keep them relevant and engaging.
    * Provide incentives for sales representatives to pursue and achieve certifications.
    * Implement mentorship programs to support new hires in achieving certification.
    """,
    visualization_suggestions="""
    * Line charts showing certification rates over time for different sales methodologies or product categories.
    * Stacked bar charts comparing certification rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low certification rates may lead to decreased sales effectiveness and missed revenue opportunities.
    * High certification rates without corresponding sales performance improvements may indicate a need for more practical training.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and manage certification progress for sales representatives.
    * Sales enablement platforms that provide interactive training modules and assessments.
    """,
    integration_points="""
    * Integrate certification tracking with performance management systems to correlate certification rates with sales results.
    * Link certification data with customer relationship management (CRM) systems to understand the impact on customer interactions.
    """,
    change_impact_analysis="""
    * Improving the sales certification rate can lead to better customer interactions and increased sales effectiveness.
    * However, focusing solely on certification rates may neglect other important aspects of sales performance, such as customer relationship building.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Certification", "Enablement Feedback", "Enablement Platform", "Knowledge Base", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
