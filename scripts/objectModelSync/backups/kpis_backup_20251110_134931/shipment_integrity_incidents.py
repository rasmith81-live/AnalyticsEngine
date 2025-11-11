"""
Shipment Integrity Incidents

The number of incidents where a shipment
"""

SHIPMENT_INTEGRITY_INCIDENTS = {
    "code": "SHIPMENT_INTEGRITY_INCIDENTS",
    "name": "Shipment Integrity Incidents",
    "description": "The number of incidents where a shipment",
    "formula": "Total Number of Shipment Integrity Incidents",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Shipment Integrity Incidents to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:43:24.756612"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        160,
                        154,
                        182,
                        184,
                        169,
                        153,
                        182,
                        138,
                        160,
                        151,
                        184,
                        144
                ],
                "unit": "count"
        },
        "current": {
                "value": 144,
                "unit": "count",
                "change": -40,
                "change_percent": -21.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 163.42,
                "min": 138,
                "max": 184,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.37,
                        "percentage": 16.2
                },
                {
                        "category": "Category B",
                        "value": 19.07,
                        "percentage": 13.2
                },
                {
                        "category": "Category C",
                        "value": 34.32,
                        "percentage": 23.8
                },
                {
                        "category": "Category D",
                        "value": 12.88,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 54.36,
                        "percentage": 37.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.756101",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Shipment Integrity Incidents"
        }
    },
}
