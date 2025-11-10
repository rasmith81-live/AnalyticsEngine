"""
Revenue Forecast Accuracy KPI

Module: Business Development
"""

from analytics_models import KPI

REVENUE_FORECAST_ACCURACY = KPI(
    name="Revenue Forecast Accuracy",
    code="REVENUE_FORECAST_ACCURACY",
    description="The accuracy of the sales team's revenue forecasts compared to actual revenue results.",
    
    # Definition & Context
    kpi_definition="The accuracy of the sales team's revenue forecasts compared to actual revenue results.",
    expected_business_insights="Indicates the effectiveness of sales forecasting and can guide strategic decision making.",
    measurement_approach="Measures the accuracy of predicted sales revenue against the actual revenue.",
    
    # Calculation
    formula="(Absolute Value of (Actual Revenue - Forecasted Revenue) / Actual Revenue) * 100",
    
    # Analysis
    trend_analysis="Consistently accurate revenue forecasts may indicate a strong understanding of market trends and customer behavior. An increasing gap between forecasted and actual revenue could signal a need for better data analysis or adjustments to sales strategies.",
    diagnostic_questions=['Are there specific sales channels or products that consistently over or underperform in revenue forecasts?', 'How do external factors such as economic conditions or industry trends impact the accuracy of our revenue forecasts?'],
    actionable_steps={
        "operational": ['Implement regular reviews and updates of sales forecasts based on real-time market data and customer feedback.'],
        "strategic": ['Provide ongoing training and support for sales teams to improve their understanding of forecasting tools and techniques.', 'Utilize advanced analytics and machine learning tools to enhance the accuracy of revenue forecasts.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts comparing forecasted revenue against actual revenue over time.', 'Stacked bar graphs showing the variance between forecasted and actual revenue by product category or sales channel.']
    ],
    risk_warnings=['Inaccurate revenue forecasts can lead to financial instability and missed growth opportunities.', 'Overly optimistic forecasts may result in overcommitment of resources and underperformance against targets.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Utilize CRM systems with built-in forecasting modules to track and analyze revenue projections.', 'Implement business intelligence tools such as Tableau or Power BI for in-depth analysis of sales data and forecasting accuracy.'],
    integration_points=['Integrate revenue forecasting with financial planning and budgeting systems to align sales targets with overall business goals.', 'Link forecasting tools with inventory management systems to ensure accurate demand planning and inventory optimization.'],
    
    # Impact
    change_impact="Improving revenue forecast accuracy can lead to better resource allocation and strategic decision-making across the organization. However, overly conservative forecasts may limit investment and growth opportunities, impacting long-term competitiveness.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
