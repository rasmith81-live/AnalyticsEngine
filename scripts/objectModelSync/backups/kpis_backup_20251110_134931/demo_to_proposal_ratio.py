"""
Demo-to-Proposal Ratio

The ratio of demos conducted to the proposals generated for prospects.
"""

DEMO_TO_PROPOSAL_RATIO = {
    "code": "DEMO_TO_PROPOSAL_RATIO",
    "name": "Demo-to-Proposal Ratio",
    "description": "The ratio of demos conducted to the proposals generated for prospects.",
    "formula": "Number of Proposals Sent / Number of Demos Conducted * 100",
    "calculation_formula": "Number of Proposals Sent / Number of Demos Conducted * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Demo-to-Proposal Ratio to be added.",
    "trend_analysis": """

    * An increasing demo-to-proposal ratio may indicate a more targeted approach in conducting demos, leading to higher quality prospects.
    * A decreasing ratio could signal a disconnect between the demos and the proposals, potentially pointing to issues in the sales process or product fit.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales representatives or teams with significantly higher or lower demo-to-proposal ratios?
    * What feedback have we received from prospects regarding the quality and relevance of the proposals generated?
    
    """,
    "actionable_tips": """

    * Provide additional training and support for sales representatives to improve their demo-to-proposal conversion skills.
    * Regularly review and update the content and format of proposals to ensure they align with the needs and expectations of prospects.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of demo-to-proposal ratios over time for individual sales representatives or teams.
    * Pie charts comparing the distribution of proposals generated from different types of demos (e.g., in-person, virtual, product-specific).
    
    """,
    "risk_warnings": """

    * A consistently low demo-to-proposal ratio may lead to wasted resources and decreased sales efficiency.
    * High variability in the ratio across different sales representatives could indicate a lack of standardized sales processes or training.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and analyze the conversion rates at each stage of the sales process.
    * Sales enablement platforms to provide sales representatives with the necessary tools and content to create compelling proposals.
    
    """,
    "integration_points": """

    * Integrate demo-to-proposal ratios with lead generation systems to identify the most effective sources of leads for generating high-quality proposals.
    * Link this KPI with customer feedback and satisfaction metrics to understand the impact of proposals on overall customer experience.
    
    """,
    "change_impact_analysis": """

    * Improving the demo-to-proposal ratio can lead to more efficient use of sales resources and potentially higher conversion rates.
    * However, a significant increase in the ratio may also indicate a more conservative approach in pursuing new prospects, potentially limiting overall sales growth.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Demo", "Product", "Product Adoption", "Product Usage", "Proposal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.439053"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        53.52,
                        44.75,
                        43.92,
                        49.56,
                        50.17,
                        51.25,
                        59.19,
                        44.69,
                        54.62,
                        42.61,
                        58.04,
                        46.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.89,
                "unit": "%",
                "change": -11.15,
                "change_percent": -19.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 49.93,
                "min": 42.61,
                "max": 59.19,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.24,
                        "percentage": 21.8
                },
                {
                        "category": "Category B",
                        "value": 6.17,
                        "percentage": 13.2
                },
                {
                        "category": "Category C",
                        "value": 9.73,
                        "percentage": 20.8
                },
                {
                        "category": "Category D",
                        "value": 2.84,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 17.91,
                        "percentage": 38.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.439053",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Demo-to-Proposal Ratio"
        }
    },
}
