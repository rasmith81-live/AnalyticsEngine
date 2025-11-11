"""
Buyer Efficiency

The number of purchase orders processed per buyer, indicating the efficiency of the
"""

BUYER_EFFICIENCY = {
    "code": "BUYER_EFFICIENCY",
    "name": "Buyer Efficiency",
    "description": "The number of purchase orders processed per buyer, indicating the efficiency of the",
    "formula": "Total Orders Processed or Cost Savings / Number of Buyers",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Buyer Efficiency to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Employee", "Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.670304"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        342,
                        341,
                        333,
                        352,
                        341,
                        321,
                        314,
                        358,
                        326,
                        355,
                        330,
                        332
                ],
                "unit": "count"
        },
        "current": {
                "value": 332,
                "unit": "count",
                "change": 2,
                "change_percent": 0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 337.08,
                "min": 314,
                "max": 358,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 99.71,
                        "percentage": 30.0
                },
                {
                        "category": "Segment B",
                        "value": 55.2,
                        "percentage": 16.6
                },
                {
                        "category": "Segment C",
                        "value": 44.05,
                        "percentage": 13.3
                },
                {
                        "category": "Segment D",
                        "value": 30.74,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 102.3,
                        "percentage": 30.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.409713",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Buyer Efficiency"
        }
    },
}
