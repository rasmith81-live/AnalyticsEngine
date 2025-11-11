"""
Customer Journey Completion Rate

The percentage of customers completing the intended journey or experience designed by the company.
"""

CUSTOMER_JOURNEY_COMPLETION_RATE = {
    "code": "CUSTOMER_JOURNEY_COMPLETION_RATE",
    "name": "Customer Journey Completion Rate",
    "description": "The percentage of customers completing the intended journey or experience designed by the company.",
    "formula": "(Number of Customers Completing the Journey / Total Number of Customers Starting the Journey) * 100",
    "calculation_formula": "(Number of Customers Completing the Journey / Total Number of Customers Starting the Journey) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Journey Completion Rate to be added.",
    "trend_analysis": """


    * An increasing customer journey completion rate may indicate improved customer experience or more effective sales processes.
    * A decreasing rate could signal issues with product quality, customer service, or marketing effectiveness.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific touchpoints in the customer journey where a drop-off in completion occurs?
    * How does our customer journey completion rate compare with industry benchmarks or with our competitors?
    
    
    """,
    "actionable_tips": """


    * Conduct customer journey mapping to identify pain points and optimize the experience.
    * Provide additional training and resources to sales and customer service teams to ensure they can effectively guide customers through the journey.
    * Implement feedback mechanisms to capture customer insights and improve the journey based on their input.
    
    
    """,
    "visualization_suggestions": """


    * Funnel charts to visualize the drop-off at each stage of the customer journey.
    * Line graphs to track the trend of completion rates over time.
    
    
    """,
    "risk_warnings": """


    * Low completion rates can lead to lost sales and reduced customer loyalty.
    * Consistently high completion rates may indicate a lack of challenge or engagement in the customer journey, potentially leading to complacency or disinterest.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems to track customer interactions and identify areas for improvement.
    * Analytics tools to monitor and analyze customer behavior throughout the journey.
    
    
    """,
    "integration_points": """


    * Integrate customer journey completion data with marketing automation platforms to personalize and optimize the journey for different customer segments.
    * Link completion rate with sales performance metrics to understand the impact on revenue and customer acquisition costs.
    
    
    """,
    "change_impact_analysis": """


    * Improving the customer journey completion rate can lead to increased customer satisfaction and loyalty, potentially impacting long-term revenue and profitability.
    * However, changes in the completion rate may also affect sales team workload and resource allocation, requiring adjustments in sales management strategies.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"], "last_validated": "2025-11-10T13:49:32.841384"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
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
                        67.58,
                        64.77,
                        52.56,
                        59.05,
                        65.42,
                        67.24,
                        58.39,
                        66.53,
                        53.74,
                        69.94,
                        71.91,
                        66.42
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.42,
                "unit": "%",
                "change": -5.49,
                "change_percent": -7.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.63,
                "min": 52.56,
                "max": 71.91,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.28,
                        "percentage": 18.5
                },
                {
                        "category": "Category B",
                        "value": 10.96,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 11.15,
                        "percentage": 16.8
                },
                {
                        "category": "Category D",
                        "value": 7.29,
                        "percentage": 11.0
                },
                {
                        "category": "Other",
                        "value": 24.74,
                        "percentage": 37.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.289428",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Journey Completion Rate"
        }
    },
}
