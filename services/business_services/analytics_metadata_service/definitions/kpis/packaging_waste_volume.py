"""
Packaging Waste Volume

The total volume of waste generated from packaging materials, highlighting opportunities for waste reduction and recycling.
"""

PACKAGING_WASTE_VOLUME = {
    "code": "PACKAGING_WASTE_VOLUME",
    "name": "Packaging Waste Volume",
    "description": "The total volume of waste generated from packaging materials, highlighting opportunities for waste reduction and recycling.",
    "formula": "Total Waste Volume / Total Packaging Units",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Waste Volume to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.149325"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        497.38,
                        482.69,
                        469.49,
                        427.76,
                        549.93,
                        485.41,
                        529.33,
                        485.53,
                        416.3,
                        472.53,
                        543.91,
                        543.13
                ],
                "unit": "units"
        },
        "current": {
                "value": 543.13,
                "unit": "units",
                "change": -0.78,
                "change_percent": -0.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 491.95,
                "min": 416.3,
                "max": 549.93,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 145.79,
                        "percentage": 26.8
                },
                {
                        "category": "Segment B",
                        "value": 124.93,
                        "percentage": 23.0
                },
                {
                        "category": "Segment C",
                        "value": 72.09,
                        "percentage": 13.3
                },
                {
                        "category": "Segment D",
                        "value": 24.76,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 175.56,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.381751",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packaging Waste Volume"
        }
    },
}
