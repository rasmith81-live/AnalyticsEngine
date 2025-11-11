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
                        76.34,
                        70.72,
                        74.73,
                        77.12,
                        70.32,
                        69.74,
                        67.68,
                        61.86,
                        64.48,
                        61.09,
                        58.73,
                        58.75
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.75,
                "unit": "%",
                "change": 0.02,
                "change_percent": 0.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.63,
                "min": 58.73,
                "max": 77.12,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 13.25,
                        "percentage": 22.6
                },
                {
                        "category": "Existing Customers",
                        "value": 12.75,
                        "percentage": 21.7
                },
                {
                        "category": "VIP Customers",
                        "value": 10.36,
                        "percentage": 17.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.18,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 17.21,
                        "percentage": 29.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.840992",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Team Utilization Rate"
        }
    },
}
