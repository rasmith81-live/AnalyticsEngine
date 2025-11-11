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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:33.568404"},
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
                        397,
                        380,
                        398,
                        397,
                        393,
                        396,
                        392,
                        394,
                        360,
                        368,
                        386,
                        386
                ],
                "unit": "count"
        },
        "current": {
                "value": 386,
                "unit": "count",
                "change": 0,
                "change_percent": 0.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 387.25,
                "min": 360,
                "max": 398,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 128.77,
                        "percentage": 33.4
                },
                {
                        "category": "Segment B",
                        "value": 45.31,
                        "percentage": 11.7
                },
                {
                        "category": "Segment C",
                        "value": 42.55,
                        "percentage": 11.0
                },
                {
                        "category": "Segment D",
                        "value": 41.47,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 127.9,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.369082",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Shipment Integrity Incidents"
        }
    },
}
