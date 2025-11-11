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
                        17.6,
                        22.9,
                        23.0,
                        16.7,
                        20.6,
                        23.7,
                        24.2,
                        18.8,
                        18.5,
                        21.0,
                        22.3,
                        20.9
                ],
                "unit": "days"
        },
        "current": {
                "value": 20.9,
                "unit": "days",
                "change": -1.4,
                "change_percent": -6.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 20.85,
                "min": 16.7,
                "max": 24.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 7.02,
                        "percentage": 33.6
                },
                {
                        "category": "Segment B",
                        "value": 4.1,
                        "percentage": 19.6
                },
                {
                        "category": "Segment C",
                        "value": 2.54,
                        "percentage": 12.2
                },
                {
                        "category": "Segment D",
                        "value": 1.37,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 5.87,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.572029",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supplier Lead Time Variability"
        }
    },
}
