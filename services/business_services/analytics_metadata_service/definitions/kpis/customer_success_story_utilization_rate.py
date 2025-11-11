"""
Customer Success Story Utilization Rate

The rate at which customer success stories and case studies are used in the sales process.
"""

CUSTOMER_SUCCESS_STORY_UTILIZATION_RATE = {
    "code": "CUSTOMER_SUCCESS_STORY_UTILIZATION_RATE",
    "name": "Customer Success Story Utilization Rate",
    "description": "The rate at which customer success stories and case studies are used in the sales process.",
    "formula": "(Number of Times Success Stories are Used / Total Number of Sales Engagements) * 100",
    "calculation_formula": "(Number of Times Success Stories are Used / Total Number of Sales Engagements) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Success Story Utilization Rate to be added.",
    "trend_analysis": """



    * An increasing customer success story utilization rate may indicate a more effective sales process and better alignment with customer needs.
    * A decreasing rate could signal a lack of relevant success stories or a disconnect between the sales team and customer needs.
    
    
    
    """,
    "diagnostic_questions": """



    * Are the customer success stories being used at the right stages of the sales process?
    * Are the success stories resonating with the target audience, or do they need to be tailored to different buyer personas?
    
    
    
    """,
    "actionable_tips": """



    * Train the sales team on how to effectively incorporate customer success stories into their pitches and presentations.
    * Create a library of success stories that cover a wide range of industries and use cases to ensure relevance to different prospects.
    * Solicit feedback from the sales team and customers to continuously improve the quality and impact of the success stories.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of success story utilization over time.
    * Pie charts to illustrate the distribution of success story usage across different customer segments or product lines.
    
    
    
    """,
    "risk_warnings": """



    * A low utilization rate may indicate a disconnect between the sales team and the value proposition of the product or service.
    * Over-reliance on a few success stories may lead to a lack of variety and relevance for different prospects.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems with built-in capabilities for tracking the usage of customer success stories.
    * Content management systems to organize and categorize success stories for easy access by the sales team.
    
    
    
    """,
    "integration_points": """



    * Integrate success story utilization data with sales performance metrics to understand the impact of using these stories on closing deals.
    * Link success story usage with customer feedback and satisfaction scores to gauge the effectiveness of the stories in influencing purchase decisions.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the utilization rate can lead to higher conversion rates and increased customer satisfaction, ultimately impacting revenue and customer retention.
    * On the other hand, a low utilization rate may indicate missed opportunities and a need for reevaluation of the sales strategy and messaging.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.888251"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        74.99,
                        77.98,
                        64.09,
                        78.41,
                        78.01,
                        68.52,
                        82.55,
                        75.05,
                        70.11,
                        70.31,
                        64.26,
                        66.52
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.52,
                "unit": "%",
                "change": 2.26,
                "change_percent": 3.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 72.57,
                "min": 64.09,
                "max": 82.55,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 17.25,
                        "percentage": 25.9
                },
                {
                        "category": "Existing Customers",
                        "value": 11.36,
                        "percentage": 17.1
                },
                {
                        "category": "VIP Customers",
                        "value": 10.85,
                        "percentage": 16.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 6.05,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 21.01,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.831144",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Story Utilization Rate"
        }
    },
}
