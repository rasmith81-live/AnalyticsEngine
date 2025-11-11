"""
Annual Contract Value (ACV)

The average annual contract value of subscriptions or service agreements for key accounts.
"""

ANNUAL_CONTRACT_VALUE_ACV = {
    "code": "ANNUAL_CONTRACT_VALUE_ACV",
    "name": "Annual Contract Value (ACV)",
    "description": "The average annual contract value of subscriptions or service agreements for key accounts.",
    "formula": "Total Value of Contract / Number of Years in Contract",
    "calculation_formula": "Total Value of Contract / Number of Years in Contract",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Annual Contract Value (ACV) to be added.",
    "trend_analysis": """



    * Increasing ACV may indicate successful upselling or cross-selling efforts with key accounts.
    * Decreasing ACV could signal dissatisfaction or attrition among key accounts.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that are driving the increase or decrease in ACV?
    * How does the ACV of key accounts compare to non-key accounts, and what insights can be gained from the comparison?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and adjust pricing strategies to maximize ACV without sacrificing customer satisfaction.
    * Invest in building stronger relationships with key accounts to increase loyalty and retention, ultimately leading to higher ACV.
    * Provide personalized solutions and offerings tailored to the specific needs and goals of key accounts.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the ACV trends of key accounts over time.
    * Pie charts comparing the distribution of ACV across different products or services for key accounts.
    
    
    
    """,
    "risk_warnings": """



    * Significant fluctuations in ACV may indicate instability or uncertainty within key accounts, posing a risk to revenue projections.
    * Consistently low ACV may suggest that key accounts are not fully leveraging the value of the products or services, leading to potential churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track interactions and opportunities with key accounts.
    * Data analytics tools to identify patterns and correlations that can help optimize ACV strategies.
    
    
    
    """,
    "integration_points": """



    * Integrate ACV data with sales performance metrics to understand the impact of individual sales efforts on key account value.
    * Link ACV tracking with customer support systems to ensure that service levels align with the value provided to key accounts.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing ACV may lead to higher revenue and profitability, but it could also require additional resources to support the expanded value provided to key accounts.
    * Conversely, a decrease in ACV can impact overall sales performance and may require adjustments in sales strategies and customer engagement approaches.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Contract", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.640352"},
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
                        375,
                        402,
                        415,
                        388,
                        387,
                        391,
                        395,
                        415,
                        369,
                        370,
                        404,
                        385
                ],
                "unit": "count"
        },
        "current": {
                "value": 385,
                "unit": "count",
                "change": -19,
                "change_percent": -4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 391.33,
                "min": 369,
                "max": 415,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 91.11,
                        "percentage": 23.7
                },
                {
                        "category": "Segment B",
                        "value": 94.26,
                        "percentage": 24.5
                },
                {
                        "category": "Segment C",
                        "value": 68.72,
                        "percentage": 17.8
                },
                {
                        "category": "Segment D",
                        "value": 32.99,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 97.92,
                        "percentage": 25.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.352583",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Annual Contract Value (ACV)"
        }
    },
}
