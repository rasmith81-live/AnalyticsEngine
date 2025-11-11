"""
Average Deal Discount

The average percentage discount applied to deals, which can reflect the sales team's negotiation skills and pricing strategy.
"""

AVERAGE_DEAL_DISCOUNT = {
    "code": "AVERAGE_DEAL_DISCOUNT",
    "name": "Average Deal Discount",
    "description": "The average percentage discount applied to deals, which can reflect the sales team's negotiation skills and pricing strategy.",
    "formula": "(Total Discounts Given / Number of Deals Closed) * 100",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Deal Discount to be added.",
    "trend_analysis": "An increasing average deal discount may indicate a need for better pricing strategies or a lack of negotiation skills among the sales team. A decreasing average deal discount could signal improved negotiation tactics or a shift towards value-based selling rather than discounting.",
    "diagnostic_questions": ["Are there specific products or customer segments that consistently receive higher discounts?", "How does our average deal discount compare with industry benchmarks or competitors' pricing strategies?"],
    "actionable_tips": """

* Monitor this KPI regularly
* Set appropriate targets and thresholds
    
    """,
    "visualization_suggestions": """

* Line chart for time series analysis
* Bar chart for comparisons
    
    """,
    "risk_warnings": ["Consistently high average deal discounts can erode profit margins and devalue the company's offerings in the market.", "Overly aggressive discounting may lead to customer expectations of perpetual discounts, impacting long-term revenue potential."],
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": ["Integrate average deal discount data with sales performance metrics to understand the relationship between discounting and revenue generation.", "Link discounting information with customer relationship management systems to track the impact of discounts on customer retention and satisfaction."],
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUS_DEV"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "required_objects": ["Channel Deal", "Deal", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.646181"},
    "required_objects": [],
    "modules": ["BUS_DEV"],
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
                        219,
                        210,
                        254,
                        210,
                        219,
                        218,
                        248,
                        220,
                        243,
                        247,
                        237,
                        242
                ],
                "unit": "count"
        },
        "current": {
                "value": 242,
                "unit": "count",
                "change": 5,
                "change_percent": 2.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 230.58,
                "min": 210,
                "max": 254,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 80.32,
                        "percentage": 33.2
                },
                {
                        "category": "Category B",
                        "value": 45.71,
                        "percentage": 18.9
                },
                {
                        "category": "Category C",
                        "value": 40.57,
                        "percentage": 16.8
                },
                {
                        "category": "Category D",
                        "value": 16.05,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 59.35,
                        "percentage": 24.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.018867",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Deal Discount"
        }
    },
}
