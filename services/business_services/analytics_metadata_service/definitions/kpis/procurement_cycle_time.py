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
                        25.8,
                        26.7,
                        22.3,
                        24.6,
                        25.8,
                        23.6,
                        25.1,
                        22.0,
                        21.1,
                        23.3,
                        23.7,
                        19.8
                ],
                "unit": "days"
        },
        "current": {
                "value": 19.8,
                "unit": "days",
                "change": -3.9,
                "change_percent": -16.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 23.65,
                "min": 19.8,
                "max": 26.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 5.97,
                        "percentage": 30.2
                },
                {
                        "category": "Segment B",
                        "value": 4.4,
                        "percentage": 22.2
                },
                {
                        "category": "Segment C",
                        "value": 3.23,
                        "percentage": 16.3
                },
                {
                        "category": "Segment D",
                        "value": 1.76,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 4.44,
                        "percentage": 22.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.603760",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Procurement Cycle Time"
        }
    },
}
