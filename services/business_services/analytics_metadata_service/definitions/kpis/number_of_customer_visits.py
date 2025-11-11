"""
Number of Customer Visits

The total number of in-person meetings the sales team has with potential or existing customers.
"""

NUMBER_OF_CUSTOMER_VISITS = {
    "code": "NUMBER_OF_CUSTOMER_VISITS",
    "name": "Number of Customer Visits",
    "description": "The total number of in-person meetings the sales team has with potential or existing customers.",
    "formula": "Sum of all Customer Visits",
    "calculation_formula": "Sum of all Customer Visits",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Customer Visits to be added.",
    "trend_analysis": """



    * An increasing number of customer visits may indicate a proactive sales team or a growing customer base.
    * A decreasing number of visits could signal a lack of sales team effectiveness or a shift in customer preferences towards remote communication.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific regions or customer segments that the sales team is neglecting in their visitation schedule?
    * How do the conversion rates from these visits compare to historical data or industry benchmarks?
    
    
    
    """,
    "actionable_tips": """



    * Implement a customer relationship management (CRM) system to track and prioritize customer visits.
    * Provide sales training to improve the effectiveness of in-person meetings and increase conversion rates.
    * Regularly review and adjust the visitation schedule based on customer feedback and sales performance data.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of customer visits over time.
    * Geospatial maps to visualize the distribution of customer visits across different regions.
    
    
    
    """,
    "risk_warnings": """



    * A low number of customer visits may lead to missed sales opportunities and decreased customer engagement.
    * Over-reliance on in-person meetings may result in higher travel costs and inefficiencies.
    
    
    
    """,
    "tracking_tools": """



    * CRM software like Salesforce or HubSpot for tracking and managing customer visits.
    * Route optimization tools to minimize travel time and maximize the number of visits in a day.
    
    
    
    """,
    "integration_points": """



    * Integrate customer visit data with sales performance metrics to understand the impact of visits on overall sales results.
    * Link customer visit information with customer feedback systems to measure the effectiveness of in-person interactions.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing the number of customer visits may lead to higher sales but also higher travel and entertainment expenses.
    * Reducing the number of visits may free up sales team time for other activities but could also result in decreased customer satisfaction and loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Meeting", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.085794"},
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
                        540.08,
                        564.73,
                        498.68,
                        562.1,
                        555.85,
                        479.14,
                        518.8,
                        440.2,
                        467.32,
                        518.81,
                        576.53,
                        454.98
                ],
                "unit": "units"
        },
        "current": {
                "value": 454.98,
                "unit": "units",
                "change": -121.55,
                "change_percent": -21.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 514.77,
                "min": 440.2,
                "max": 576.53,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 153.93,
                        "percentage": 33.8
                },
                {
                        "category": "Existing Customers",
                        "value": 92.26,
                        "percentage": 20.3
                },
                {
                        "category": "VIP Customers",
                        "value": 54.66,
                        "percentage": 12.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 30.1,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 124.03,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.258024",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Number of Customer Visits"
        }
    },
}
