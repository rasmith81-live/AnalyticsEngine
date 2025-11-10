"""
Deal Size KPI

The value of closed deals. Can be aggregated using various arithmetic functions
(average, median, sum, min, max) and filtered by time period.
"""

from analytics_models import KPI

DEAL_SIZE = KPI(
    name="Deal Size",
    code="DEAL_SIZE",
    description="The value of closed deals, supporting multiple aggregation methods (average, median, sum, min, max) and time period filters.",
    
    # Definition & Context
    kpi_definition="The value of closed deals. This metric can be aggregated using various arithmetic functions (average, median, sum, min, max) and filtered by time period (daily, weekly, monthly, quarterly, annually) to provide flexible analysis of deal performance.",
    expected_business_insights="Provides insights into sales team performance, pricing strategies, and revenue patterns. Helps with forecasting, target setting, and identifying trends in deal values across different time periods and customer segments.",
    measurement_approach="Measures the revenue value of closed deals. Can be analyzed as individual deal values or aggregated using arithmetic functions. Supports filtering by time period, product, customer segment, sales representative, and other dimensions.",
    
    # Calculation
    formula="Revenue Value per Closed Deal (base metric). Aggregations: AVG(deal_value), MEDIAN(deal_value), SUM(deal_value), MIN(deal_value), MAX(deal_value)",
    calculation_formula="Base: Individual deal revenue value. Common aggregations: Total Revenue from Closed Deals / Number of Closed Deals (average), SUM(deal_value) (total), MEDIAN(deal_value) (median)",
    
    # Analysis
    trend_analysis="""
    * Increasing deal size may indicate successful upselling, cross-selling strategies, or improved market positioning.
    * Decreasing deal size could signal increased competition, pricing pressure, or changes in customer preferences.
    * Variability in deal size may reflect diverse customer segments or product mix.
    * Seasonal patterns may emerge when analyzing by time period.
    """,
    diagnostic_questions=[
        'Are there specific products, services, or customer segments driving variation in deal size?',
        'How does deal size compare to industry benchmarks or historical data?',
        'What is the distribution of deal sizes (are most deals clustered around the average or widely dispersed)?',
        'How does deal size vary by sales representative, region, or channel?',
        'Are there seasonal patterns or trends in deal size over different time periods?'
    ],
    actionable_steps={
        "operational": [
            'Implement targeted pricing strategies to maximize deal size without sacrificing volume.',
            'Train sales teams on value-based selling to increase deal values.',
            'Offer bundled solutions to increase overall deal size.'
        ],
        "strategic": [
            'Invest in sales training and coaching to improve negotiation and upselling skills.',
            'Explore cross-selling opportunities to increase the value of each deal.',
            'Analyze deal size distribution to identify opportunities for customer segmentation.',
            'Implement pricing strategies that encourage customers to opt for higher-value packages.'
        ]
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "line_chart", "description": "Track deal size trends over time (daily, weekly, monthly, quarterly) with multiple aggregation methods."},
        {"type": "histogram", "description": "Show distribution of deal sizes to identify patterns and outliers."},
        {"type": "box_plot", "description": "Display deal size distribution with quartiles, median, and outliers."},
        {"type": "scatter_plot", "description": "Visualize relationship between deal size and other variables (sales cycle length, customer demographics, product category)."},
        {"type": "bar_chart", "description": "Compare deal size averages by product category, sales representative, or region."},
        {"type": "heatmap", "description": "Show deal size patterns across time periods and dimensions (e.g., month vs. product line)."}
    ],
    risk_warnings=[
        'Significant fluctuations in deal size can impact revenue forecasts and financial planning.',
        'Consistently low deal sizes may indicate need for product or pricing adjustments.',
        'Overemphasis on deal size may lead to neglecting customer satisfaction and retention.',
        'High variance in deal size may indicate inconsistent sales processes or targeting.'
    ],
    
    # Tools & Integration
    suggested_tracking_tools=[
        'Customer Relationship Management (CRM) software to track deal sizes and customer interactions.',
        'Business intelligence tools for in-depth analysis of deal size trends and patterns.',
        'Data analytics platforms supporting multiple aggregation functions and time-based filtering.'
    ],
    integration_points=[
        'Integrate deal size data with sales performance metrics to identify correlations and opportunities.',
        'Link deal size analysis with product development and marketing strategies to align offerings with customer preferences.',
        'Connect with customer feedback systems to understand correlation between deal size and satisfaction.',
        'Integrate with forecasting models to improve revenue predictions.'
    ],
    
    # Impact
    change_impact="Increasing deal size may lead to higher revenue and profitability, but could require adjustments in sales processes and customer targeting. Decreasing deal size may impact overall sales performance and require reevaluation of pricing and product positioning. Changes in deal size distribution may indicate shifts in market dynamics or customer preferences.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "aggregation_methods": ["average", "median", "sum", "min", "max", "count"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"],
        "dimensions": ["product", "customer_segment", "sales_rep", "region", "channel"],
        "replaces": ["DEAL_SIZE_AVERAGE", "AVERAGE_DEAL_SIZE"],
        "required_objects": ["Channel Deal", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Market Segment", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
