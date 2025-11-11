"""
Supplier Capacity Utilization

The extent to which suppliers
"""

SUPPLIER_CAPACITY_UTILIZATION = {
    "code": "SUPPLIER_CAPACITY_UTILIZATION",
    "name": "Supplier Capacity Utilization",
    "description": "The extent to which suppliers",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Capacity Utilization to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Lead", "Product", "PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.616984"},
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
                        437.41,
                        313.13,
                        340.65,
                        410.61,
                        350.37,
                        382.0,
                        398.76,
                        371.42,
                        339.9,
                        403.95,
                        396.83,
                        400.03
                ],
                "unit": "units"
        },
        "current": {
                "value": 400.03,
                "unit": "units",
                "change": 3.2,
                "change_percent": 0.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 378.76,
                "min": 313.13,
                "max": 437.41,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 83.34,
                        "percentage": 20.8
                },
                {
                        "category": "Category B",
                        "value": 56.54,
                        "percentage": 14.1
                },
                {
                        "category": "Category C",
                        "value": 55.05,
                        "percentage": 13.8
                },
                {
                        "category": "Category D",
                        "value": 49.25,
                        "percentage": 12.3
                },
                {
                        "category": "Other",
                        "value": 155.85,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.833934",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Capacity Utilization"
        }
    },
}
