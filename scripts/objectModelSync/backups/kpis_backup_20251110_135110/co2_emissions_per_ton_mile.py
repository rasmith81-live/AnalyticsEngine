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
                        729.39,
                        638.77,
                        714.12,
                        610.4,
                        628.41,
                        660.47,
                        704.71,
                        739.9,
                        684.12,
                        752.12,
                        748.97,
                        715.94
                ],
                "unit": "units"
        },
        "current": {
                "value": 715.94,
                "unit": "units",
                "change": -33.03,
                "change_percent": -4.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 693.94,
                "min": 610.4,
                "max": 752.12,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 239.78,
                        "percentage": 33.5
                },
                {
                        "category": "Category B",
                        "value": 118.32,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 100.48,
                        "percentage": 14.0
                },
                {
                        "category": "Category D",
                        "value": 38.36,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 219.0,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.117738",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "CO2 Emissions per Ton-Mile"
        }
    },
}
