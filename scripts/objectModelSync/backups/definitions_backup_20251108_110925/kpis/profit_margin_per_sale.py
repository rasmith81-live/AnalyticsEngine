"""
Profit Margin per Sale KPI

The profit generated from each sale, expressed as a percentage or absolute value.
Can be aggregated using various arithmetic functions and filtered by time period.
"""

from analytics_models import KPI

PROFIT_MARGIN_PER_SALE = KPI(
    name="Profit Margin per Sale",
    code="PROFIT_MARGIN_PER_SALE",
    description="The profit generated from each sale, supporting multiple aggregation methods (average, median, sum, min, max) and time period filters. Can be expressed as percentage margin or absolute profit value.",
    
    # Definition & Context
    kpi_definition="The profit generated from each sale, indicating the profitability of the sales process. This metric can be aggregated using various arithmetic functions (average, median, sum, min, max) and filtered by time period (daily, weekly, monthly, quarterly, annually) to provide flexible analysis of sales profitability.",
    expected_business_insights="Provides insights into the profitability of sales activities, informs pricing strategies, and helps identify high-margin products, customer segments, and sales representatives. Reveals whether current pricing strategies are effective and highlights opportunities for cost optimization or revenue enhancement.",
    measurement_approach="Measures the profit earned from each sale after subtracting costs. Can be analyzed as individual sale profitability or aggregated using arithmetic functions. Supports filtering by time period, product, customer segment, sales representative, and other dimensions. Can be expressed as percentage margin or absolute profit value.",
    
    # Calculation
    formula="Base: (Revenue - Cost of Goods Sold) per Sale. Percentage: ((Revenue - COGS) / Revenue) × 100. Aggregations: AVG(profit_margin), MEDIAN(profit_margin), SUM(profit), MIN(profit_margin), MAX(profit_margin)",
    calculation_formula="Base: (Total Revenue - Cost of Goods Sold) / Number of Sales (average). Percentage: ((Revenue - COGS) / Revenue) × 100. Absolute: (Revenue - COGS) per sale",
    
    # Analysis
    trend_analysis="""
    * Increasing profit margins per sale may indicate successful pricing strategies, cost-saving measures, or improved product mix.
    * Decreasing margins could signal increased competition, rising production costs, ineffective pricing strategies, or shift to lower-margin products.
    * Variability in profit margins may reflect diverse product portfolios or customer segments.
    * Seasonal patterns may emerge when analyzing by time period.
    * Significantly high margins may indicate overpricing and potential loss of market share.
    """,
    diagnostic_questions=[
        'Are there specific products or services with consistently high or low profit margins?',
        'How do our profit margins compare to industry benchmarks or historical data?',
        'What is the distribution of profit margins (are most sales clustered around the average or widely dispersed)?',
        'How does profit margin vary by sales representative, region, channel, or customer segment?',
        'Are there seasonal patterns or trends in profit margins over different time periods?',
        'Which products or customer segments contribute most to overall profitability?'
    ],
    actionable_steps={
        "operational": [
            'Regularly review pricing strategies and adjust based on market conditions and cost fluctuations.',
            'Identify and eliminate inefficiencies in the production or sales process to improve overall profitability.',
            'Monitor cost of goods sold and negotiate better supplier terms.'
        ],
        "strategic": [
            'Implement cost-saving measures such as bulk purchasing or renegotiating supplier contracts.',
            'Focus on upselling or cross-selling higher-margin products or services.',
            'Provide sales teams with training on value-based selling and margin-aware selling techniques.',
            'Analyze profit margin distribution to identify opportunities for customer segmentation.',
            'Develop pricing strategies that balance volume and profitability.'
        ]
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "line_chart", "description": "Track profit margins over time (daily, weekly, monthly, quarterly) with multiple aggregation methods."},
        {"type": "histogram", "description": "Show distribution of profit margins to identify patterns and outliers."},
        {"type": "box_plot", "description": "Display profit margin distribution with quartiles, median, and outliers."},
        {"type": "pareto_chart", "description": "Identify which products or services contribute the most to overall profit margins."},
        {"type": "scatter_plot", "description": "Visualize relationship between profit margin and other variables (deal size, sales cycle length, customer segment)."},
        {"type": "bar_chart", "description": "Compare profit margins by product category, sales representative, or region."},
        {"type": "heatmap", "description": "Show profit margin patterns across time periods and dimensions (e.g., month vs. product line)."}
    ],
    risk_warnings=[
        'Declining profit margins may lead to reduced profitability and financial instability.',
        'Over-reliance on high-margin products or services may pose a risk if market demand shifts.',
        'Significantly high profit margins may indicate overpricing and potential loss of market share.',
        'Aggressive cost-cutting measures to improve margins could impact product quality and customer satisfaction.',
        'High variance in profit margins may indicate inconsistent pricing or cost management.'
    ],
    
    # Tools & Integration
    suggested_tracking_tools=[
        'Financial management software like QuickBooks or Xero for detailed profit margin analysis.',
        'Customer relationship management (CRM) systems to track customer preferences and identify high-margin segments.',
        'Business intelligence tools for in-depth analysis of profit margin trends and patterns.',
        'Data analytics platforms supporting multiple aggregation functions and time-based filtering.'
    ],
    integration_points=[
        'Integrate profit margin analysis with sales and marketing systems to align pricing strategies with customer segments.',
        'Link with inventory management systems to ensure sufficient stock levels for high-margin products and optimize stock based on profitability.',
        'Connect with sales performance metrics to identify top-performing products, services, and sales representatives.',
        'Integrate with cost accounting systems for accurate COGS tracking.',
        'Link to forecasting models to improve profitability predictions.'
    ],
    
    # Impact
    change_impact="Improving profit margins can lead to increased revenue and overall business growth. However, aggressive margin increases may impact customer loyalty and satisfaction if perceived as price gouging. Cost-cutting measures to improve margins must be balanced against maintaining product quality and customer satisfaction. Changes in profit margin distribution may indicate shifts in market dynamics, competitive positioning, or product mix.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_DEVELOPMENT", "INSIDE_SALES", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "aggregation_methods": ["average", "median", "sum", "min", "max", "count"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"],
        "dimensions": ["product", "customer_segment", "sales_rep", "region", "channel"],
        "metric_types": ["percentage", "absolute_value"],
        "replaces": ["AVERAGE_PROFIT_MARGIN_PER_SALE"],
        "required_objects": ["Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Lost Sale", "Market Segment", "Opportunity", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
