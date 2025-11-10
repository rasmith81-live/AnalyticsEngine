"""
Sales Forecast Accuracy KPI

The accuracy of the sales team's revenue forecasts.
"""

from analytics_models import KPI

SALES_FORECAST_ACCURACY = KPI(
    name="Sales Forecast Accuracy",
    code="SALES_FORECAST_ACCURACY",
    category="Inside Sales",
    
    # Core Definition
    description="The accuracy of the sales team\'s revenue forecasts.",
    kpi_definition="The accuracy of the sales team\'s revenue forecasts.",
    expected_business_insights="Measures the precision of sales forecasting methods and can highlight areas that need improvement.",
    measurement_approach="The accuracy of sales forecasts compared to actual sales.",
    
    # Formula
    formula="(Total Actual Sales / Total Forecasted Sales) * 100",
    calculation_formula="(Total Actual Sales / Total Forecasted Sales) * 100",
    
    # Analysis
    trend_analysis="""
    * Consistently accurate forecasts may indicate a deep understanding of market dynamics and customer behavior.
    * An increasing forecast error rate could signal a need for better data analysis or adjustments to sales strategies.
    """,
    diagnostic_questions="""
    * Are there specific sales territories or product lines that consistently over- or underestimate forecasts?
    * How do external factors such as economic conditions or industry trends impact the accuracy of our sales forecasts?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update sales forecasting models based on historical data and current market conditions.
    * Provide ongoing training and support for the sales team to improve their understanding of forecasting tools and techniques.
    * Implement a collaborative approach between sales and marketing teams to gather more accurate customer insights and market data.
    """,
    visualization_suggestions="""
    * Line charts showing the variance between forecasted and actual sales figures over time.
    * Pie charts comparing forecast accuracy by product category or sales region.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Inaccurate sales forecasts can lead to inventory imbalances, excess stock, or stockouts, impacting overall business performance.
    * Over-reliance on inaccurate forecasts may result in missed sales opportunities or ineffective resource allocation.
    """,
    tracking_tools="""
    * Utilize advanced CRM systems with built-in forecasting modules to streamline data collection and analysis.
    * Implement business intelligence tools such as Tableau or Power BI for in-depth sales forecasting visualization and analysis.
    """,
    integration_points="""
    * Integrate sales forecasting with inventory management systems to ensure alignment between projected sales and available stock levels.
    * Link sales forecasts with financial planning and budgeting processes to optimize resource allocation and investment decisions.
    """,
    change_impact_analysis="""
    * Improving sales forecast accuracy can lead to better resource utilization, improved inventory turnover, and increased customer satisfaction.
    * However, overestimating or underestimating sales forecasts can impact production planning, cash flow, and overall business profitability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07"
        "replaces": ["SALES_FORECAST_ACCURACY_RATE"],
        "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
