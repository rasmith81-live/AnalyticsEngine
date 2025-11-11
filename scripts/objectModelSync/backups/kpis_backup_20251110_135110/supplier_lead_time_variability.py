"""
Supplier Lead Time Variability

The consistency of supplier lead times over a period, with lower variability indicating more reliable delivery schedules.
"""

SUPPLIER_LEAD_TIME_VARIABILITY = {
    "code": "SUPPLIER_LEAD_TIME_VARIABILITY",
    "name": "Supplier Lead Time Variability",
    "description": "The consistency of supplier lead times over a period, with lower variability indicating more reliable delivery schedules.",
    "formula": "Standard Deviation of Supplier Lead Time",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Lead Time Variability to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Delivery", "Lead", "Supplier"], "last_validated": "2025-11-10T13:49:33.640403"},
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
                        23.5,
                        24.6,
                        19.5,
                        22.1,
                        25.0,
                        20.2,
                        21.5,
                        24.1,
                        25.8,
                        25.3,
                        20.9,
                        19.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 19.5,
                "unit": "days",
                "change": -1.4,
                "change_percent": -6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 22.67,
                "min": 19.5,
                "max": 25.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 6.08,
                        "percentage": 31.2
                },
                {
                        "category": "Category B",
                        "value": 4.37,
                        "percentage": 22.4
                },
                {
                        "category": "Category C",
                        "value": 3.15,
                        "percentage": 16.2
                },
                {
                        "category": "Category D",
                        "value": 1.59,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 4.31,
                        "percentage": 22.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.870496",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supplier Lead Time Variability"
        }
    },
}
