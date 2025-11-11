"""
Emergency Procedure Testing Frequency

The frequency at which emergency procedures are tested, indicating the preparedness for potential supply chain disruptions.
"""

EMERGENCY_PROCEDURE_TESTING_FREQUENCY = {
    "code": "EMERGENCY_PROCEDURE_TESTING_FREQUENCY",
    "name": "Emergency Procedure Testing Frequency",
    "description": "The frequency at which emergency procedures are tested, indicating the preparedness for potential supply chain disruptions.",
    "formula": "Total Number of Emergency Tests and Drills / Time Period",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Emergency Procedure Testing Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.941684"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        303,
                        293,
                        307,
                        294,
                        298,
                        300,
                        292,
                        332,
                        321,
                        318,
                        307,
                        323
                ],
                "unit": "count"
        },
        "current": {
                "value": 323,
                "unit": "count",
                "change": 16,
                "change_percent": 5.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 307.33,
                "min": 292,
                "max": 332,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 97.97,
                        "percentage": 30.3
                },
                {
                        "category": "Segment B",
                        "value": 71.57,
                        "percentage": 22.2
                },
                {
                        "category": "Segment C",
                        "value": 50.98,
                        "percentage": 15.8
                },
                {
                        "category": "Segment D",
                        "value": 29.41,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 73.07,
                        "percentage": 22.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.955064",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Emergency Procedure Testing Frequency"
        }
    },
}
