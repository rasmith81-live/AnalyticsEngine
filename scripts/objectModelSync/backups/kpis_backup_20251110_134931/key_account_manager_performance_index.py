"""
Key Account Manager Performance Index

An overall performance metric for key account managers that includes various performance-related KPIs.
"""

KEY_ACCOUNT_MANAGER_PERFORMANCE_INDEX = {
    "code": "KEY_ACCOUNT_MANAGER_PERFORMANCE_INDEX",
    "name": "Key Account Manager Performance Index",
    "description": "An overall performance metric for key account managers that includes various performance-related KPIs.",
    "formula": "Custom formula based on factors like revenue growth, account retention, customer satisfaction, etc.",
    "calculation_formula": "Custom formula based on factors like revenue growth, account retention, customer satisfaction, etc.",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Key Account Manager Performance Index to be added.",
    "trend_analysis": """

    * Increasing Key Account Manager Performance Index may indicate improved customer satisfaction and retention.
    * Decreasing index could signal a decline in key account management effectiveness or a shift in customer needs.
    
    """,
    "diagnostic_questions": """

    * Are there specific key accounts that are consistently underperforming?
    * How does our Key Account Manager Performance Index compare with industry benchmarks or competitor performance?
    
    """,
    "actionable_tips": """

    * Invest in ongoing training and development for key account managers to enhance their skills and knowledge.
    * Implement a customer relationship management (CRM) system to better track and manage key account interactions and opportunities.
    * Regularly review and adjust key account strategies based on changing customer needs and market dynamics.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of the Key Account Manager Performance Index over time.
    * Stacked bar graphs comparing the performance of individual key account managers within the organization.
    
    """,
    "risk_warnings": """

    * Low Key Account Manager Performance Index can lead to loss of key accounts and revenue.
    * Inconsistent performance across key account managers may indicate a need for standardization and improvement in key account management processes.
    
    """,
    "tracking_tools": """

    * CRM platforms like Salesforce or HubSpot for tracking key account interactions and opportunities.
    * Performance management software to monitor and evaluate the performance of key account managers against set targets and goals.
    
    """,
    "integration_points": """

    * Integrate Key Account Manager Performance Index with sales and revenue data to understand the impact of key account management on overall business performance.
    * Link performance data with customer feedback and satisfaction metrics to gain a comprehensive view of key account management effectiveness.
    
    """,
    "change_impact_analysis": """

    * Improving the Key Account Manager Performance Index can lead to increased customer loyalty and lifetime value.
    * Conversely, a decline in performance may result in customer dissatisfaction and potential loss of business.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Renewal Management", "Revenue Forecast", "Sale", "Sales Representative"], "last_validated": "2025-11-10T13:43:23.567768"},
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
                        186,
                        167,
                        212,
                        202,
                        182,
                        201,
                        194,
                        182,
                        212,
                        191,
                        199,
                        166
                ],
                "unit": "count"
        },
        "current": {
                "value": 166,
                "unit": "count",
                "change": -33,
                "change_percent": -16.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 191.17,
                "min": 166,
                "max": 212,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 46.34,
                        "percentage": 27.9
                },
                {
                        "category": "Category B",
                        "value": 37.66,
                        "percentage": 22.7
                },
                {
                        "category": "Category C",
                        "value": 27.72,
                        "percentage": 16.7
                },
                {
                        "category": "Category D",
                        "value": 7.66,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 46.62,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.567768",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Key Account Manager Performance Index"
        }
    },
}
