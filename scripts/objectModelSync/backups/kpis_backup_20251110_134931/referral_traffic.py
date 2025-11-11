"""
Referral Traffic

The amount of traffic coming to your site through existing customers referring new customers.
"""

REFERRAL_TRAFFIC = {
    "code": "REFERRAL_TRAFFIC",
    "name": "Referral Traffic",
    "description": "The amount of traffic coming to your site through existing customers referring new customers.",
    "formula": "Total Number of Visitors via Referral Links",
    "calculation_formula": "Total Number of Visitors via Referral Links",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Referral Traffic to be added.",
    "trend_analysis": """

    * An increasing referral traffic may indicate a growing customer base and positive word-of-mouth marketing.
    * A decreasing trend could signal a decline in customer satisfaction or engagement, leading to fewer referrals.
    
    """,
    "diagnostic_questions": """

    * Are there specific customer segments or products that are driving the majority of referral traffic?
    * How does our referral traffic compare with industry benchmarks or seasonal fluctuations?
    
    """,
    "actionable_tips": """

    * Implement a customer referral program to incentivize existing customers to refer new ones.
    * Enhance customer experience to encourage positive word-of-mouth and increase referrals.
    * Regularly engage with existing customers through targeted marketing and personalized communication to keep them engaged and likely to refer others.
    
    """,
    "visualization_suggestions": """

    * Line charts showing referral traffic over time to identify trends and patterns.
    * Pie charts to visualize the distribution of referral traffic by customer segments or products.
    
    """,
    "risk_warnings": """

    * A decline in referral traffic may indicate underlying issues with customer satisfaction or loyalty.
    * Dependence on a few customers for the majority of referrals can pose a risk if their engagement decreases.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and manage customer referrals and engagement.
    * Social media monitoring tools to identify and leverage customer advocacy and referrals on social platforms.
    
    """,
    "integration_points": """

    * Integrate referral traffic data with customer relationship management systems to better understand the impact of referrals on customer lifetime value.
    * Link referral traffic with sales and marketing systems to attribute referrals to specific campaigns or initiatives.
    
    """,
    "change_impact_analysis": """

    * Increasing referral traffic can lead to higher customer acquisition at a lower cost, positively impacting overall sales performance.
    * Conversely, a decline in referral traffic may lead to increased customer acquisition costs and reduced sales efficiency.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Referral"], "last_validated": "2025-11-10T13:43:24.055628"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
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
                        525,
                        524,
                        512,
                        481,
                        484,
                        516,
                        511,
                        525,
                        497,
                        499,
                        499,
                        504
                ],
                "unit": "count"
        },
        "current": {
                "value": 504,
                "unit": "count",
                "change": 5,
                "change_percent": 1.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 506.42,
                "min": 481,
                "max": 525,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 99.73,
                        "percentage": 19.8
                },
                {
                        "category": "Category B",
                        "value": 136.21,
                        "percentage": 27.0
                },
                {
                        "category": "Category C",
                        "value": 51.92,
                        "percentage": 10.3
                },
                {
                        "category": "Category D",
                        "value": 42.19,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 173.95,
                        "percentage": 34.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.055628",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Referral Traffic"
        }
    },
}
