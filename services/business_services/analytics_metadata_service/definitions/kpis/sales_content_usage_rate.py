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
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product Usage", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.397895"},
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
                        76.86,
                        57.86,
                        68.22,
                        76.77,
                        61.78,
                        76.81,
                        73.64,
                        67.75,
                        65.77,
                        60.52,
                        61.35,
                        76.24
                ],
                "unit": "%"
        },
        "current": {
                "value": 76.24,
                "unit": "%",
                "change": 14.89,
                "change_percent": 24.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.63,
                "min": 57.86,
                "max": 76.86,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 23.79,
                        "percentage": 31.2
                },
                {
                        "category": "Channel Sales",
                        "value": 8.48,
                        "percentage": 11.1
                },
                {
                        "category": "Online Sales",
                        "value": 14.14,
                        "percentage": 18.5
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.08,
                        "percentage": 4.0
                },
                {
                        "category": "Other",
                        "value": 26.75,
                        "percentage": 35.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.922323",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Content Usage Rate"
        }
    },
}
