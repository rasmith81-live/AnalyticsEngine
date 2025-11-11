"""
CO2 Emissions per Ton-Mile

The amount of CO2 emitted for transporting one ton of material over one mile.
"""

CO2_EMISSIONS_PER_TON_MILE = {
    "code": "CO2_EMISSIONS_PER_TON_MILE",
    "name": "CO2 Emissions per Ton-Mile",
    "description": "The amount of CO2 emitted for transporting one ton of material over one mile.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for CO2 Emissions per Ton-Mile to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:32.700088"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        941.55,
                        958.24,
                        944.18,
                        894.93,
                        918.12,
                        928.53,
                        893.93,
                        868.15,
                        900.15,
                        887.02,
                        840.18,
                        962.11
                ],
                "unit": "units"
        },
        "current": {
                "value": 962.11,
                "unit": "units",
                "change": 121.93,
                "change_percent": 14.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 911.42,
                "min": 840.18,
                "max": 962.11,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 283.18,
                        "percentage": 29.4
                },
                {
                        "category": "Segment B",
                        "value": 174.0,
                        "percentage": 18.1
                },
                {
                        "category": "Segment C",
                        "value": 78.97,
                        "percentage": 8.2
                },
                {
                        "category": "Segment D",
                        "value": 108.31,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 317.65,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.479748",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "CO2 Emissions per Ton-Mile"
        }
    },
}
