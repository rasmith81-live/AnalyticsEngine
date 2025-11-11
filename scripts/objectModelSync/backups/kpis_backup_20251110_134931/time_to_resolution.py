"""
Time to Resolution

The amount of time it takes for the Customer Success Team to resolve a customer issue. This KPI measures the team's effectiveness in providing timely solutions to customer problems.
"""

TIME_TO_RESOLUTION = {
    "code": "TIME_TO_RESOLUTION",
    "name": "Time to Resolution",
    "description": "The amount of time it takes for the Customer Success Team to resolve a customer issue. This KPI measures the team's effectiveness in providing timely solutions to customer problems.",
    "formula": "Average Time Between Ticket Creation and Resolution",
    "calculation_formula": "Average Time Between Ticket Creation and Resolution",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Resolution to be added.",
    "trend_analysis": """

    * Increasing time to resolution may indicate growing customer issues or inefficiencies in the support process.
    * Decreasing time to resolution can signal improved customer support workflows or better product stability.
    
    """,
    "diagnostic_questions": """

    * Are there common patterns or root causes behind prolonged resolution times?
    * How does our time to resolution compare with industry benchmarks or customer expectations?
    
    """,
    "actionable_tips": """

    * Implement customer support automation to streamline issue identification and resolution.
    * Provide ongoing training and resources for the support team to enhance their problem-solving skills.
    * Regularly review and update support processes to eliminate bottlenecks and inefficiencies.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average time to resolution over time.
    * Pareto charts to identify the most common issues and their resolution times.
    
    """,
    "risk_warnings": """

    * Extended resolution times can lead to customer dissatisfaction and potential churn.
    * Consistently high resolution times may indicate systemic issues in product quality or customer support.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems with built-in support ticketing and tracking capabilities.
    * Workflow automation tools to streamline issue escalation and assignment.
    
    """,
    "integration_points": """

    * Integrate time to resolution data with customer satisfaction metrics to understand the impact of support performance on customer happiness.
    * Link resolution time tracking with product development systems to address recurring issues at their root.
    
    """,
    "change_impact_analysis": """

    * Reducing time to resolution can lead to higher customer satisfaction and loyalty, positively impacting long-term revenue.
    * However, overly aggressive targets for resolution times may sacrifice the quality of support provided.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"], "last_validated": "2025-11-10T13:43:25.053470"},
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
                        3.8,
                        9.3,
                        3.6,
                        10.4,
                        11.2,
                        5.8,
                        9.4,
                        4.3,
                        10.6,
                        3.6,
                        5.1,
                        11.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 11.1,
                "unit": "days",
                "change": 6.0,
                "change_percent": 117.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 7.35,
                "min": 3.6,
                "max": 11.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 2.47,
                        "percentage": 22.3
                },
                {
                        "category": "Category B",
                        "value": 2.57,
                        "percentage": 23.2
                },
                {
                        "category": "Category C",
                        "value": 1.74,
                        "percentage": 15.7
                },
                {
                        "category": "Category D",
                        "value": 1.03,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 3.29,
                        "percentage": 29.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.053470",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time to Resolution"
        }
    },
}
