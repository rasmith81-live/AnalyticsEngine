"""
Renewal Rate

The percentage of customers who renew a subscription or service agreement.
"""

RENEWAL_RATE = {
    "code": "RENEWAL_RATE",
    "name": "Renewal Rate",
    "description": "The percentage of customers who renew a subscription or service agreement.",
    "formula": "(Number of Renewals / Number of Eligible Renewals) * 100",
    "calculation_formula": "(Number of Renewals / Number of Eligible Renewals) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Renewal Rate to be added.",
    "trend_analysis": """



    * A rising renewal rate may indicate improved customer satisfaction and loyalty.
    * A decreasing rate could signal increased competition or dissatisfaction with the product or service.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific reasons why customers are not renewing their subscriptions or service agreements?
    * How does our renewal rate compare with industry benchmarks or with our historical data?
    
    
    
    """,
    "actionable_tips": """



    * Enhance the quality of customer service and support to increase satisfaction and retention.
    * Offer incentives or discounts for long-term commitments to encourage renewals.
    * Regularly communicate with customers to understand their needs and address any issues before renewal decisions are made.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of renewal rates over time.
    * Pie charts comparing renewal rates by customer segment or product/service category.
    
    
    
    """,
    "risk_warnings": """



    * A declining renewal rate can lead to reduced recurring revenue and impact overall sales performance.
    * High renewal rates without corresponding customer satisfaction may indicate a lack of competitive alternatives, posing a risk in the long term.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for retention.
    * Survey tools to gather feedback from customers about their renewal decisions and experiences.
    
    
    
    """,
    "integration_points": """



    * Integrate renewal rate data with customer feedback systems to understand the reasons behind non-renewals.
    * Link renewal rate tracking with sales and marketing systems to align efforts towards customer retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the renewal rate can lead to increased customer lifetime value and overall revenue.
    * However, aggressive tactics to boost renewal rates may impact customer trust and brand reputation if not handled carefully.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Product", "Renewal Management", "Service Level Agreement", "Subscription"], "last_validated": "2025-11-10T13:49:33.331313"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
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
                        62.38,
                        61.94,
                        55.89,
                        67.96,
                        63.37,
                        70.29,
                        56.17,
                        57.88,
                        69.63,
                        68.65,
                        69.77,
                        61.59
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.59,
                "unit": "%",
                "change": -8.18,
                "change_percent": -11.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.79,
                "min": 55.89,
                "max": 70.29,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.24,
                        "percentage": 34.5
                },
                {
                        "category": "Segment B",
                        "value": 9.76,
                        "percentage": 15.8
                },
                {
                        "category": "Segment C",
                        "value": 6.06,
                        "percentage": 9.8
                },
                {
                        "category": "Segment D",
                        "value": 6.59,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 17.94,
                        "percentage": 29.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.779014",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Renewal Rate"
        }
    },
}
