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
                        821.01,
                        748.34,
                        747.52,
                        760.26,
                        837.38,
                        725.98,
                        793.91,
                        703.46,
                        705.75,
                        757.8,
                        837.43,
                        777.33
                ],
                "unit": "units"
        },
        "current": {
                "value": 777.33,
                "unit": "units",
                "change": -60.1,
                "change_percent": -7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 768.01,
                "min": 703.46,
                "max": 837.43,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 133.66,
                        "percentage": 17.2
                },
                {
                        "category": "Segment B",
                        "value": 122.96,
                        "percentage": 15.8
                },
                {
                        "category": "Segment C",
                        "value": 137.23,
                        "percentage": 17.7
                },
                {
                        "category": "Segment D",
                        "value": 56.34,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 327.14,
                        "percentage": 42.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.495276",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Capacity Utilization"
        }
    },
}
