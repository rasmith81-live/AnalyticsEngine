"""
Sales Cycle Length KPI

The duration from initial contact to deal closure. Can be aggregated using various 
arithmetic functions and filtered by time period.
"""

from analytics_models import KPI

SALES_CYCLE_LENGTH = KPI(
    name="Sales Cycle Length",
    code="SALES_CYCLE_LENGTH",
    description="The duration from initial contact with a lead to deal closure, supporting multiple aggregation methods (average, median, min, max, percentile) and time period filters.",
    
    # Definition & Context
    kpi_definition="The duration from initial contact with a lead to deal closure. This metric can be aggregated using various arithmetic functions (average, median, min, max, percentiles) and filtered by time period (daily, weekly, monthly, quarterly, annually) to provide flexible analysis of sales process efficiency. Measures the time taken to close a deal and indicates the effectiveness of training, coaching, and sales processes.",
    expected_business_insights="Reflects the efficiency of the sales process and helps identify areas for acceleration. Reveals the impact of training and coaching on sales effectiveness. Helps with forecasting, resource planning, and identifying bottlenecks in the sales process. Indicates sales rep efficiency and the quality of lead qualification.",
    measurement_approach="Measures the duration from initial contact with a lead to the closing of a sale. Can be analyzed as individual deal cycle times or aggregated using arithmetic functions. Supports filtering by time period, sales stage, product, customer segment, sales representative, and other dimensions. Can be measured in days, weeks, or months.",
    
    # Calculation
    formula="Duration from First Contact to Deal Closure (base metric). Aggregations: AVG(cycle_duration), MEDIAN(cycle_duration), MIN(cycle_duration), MAX(cycle_duration), PERCENTILE(cycle_duration, p)",
    calculation_formula="Base: (Deal Close Date - First Contact Date). Common aggregations: SUM(cycle_duration) / COUNT(deals) (average), MEDIAN(cycle_duration), MIN/MAX(cycle_duration)",
    
    # Analysis
    trend_analysis="""
    * Shortening sales cycle length may indicate improved lead nurturing, qualification processes, effective training, or streamlined sales processes.
    * An increasing cycle length could signal issues with sales team efficiency, ineffective training or coaching methods, changes in customer buying behavior, or increased competition.
    * Variability in cycle length may reflect diverse customer segments, product complexity, or deal sizes.
    * Seasonal patterns may emerge when analyzing by time period.
    * Rapidly decreasing cycle times may indicate a focus on quantity over quality, potentially leading to customer dissatisfaction.
    """,
    diagnostic_questions=[
        'Are there specific stages in the sales cycle where leads tend to get stuck or delayed?',
        'How does our sales cycle length compare with industry benchmarks or competitors?',
        'What is the distribution of cycle lengths (are most deals clustered around the average or widely dispersed)?',
        'How does cycle length vary by sales representative, product, customer segment, or deal size?',
        'Are there seasonal patterns or trends in cycle length over different time periods?',
        'Which factors correlate most strongly with shorter or longer cycle times?',
        'How does training and coaching impact cycle length for individual reps?'
    ],
    actionable_steps={
        "operational": [
            'Implement sales automation tools to streamline lead management and follow-up processes.',
            'Provide targeted training and coaching for sales reps to improve their skills in each stage of the sales cycle.',
            'Analyze successful deals to identify best practices that can be shared with the entire sales team.',
            'Monitor cycle length in real-time to identify and address delays quickly.'
        ],
        "strategic": [
            'Provide targeted training and coaching to sales teams to improve their ability to move leads through the sales cycle efficiently.',
            'Regularly review and optimize the sales process to identify and remove any bottlenecks or unnecessary steps.',
            'Analyze cycle length patterns to identify opportunities for process improvement.',
            'Invest in sales enablement tools and resources to accelerate the sales process.',
            'Review lead qualification criteria to ensure quality leads enter the pipeline.'
        ]
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "line_chart", "description": "Track sales cycle length over time (daily, weekly, monthly, quarterly) with multiple aggregation methods."},
        {"type": "histogram", "description": "Show distribution of cycle lengths to identify patterns and outliers."},
        {"type": "box_plot", "description": "Display cycle length distribution with quartiles, median, and outliers."},
        {"type": "funnel_chart", "description": "Visualize the drop-off and time spent at each stage of the sales cycle."},
        {"type": "scatter_plot", "description": "Visualize relationship between cycle length and other variables (deal size, customer segment, sales rep experience)."},
        {"type": "bar_chart", "description": "Compare cycle length by sales representative, product, or region."},
        {"type": "heatmap", "description": "Show cycle length patterns across time periods and dimensions (e.g., month vs. product line)."}
    ],
    risk_warnings=[
        'Lengthening sales cycle may result in increased customer acquisition costs and reduced revenue generation.',
        'Shortening the sales cycle without proper lead qualification may lead to lower quality customers and increased churn.',
        'Long sales cycle times can lead to decreased revenue and missed opportunities.',
        'Rapidly decreasing cycle times may indicate a focus on quantity over quality, potentially leading to customer dissatisfaction.',
        'High variance in cycle length may indicate inconsistent sales processes or unequal territory assignments.'
    ],
    
    # Tools & Integration
    suggested_tracking_tools=[
        'Customer Relationship Management (CRM) software to track and analyze lead movement through the sales cycle.',
        'Sales enablement platforms to provide sales teams with the necessary tools and content to move leads through the cycle efficiently.',
        'Sales performance management platforms to monitor and assess the effectiveness of sales training and coaching programs.',
        'Business intelligence tools for in-depth analysis of cycle length trends and patterns.',
        'Data analytics platforms supporting multiple aggregation functions and time-based filtering.'
    ],
    integration_points=[
        'Integrate sales cycle length data with marketing automation systems to align lead generation efforts with the sales process.',
        'Link sales cycle length with customer relationship management systems to track the impact on customer lifetime value.',
        'Integrate with performance evaluations to identify correlations between training/coaching and sales outcomes.',
        'Link with customer feedback systems to understand the impact of sales effectiveness on customer satisfaction.',
        'Connect with forecasting models to improve revenue predictions based on cycle length trends.'
    ],
    
    # Impact
    change_impact="Shortening the sales cycle can lead to increased revenue, faster growth, and improved sales productivity, but may also require additional resources to handle increased sales volume. Lengthening the sales cycle may reduce immediate revenue but could result in higher quality customers and improved long-term retention. Overly aggressive efforts to shorten the cycle time may result in compromised customer relationships and decreased deal quality. Changes in cycle length patterns may indicate shifts in market dynamics, competitive landscape, or sales effectiveness.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "aggregation_methods": ["average", "median", "sum", "min", "max", "count", "percentile"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"],
        "dimensions": ["sales_rep", "product", "customer_segment", "deal_size", "region", "sales_stage"],
        "time_units": ["days", "weeks", "months"],
        "replaces": ["SALES_CYCLE_TIME"],
        "required_objects": ["Channel Deal", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Lead Qualification", "Lost Sale", "Market Segment", "Opportunity", "Partner Training", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
