"""
Response Time

The amount of time it takes for the Customer Success Team to respond to a customer inquiry or request for assistance. This KPI measures the team's efficiency in handling customer issues.
"""

RESPONSE_TIME = {
    "code": "RESPONSE_TIME",
    "name": "Response Time",
    "description": "The amount of time it takes for the Customer Success Team to respond to a customer inquiry or request for assistance. This KPI measures the team's efficiency in handling customer issues.",
    "formula": "Average Time Between Customer Inquiry and Response",
    "calculation_formula": "Average Time Between Customer Inquiry and Response",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Response Time to be added.",
    "trend_analysis": """



    * Increasing response times may indicate a growing workload for the Customer Success Team or inefficiencies in the support process.
    * Decreasing response times can signal improved team productivity, better resource allocation, or enhanced communication channels.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific types of customer inquiries that consistently take longer to address?
    * How do response times vary across different channels of customer communication (e.g., email, phone, chat)?
    
    
    
    """,
    "actionable_tips": """



    * Implement automated ticketing systems to prioritize and route customer inquiries more efficiently.
    * Provide ongoing training and coaching to the Customer Success Team to enhance their problem-solving and communication skills.
    * Regularly review and optimize the customer support workflow to identify and eliminate bottlenecks.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average response time over time to identify trends and seasonality.
    * Stacked bar charts comparing response times across different customer support channels.
    
    
    
    """,
    "risk_warnings": """



    * Long response times can lead to customer frustration, dissatisfaction, and potential churn.
    * Inconsistent or excessively short response times may indicate rushed or incomplete issue resolution, impacting customer satisfaction.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software with built-in ticketing and response time tracking capabilities.
    * Helpdesk platforms that offer automation, routing, and reporting features to streamline customer support operations.
    
    
    
    """,
    "integration_points": """



    * Integrate response time data with customer feedback systems to understand the correlation between response times and customer satisfaction.
    * Link response time metrics with employee performance evaluations to incentivize timely and effective customer support.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving response times can enhance customer loyalty and retention, leading to increased customer lifetime value.
    * However, overly aggressive targets for response times may result in increased stress and burnout among customer support staff.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.342085"},
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
                        3.2,
                        8.7,
                        4.5,
                        4.2,
                        5.0,
                        4.4,
                        8.9,
                        3.7,
                        7.5,
                        3.1,
                        7.1,
                        8.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 8.0,
                "unit": "days",
                "change": 0.9,
                "change_percent": 12.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 5.69,
                "min": 3.1,
                "max": 8.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 1.95,
                        "percentage": 24.4
                },
                {
                        "category": "Existing Customers",
                        "value": 1.08,
                        "percentage": 13.5
                },
                {
                        "category": "VIP Customers",
                        "value": 1.32,
                        "percentage": 16.5
                },
                {
                        "category": "At-Risk Customers",
                        "value": 0.59,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 3.06,
                        "percentage": 38.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.805776",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Response Time"
        }
    },
}
