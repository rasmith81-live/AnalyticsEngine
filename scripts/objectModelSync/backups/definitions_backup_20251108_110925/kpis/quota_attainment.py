"""
Quota Attainment KPI

The percentage of sales quota achieved by sales representatives or teams.
Can be aggregated using various arithmetic functions and filtered by time period.
"""

from analytics_models import KPI

QUOTA_ATTAINMENT = KPI(
    name="Quota Attainment",
    code="QUOTA_ATTAINMENT",
    category="Business Development",
    
    # Core Definition
    description="The percentage of sales quota achieved by sales representatives or teams, supporting multiple aggregation methods (average, median, min, max, count) and time period filters.",
    kpi_definition="The percentage of sales quota achieved by sales representatives or teams. This metric can be aggregated using various arithmetic functions (average, median, min, max, count) and filtered by time period (daily, weekly, monthly, quarterly, annually) to provide flexible analysis of sales performance against targets. Can measure individual rep attainment or percentage of reps meeting quota.",
    expected_business_insights="Evaluates sales performance and effectiveness of sales targets. Indicates the effectiveness of the sales team and can impact sales strategy, incentive programs, and resource allocation. Helps identify high performers, underperformers, and areas needing support or training.",
    measurement_approach="Measures the percentage of sales quota achieved. Can be calculated as: (1) Individual/team achievement: (Actual Sales / Quota) × 100, or (2) Team success rate: (Number of Reps Meeting Quota / Total Reps) × 100. Supports filtering by time period, territory, product line, sales representative, and other dimensions.",
    
    # Formula
    formula="Individual/Team: (Total Sales Achieved / Sales Quota) × 100. Success Rate: (Number of Reps Meeting or Exceeding Quota / Total Number of Reps) × 100. Aggregations: AVG(quota_attainment), MEDIAN(quota_attainment), MIN(quota_attainment), MAX(quota_attainment)",
    calculation_formula="Base: (Actual Sales / Sales Quota) × 100. Alternative: (Reps Meeting Quota / Total Reps) × 100. Common aggregations: Average across team, Median attainment, Min/Max performers",
    
    # Analysis
    trend_analysis="""
    * Consistently increasing quota attainment may indicate improved sales strategies, market conditions, or effective training programs.
    * A decreasing trend could signal need for sales process optimization, changes in target setting, increased competition, or ineffective sales management.
    * Variability in quota attainment may reflect diverse territories, product lines, or experience levels.
    * Seasonal patterns may emerge when analyzing by time period.
    * High quota attainment without corresponding revenue growth could signal overly conservative quotas or discounting practices.
    """,
    diagnostic_questions=[
        'Are there specific regions, territories, or product lines where quota attainment is consistently low?',
        'How does the quota attainment of new sales representatives compare to more experienced ones?',
        'How does our quota attainment compare with industry benchmarks or historical performance?',
        'What is the distribution of quota attainment (are most reps clustered around the average or widely dispersed)?',
        'Are quotas aligned with market conditions and individual sales territories?',
        'Which factors correlate most strongly with high quota attainment?'
    ],
    actionable_steps={
        "operational": [
            'Provide additional training and support for sales representatives who consistently fall short of their quotas.',
            'Regularly review and adjust sales targets to align with market conditions and business goals.',
            'Implement a mentorship program to pair high-performing sales representatives with those struggling to meet their quotas.',
            'Monitor quota attainment in real-time to provide timely coaching and support.'
        ],
        "strategic": [
            'Adjust quotas to better align with market conditions and individual sales territories.',
            'Implement a more robust sales incentive program to motivate representatives to exceed their quotas.',
            'Analyze quota attainment patterns to identify best practices and replicate success.',
            'Invest in sales enablement tools and resources to help reps meet their targets.',
            'Review quota-setting methodology to ensure targets are challenging but achievable.'
        ]
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "line_chart", "description": "Track quota attainment over time (daily, weekly, monthly, quarterly) for individuals or teams with multiple aggregation methods."},
        {"type": "histogram", "description": "Show distribution of quota attainment to identify patterns and outliers."},
        {"type": "box_plot", "description": "Display quota attainment distribution with quartiles, median, and outliers."},
        {"type": "bar_chart", "description": "Compare quota attainment by sales representative, territory, or product line."},
        {"type": "pie_chart", "description": "Show percentage of reps meeting, exceeding, or missing quota."},
        {"type": "heatmap", "description": "Show quota attainment patterns across time periods and dimensions (e.g., month vs. territory)."},
        {"type": "waterfall_chart", "description": "Visualize individual rep contributions to overall team quota attainment."}
    ],
    risk_warnings=[
        'Consistently low quota attainment may lead to decreased revenue, missed business opportunities, and impact team morale.',
        'High quota attainment without proper support or resources may lead to burnout and decreased job satisfaction among sales representatives.',
        'Consistently low quota attainment rates may indicate issues with sales team performance, market demand, or unrealistic quota setting.',
        'High quota attainment rates without corresponding revenue growth could signal overly conservative quotas or aggressive discounting.',
        'Wide variance in quota attainment may indicate inconsistent sales processes or unequal territory assignments.'
    ],
    
    # Tools & Integration
    suggested_tracking_tools=[
        'Customer Relationship Management (CRM) software to track individual sales performance and identify areas for improvement.',
        'Sales enablement platforms to provide sales representatives with the necessary tools and resources to meet their quotas.',
        'Sales performance management software to track and analyze individual and team quota attainment.',
        'Business intelligence tools for in-depth analysis of quota attainment trends and patterns.',
        'Data analytics platforms supporting multiple aggregation functions and time-based filtering.'
    ],
    integration_points=[
        'Integrate quota attainment data with performance management systems to align individual goals with overall business objectives.',
        'Link quota attainment with incentive and compensation systems to reward high performers and provide additional support to those struggling to meet their targets.',
        'Integrate with sales forecasting to better align quotas with expected market demand.',
        'Connect with training and coaching systems to identify development needs.',
        'Link to territory management systems to optimize territory assignments and quotas.'
    ],
    
    # Impact
    change_impact="Improving quota attainment can lead to increased revenue, market share, and customer satisfaction, but may also require additional resources, support, and training for the sales team. Conversely, consistently low quota attainment can impact overall company performance, team morale, employee retention, and customer satisfaction. Changes in quota attainment patterns may indicate shifts in market conditions, competitive landscape, or sales effectiveness.",
    
    # Metadata
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_DEVELOPMENT", "SALES_STRATEGY", "SALES_ENABLEMENT", "SALES_OPERATIONS"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "aggregation_methods": ["average", "median", "sum", "min", "max", "count"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"],
        "dimensions": ["sales_rep", "team", "territory", "product_line", "region", "customer_segment"],
        "calculation_types": ["individual_attainment", "team_success_rate"],
        "replaces": ["QUOTA_ATTAINMENT_RATE"],
        "required_objects": ["Competitive Analysis", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Meeting", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Quota Plan", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Territory Assignment"]
    }
)
