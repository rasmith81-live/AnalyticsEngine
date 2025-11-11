"""
Appointments per Period

The number of appointments set by the Sales Development team per time period, supporting multiple time period filters (daily, weekly, monthly, quarterly, annually).
"""

APPOINTMENTS_PER_PERIOD = {
    "code": "APPOINTMENTS_PER_PERIOD",
    "name": "Appointments per Period",
    "description": "The number of appointments set by the Sales Development team per time period, supporting multiple time period filters (daily, weekly, monthly, quarterly, annually).",
    "formula": "Total Number of Appointments / Time Period. Aggregations: COUNT(appointments), AVG(appointments_per_rep), SUM(appointments)",
    "calculation_formula": "Base: Total Number of Appointments in Period. Per Rep: Total Appointments / Number of Reps. Rate: Appointments / Time Period",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Appointments per Period to be added.",
    "trend_analysis": """



    * Appointments per period may show an increasing trend if the sales development team is effectively targeting and engaging with potential leads.
    * A decreasing trend could indicate a need for improved lead generation strategies, decline in customer interest, or seasonal variations.
    * Variability across periods may reflect campaign effectiveness, market conditions, or team capacity.
    * Day-of-week or time-of-year patterns may emerge when analyzing by shorter time periods.
    
    
    
    """,
    "diagnostic_questions": ["Are there specific industries or segments that are responding more positively to our appointment setting efforts?", "How do our appointment numbers compare to industry benchmarks or seasonal variations?", "What is the distribution of appointments across sales reps (are some significantly more productive)?", "Are there patterns by day of week, time of month, or season?", "How does appointment volume correlate with lead quality and conversion rates?", "What is the optimal appointment volume per rep to maintain quality?"],
    "actionable_tips": ["Implement targeted outreach campaigns to specific industries or customer segments that have shown higher appointment conversion rates.", "Provide additional training and resources to the sales development team to improve their lead generation and appointment setting skills.", "Utilize customer relationship management (CRM) software to track and follow up on appointments more effectively.", "Analyze patterns to optimize outreach timing and frequency.", "Set realistic targets based on historical performance and seasonality."],
    "visualization_suggestions": [{"type": "line_chart", "description": "Track appointment trends over time (daily, weekly, monthly, quarterly) to identify patterns and seasonality."}, {"type": "bar_chart", "description": "Compare appointment numbers across different sales development team members or territories."}, {"type": "heatmap", "description": "Show appointment patterns by day of week and time of day."}, {"type": "histogram", "description": "Display distribution of appointments per rep to identify outliers."}, {"type": "area_chart", "description": "Show cumulative appointments over time with period comparisons."}],
    "risk_warnings": ["A consistently low number of appointments per period may lead to missed sales opportunities and revenue loss.", "An excessively high number of appointments without corresponding sales conversions could indicate a need for better lead qualification processes.", "High variance in appointments across reps may indicate training needs or territory imbalances.", "Focusing solely on appointment quantity without considering quality can lead to inefficiencies and wasted resources."],
    "tracking_tools": ["CRM systems like Salesforce or HubSpot for tracking and managing appointment setting activities.", "Sales engagement platforms such as Outreach or SalesLoft to streamline outreach and follow-up processes.", "Business intelligence tools for analyzing appointment trends across multiple time periods.", "Calendar and scheduling tools integrated with CRM for accurate appointment tracking."],
    "integration_points": ["Integrate appointment setting data with sales performance metrics to analyze the effectiveness of appointments in driving actual sales.", "Link appointment data with marketing campaign results to understand the impact of marketing efforts on appointment generation.", "Connect with lead scoring systems to correlate appointment volume with lead quality.", "Integrate with forecasting models to predict pipeline based on appointment trends."],
    "change_impact_analysis": """



    * Improving appointment numbers can lead to increased sales opportunities and revenue growth.
    * However, a focus solely on increasing appointments without considering their quality can lead to inefficiencies and wasted resources.
    * Changes in appointment patterns may indicate shifts in market dynamics, campaign effectiveness, or team productivity.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"], "aggregation_methods": ["count", "sum", "average_per_rep"], "dimensions": ["sales_rep", "territory", "lead_source", "industry", "campaign"], "replaces": ["APPOINTMENTS_PER_MONTH"], "required_objects": ["Appointment", "Competitive Analysis", "Deal", "Knowledge Base", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Territory Assignment"], "last_validated": "2025-11-10T13:49:32.645123"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        272,
                        259,
                        292,
                        297,
                        274,
                        268,
                        261,
                        288,
                        290,
                        275,
                        255,
                        263
                ],
                "unit": "count"
        },
        "current": {
                "value": 263,
                "unit": "count",
                "change": 8,
                "change_percent": 3.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 274.5,
                "min": 255,
                "max": 297,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 73.28,
                        "percentage": 27.9
                },
                {
                        "category": "Segment B",
                        "value": 60.7,
                        "percentage": 23.1
                },
                {
                        "category": "Segment C",
                        "value": 21.82,
                        "percentage": 8.3
                },
                {
                        "category": "Segment D",
                        "value": 11.78,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 95.42,
                        "percentage": 36.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.363463",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Appointments per Period"
        }
    },
}
