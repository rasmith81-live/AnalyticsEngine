"""
Sales Cycle Time Reduction Rate

The rate of reduction in the average sales cycle time due to sales enablement efforts.
"""

SALES_CYCLE_TIME_REDUCTION_RATE = {
    "code": "SALES_CYCLE_TIME_REDUCTION_RATE",
    "name": "Sales Cycle Time Reduction Rate",
    "description": "The rate of reduction in the average sales cycle time due to sales enablement efforts.",
    "formula": "(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    "calculation_formula": "(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Cycle Time Reduction Rate to be added.",
    "trend_analysis": """



    * An increasing sales cycle time reduction rate may indicate inefficiencies in the sales process or a lack of alignment between sales and marketing efforts.
    * A decreasing rate can signal improved sales enablement strategies, better use of technology, or more effective training for sales teams.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific stages in the sales cycle where the reduction rate is slower or faster?
    * How do our sales cycle time reduction rate compare with industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Implement sales enablement tools and technologies to automate manual tasks and streamline the sales process.
    * Provide ongoing training and coaching for sales teams to improve their efficiency and effectiveness in closing deals.
    * Analyze customer feedback and sales data to identify bottlenecks in the sales cycle and address them proactively.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales cycle time reduction rate over time.
    * Funnel charts to visualize the conversion rates at each stage of the sales cycle.
    
    
    
    """,
    "risk_warnings": """



    * A slow or stagnant reduction rate may lead to missed sales opportunities and decreased revenue.
    * Rapid reduction without proper analysis may result in overlooked quality or customer satisfaction issues.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) systems to track and analyze the sales cycle and customer interactions.
    * Sales enablement platforms to provide sales teams with the necessary content, training, and tools to close deals more effectively.
    
    
    
    """,
    "integration_points": """



    * Integrate sales cycle time reduction rate with customer feedback systems to understand the impact of sales processes on customer satisfaction.
    * Link with marketing automation systems to ensure alignment between marketing efforts and the sales cycle.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the sales cycle time reduction rate can lead to increased revenue and customer satisfaction, but it may also require investment in technology and training.
    * Conversely, a slow reduction rate can impact the overall sales performance and the ability to meet revenue targets.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.406300"},
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
                        65.8,
                        73.69,
                        77.41,
                        71.23,
                        77.59,
                        79.14,
                        73.93,
                        66.41,
                        69.03,
                        72.71,
                        73.61,
                        72.65
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.65,
                "unit": "%",
                "change": -0.96,
                "change_percent": -1.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.77,
                "min": 65.8,
                "max": 79.14,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 14.8,
                        "percentage": 20.4
                },
                {
                        "category": "Channel Sales",
                        "value": 16.15,
                        "percentage": 22.2
                },
                {
                        "category": "Online Sales",
                        "value": 13.76,
                        "percentage": 18.9
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.81,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 23.13,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.941592",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Cycle Time Reduction Rate"
        }
    },
}
