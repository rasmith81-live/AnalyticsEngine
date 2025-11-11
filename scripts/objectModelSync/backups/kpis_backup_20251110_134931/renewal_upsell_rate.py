"""
Renewal Upsell Rate

The percentage of renewal opportunities where an upsell was achieved.
"""

RENEWAL_UPSELL_RATE = {
    "code": "RENEWAL_UPSELL_RATE",
    "name": "Renewal Upsell Rate",
    "description": "The percentage of renewal opportunities where an upsell was achieved.",
    "formula": "(Number of Renewals with Upsell / Total Number of Renewals) * 100",
    "calculation_formula": "(Number of Renewals with Upsell / Total Number of Renewals) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Renewal Upsell Rate to be added.",
    "trend_analysis": """

    * An increasing renewal upsell rate may indicate successful sales strategies and a strong understanding of customer needs.
    * A decreasing rate could signal missed opportunities for upselling or a decline in customer satisfaction and loyalty.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or services that consistently lead to successful upsells during renewals?
    * How does our renewal upsell rate compare with industry benchmarks or with historical data?
    
    """,
    "actionable_tips": """

    * Train sales teams to identify upsell opportunities and effectively communicate the value of additional products or services.
    * Implement customer segmentation strategies to tailor upsell offers based on specific customer needs and preferences.
    * Regularly review and update product or service offerings to ensure they align with customer demands and market trends.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of renewal upsell rates over time.
    * Pie charts to visualize the distribution of successful upsells by product or service category.
    
    """,
    "risk_warnings": """

    * A low renewal upsell rate may lead to missed revenue opportunities and reduced customer lifetime value.
    * Consistently high upsell rates could indicate aggressive or pushy sales tactics that may harm customer relationships.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track customer interactions and identify upsell opportunities.
    * Data analytics tools to analyze customer behavior and preferences for targeted upsell strategies.
    
    """,
    "integration_points": """

    * Integrate renewal upsell rate data with customer feedback and satisfaction scores to understand the impact of upselling on overall customer experience.
    * Link upsell performance with sales compensation and incentive programs to align sales efforts with upsell goals.
    
    """,
    "change_impact_analysis": """

    * Improving the renewal upsell rate can lead to increased revenue and customer loyalty, but may also require additional resources for sales training and customer segmentation.
    * Conversely, a declining upsell rate may indicate a need for reevaluation of sales strategies and product offerings to maintain competitiveness in the market.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Purchase History", "Renewal Management"], "last_validated": "2025-11-10T13:43:24.068726"},
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
                        52.35,
                        53.74,
                        42.63,
                        50.12,
                        50.57,
                        48.04,
                        56.87,
                        42.73,
                        47.59,
                        50.52,
                        50.21,
                        46.83
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.83,
                "unit": "%",
                "change": -3.38,
                "change_percent": -6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 49.35,
                "min": 42.63,
                "max": 56.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.17,
                        "percentage": 34.5
                },
                {
                        "category": "Category B",
                        "value": 10.15,
                        "percentage": 21.7
                },
                {
                        "category": "Category C",
                        "value": 3.1,
                        "percentage": 6.6
                },
                {
                        "category": "Category D",
                        "value": 4.92,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 12.49,
                        "percentage": 26.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.068726",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Renewal Upsell Rate"
        }
    },
}
