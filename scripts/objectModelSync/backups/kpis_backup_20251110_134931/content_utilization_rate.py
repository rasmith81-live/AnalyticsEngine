"""
Content Utilization Rate

The rate at which sales enablement materials are used by the sales team in their sales process.
"""

CONTENT_UTILIZATION_RATE = {
    "code": "CONTENT_UTILIZATION_RATE",
    "name": "Content Utilization Rate",
    "description": "The rate at which sales enablement materials are used by the sales team in their sales process.",
    "formula": "(Number of Times Content is Used / Total Available Content Pieces) * 100",
    "calculation_formula": "(Number of Times Content is Used / Total Available Content Pieces) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Content Utilization Rate to be added.",
    "trend_analysis": """

    * Increasing content utilization rate may indicate better alignment of sales materials with customer needs.
    * Decreasing rate could signal a lack of awareness or training on available sales enablement resources.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales enablement materials that are consistently underutilized?
    * How does the content utilization rate correlate with sales performance and conversion metrics?
    
    """,
    "actionable_tips": """

    * Regularly communicate the availability and benefits of sales enablement materials to the sales team.
    * Collect feedback from the sales team to understand their needs and preferences for sales enablement content.
    * Provide training and guidance on how to effectively use sales enablement materials in the sales process.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of content utilization rate over time.
    * Stacked bar charts comparing the utilization rates of different types of sales enablement materials.
    
    """,
    "risk_warnings": """

    * Low content utilization rate may lead to missed sales opportunities and decreased productivity.
    * High content utilization rate without corresponding sales performance improvements may indicate ineffective or irrelevant sales enablement materials.
    
    """,
    "tracking_tools": """

    * Sales enablement platforms like Seismic or Highspot for tracking and analyzing content utilization.
    * Customer relationship management (CRM) systems to link content utilization with sales outcomes.
    
    """,
    "integration_points": """

    * Integrate content utilization data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link content utilization with training and development programs to ensure alignment with sales strategies.
    
    """,
    "change_impact_analysis": """

    * Improving content utilization rate can lead to better customer engagement and higher conversion rates.
    * However, increasing the utilization rate without maintaining content quality can negatively impact the sales process and customer experience.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.140679"},
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
                        70.87,
                        78.96,
                        69.14,
                        70.69,
                        66.26,
                        80.63,
                        83.66,
                        65.23,
                        81.37,
                        75.76,
                        67.73,
                        76.28
                ],
                "unit": "%"
        },
        "current": {
                "value": 76.28,
                "unit": "%",
                "change": 8.55,
                "change_percent": 12.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.88,
                "min": 65.23,
                "max": 83.66,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.04,
                        "percentage": 28.9
                },
                {
                        "category": "Category B",
                        "value": 13.23,
                        "percentage": 17.3
                },
                {
                        "category": "Category C",
                        "value": 13.9,
                        "percentage": 18.2
                },
                {
                        "category": "Category D",
                        "value": 7.55,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 19.56,
                        "percentage": 25.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.140679",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Content Utilization Rate"
        }
    },
}
