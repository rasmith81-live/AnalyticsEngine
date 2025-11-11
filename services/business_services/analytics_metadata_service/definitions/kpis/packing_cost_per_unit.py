"""
Packing Cost per Unit

The average cost incurred to pack a single unit, helping to assess cost-efficiency in packing operations.
"""

PACKING_COST_PER_UNIT = {
    "code": "PACKING_COST_PER_UNIT",
    "name": "Packing Cost per Unit",
    "description": "The average cost incurred to pack a single unit, helping to assess cost-efficiency in packing operations.",
    "formula": "Total Packing Costs / Total Units Packed",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Cost per Unit to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.151458"},
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
                        58812.4,
                        46011.49,
                        55627.54,
                        51894.16,
                        54794.98,
                        58018.03,
                        53319.44,
                        55868.67,
                        57535.76,
                        58423.4,
                        55033.48,
                        56082.51
                ],
                "unit": "$"
        },
        "current": {
                "value": 56082.51,
                "unit": "$",
                "change": 1049.03,
                "change_percent": 1.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 55118.49,
                "min": 46011.49,
                "max": 58812.4,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12295.55,
                        "percentage": 21.9
                },
                {
                        "category": "Segment B",
                        "value": 8292.44,
                        "percentage": 14.8
                },
                {
                        "category": "Segment C",
                        "value": 7473.49,
                        "percentage": 13.3
                },
                {
                        "category": "Segment D",
                        "value": 7554.13,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 20466.9,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.381751",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Packing Cost per Unit"
        }
    },
}
