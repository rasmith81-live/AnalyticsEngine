"""
Deal Acceleration Rate

The rate at which sales enablement tools and strategies help to shorten the sales cycle for deals in the pipeline.
"""

DEAL_ACCELERATION_RATE = {
    "code": "DEAL_ACCELERATION_RATE",
    "name": "Deal Acceleration Rate",
    "description": "The rate at which sales enablement tools and strategies help to shorten the sales cycle for deals in the pipeline.",
    "formula": "(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    "calculation_formula": "(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Acceleration Rate to be added.",
    "trend_analysis": """

    * Increasing deal acceleration rate may indicate the effectiveness of new sales enablement tools or strategies.
    * A decreasing rate could signal a need for reevaluation of current sales enablement methods or a shift in customer behavior.
    
    """,
    "diagnostic_questions": """

    * Are there specific stages in the sales cycle where deals tend to get stuck or delayed?
    * How do our deal acceleration rates compare with industry benchmarks or with competitors?
    
    """,
    "actionable_tips": """

    * Provide targeted training for sales teams on how to effectively use sales enablement tools to move deals forward.
    * Analyze customer feedback to identify potential pain points in the sales process and address them with relevant enablement resources.
    * Regularly review and update the sales enablement toolkit to ensure it aligns with the evolving needs of the sales team and customers.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of deal acceleration rates over time.
    * Funnel charts to visualize the progression of deals through different stages of the sales cycle.
    
    """,
    "risk_warnings": """

    * A consistently low deal acceleration rate may lead to missed revenue targets and decreased sales team motivation.
    * A sudden spike in deal acceleration rate could indicate a potential issue with deal quality or customer satisfaction.
    
    """,
    "tracking_tools": """

    * CRM systems with built-in sales enablement features to track the impact of enablement tools on deal acceleration.
    * Data analytics platforms to identify patterns and correlations between enablement strategies and deal acceleration rates.
    
    """,
    "integration_points": """

    * Integrate deal acceleration rate tracking with performance management systems to align sales team incentives with the goal of shortening the sales cycle.
    * Link sales enablement platforms with customer relationship management systems to understand the impact of enablement tools on customer interactions and deal progression.
    
    """,
    "change_impact_analysis": """

    * Improving deal acceleration rates can lead to increased sales efficiency and potentially higher revenue generation.
    * However, a focus solely on accelerating deals may impact the quality of customer interactions and long-term customer relationships.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.400780"},
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
                        57.73,
                        51.26,
                        61.47,
                        60.23,
                        51.34,
                        61.86,
                        50.25,
                        53.5,
                        59.7,
                        50.11,
                        66.28,
                        52.22
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.22,
                "unit": "%",
                "change": -14.06,
                "change_percent": -21.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.33,
                "min": 50.11,
                "max": 66.28,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.49,
                        "percentage": 33.5
                },
                {
                        "category": "Category B",
                        "value": 5.37,
                        "percentage": 10.3
                },
                {
                        "category": "Category C",
                        "value": 4.92,
                        "percentage": 9.4
                },
                {
                        "category": "Category D",
                        "value": 3.69,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 20.75,
                        "percentage": 39.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.400780",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Deal Acceleration Rate"
        }
    },
}
