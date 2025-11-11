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
                        75.72,
                        70.62,
                        74.31,
                        65.37,
                        73.62,
                        78.07,
                        65.8,
                        63.52,
                        63.46,
                        69.16,
                        63.13,
                        78.72
                ],
                "unit": "%"
        },
        "current": {
                "value": 78.72,
                "unit": "%",
                "change": 15.59,
                "change_percent": 24.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 70.12,
                "min": 63.13,
                "max": 78.72,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 22.01,
                        "percentage": 28.0
                },
                {
                        "category": "Existing Customers",
                        "value": 16.73,
                        "percentage": 21.3
                },
                {
                        "category": "VIP Customers",
                        "value": 7.16,
                        "percentage": 9.1
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.56,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 28.26,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.703283",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Journey Completion Rate"
        }
    },
}
