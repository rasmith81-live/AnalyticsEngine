"""
Customer Cohort Retention Rate

The retention rate of specific customer cohorts over time, which can highlight trends or patterns in customer loyalty.
"""

CUSTOMER_COHORT_RETENTION_RATE = {
    "code": "CUSTOMER_COHORT_RETENTION_RATE",
    "name": "Customer Cohort Retention Rate",
    "description": "The retention rate of specific customer cohorts over time, which can highlight trends or patterns in customer loyalty.",
    "formula": "(Number of Customers Remaining from a Cohort / Total Number of Customers in the Cohort at the Start of the Period) * 100",
    "calculation_formula": "(Number of Customers Remaining from a Cohort / Total Number of Customers in the Cohort at the Start of the Period) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Cohort Retention Rate to be added.",
    "trend_analysis": """

    * Increasing customer cohort retention rate may indicate improved customer satisfaction or loyalty programs.
    * A decreasing rate could signal issues with product quality, customer service, or competitive pressures.
    
    """,
    "diagnostic_questions": """

    * Are there specific customer segments or product lines that are experiencing higher or lower retention rates?
    * How does our customer cohort retention rate compare with industry benchmarks or seasonal fluctuations?
    
    """,
    "actionable_tips": """

    * Implement targeted customer retention strategies based on customer segmentation and preferences.
    * Enhance product quality, customer service, and overall customer experience to improve retention rates.
    * Regularly communicate with customers to gather feedback and address any issues proactively.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the retention rate trends for different customer cohorts over time.
    * Cohort analysis graphs to compare the retention rates of different customer segments.
    
    """,
    "risk_warnings": """

    * Low customer cohort retention rates can lead to decreased revenue and market share.
    * Consistently declining retention rates may indicate fundamental issues with the product or service offering.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and analyze customer interactions and feedback.
    * Customer survey tools to gather insights on customer satisfaction and loyalty.
    
    """,
    "integration_points": """

    * Integrate customer cohort retention data with marketing automation platforms to personalize customer communication and engagement.
    * Link retention rate analysis with sales and product development processes to align offerings with customer needs and preferences.
    
    """,
    "change_impact_analysis": """

    * Improving customer cohort retention can lead to increased customer lifetime value and positive word-of-mouth referrals.
    * Conversely, declining retention rates can impact overall sales performance and brand reputation.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Loyalty Program", "Opportunity"], "last_validated": "2025-11-10T13:43:23.220394"},
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
                        69.04,
                        70.04,
                        67.49,
                        54.67,
                        69.33,
                        72.24,
                        65.13,
                        66.58,
                        72.64,
                        65.51,
                        70.33,
                        61.16
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.16,
                "unit": "%",
                "change": -9.17,
                "change_percent": -13.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.01,
                "min": 54.67,
                "max": 72.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.31,
                        "percentage": 20.1
                },
                {
                        "category": "Category B",
                        "value": 9.38,
                        "percentage": 15.3
                },
                {
                        "category": "Category C",
                        "value": 5.94,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 8.76,
                        "percentage": 14.3
                },
                {
                        "category": "Other",
                        "value": 24.77,
                        "percentage": 40.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.220394",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Cohort Retention Rate"
        }
    },
}
