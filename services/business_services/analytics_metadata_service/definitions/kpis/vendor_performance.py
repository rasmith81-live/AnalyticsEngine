"""
Vendor Performance

The overall performance of the company
"""

VENDOR_PERFORMANCE = {
    "code": "VENDOR_PERFORMANCE",
    "name": "Vendor Performance",
    "description": "The overall performance of the company",
    "formula": "Qualitative and Quantitative Score based on Predefined Performance Criteria",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Vendor Performance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Delivery", "Product", "PurchaseOrder", "QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:49:33.784357"},
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
                        520.07,
                        497.35,
                        471.97,
                        505.25,
                        458.4,
                        495.64,
                        495.1,
                        462.24,
                        518.99,
                        525.38,
                        475.68,
                        473.89
                ],
                "unit": "units"
        },
        "current": {
                "value": 473.89,
                "unit": "units",
                "change": -1.79,
                "change_percent": -0.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 491.66,
                "min": 458.4,
                "max": 525.38,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 140.33,
                        "percentage": 29.6
                },
                {
                        "category": "Segment B",
                        "value": 89.13,
                        "percentage": 18.8
                },
                {
                        "category": "Segment C",
                        "value": 84.24,
                        "percentage": 17.8
                },
                {
                        "category": "Segment D",
                        "value": 42.41,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 117.78,
                        "percentage": 24.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.944453",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Vendor Performance"
        }
    },
}
