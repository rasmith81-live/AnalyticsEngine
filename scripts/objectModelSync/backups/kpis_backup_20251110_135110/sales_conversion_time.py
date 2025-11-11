"""
Sales Conversion Time

The average amount of time it takes a lead to become a sale, indicating the efficiency of the sales process.
"""

SALES_CONVERSION_TIME = {
    "code": "SALES_CONVERSION_TIME",
    "name": "Sales Conversion Time",
    "description": "The average amount of time it takes a lead to become a sale, indicating the efficiency of the sales process.",
    "formula": "Average Time from Lead Generation to Closing the Sale",
    "calculation_formula": "Average Time from Lead Generation to Closing the Sale",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Conversion Time to be added.",
    "trend_analysis": """


    * A decreasing sales conversion time may indicate improvements in the sales process, such as better lead qualification or more effective closing techniques.
    * An increasing conversion time could signal issues in the sales process, such as longer lead nurturing times or ineffective follow-up strategies.
    
    
    """,
    "diagnostic_questions": """


    * What are the average times spent in each stage of the sales process, from lead qualification to closing?
    * Are there specific points in the sales process where leads tend to get stuck or delayed?
    
    
    """,
    "actionable_tips": """


    * Implement sales automation tools to streamline lead management and follow-up processes.
    * Provide additional training and resources for sales representatives to improve their efficiency in moving leads through the sales process.
    * Analyze and optimize the sales process to identify and eliminate bottlenecks that may be prolonging conversion times.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the average conversion time over specific time periods to identify trends.
    * Funnel charts to visualize the drop-off points in the sales process where leads may be getting delayed.
    
    
    """,
    "risk_warnings": """


    * Long conversion times can lead to lost opportunities and potential revenue.
    * Rapidly decreasing conversion times may indicate a focus on quantity over quality, potentially leading to customer dissatisfaction or churn.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track lead interactions and monitor sales pipeline velocity.
    * Sales analytics platforms to identify patterns and insights that can help improve the sales process.
    
    
    """,
    "integration_points": """


    * Integrate sales conversion time data with marketing analytics to understand the quality of leads being generated and their impact on the sales process.
    * Link with customer feedback systems to correlate conversion times with customer satisfaction and identify areas for improvement.
    
    
    """,
    "change_impact_analysis": """


    * Reducing sales conversion time can lead to increased revenue and improved sales team morale, but it may also require additional resources and investments in technology.
    * Significantly increasing sales conversion time may indicate a need for reevaluation of sales strategies and resource allocation.
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Lead", "Lead Qualification", "Lost Sale", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.401556"},
    "required_objects": [],
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
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
                        28.9,
                        27.4,
                        28.9,
                        28.5,
                        31.9,
                        26.8,
                        27.6,
                        31.8,
                        28.9,
                        28.1,
                        29.6,
                        28.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 28.5,
                "unit": "days",
                "change": -1.1,
                "change_percent": -3.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 28.91,
                "min": 26.8,
                "max": 31.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.51,
                        "percentage": 33.4
                },
                {
                        "category": "Category B",
                        "value": 3.0,
                        "percentage": 10.5
                },
                {
                        "category": "Category C",
                        "value": 2.48,
                        "percentage": 8.7
                },
                {
                        "category": "Category D",
                        "value": 3.63,
                        "percentage": 12.7
                },
                {
                        "category": "Other",
                        "value": 9.88,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.352343",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Sales Conversion Time"
        }
    },
}
