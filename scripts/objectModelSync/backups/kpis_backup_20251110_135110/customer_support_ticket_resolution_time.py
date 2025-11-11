"""
Customer Support Ticket Resolution Time

The average time it takes for the sales or support team to resolve customer issues or support tickets.
"""

CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME = {
    "code": "CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME",
    "name": "Customer Support Ticket Resolution Time",
    "description": "The average time it takes for the sales or support team to resolve customer issues or support tickets.",
    "formula": "Total Time Taken to Resolve Tickets / Number of Tickets Resolved",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Support Ticket Resolution Time to be added.",
    "trend_analysis": "Trend analysis to be defined.",
    "diagnostic_questions": """

* What factors are influencing this metric?
* Are there any anomalies in the data?
    
    """,
    "actionable_tips": """

* Monitor this KPI regularly
* Set appropriate targets and thresholds
    
    """,
    "visualization_suggestions": """

* Line chart for time series analysis
* Bar chart for comparisons
    
    """,
    "risk_warnings": "* Monitor for significant deviations from expected values",
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": "* Integrate with related business metrics",
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "PurchaseOrder", "SupportTicket"], "last_validated": "2025-11-10T13:49:32.892751"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        268,
                        254,
                        245,
                        252,
                        241,
                        230,
                        259,
                        237,
                        230,
                        264,
                        272,
                        234
                ],
                "unit": "count"
        },
        "current": {
                "value": 234,
                "unit": "count",
                "change": -38,
                "change_percent": -14.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 248.83,
                "min": 230,
                "max": 272,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 49.28,
                        "percentage": 21.1
                },
                {
                        "category": "Category B",
                        "value": 32.73,
                        "percentage": 14.0
                },
                {
                        "category": "Category C",
                        "value": 41.39,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 14.78,
                        "percentage": 6.3
                },
                {
                        "category": "Other",
                        "value": 95.82,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.381702",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Support Ticket Resolution Time"
        }
    },
}
