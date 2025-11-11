"""
Advocacy Actions

The number of times customers engage in advocacy behaviors, such as providing testimonials or participating in case studies.
"""

ADVOCACY_ACTIONS = {
    "code": "ADVOCACY_ACTIONS",
    "name": "Advocacy Actions",
    "description": "The number of times customers engage in advocacy behaviors, such as providing testimonials or participating in case studies.",
    "formula": "Total Number of Advocacy Actions Taken by Customers / Total Number of Customers",
    "calculation_formula": "Total Number of Advocacy Actions Taken by Customers / Total Number of Customers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Advocacy Actions to be added.",
    "trend_analysis": """


    * Increasing advocacy actions may indicate a growing base of satisfied customers willing to share their positive experiences.
    * Conversely, a decrease in advocacy actions could signal dissatisfaction or a lack of engagement with the customer base.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products or services that customers are more likely to advocate for?
    * What barriers or incentives exist that may impact customer willingness to participate in advocacy actions?
    
    
    """,
    "actionable_tips": """


    * Implement a formal customer advocacy program to encourage and reward customer participation.
    * Regularly solicit feedback and testimonials from satisfied customers to build a library of advocacy content.
    * Provide training and resources to sales and customer service teams to effectively identify and nurture potential advocates.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of advocacy actions over time.
    * Pie charts to illustrate the distribution of advocacy actions by customer segment or product category.
    
    
    """,
    "risk_warnings": """


    * A lack of advocacy actions may indicate a disconnect between customer expectations and the actual experience provided.
    * Overreliance on a small group of advocates may lead to skewed perceptions of overall customer satisfaction.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems to track and manage customer interactions and feedback.
    * Advocacy marketing platforms to automate and streamline the process of gathering and leveraging customer testimonials and case studies.
    
    
    """,
    "integration_points": """


    * Integrate advocacy actions with sales and marketing systems to measure the impact on lead generation and conversion rates.
    * Link customer advocacy data with customer satisfaction metrics to understand the relationship between advocacy and overall satisfaction.
    
    
    """,
    "change_impact_analysis": """


    * Increased advocacy actions can lead to higher brand visibility and credibility, positively impacting sales and marketing efforts.
    * Conversely, a decline in advocacy actions may result in decreased trust and loyalty, affecting customer retention and lifetime value.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity"], "last_validated": "2025-11-10T13:49:32.639283"},
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
                        70,
                        64,
                        92,
                        84,
                        63,
                        80,
                        99,
                        59,
                        80,
                        58,
                        79,
                        55
                ],
                "unit": "count"
        },
        "current": {
                "value": 55,
                "unit": "count",
                "change": -24,
                "change_percent": -30.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 73.58,
                "min": 55,
                "max": 99,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.08,
                        "percentage": 22.0
                },
                {
                        "category": "Category B",
                        "value": 8.04,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 5.44,
                        "percentage": 9.9
                },
                {
                        "category": "Category D",
                        "value": 7.47,
                        "percentage": 13.6
                },
                {
                        "category": "Other",
                        "value": 21.97,
                        "percentage": 39.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.006539",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Advocacy Actions"
        }
    },
}
