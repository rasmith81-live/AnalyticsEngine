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
                        274.8,
                        233.42,
                        186.49,
                        260.94,
                        181.58,
                        263.69,
                        210.72,
                        215.84,
                        179.92,
                        260.28,
                        240.96,
                        259.98
                ],
                "unit": "units"
        },
        "current": {
                "value": 259.98,
                "unit": "units",
                "change": 19.02,
                "change_percent": 7.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 230.72,
                "min": 179.92,
                "max": 274.8,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 90.6,
                        "percentage": 34.8
                },
                {
                        "category": "Category B",
                        "value": 35.93,
                        "percentage": 13.8
                },
                {
                        "category": "Category C",
                        "value": 31.42,
                        "percentage": 12.1
                },
                {
                        "category": "Category D",
                        "value": 27.03,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 75.0,
                        "percentage": 28.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.217493",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Vendor Performance"
        }
    },
}
