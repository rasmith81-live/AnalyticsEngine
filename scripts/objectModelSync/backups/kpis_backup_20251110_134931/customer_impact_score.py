"""
Customer Impact Score

A measure of the estimated impact or influence of a customer on potential new sales or market perception.
"""

CUSTOMER_IMPACT_SCORE = {
    "code": "CUSTOMER_IMPACT_SCORE",
    "name": "Customer Impact Score",
    "description": "A measure of the estimated impact or influence of a customer on potential new sales or market perception.",
    "formula": "Sum of Impact Metrics Across Customers / Total Number of Customers",
    "calculation_formula": "Sum of Impact Metrics Across Customers / Total Number of Customers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Impact Score to be added.",
    "trend_analysis": """

    * An increasing customer impact score may indicate a growing influence of certain customers on potential new sales or market perception.
    * A decreasing score could signal a decline in customer influence or a shift in market dynamics.
    
    """,
    "diagnostic_questions": """

    * Which customers are driving the highest impact score, and what factors contribute to their influence?
    * How does the customer impact score align with actual sales performance and customer feedback?
    
    """,
    "actionable_tips": """

    * Identify key customers and tailor sales and marketing strategies to maximize their impact.
    * Regularly assess and update the customer impact score based on changing market conditions and customer behaviors.
    * Invest in relationship-building activities with high-impact customers to strengthen their influence and advocacy.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of customer impact scores over time.
    * Comparison charts to visualize the impact scores of different customer segments or regions.
    
    """,
    "risk_warnings": """

    * A declining customer impact score may indicate a loss of influence in key market segments.
    * Over-reliance on a few high-impact customers can create vulnerability if their influence diminishes.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track customer interactions and impact on sales.
    * Social listening tools to monitor customer sentiment and influence in the market.
    
    """,
    "integration_points": """

    * Integrate customer impact scores with sales and marketing analytics to understand the correlation between customer influence and actual sales performance.
    * Link customer impact data with customer service systems to ensure consistent and personalized interactions with high-impact customers.
    
    """,
    "change_impact_analysis": """

    * An increase in customer impact score may lead to higher sales and improved market perception, but it could also create dependency on a few key customers.
    * A decrease in the score may require strategic shifts to regain influence and maintain market competitiveness.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.279549"},
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
                        410,
                        417,
                        405,
                        404,
                        416,
                        373,
                        386,
                        417,
                        374,
                        374,
                        391,
                        374
                ],
                "unit": "count"
        },
        "current": {
                "value": 374,
                "unit": "count",
                "change": -17,
                "change_percent": -4.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 395.08,
                "min": 373,
                "max": 417,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 76.98,
                        "percentage": 20.6
                },
                {
                        "category": "Category B",
                        "value": 86.27,
                        "percentage": 23.1
                },
                {
                        "category": "Category C",
                        "value": 66.37,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 31.65,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 112.73,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.279549",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Impact Score"
        }
    },
}
