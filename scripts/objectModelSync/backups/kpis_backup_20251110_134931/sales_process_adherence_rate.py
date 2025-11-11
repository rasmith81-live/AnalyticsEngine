"""
Sales Process Adherence Rate

The percentage of sales reps following the prescribed sales process.
"""

SALES_PROCESS_ADHERENCE_RATE = {
    "code": "SALES_PROCESS_ADHERENCE_RATE",
    "name": "Sales Process Adherence Rate",
    "description": "The percentage of sales reps following the prescribed sales process.",
    "formula": "(Number of Sales Following the Process / Total Number of Sales) * 100",
    "calculation_formula": "(Number of Sales Following the Process / Total Number of Sales) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Process Adherence Rate to be added.",
    "trend_analysis": """

    * An increasing sales process adherence rate may indicate better training or improved understanding of the sales process among reps.
    * A decreasing rate could signal a need for process re-evaluation, changes in market conditions, or lack of enforcement from sales management.
    
    """,
    "diagnostic_questions": """

    * Are there specific stages of the sales process where adherence tends to drop off?
    * How does the sales process adherence rate vary among different sales teams or regions?
    
    """,
    "actionable_tips": """

    * Regularly review and update the sales process to ensure it aligns with current market conditions and customer needs.
    * Provide ongoing training and coaching to reinforce the importance of following the sales process.
    * Implement sales management tools and CRM systems that can track and report on sales process adherence.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of sales process adherence rate over time.
    * Comparison bar charts to visualize adherence rates across different sales teams or regions.
    
    """,
    "risk_warnings": """

    * Low sales process adherence can lead to inconsistent customer experiences and lost sales opportunities.
    * High adherence without flexibility can result in missed opportunities for creative problem-solving and relationship-building.
    
    """,
    "tracking_tools": """

    * CRM systems with built-in process adherence tracking and reporting capabilities.
    * Sales enablement platforms that provide guidance and support for following the sales process.
    
    """,
    "integration_points": """

    * Integrate sales process adherence data with performance management systems to align coaching and development efforts with individual needs.
    * Link adherence metrics with customer feedback and satisfaction scores to understand the impact on customer experience.
    
    """,
    "change_impact_analysis": """

    * Improving sales process adherence can lead to more predictable sales outcomes and better customer relationships.
    * However, overly rigid adherence may stifle innovation and creativity in sales approaches.
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.530935"},
    "required_objects": [],
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
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
                        77.03,
                        62.65,
                        74.78,
                        73.31,
                        72.91,
                        65.83,
                        81.31,
                        77.79,
                        73.38,
                        77.12,
                        75.84,
                        64.32
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.32,
                "unit": "%",
                "change": -11.52,
                "change_percent": -15.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.02,
                "min": 62.65,
                "max": 81.31,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.13,
                        "percentage": 25.1
                },
                {
                        "category": "Category B",
                        "value": 15.62,
                        "percentage": 24.3
                },
                {
                        "category": "Category C",
                        "value": 8.52,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 5.15,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 18.9,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.530935",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Process Adherence Rate"
        }
    },
}
