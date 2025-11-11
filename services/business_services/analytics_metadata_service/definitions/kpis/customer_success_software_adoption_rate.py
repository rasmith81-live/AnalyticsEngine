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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product Adoption", "Sales Team"], "last_validated": "2025-11-10T13:49:32.887194"},
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
                        65.37,
                        66.43,
                        61.87,
                        61.3,
                        67.52,
                        74.22,
                        60.12,
                        58.82,
                        68.21,
                        73.39,
                        60.37,
                        75.02
                ],
                "unit": "%"
        },
        "current": {
                "value": 75.02,
                "unit": "%",
                "change": 14.65,
                "change_percent": 24.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 66.05,
                "min": 58.82,
                "max": 75.02,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 12.14,
                        "percentage": 16.2
                },
                {
                        "category": "Existing Customers",
                        "value": 15.11,
                        "percentage": 20.1
                },
                {
                        "category": "VIP Customers",
                        "value": 16.54,
                        "percentage": 22.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.23,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 27.0,
                        "percentage": 36.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.822378",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Software Adoption Rate"
        }
    },
}
