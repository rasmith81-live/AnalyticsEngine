"""
Product Quality Score

A measure of customer perceptions of product quality, often collected through customer surveys or feedback mechanisms.
"""

PRODUCT_QUALITY_SCORE = {
    "code": "PRODUCT_QUALITY_SCORE",
    "name": "Product Quality Score",
    "description": "A measure of customer perceptions of product quality, often collected through customer surveys or feedback mechanisms.",
    "formula": "Sum of weighted quality metrics (based on defect rates, user feedback, etc.) / Total number of quality metrics",
    "calculation_formula": "Sum of weighted quality metrics (based on defect rates, user feedback, etc.) / Total number of quality metrics",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Quality Score to be added.",
    "trend_analysis": """



    * An increasing product quality score may indicate improvements in production processes or customer satisfaction.
    * A decreasing score could signal issues with product consistency, customer service, or market competition.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or features that consistently receive lower quality scores?
    * How do our product quality scores compare with industry benchmarks or customer expectations?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular quality control checks throughout the production process.
    * Invest in customer feedback mechanisms to identify areas for product improvement.
    * Train and empower customer service teams to address product quality concerns effectively.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of product quality scores over time.
    * Pareto charts to identify the most common reasons for low product quality scores.
    
    
    
    """,
    "risk_warnings": """



    * Consistently low product quality scores can lead to customer churn and negative word-of-mouth.
    * High variability in product quality scores may indicate inconsistent production processes.
    
    
    
    """,
    "tracking_tools": """



    * Quality management software like MasterControl or ETQ to track and analyze product quality data.
    * Customer feedback platforms such as SurveyMonkey or Medallia to gather and analyze customer perceptions of product quality.
    
    
    
    """,
    "integration_points": """



    * Integrate product quality score tracking with production management systems to identify and address quality issues at the source.
    * Link quality score data with customer relationship management (CRM) systems to understand the impact on customer satisfaction and retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving product quality scores can lead to increased customer satisfaction and loyalty, ultimately impacting revenue and brand reputation positively.
    * Conversely, declining product quality scores may result in increased customer complaints, returns, and decreased sales.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Product", "Product Adoption", "Product Usage"], "last_validated": "2025-11-10T13:49:33.270724"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        67,
                        86,
                        87,
                        64,
                        85,
                        106,
                        94,
                        89,
                        71,
                        80,
                        107,
                        72
                ],
                "unit": "count"
        },
        "current": {
                "value": 72,
                "unit": "count",
                "change": -35,
                "change_percent": -32.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 84.0,
                "min": 64,
                "max": 107,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 15.91,
                        "percentage": 22.1
                },
                {
                        "category": "Product Line B",
                        "value": 15.27,
                        "percentage": 21.2
                },
                {
                        "category": "Product Line C",
                        "value": 8.49,
                        "percentage": 11.8
                },
                {
                        "category": "Services",
                        "value": 9.7,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 22.63,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.643986",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Product Quality Score"
        }
    },
}
