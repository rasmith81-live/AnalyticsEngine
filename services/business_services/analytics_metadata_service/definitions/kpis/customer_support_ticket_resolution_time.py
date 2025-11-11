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
                        318,
                        312,
                        335,
                        313,
                        314,
                        307,
                        341,
                        319,
                        339,
                        322,
                        306,
                        309
                ],
                "unit": "count"
        },
        "current": {
                "value": 309,
                "unit": "count",
                "change": 3,
                "change_percent": 1.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 319.58,
                "min": 306,
                "max": 341,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 55.47,
                        "percentage": 18.0
                },
                {
                        "category": "Existing Customers",
                        "value": 59.8,
                        "percentage": 19.4
                },
                {
                        "category": "VIP Customers",
                        "value": 33.92,
                        "percentage": 11.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 34.26,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 125.55,
                        "percentage": 40.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.844289",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Support Ticket Resolution Time"
        }
    },
}
