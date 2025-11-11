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
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Purchase History", "Renewal Management"], "last_validated": "2025-11-10T13:49:33.332903"},
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
                        54.6,
                        62.24,
                        55.53,
                        60.83,
                        52.58,
                        56.56,
                        53.15,
                        55.95,
                        59.41,
                        55.31,
                        55.95,
                        58.57
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.57,
                "unit": "%",
                "change": 2.62,
                "change_percent": 4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.72,
                "min": 52.58,
                "max": 62.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.79,
                        "percentage": 21.8
                },
                {
                        "category": "Segment B",
                        "value": 15.45,
                        "percentage": 26.4
                },
                {
                        "category": "Segment C",
                        "value": 9.82,
                        "percentage": 16.8
                },
                {
                        "category": "Segment D",
                        "value": 2.32,
                        "percentage": 4.0
                },
                {
                        "category": "Other",
                        "value": 18.19,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.783655",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Renewal Upsell Rate"
        }
    },
}
