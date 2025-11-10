"""
Average Revenue per Unit (ARPU) KPI

Module: Business Development
"""

from analytics_models import KPI

AVERAGE_REVENUE_PER_UNIT_ARPU = KPI(
    name="Average Revenue per Unit (ARPU)",
    code="AVERAGE_REVENUE_PER_UNIT_ARPU",
    description="The average revenue generated per unit sold, which helps assess the value of a company's products or services.",
    
    # Definition & Context
    kpi_definition="The average revenue generated per unit sold, which helps assess the value of a company's products or services.",
    expected_business_insights="Assists in evaluating the value generated from customers and helps in pricing strategies.",
    measurement_approach="Calculates the average revenue generated per unit sold or customer served.",
    
    # Calculation
    formula="Total Revenue / Total Number of Units or Customers",
    
    # Analysis
    trend_analysis="ARPU may increase over time as a result of product or service upgrades, pricing changes, or upselling strategies. A decreasing ARPU could indicate market saturation, increased competition, or a shift towards lower-priced offerings.",
    diagnostic_questions=['What factors have contributed to the recent trend in ARPU?', 'Are there specific customer segments or product lines driving changes in ARPU?'],
    actionable_steps={
        "operational": ['Focus on cross-selling and upselling to existing customers to increase the average revenue per unit.'],
        "strategic": ['Regularly review and adjust pricing strategies to maximize ARPU without sacrificing customer satisfaction.', 'Introduce premium or value-added features to existing products or services to justify higher prices.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts to visualize ARPU trends over time.', 'Pie charts to compare the contribution of different product lines or customer segments to overall ARPU.']
    ],
    risk_warnings=['A declining ARPU may indicate a loss of competitive advantage or declining perceived value of products or services.', 'Significant fluctuations in ARPU could signal instability in the market or customer base.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) systems to track customer purchasing behavior and identify opportunities for upselling.', 'Business intelligence and analytics tools to analyze customer segments and purchasing patterns that impact ARPU.'],
    integration_points=['Integrate ARPU tracking with sales and marketing systems to align efforts towards maximizing average revenue per unit.', 'Link ARPU with customer feedback and satisfaction metrics to ensure that pricing strategies align with perceived value.'],
    
    # Impact
    change_impact="Increasing ARPU may lead to higher customer lifetime value and improved overall revenue. However, aggressive pricing strategies to increase ARPU may lead to customer churn and reduced market share.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_PERFORMANCE"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Quarterly Business Review", "Revenue Forecast", "Sale"]
    }
)
