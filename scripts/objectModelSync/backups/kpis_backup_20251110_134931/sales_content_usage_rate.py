"""
Sales Content Usage Rate

The usage rate of sales content created by the sales enablement team by sales reps, such as presentations, proposals, and case studies.
"""

SALES_CONTENT_USAGE_RATE = {
    "code": "SALES_CONTENT_USAGE_RATE",
    "name": "Sales Content Usage Rate",
    "description": "The usage rate of sales content created by the sales enablement team by sales reps, such as presentations, proposals, and case studies.",
    "formula": "(Number of Times Content is Used / Total Number of Sales Activities) * 100",
    "calculation_formula": "(Number of Times Content is Used / Total Number of Sales Activities) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Content Usage Rate to be added.",
    "trend_analysis": """

    * An increasing sales content usage rate may indicate better alignment between the content created and the needs of sales reps, resulting in more effective sales interactions.
    * A decreasing rate could signal a lack of relevance or accessibility of the content, leading to missed sales opportunities or ineffective customer engagements.
    
    """,
    "diagnostic_questions": """

    * Are sales reps actively using the provided sales content, and if not, what barriers are preventing its usage?
    * How does the usage rate of different types of sales content vary, and what insights can be gained from this variation?
    
    """,
    "actionable_tips": """

    * Regularly gather feedback from sales reps to understand their content needs and preferences, and adjust content creation accordingly.
    * Ensure easy access to sales content through a centralized and user-friendly platform, and provide training on how to effectively utilize the available resources.
    * Monitor the performance of sales content in terms of conversion rates and customer feedback, and iterate on content creation based on these insights.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the usage rate of different types of sales content over time to identify trends and patterns.
    * Stacked bar charts comparing the overall usage rate of sales content across different sales teams or regions to pinpoint areas of high and low adoption.
    
    """,
    "risk_warnings": """

    * A low sales content usage rate may lead to inconsistent messaging and missed sales opportunities, impacting revenue and customer relationships.
    * An excessively high usage rate of certain content may indicate a lack of variety or customization, potentially leading to decreased effectiveness in engaging diverse customer segments.
    
    """,
    "tracking_tools": """

    * Sales enablement platforms like Seismic or Highspot that provide analytics on content usage and performance.
    * Customer relationship management (CRM) systems with integrated content management capabilities to track content usage in the context of sales activities.
    
    """,
    "integration_points": """

    * Integrate sales content usage data with sales performance metrics to understand the impact of content on sales outcomes and identify areas for improvement.
    * Link content usage with customer feedback and engagement data to assess the effectiveness of content in driving customer interactions and conversions.
    
    """,
    "change_impact_analysis": """

    * An increase in sales content usage rate can lead to improved sales productivity and customer engagement, potentially driving revenue growth.
    * Conversely, a decrease in usage rate may result in missed sales opportunities and a negative impact on the overall effectiveness of the sales team.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product Usage", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.198907"},
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
                        59.16,
                        56.53,
                        47.3,
                        43.22,
                        54.79,
                        52.17,
                        57.76,
                        58.34,
                        60.98,
                        54.79,
                        51.12,
                        50.56
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.56,
                "unit": "%",
                "change": -0.56,
                "change_percent": -1.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.89,
                "min": 43.22,
                "max": 60.98,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.14,
                        "percentage": 18.1
                },
                {
                        "category": "Category B",
                        "value": 8.12,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 8.29,
                        "percentage": 16.4
                },
                {
                        "category": "Category D",
                        "value": 4.0,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 21.01,
                        "percentage": 41.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.198907",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Content Usage Rate"
        }
    },
}
