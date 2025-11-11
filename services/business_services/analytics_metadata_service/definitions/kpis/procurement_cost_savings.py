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
                        13075.5,
                        18491.15,
                        9861.92,
                        23859.62,
                        22528.6,
                        23027.2,
                        20851.27,
                        19281.63,
                        17938.09,
                        23604.05,
                        12740.21,
                        10979.4
                ],
                "unit": "$"
        },
        "current": {
                "value": 10979.4,
                "unit": "$",
                "change": -1760.81,
                "change_percent": -13.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 18019.89,
                "min": 9861.92,
                "max": 23859.62,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 3768.69,
                        "percentage": 34.3
                },
                {
                        "category": "Segment B",
                        "value": 1952.27,
                        "percentage": 17.8
                },
                {
                        "category": "Segment C",
                        "value": 830.52,
                        "percentage": 7.6
                },
                {
                        "category": "Segment D",
                        "value": 585.97,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 3841.95,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.595499",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Procurement Cost Savings"
        }
    },
}
