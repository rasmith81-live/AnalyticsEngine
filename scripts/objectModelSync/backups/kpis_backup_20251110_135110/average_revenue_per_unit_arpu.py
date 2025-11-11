"""
Average Revenue per Unit (ARPU)

The average revenue generated per unit sold, which helps assess the value of a company's products or services.
"""

AVERAGE_REVENUE_PER_UNIT_ARPU = {
    "code": "AVERAGE_REVENUE_PER_UNIT_ARPU",
    "name": "Average Revenue per Unit (ARPU)",
    "description": "The average revenue generated per unit sold, which helps assess the value of a company's products or services.",
    "formula": "Total Revenue / Total Number of Units or Customers",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Revenue per Unit (ARPU) to be added.",
    "trend_analysis": "ARPU may increase over time as a result of product or service upgrades, pricing changes, or upselling strategies. A decreasing ARPU could indicate market saturation, increased competition, or a shift towards lower-priced offerings.",
    "diagnostic_questions": ["What factors have contributed to the recent trend in ARPU?", "Are there specific customer segments or product lines driving changes in ARPU?"],
    "actionable_tips": """

* Monitor this KPI regularly
* Set appropriate targets and thresholds
    
    """,
    "visualization_suggestions": """

* Line chart for time series analysis
* Bar chart for comparisons
    
    """,
    "risk_warnings": ["A declining ARPU may indicate a loss of competitive advantage or declining perceived value of products or services.", "Significant fluctuations in ARPU could signal instability in the market or customer base."],
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": ["Integrate ARPU tracking with sales and marketing systems to align efforts towards maximizing average revenue per unit.", "Link ARPU with customer feedback and satisfaction metrics to ensure that pricing strategies align with perceived value."],
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUS_DEV", "SALES_PERFORMANCE"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Quarterly Business Review", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.654926"},
    "required_objects": [],
    "modules": ["BUS_DEV", "SALES_PERFORMANCE"],
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
                        207,
                        208,
                        219,
                        219,
                        210,
                        215,
                        205,
                        225,
                        219,
                        220,
                        185,
                        213
                ],
                "unit": "count"
        },
        "current": {
                "value": 213,
                "unit": "count",
                "change": 28,
                "change_percent": 15.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 212.08,
                "min": 185,
                "max": 225,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 57.93,
                        "percentage": 27.2
                },
                {
                        "category": "Category B",
                        "value": 39.23,
                        "percentage": 18.4
                },
                {
                        "category": "Category C",
                        "value": 30.39,
                        "percentage": 14.3
                },
                {
                        "category": "Category D",
                        "value": 9.06,
                        "percentage": 4.3
                },
                {
                        "category": "Other",
                        "value": 76.39,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.034459",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Revenue per Unit (ARPU)"
        }
    },
}
