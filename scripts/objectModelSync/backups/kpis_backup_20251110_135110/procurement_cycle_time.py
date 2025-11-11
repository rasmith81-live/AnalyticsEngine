"""
Procurement Cycle Time

The time taken to complete the procurement process from requisition to purchase order and receiving the goods or services.
"""

PROCUREMENT_CYCLE_TIME = {
    "code": "PROCUREMENT_CYCLE_TIME",
    "name": "Procurement Cycle Time",
    "description": "The time taken to complete the procurement process from requisition to purchase order and receiving the goods or services.",
    "formula": "Time of Purchase Order Creation - Time of Requisition",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement Cycle Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.255702"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        30.6,
                        29.8,
                        33.3,
                        26.9,
                        31.7,
                        33.1,
                        28.3,
                        28.9,
                        26.2,
                        28.4,
                        28.0,
                        27.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 27.1,
                "unit": "days",
                "change": -0.9,
                "change_percent": -3.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 29.36,
                "min": 26.2,
                "max": 33.3,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.58,
                        "percentage": 28.0
                },
                {
                        "category": "Category B",
                        "value": 5.01,
                        "percentage": 18.5
                },
                {
                        "category": "Category C",
                        "value": 2.63,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 2.92,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 8.96,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.953613",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Procurement Cycle Time"
        }
    },
}
