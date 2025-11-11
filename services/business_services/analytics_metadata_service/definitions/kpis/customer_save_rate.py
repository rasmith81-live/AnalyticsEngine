"""
Customer Save Rate

The percentage of customers who were at the brink of leaving but were retained by the company.
"""

CUSTOMER_SAVE_RATE = {
    "code": "CUSTOMER_SAVE_RATE",
    "name": "Customer Save Rate",
    "description": "The percentage of customers who were at the brink of leaving but were retained by the company.",
    "formula": "(Number of Customers Retained / Number of Customers Attempting to Leave) * 100",
    "calculation_formula": "(Number of Customers Retained / Number of Customers Attempting to Leave) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Save Rate to be added.",
    "trend_analysis": """



    * An increasing customer save rate may indicate improved customer retention strategies or enhanced customer service efforts.
    * A decreasing rate could signal dissatisfaction with the company's products or services, or increased competition in the market.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the common reasons customers consider leaving, and how can we address those specific issues?
    * Are there patterns or commonalities among the customers who were successfully retained, and how can we replicate those successes?
    
    
    
    """,
    "actionable_tips": """



    * Implement proactive customer outreach and engagement strategies to address potential churn before it happens.
    * Personalize the customer experience to better meet individual needs and preferences, increasing the likelihood of retention.
    * Invest in ongoing customer education and support to build long-term relationships and loyalty.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the customer save rate over time to identify trends and seasonal variations.
    * Pie charts to compare the reasons for customer churn and the success rates of different retention strategies.
    
    
    
    """,
    "risk_warnings": """



    * A low customer save rate may indicate a lack of effective retention strategies, leading to potential revenue loss.
    * High customer save rates may mask underlying issues with product quality or customer satisfaction, leading to long-term negative impacts.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify at-risk customers.
    * Survey and feedback tools to gather insights from customers about their experiences and reasons for considering leaving.
    
    
    
    """,
    "integration_points": """



    * Integrate customer save rate data with sales and marketing systems to align retention efforts with overall business goals.
    * Link customer save rate with customer support systems to ensure a seamless experience for at-risk customers.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the customer save rate can lead to increased customer lifetime value and overall revenue growth.
    * Conversely, a declining customer save rate can indicate a need for significant changes in customer retention strategies and may impact overall business performance.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"], "last_validated": "2025-11-10T13:49:32.880243"},
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
                        49.39,
                        42.53,
                        47.47,
                        43.19,
                        44.67,
                        53.37,
                        46.34,
                        49.84,
                        46.04,
                        59.97,
                        59.25,
                        42.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 42.71,
                "unit": "%",
                "change": -16.54,
                "change_percent": -27.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 48.73,
                "min": 42.53,
                "max": 59.97,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 10.91,
                        "percentage": 25.5
                },
                {
                        "category": "Existing Customers",
                        "value": 9.48,
                        "percentage": 22.2
                },
                {
                        "category": "VIP Customers",
                        "value": 7.0,
                        "percentage": 16.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.51,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 10.81,
                        "percentage": 25.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.804963",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Save Rate"
        }
    },
}
