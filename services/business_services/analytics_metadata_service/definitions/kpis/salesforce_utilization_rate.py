"""
Salesforce Utilization Rate

The degree to which the sales team is effectively using salesforce automation tools or customer relationship management (CRM) systems.
"""

SALESFORCE_UTILIZATION_RATE = {
    "code": "SALESFORCE_UTILIZATION_RATE",
    "name": "Salesforce Utilization Rate",
    "description": "The degree to which the sales team is effectively using salesforce automation tools or customer relationship management (CRM) systems.",
    "formula": "(Number of Active CRM Users / Total Number of Sales Team Members) * 100",
    "calculation_formula": "(Number of Active CRM Users / Total Number of Sales Team Members) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Salesforce Utilization Rate to be added.",
    "trend_analysis": """



    * An increasing Salesforce Utilization Rate may indicate better adoption of CRM tools and improved data management.
    * A decreasing rate could signal resistance to CRM implementation or lack of training on the system.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific features within the CRM system that are underutilized by the sales team?
    * How does our Salesforce Utilization Rate compare to industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Provide comprehensive training and ongoing support for sales team members to maximize CRM utilization.
    * Regularly review and update the CRM system to ensure it aligns with the evolving needs of the sales team.
    * Incentivize CRM usage through performance metrics and recognition for effective utilization.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of Salesforce Utilization Rate over time.
    * Pie charts illustrating the distribution of CRM tool usage across the sales team.
    
    
    
    """,
    "risk_warnings": """



    * Low Salesforce Utilization Rate can lead to inaccurate data, missed opportunities, and decreased productivity.
    * Resistance to CRM adoption may indicate broader issues with organizational change management or communication.
    
    
    
    """,
    "tracking_tools": """



    * CRM platforms like Salesforce, HubSpot, or Zoho CRM for comprehensive sales and customer management.
    * Data analytics tools to track and analyze CRM usage patterns and identify areas for improvement.
    
    
    
    """,
    "integration_points": """



    * Integrate CRM data with marketing automation systems to align sales and marketing efforts and improve lead management.
    * Link CRM with customer support systems to provide a seamless experience for customers across different touchpoints.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving Salesforce Utilization Rate can lead to better customer insights, improved sales forecasting, and more targeted marketing efforts.
    * However, pushing for higher CRM usage may require a cultural shift and change management efforts within the sales team.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product Usage", "Prospect Engagement", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.544792"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        78.07,
                        75.56,
                        64.31,
                        78.91,
                        70.39,
                        61.43,
                        73.14,
                        60.88,
                        65.1,
                        63.26,
                        68.15,
                        59.91
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.91,
                "unit": "%",
                "change": -8.24,
                "change_percent": -12.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 68.26,
                "min": 59.91,
                "max": 78.91,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 18.8,
                        "percentage": 31.4
                },
                {
                        "category": "Channel Sales",
                        "value": 11.7,
                        "percentage": 19.5
                },
                {
                        "category": "Online Sales",
                        "value": 6.42,
                        "percentage": 10.7
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.45,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 18.54,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.309365",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Salesforce Utilization Rate"
        }
    },
}
