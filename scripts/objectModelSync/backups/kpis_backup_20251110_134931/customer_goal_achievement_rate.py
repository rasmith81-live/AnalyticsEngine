"""
Customer Goal Achievement Rate

The rate at which customers achieve their desired outcomes or goals with the company's products or services.
"""

CUSTOMER_GOAL_ACHIEVEMENT_RATE = {
    "code": "CUSTOMER_GOAL_ACHIEVEMENT_RATE",
    "name": "Customer Goal Achievement Rate",
    "description": "The rate at which customers achieve their desired outcomes or goals with the company's products or services.",
    "formula": "(Number of Customers Achieving Their Goals / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Achieving Their Goals / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Goal Achievement Rate to be added.",
    "trend_analysis": """

    * An increasing customer goal achievement rate may indicate improved product quality or better customer support.
    * A decreasing rate could signal issues with product performance, customer onboarding, or changing customer needs.
    
    """,
    "diagnostic_questions": """

    * Are there common barriers that prevent customers from achieving their goals?
    * How does our customer goal achievement rate compare with industry benchmarks or competitor performance?
    
    """,
    "actionable_tips": """

    * Enhance customer onboarding processes to ensure clear goal setting and alignment with customer expectations.
    * Provide ongoing training and support to help customers maximize the value of our products or services.
    * Regularly gather customer feedback to identify areas for improvement and address any obstacles to goal achievement.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend in customer goal achievement rate over time.
    * Stacked bar charts comparing goal achievement rates across different customer segments or product categories.
    
    """,
    "risk_warnings": """

    * A low customer goal achievement rate can lead to customer churn and negative word-of-mouth, impacting future sales.
    * Consistently high achievement rates may indicate that customer goals are too easy to attain, potentially devaluing the product or service.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems to track customer interactions and progress towards goals.
    * Survey and feedback tools to gather insights into customer satisfaction and goal attainment.
    
    """,
    "integration_points": """

    * Integrate customer goal achievement data with sales and marketing systems to better understand the impact on customer acquisition and retention.
    * Link with product development and innovation processes to align new features or improvements with customer goals.
    
    """,
    "change_impact_analysis": """

    * Improving the customer goal achievement rate can lead to higher customer lifetime value and increased brand loyalty.
    * However, overly aggressive goal setting may lead to customer frustration and dissatisfaction, impacting overall customer experience.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Goal", "Product"], "last_validated": "2025-11-10T13:43:23.273667"},
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
                        33.65,
                        38.69,
                        48.11,
                        46.85,
                        46.05,
                        43.16,
                        37.97,
                        46.16,
                        43.06,
                        35.51,
                        47.19,
                        44.68
                ],
                "unit": "%"
        },
        "current": {
                "value": 44.68,
                "unit": "%",
                "change": -2.51,
                "change_percent": -5.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 42.59,
                "min": 33.65,
                "max": 48.11,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.43,
                        "percentage": 34.5
                },
                {
                        "category": "Category B",
                        "value": 8.88,
                        "percentage": 19.9
                },
                {
                        "category": "Category C",
                        "value": 5.02,
                        "percentage": 11.2
                },
                {
                        "category": "Category D",
                        "value": 1.68,
                        "percentage": 3.8
                },
                {
                        "category": "Other",
                        "value": 13.67,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.273667",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Goal Achievement Rate"
        }
    },
}
