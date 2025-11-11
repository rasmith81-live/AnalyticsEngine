"""
Customer Engagement Rate

The level of interaction and engagement a customer has with the brand or sales team.
"""

CUSTOMER_ENGAGEMENT_RATE = {
    "code": "CUSTOMER_ENGAGEMENT_RATE",
    "name": "Customer Engagement Rate",
    "description": "The level of interaction and engagement a customer has with the brand or sales team.",
    "formula": "(Number of Engaged Customers / Total Customers) * 100",
    "calculation_formula": "(Number of Engaged Customers / Total Customers) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Engagement Rate to be added.",
    "trend_analysis": """


    * An increasing customer engagement rate may indicate successful marketing efforts or improved customer service.
    * A decreasing rate could signal a decline in brand relevance or customer satisfaction.
    
    
    """,
    "diagnostic_questions": """


    * What specific interactions or touchpoints are included in the calculation of customer engagement?
    * How does the customer engagement rate vary across different customer segments or demographics?
    
    
    """,
    "actionable_tips": """


    * Implement a customer relationship management (CRM) system to better track and manage customer interactions.
    * Invest in training for the sales team to improve their ability to engage and build relationships with customers.
    * Regularly solicit feedback from customers to understand how to enhance their engagement with the brand.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer engagement rate over time.
    * Pie charts to illustrate the distribution of customer engagement across different channels or touchpoints.
    
    
    """,
    "risk_warnings": """


    * A consistently low customer engagement rate may lead to decreased customer loyalty and retention.
    * High fluctuations in the engagement rate could indicate inconsistent customer experiences or ineffective marketing strategies.
    
    
    """,
    "tracking_tools": """


    * Customer engagement platforms like HubSpot or Salesforce for tracking and managing customer interactions.
    * Social media monitoring tools to gauge customer engagement on various social platforms.
    
    
    """,
    "integration_points": """


    * Integrate customer engagement data with sales performance metrics to understand the impact of engagement on sales outcomes.
    * Link customer engagement with customer support systems to ensure a seamless and consistent customer experience.
    
    
    """,
    "change_impact_analysis": """


    * Improving customer engagement can lead to increased customer lifetime value and brand advocacy.
    * However, a focus solely on increasing engagement without considering quality may lead to superficial interactions that do not drive meaningful customer relationships.
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.823506"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        54.58,
                        46.86,
                        49.84,
                        45.97,
                        48.88,
                        42.78,
                        50.37,
                        48.08,
                        43.48,
                        48.35,
                        47.8,
                        44.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 44.93,
                "unit": "%",
                "change": -2.87,
                "change_percent": -6.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 47.66,
                "min": 42.78,
                "max": 54.58,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.25,
                        "percentage": 18.4
                },
                {
                        "category": "Category B",
                        "value": 7.06,
                        "percentage": 15.7
                },
                {
                        "category": "Category C",
                        "value": 9.79,
                        "percentage": 21.8
                },
                {
                        "category": "Category D",
                        "value": 5.44,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 14.39,
                        "percentage": 32.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.248921",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Engagement Rate"
        }
    },
}
