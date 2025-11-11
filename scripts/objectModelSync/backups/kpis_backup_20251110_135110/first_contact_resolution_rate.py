"""
First Contact Resolution Rate

The percentage of customer support issues resolved during the first interaction with a customer.
"""

FIRST_CONTACT_RESOLUTION_RATE = {
    "code": "FIRST_CONTACT_RESOLUTION_RATE",
    "name": "First Contact Resolution Rate",
    "description": "The percentage of customer support issues resolved during the first interaction with a customer.",
    "formula": "(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
    "calculation_formula": "(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for First Contact Resolution Rate to be added.",
    "trend_analysis": """


    * An increasing first contact resolution rate may indicate improved training and knowledge among customer support staff.
    * A decreasing rate could signal a need for process improvements or changes in customer support protocols.
    
    
    """,
    "diagnostic_questions": """


    * Are there common reasons why customer support interactions require multiple contacts to resolve?
    * How does our first contact resolution rate compare with industry benchmarks or customer expectations?
    
    
    """,
    "actionable_tips": """


    * Invest in ongoing training and development for customer support teams to enhance their problem-solving abilities.
    * Implement a knowledge base or self-service options for customers to address common issues without the need for direct support.
    * Analyze customer support interactions to identify recurring issues and develop proactive solutions.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of first contact resolution rate over time.
    * Pie charts to illustrate the percentage of different types of issues resolved on the first contact.
    
    
    """,
    "risk_warnings": """


    * A low first contact resolution rate can lead to customer frustration and dissatisfaction.
    * Repeated contacts for the same issue may indicate underlying product or service problems that need to be addressed.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems with robust ticketing and case management capabilities.
    * Analytics tools to track and analyze customer support interactions and resolution rates.
    
    
    """,
    "integration_points": """


    * Integrate first contact resolution rate data with customer satisfaction surveys to understand the impact of support interactions on overall satisfaction.
    * Link with sales and marketing systems to identify patterns in customer issues and proactively address them.
    
    
    """,
    "change_impact_analysis": """


    * Improving first contact resolution rate can lead to higher customer satisfaction and loyalty, impacting long-term customer retention and revenue.
    * However, focusing solely on speed of resolution may impact the depth of support provided, potentially affecting overall customer experience.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Support Ticket"], "replaces": ["FIRST_CONTACT_RESOLUTION_FCR"], "last_validated": "2025-11-10T13:49:32.956709"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "OUTSIDE_SALES"],
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
                        39.59,
                        38.92,
                        49.22,
                        55.19,
                        40.3,
                        53.36,
                        52.42,
                        46.55,
                        48.76,
                        40.09,
                        42.49,
                        50.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.96,
                "unit": "%",
                "change": 8.47,
                "change_percent": 19.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 46.49,
                "min": 38.92,
                "max": 55.19,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.22,
                        "percentage": 31.8
                },
                {
                        "category": "Category B",
                        "value": 10.8,
                        "percentage": 21.2
                },
                {
                        "category": "Category C",
                        "value": 4.37,
                        "percentage": 8.6
                },
                {
                        "category": "Category D",
                        "value": 4.45,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 15.12,
                        "percentage": 29.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.490046",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "First Contact Resolution Rate"
        }
    },
}
