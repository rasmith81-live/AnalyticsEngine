"""
Procurement Cost Savings

The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management. Reflects the direct financial impact of procurement activities and supports budget optimization.
"""

PROCUREMENT_COST_SAVINGS = {
    "code": "PROCUREMENT_COST_SAVINGS",
    "name": "Procurement Cost Savings",
    "description": "The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management. Reflects the direct financial impact of procurement activities and supports budget optimization.",
    "formula": "Baseline Spend - Current Spend",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement Cost Savings to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier", "PurchaseOrder", "Contract"], "last_validated": "2025-11-10T13:49:33.253037"},
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
                        26032.36,
                        22610.93,
                        17238.02,
                        17406.71,
                        22525.14,
                        24161.27,
                        23630.21,
                        17484.77,
                        24160.96,
                        18564.49,
                        24194.88,
                        25513.6
                ],
                "unit": "$"
        },
        "current": {
                "value": 25513.6,
                "unit": "$",
                "change": 1318.72,
                "change_percent": 5.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 21960.28,
                "min": 17238.02,
                "max": 26032.36,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 5891.76,
                        "percentage": 23.1
                },
                {
                        "category": "Category B",
                        "value": 5129.44,
                        "percentage": 20.1
                },
                {
                        "category": "Category C",
                        "value": 4325.85,
                        "percentage": 17.0
                },
                {
                        "category": "Category D",
                        "value": 2713.18,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 7453.37,
                        "percentage": 29.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.948854",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Procurement Cost Savings"
        }
    },
}
