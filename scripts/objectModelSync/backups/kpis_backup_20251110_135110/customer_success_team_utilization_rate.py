"""
Customer Success Team Utilization Rate

The percentage of time customer success team members spend on productive or billable work.
"""

CUSTOMER_SUCCESS_TEAM_UTILIZATION_RATE = {
    "code": "CUSTOMER_SUCCESS_TEAM_UTILIZATION_RATE",
    "name": "Customer Success Team Utilization Rate",
    "description": "The percentage of time customer success team members spend on productive or billable work.",
    "formula": "Total Customer Engagement Time by the Team / Total Available Work Time",
    "calculation_formula": "Total Customer Engagement Time by the Team / Total Available Work Time",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Success Team Utilization Rate to be added.",
    "trend_analysis": """


    * An increasing customer success team utilization rate may indicate higher demand for customer support or onboarding services.
    * A decreasing rate could signal inefficiencies in customer success processes or underutilization of team members.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific customer segments or products that require more attention from the customer success team?
    * How does our customer success team utilization rate compare with industry benchmarks or with periods of high customer acquisition?
    
    
    """,
    "actionable_tips": """


    * Implement training and coaching programs to enhance the efficiency and effectiveness of customer success team members.
    * Leverage customer success software and automation tools to streamline repetitive tasks and free up time for more value-added activities.
    * Regularly review and optimize customer success workflows to eliminate bottlenecks and improve productivity.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer success team utilization rate over time.
    * Stacked bar charts comparing the distribution of time spent on different types of customer success activities.
    
    
    """,
    "risk_warnings": """


    * A low customer success team utilization rate may lead to missed opportunities for customer engagement and retention.
    * An excessively high rate could result in burnout and decreased quality of customer interactions.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems to track and analyze customer interactions and success activities.
    * Time tracking and productivity tools to monitor and optimize the use of customer success team members' time.
    
    
    """,
    "integration_points": """


    * Integrate customer success team utilization data with sales and marketing systems to align efforts and improve customer lifecycle management.
    * Link utilization rate with customer feedback and satisfaction metrics to understand the impact of customer success efforts on overall customer experience.
    
    
    """,
    "change_impact_analysis": """


    * Improving the customer success team utilization rate can lead to higher customer satisfaction and retention, positively impacting long-term revenue and profitability.
    * However, over-optimizing the rate without considering the quality of interactions may result in decreased customer loyalty and trust.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Prospect Engagement", "Sales Team"], "last_validated": "2025-11-10T13:49:32.891670"},
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
                        65.4,
                        65.39,
                        58.03,
                        52.07,
                        60.8,
                        69.63,
                        61.72,
                        54.56,
                        65.62,
                        70.36,
                        60.22,
                        65.18
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.18,
                "unit": "%",
                "change": 4.96,
                "change_percent": 8.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 62.41,
                "min": 52.07,
                "max": 70.36,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.96,
                        "percentage": 24.5
                },
                {
                        "category": "Category B",
                        "value": 15.27,
                        "percentage": 23.4
                },
                {
                        "category": "Category C",
                        "value": 5.37,
                        "percentage": 8.2
                },
                {
                        "category": "Category D",
                        "value": 7.34,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 21.24,
                        "percentage": 32.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.379114",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Team Utilization Rate"
        }
    },
}
