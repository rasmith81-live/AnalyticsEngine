"""
Contract Renewal Rate

The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the
"""

CONTRACT_RENEWAL_RATE = {
    "code": "CONTRACT_RENEWAL_RATE",
    "name": "Contract Renewal Rate",
    "description": "The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the",
    "formula": "(Number of Contracts Renewed / Number of Contracts Up for Renewal) * 100",
    "calculation_formula": "(Number of Contracts Renewed / Number of Contracts Up for Renewal) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Contract Renewal Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Contract", "Customer"], "last_validated": "2025-11-10T13:49:32.716316"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        64.2,
                        82.61,
                        67.35,
                        67.67,
                        80.13,
                        68.95,
                        76.69,
                        67.81,
                        72.51,
                        75.82,
                        65.58,
                        80.86
                ],
                "unit": "%"
        },
        "current": {
                "value": 80.86,
                "unit": "%",
                "change": 15.28,
                "change_percent": 23.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.52,
                "min": 64.2,
                "max": 82.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.23,
                        "percentage": 17.6
                },
                {
                        "category": "Segment B",
                        "value": 15.58,
                        "percentage": 19.3
                },
                {
                        "category": "Segment C",
                        "value": 9.88,
                        "percentage": 12.2
                },
                {
                        "category": "Segment D",
                        "value": 5.03,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 36.14,
                        "percentage": 44.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.511220",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Contract Renewal Rate"
        }
    },
}
