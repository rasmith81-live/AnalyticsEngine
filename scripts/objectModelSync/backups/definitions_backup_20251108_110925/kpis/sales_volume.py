"""
Sales Volume KPI

The total number of sales made by the outside sales team.
"""

from analytics_models import KPI

SALES_VOLUME = KPI(
    name="Sales Volume",
    code="SALES_VOLUME",
    category="Outside Sales",
    
    # Core Definition
    description="The total number of sales made by the outside sales team.",
    kpi_definition="The total number of sales made by the outside sales team.",
    expected_business_insights="Provides insights into market demand and sales effectiveness, which can impact inventory management and marketing strategies.",
    measurement_approach="Measures the total number of products sold or total revenue generated from sales.",
    
    # Formula
    formula="Sum of all Products Sold or Total Revenue from Sales",
    calculation_formula="Sum of all Products Sold or Total Revenue from Sales",
    
    # Analysis
    trend_analysis="""
    * Increasing sales volume may indicate growing market demand or improved sales strategies.
    * Decreasing sales volume could signal market saturation, ineffective sales tactics, or economic downturn.
    """,
    diagnostic_questions="""
    * What factors have contributed to the changes in sales volume over time?
    * Are there specific products or regions driving the changes in sales volume?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in sales training and development programs to improve the effectiveness of the sales team.
    * Explore new markets or customer segments to expand the potential customer base.
    * Implement customer relationship management (CRM) software to better track and manage sales activities.
    """,
    visualization_suggestions="""
    * Line charts to visualize the trend in sales volume over time.
    * Pie charts to compare sales volume by product category or region.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low sales volume can lead to revenue shortfalls and financial instability.
    * High sales volume without proper capacity planning can result in fulfillment challenges and customer dissatisfaction.
    """,
    tracking_tools="""
    * CRM systems like Salesforce or HubSpot for tracking and managing sales activities.
    * Data analytics tools to identify patterns and insights related to sales volume.
    """,
    integration_points="""
    * Integrate sales volume data with inventory management systems to ensure adequate stock levels to meet demand.
    * Link sales volume with customer relationship management platforms to understand customer buying behavior and preferences.
    """,
    change_impact_analysis="""
    * Increasing sales volume may require additional resources and infrastructure to support higher demand.
    * Decreasing sales volume can impact cash flow and profitability, potentially leading to cost-cutting measures.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
