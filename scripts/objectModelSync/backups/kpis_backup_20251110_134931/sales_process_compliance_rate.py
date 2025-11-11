"""
Sales Process Compliance Rate

The percentage of sales reps who are following the defined sales process as established by the sales enablement team.
"""

SALES_PROCESS_COMPLIANCE_RATE = {
    "code": "SALES_PROCESS_COMPLIANCE_RATE",
    "name": "Sales Process Compliance Rate",
    "description": "The percentage of sales reps who are following the defined sales process as established by the sales enablement team.",
    "formula": "(Number of Sales Followed Process / Total Number of Sales) * 100",
    "calculation_formula": "(Number of Sales Followed Process / Total Number of Sales) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Process Compliance Rate to be added.",
    "trend_analysis": """

    * An increasing sales process compliance rate may indicate better adoption of the defined sales process and improved sales performance.
    * A decreasing rate could signal resistance to the sales process, lack of understanding, or the need for process refinement.
    
    """,
    "diagnostic_questions": """

    * Are there specific stages or aspects of the sales process where compliance tends to be lower?
    * How are sales reps being trained and supported to ensure understanding and adherence to the defined sales process?
    
    """,
    "actionable_tips": """

    * Provide regular training and reinforcement of the sales process to ensure understanding and adoption.
    * Seek feedback from sales reps on the effectiveness of the sales process and make adjustments as needed.
    * Use sales enablement tools and technologies to automate and guide the sales process, making it easier for reps to comply.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the compliance rate over time to identify trends and patterns.
    * Comparison charts to visualize compliance rates across different sales teams or regions.
    
    """,
    "risk_warnings": """

    * Low sales process compliance can lead to inconsistent sales performance and missed opportunities.
    * High compliance without corresponding sales results may indicate a need to revisit the effectiveness of the defined sales process.
    
    """,
    "tracking_tools": """

    * Sales enablement platforms like Highspot or Seismic that provide guidance and support for the sales process.
    * CRM systems with built-in sales process tracking and reporting capabilities.
    
    """,
    "integration_points": """

    * Integrate sales process compliance data with performance management systems to align individual and team goals with process adherence.
    * Link compliance metrics with customer relationship management systems to understand the impact of the sales process on customer interactions and outcomes.
    
    """,
    "change_impact_analysis": """

    * Improving sales process compliance can lead to more predictable and consistent sales outcomes, contributing to overall business performance.
    * However, overly rigid enforcement of the sales process may stifle creativity and adaptability in sales approaches, potentially affecting customer relationships.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.538076"},
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
                        53.52,
                        48.0,
                        53.83,
                        49.26,
                        48.37,
                        54.27,
                        53.46,
                        46.02,
                        55.35,
                        55.18,
                        54.37,
                        51.8
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.8,
                "unit": "%",
                "change": -2.57,
                "change_percent": -4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 51.95,
                "min": 46.02,
                "max": 55.35,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.5,
                        "percentage": 20.3
                },
                {
                        "category": "Category B",
                        "value": 10.03,
                        "percentage": 19.4
                },
                {
                        "category": "Category C",
                        "value": 9.89,
                        "percentage": 19.1
                },
                {
                        "category": "Category D",
                        "value": 3.41,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 17.97,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.538076",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Process Compliance Rate"
        }
    },
}
