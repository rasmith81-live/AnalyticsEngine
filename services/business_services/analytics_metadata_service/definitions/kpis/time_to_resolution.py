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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.722201"},
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
                        18.2,
                        15.5,
                        14.9,
                        20.4,
                        14.4,
                        17.9,
                        18.6,
                        18.9,
                        16.5,
                        15.5,
                        20.9,
                        13.8
                ],
                "unit": "days"
        },
        "current": {
                "value": 13.8,
                "unit": "days",
                "change": -7.1,
                "change_percent": -34.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 17.13,
                "min": 13.8,
                "max": 20.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 4.25,
                        "percentage": 30.8
                },
                {
                        "category": "Segment B",
                        "value": 1.53,
                        "percentage": 11.1
                },
                {
                        "category": "Segment C",
                        "value": 1.41,
                        "percentage": 10.2
                },
                {
                        "category": "Segment D",
                        "value": 1.23,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 5.38,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.791726",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time to Resolution"
        }
    },
}
