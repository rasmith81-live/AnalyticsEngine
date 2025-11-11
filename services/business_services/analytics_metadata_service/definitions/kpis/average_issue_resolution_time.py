"""
Average Issue Resolution Time

The average time taken to resolve customer issues or complaints.
"""

AVERAGE_ISSUE_RESOLUTION_TIME = {
    "code": "AVERAGE_ISSUE_RESOLUTION_TIME",
    "name": "Average Issue Resolution Time",
    "description": "The average time taken to resolve customer issues or complaints.",
    "formula": "Sum of All Issue Resolution Times / Total Number of Issues Resolved",
    "calculation_formula": "Sum of All Issue Resolution Times / Total Number of Issues Resolved",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Issue Resolution Time to be added.",
    "trend_analysis": """



    * An increasing average issue resolution time may indicate growing customer service workload or inefficiencies in the resolution process.
    * A decreasing resolution time can signal improved customer service processes or a decline in the volume of customer issues.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific types of customer issues that consistently take longer to resolve?
    * How does our average resolution time compare with industry benchmarks or customer expectations?
    
    
    
    """,
    "actionable_tips": """



    * Implement customer service training programs to improve issue resolution efficiency.
    * Leverage customer feedback to identify recurring issues and proactively address them.
    * Invest in customer service technology to streamline issue tracking and resolution processes.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average resolution time over different time periods to identify trends.
    * Pareto charts to prioritize the types of customer issues that contribute most to the resolution time.
    
    
    
    """,
    "risk_warnings": """



    * Long resolution times can lead to customer frustration and dissatisfaction, impacting retention and loyalty.
    * Consistently high resolution times may indicate systemic issues in customer service operations that need to be addressed.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems with built-in case management and resolution tracking capabilities.
    * Workflow automation tools to streamline and standardize the issue resolution process.
    
    
    
    """,
    "integration_points": """



    * Integrate average resolution time tracking with customer feedback systems to understand the impact of resolution time on satisfaction.
    * Link resolution time data with employee performance management systems to identify training or resource needs.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving resolution time can enhance customer satisfaction and loyalty, leading to increased customer lifetime value.
    * However, overly aggressive reduction targets may compromise issue quality and customer satisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Support Ticket"], "last_validated": "2025-11-10T13:49:32.647873"},
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
                        350,
                        362,
                        360,
                        352,
                        351,
                        339,
                        337,
                        322,
                        342,
                        366,
                        323,
                        355
                ],
                "unit": "count"
        },
        "current": {
                "value": 355,
                "unit": "count",
                "change": 32,
                "change_percent": 9.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 346.58,
                "min": 322,
                "max": 366,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 54.41,
                        "percentage": 15.3
                },
                {
                        "category": "Segment B",
                        "value": 100.7,
                        "percentage": 28.4
                },
                {
                        "category": "Segment C",
                        "value": 50.85,
                        "percentage": 14.3
                },
                {
                        "category": "Segment D",
                        "value": 30.87,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 118.17,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.368596",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Issue Resolution Time"
        }
    },
}
