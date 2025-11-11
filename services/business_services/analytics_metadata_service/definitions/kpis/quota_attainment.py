"""
Quota Attainment

The percentage of sales quota achieved by sales representatives or teams, supporting multiple aggregation methods (average, median, min, max, count) and time period filters.
"""

QUOTA_ATTAINMENT = {
    "code": "QUOTA_ATTAINMENT",
    "name": "Quota Attainment",
    "description": "The percentage of sales quota achieved by sales representatives or teams, supporting multiple aggregation methods (average, median, min, max, count) and time period filters.",
    "formula": "Individual/Team: (Total Sales Achieved / Sales Quota) \u00d7 100. Success Rate: (Number of Reps Meeting or Exceeding Quota / Total Number of Reps) \u00d7 100. Aggregations: AVG(quota_attainment), MEDIAN(quota_attainment), MIN(quota_attainment), MAX(quota_attainment)",
    "calculation_formula": "Base: (Actual Sales / Sales Quota) \u00d7 100. Alternative: (Reps Meeting Quota / Total Reps) \u00d7 100. Common aggregations: Average across team, Median attainment, Min/Max performers",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Quota Attainment to be added.",
    "trend_analysis": """



    * Consistently increasing quota attainment may indicate improved sales strategies, market conditions, or effective training programs.
    * A decreasing trend could signal need for sales process optimization, changes in target setting, increased competition, or ineffective sales management.
    * Variability in quota attainment may reflect diverse territories, product lines, or experience levels.
    * Seasonal patterns may emerge when analyzing by time period.
    * High quota attainment without corresponding revenue growth could signal overly conservative quotas or discounting practices.
    
    
    
    """,
    "diagnostic_questions": ["Are there specific regions, territories, or product lines where quota attainment is consistently low?", "How does the quota attainment of new sales representatives compare to more experienced ones?", "How does our quota attainment compare with industry benchmarks or historical performance?", "What is the distribution of quota attainment (are most reps clustered around the average or widely dispersed)?", "Are quotas aligned with market conditions and individual sales territories?", "Which factors correlate most strongly with high quota attainment?"],
    "actionable_tips": """


* Monitor this KPI regularly
* Set appropriate targets and thresholds
    
    
    """,
    "visualization_suggestions": [{"type": "line_chart", "description": "Track quota attainment over time (daily, weekly, monthly, quarterly) for individuals or teams with multiple aggregation methods."}, {"type": "histogram", "description": "Show distribution of quota attainment to identify patterns and outliers."}, {"type": "box_plot", "description": "Display quota attainment distribution with quartiles, median, and outliers."}, {"type": "bar_chart", "description": "Compare quota attainment by sales representative, territory, or product line."}, {"type": "pie_chart", "description": "Show percentage of reps meeting, exceeding, or missing quota."}, {"type": "heatmap", "description": "Show quota attainment patterns across time periods and dimensions (e.g., month vs. territory)."}, {"type": "waterfall_chart", "description": "Visualize individual rep contributions to overall team quota attainment."}],
    "risk_warnings": ["Consistently low quota attainment may lead to decreased revenue, missed business opportunities, and impact team morale.", "High quota attainment without proper support or resources may lead to burnout and decreased job satisfaction among sales representatives.", "Consistently low quota attainment rates may indicate issues with sales team performance, market demand, or unrealistic quota setting.", "High quota attainment rates without corresponding revenue growth could signal overly conservative quotas or aggressive discounting.", "Wide variance in quota attainment may indicate inconsistent sales processes or unequal territory assignments."],
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": ["Integrate quota attainment data with performance management systems to align individual goals with overall business objectives.", "Link quota attainment with incentive and compensation systems to reward high performers and provide additional support to those struggling to meet their targets.", "Integrate with sales forecasting to better align quotas with expected market demand.", "Connect with training and coaching systems to identify development needs.", "Link to territory management systems to optimize territory assignments and quotas."],
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUS_DEV", "SALES_DEVELOPMENT", "SALES_STRATEGY", "SALES_ENABLEMENT", "SALES_OPERATIONS"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "aggregation_methods": ["average", "median", "sum", "min", "max", "count"], "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"], "dimensions": ["sales_rep", "team", "territory", "product_line", "region", "customer_segment"], "calculation_types": ["individual_attainment", "team_success_rate"], "replaces": ["QUOTA_ATTAINMENT_RATE"], "required_objects": ["Competitive Analysis", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Meeting", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Quota Plan", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Territory Assignment"], "last_validated": "2025-11-10T13:49:33.312638"},
    "required_objects": [],
    "modules": ["BUS_DEV", "SALES_DEVELOPMENT", "SALES_STRATEGY", "SALES_ENABLEMENT", "SALES_OPERATIONS"],
    "module_code": "BUS_DEV",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        54.55,
                        58.75,
                        58.0,
                        59.93,
                        53.57,
                        60.13,
                        70.97,
                        66.27,
                        68.17,
                        71.73,
                        72.53,
                        61.82
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.82,
                "unit": "%",
                "change": -10.71,
                "change_percent": -14.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.03,
                "min": 53.57,
                "max": 72.53,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 10.78,
                        "percentage": 17.4
                },
                {
                        "category": "Channel Sales",
                        "value": 14.99,
                        "percentage": 24.2
                },
                {
                        "category": "Online Sales",
                        "value": 7.66,
                        "percentage": 12.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.61,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 22.78,
                        "percentage": 36.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.734762",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Quota Attainment"
        }
    },
}
