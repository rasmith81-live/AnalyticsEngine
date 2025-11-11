"""
Equipment Utilization Rate

The percentage of time warehouse equipment is used compared to its availability.
"""

EQUIPMENT_UTILIZATION_RATE = {
    "code": "EQUIPMENT_UTILIZATION_RATE",
    "name": "Equipment Utilization Rate",
    "description": "The percentage of time warehouse equipment is used compared to its availability.",
    "formula": "Total Operating Time of Equipment / Total Available Time",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Equipment Utilization Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:49:32.947024"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        73.07,
                        68.67,
                        69.33,
                        76.01,
                        77.63,
                        74.96,
                        59.01,
                        57.81,
                        77.57,
                        74.26,
                        62.96,
                        63.31
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.31,
                "unit": "%",
                "change": 0.35,
                "change_percent": 0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.55,
                "min": 57.81,
                "max": 77.63,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.06,
                        "percentage": 33.3
                },
                {
                        "category": "Segment B",
                        "value": 14.63,
                        "percentage": 23.1
                },
                {
                        "category": "Segment C",
                        "value": 4.62,
                        "percentage": 7.3
                },
                {
                        "category": "Segment D",
                        "value": 5.5,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 17.5,
                        "percentage": 27.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.969550",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Equipment Utilization Rate"
        }
    },
}
