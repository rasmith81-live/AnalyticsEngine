"""
Customer Success Software Adoption Rate

The rate at which customer success software tools are adopted and effectively used by the team.
"""

CUSTOMER_SUCCESS_SOFTWARE_ADOPTION_RATE = {
    "code": "CUSTOMER_SUCCESS_SOFTWARE_ADOPTION_RATE",
    "name": "Customer Success Software Adoption Rate",
    "description": "The rate at which customer success software tools are adopted and effectively used by the team.",
    "formula": "(Number of Customers Using the Software / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Using the Software / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Success Software Adoption Rate to be added.",
    "trend_analysis": """

    * An increasing adoption rate may indicate better training and support for the customer success software tools.
    * A decreasing rate could signal resistance to change or a lack of perceived value in the software.
    
    """,
    "diagnostic_questions": """

    * Are there specific features of the software that are underutilized or causing frustration for the team?
    * How does the adoption rate compare with industry benchmarks or with the initial goals set for implementation?
    
    """,
    "actionable_tips": """

    * Provide additional training and resources to help users understand the benefits and best practices of the software.
    * Seek feedback from the team to identify any barriers to adoption and address them proactively.
    * Highlight success stories and use cases to demonstrate the positive impact of the software on the team's performance.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the adoption rate over time to identify any spikes or dips in usage.
    * Comparison charts to visualize the adoption rate across different teams or departments.
    
    """,
    "risk_warnings": """

    * Low adoption rates may lead to inefficiencies and missed opportunities for leveraging the software's capabilities.
    * Resistance to using the software could indicate broader issues with change management or communication within the organization.
    
    """,
    "tracking_tools": """

    * Customer success platforms like Gainsight or Totango to track and analyze user engagement with the software.
    * Collaboration tools such as Slack or Microsoft Teams to facilitate communication and knowledge sharing around the software.
    
    """,
    "integration_points": """

    * Integrate adoption rate data with performance reviews and goal setting to align individual objectives with software utilization.
    * Link adoption rate metrics with customer feedback and satisfaction scores to understand the impact of the software on overall success.
    
    """,
    "change_impact_analysis": """

    * Improving the adoption rate can lead to better customer retention and increased upsell opportunities.
    * On the other hand, low adoption rates may result in missed opportunities for proactive customer engagement and support.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product Adoption", "Sales Team"], "last_validated": "2025-11-10T13:43:23.369881"},
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
                        61.88,
                        45.96,
                        53.29,
                        47.31,
                        51.48,
                        55.8,
                        55.59,
                        48.29,
                        44.1,
                        49.26,
                        59.5,
                        59.84
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.84,
                "unit": "%",
                "change": 0.34,
                "change_percent": 0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 52.69,
                "min": 44.1,
                "max": 61.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.26,
                        "percentage": 15.5
                },
                {
                        "category": "Category B",
                        "value": 17.29,
                        "percentage": 28.9
                },
                {
                        "category": "Category C",
                        "value": 10.72,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 5.82,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 16.75,
                        "percentage": 28.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.369881",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Software Adoption Rate"
        }
    },
}
