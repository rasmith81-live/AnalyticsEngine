"""
Customer Meeting Frequency

The frequency at which meetings are held between the customer success team and individual customers.
"""

CUSTOMER_MEETING_FREQUENCY = {
    "code": "CUSTOMER_MEETING_FREQUENCY",
    "name": "Customer Meeting Frequency",
    "description": "The frequency at which meetings are held between the customer success team and individual customers.",
    "formula": "Total Number of Customer Meetings / Total Number of Customers",
    "calculation_formula": "Total Number of Customer Meetings / Total Number of Customers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Meeting Frequency to be added.",
    "trend_analysis": """



    * An increasing customer meeting frequency may indicate proactive customer engagement and a focus on building strong relationships.
    * A decreasing frequency could signal potential disengagement or dissatisfaction among customers, requiring immediate attention and intervention.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customers or customer segments that have seen a decline in meeting frequency?
    * How does the meeting frequency align with customer satisfaction scores or feedback?
    
    
    
    """,
    "actionable_tips": """



    * Implement a structured customer success plan that includes regular touchpoints and check-ins.
    * Utilize customer relationship management (CRM) software to track and schedule customer meetings efficiently.
    * Encourage proactive communication and outreach from the customer success team to maintain a consistent meeting frequency.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of meeting frequency over time for individual customers or customer segments.
    * Comparison bar graphs to analyze meeting frequency across different customer success managers or regions.
    
    
    
    """,
    "risk_warnings": """



    * Low meeting frequency may lead to customer churn or reduced lifetime value of customers.
    * Inconsistent or infrequent meetings can result in missed opportunities for upselling or cross-selling products or services.
    
    
    
    """,
    "tracking_tools": """



    * CRM platforms like Salesforce or HubSpot for scheduling and tracking customer meetings.
    * Customer success management software such as Gainsight or Totango for comprehensive customer engagement and success planning.
    
    
    
    """,
    "integration_points": """



    * Integrate meeting frequency data with customer feedback and satisfaction metrics to gain a holistic view of customer engagement.
    * Link meeting frequency with sales and revenue data to understand the impact of customer engagement on business performance.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing meeting frequency may lead to higher customer retention and loyalty, positively impacting overall sales and revenue.
    * However, a significant increase in meeting frequency without proper alignment with customer needs and goals could lead to resource inefficiency and increased operational costs.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Meeting", "Sales Team"], "last_validated": "2025-11-10T13:49:32.849116"},
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
                        339,
                        344,
                        311,
                        306,
                        302,
                        330,
                        299,
                        345,
                        321,
                        337,
                        327,
                        305
                ],
                "unit": "count"
        },
        "current": {
                "value": 305,
                "unit": "count",
                "change": -22,
                "change_percent": -6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 322.17,
                "min": 299,
                "max": 345,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 78.12,
                        "percentage": 25.6
                },
                {
                        "category": "Existing Customers",
                        "value": 47.45,
                        "percentage": 15.6
                },
                {
                        "category": "VIP Customers",
                        "value": 40.43,
                        "percentage": 13.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 25.21,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 113.79,
                        "percentage": 37.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.722131",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Meeting Frequency"
        }
    },
}
