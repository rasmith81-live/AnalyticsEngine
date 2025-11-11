"""
Average Order Value (AOV)

The average value of orders received from key accounts.
"""

AVERAGE_ORDER_VALUE_AOV = {
    "code": "AVERAGE_ORDER_VALUE_AOV",
    "name": "Average Order Value (AOV)",
    "description": "The average value of orders received from key accounts.",
    "formula": "Total Revenue / Total Number of Orders",
    "calculation_formula": "Total Revenue / Total Number of Orders",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Order Value (AOV) to be added.",
    "trend_analysis": """



    * Increasing average order value may indicate upselling or cross-selling success with key accounts.
    * Decreasing average order value could signal a shift in purchasing behavior or dissatisfaction with products or services.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that contribute significantly to the average order value?
    * How does the average order value compare to historical data or industry benchmarks?
    
    
    
    """,
    "actionable_tips": """



    * Implement targeted marketing campaigns to promote higher-value products or services to key accounts.
    * Offer bundled packages or discounts for larger orders to encourage higher average order values.
    * Provide personalized recommendations to key accounts based on their purchasing history and preferences.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of average order value over time.
    * Pareto charts to identify the most significant contributors to the average order value.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low average order value may indicate a lack of customer loyalty or satisfaction.
    * Over-reliance on a few high-value orders may pose a risk if those accounts are lost or reduce their purchasing volume.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and analyze purchasing behavior of key accounts.
    * Business intelligence tools to identify patterns and opportunities for increasing average order value.
    
    
    
    """,
    "integration_points": """



    * Integrate average order value data with sales performance metrics to understand the impact on overall revenue and profitability.
    * Link with inventory management systems to ensure availability of high-value products for key accounts.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing average order value may lead to higher revenue and profitability, but could also require additional resources for personalized sales efforts.
    * Conversely, a declining average order value may indicate the need for product or service improvements to maintain customer satisfaction and loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.651752"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        360,
                        376,
                        356,
                        356,
                        373,
                        401,
                        376,
                        378,
                        394,
                        367,
                        385,
                        378
                ],
                "unit": "count"
        },
        "current": {
                "value": 378,
                "unit": "count",
                "change": -7,
                "change_percent": -1.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 375.0,
                "min": 356,
                "max": 401,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 127.82,
                        "percentage": 33.8
                },
                {
                        "category": "Segment B",
                        "value": 74.0,
                        "percentage": 19.6
                },
                {
                        "category": "Segment C",
                        "value": 44.77,
                        "percentage": 11.8
                },
                {
                        "category": "Segment D",
                        "value": 15.19,
                        "percentage": 4.0
                },
                {
                        "category": "Other",
                        "value": 116.22,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.375228",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Order Value (AOV)"
        }
    },
}
