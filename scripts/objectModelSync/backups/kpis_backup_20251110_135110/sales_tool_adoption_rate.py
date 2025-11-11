"""
Sales Tool Adoption Rate

The rate at which sales reps start using new sales tools provided in training.
"""

SALES_TOOL_ADOPTION_RATE = {
    "code": "SALES_TOOL_ADOPTION_RATE",
    "name": "Sales Tool Adoption Rate",
    "description": "The rate at which sales reps start using new sales tools provided in training.",
    "formula": "(Number of Reps Using Sales Tools / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Reps Using Sales Tools / Total Number of Sales Reps) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Tool Adoption Rate to be added.",
    "trend_analysis": """


    * An increasing sales tool adoption rate may indicate effective training and coaching programs that resonate with sales reps.
    * A decreasing rate could signal resistance to change, lack of understanding of the tool's value, or inadequate support for implementation.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales tools that are consistently underutilized, and if so, why?
    * How does the adoption rate compare with the level of training and support provided to sales reps?
    
    
    """,
    "actionable_tips": """


    * Provide clear communication on the benefits and impact of using new sales tools to motivate adoption.
    * Offer ongoing training and support to address any challenges or concerns related to using the new tools.
    * Seek feedback from sales reps to understand their experiences and identify areas for improvement in the adoption process.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the adoption rate over time to identify any spikes or declines in adoption.
    * Pie charts to visualize the distribution of adoption rates across different sales tools.
    
    
    """,
    "risk_warnings": """


    * Low adoption rates may lead to underutilization of valuable sales tools and hinder overall sales performance.
    * Inadequate adoption can indicate a need for reevaluation of the training and coaching programs to ensure effectiveness.
    
    
    """,
    "tracking_tools": """


    * CRM systems with built-in sales tool tracking capabilities to monitor adoption rates and usage patterns.
    * Sales enablement platforms that provide insights into the effectiveness of different sales tools and their impact on performance.
    
    
    """,
    "integration_points": """


    * Integrate sales tool adoption data with performance management systems to correlate adoption rates with sales outcomes.
    * Link adoption rates with training and development platforms to assess the impact of training programs on tool utilization.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales tool adoption can lead to increased efficiency, better customer engagement, and ultimately, higher sales revenue.
    * On the other hand, low adoption rates may result in missed opportunities, decreased productivity, and potential frustration among sales reps.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.523052"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        78.2,
                        73.04,
                        76.91,
                        68.45,
                        61.58,
                        74.84,
                        71.88,
                        80.56,
                        61.9,
                        67.3,
                        70.04,
                        80.68
                ],
                "unit": "%"
        },
        "current": {
                "value": 80.68,
                "unit": "%",
                "change": 10.64,
                "change_percent": 15.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.11,
                "min": 61.58,
                "max": 80.68,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.29,
                        "percentage": 20.2
                },
                {
                        "category": "Category B",
                        "value": 22.03,
                        "percentage": 27.3
                },
                {
                        "category": "Category C",
                        "value": 8.16,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 3.81,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 30.39,
                        "percentage": 37.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.664196",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Tool Adoption Rate"
        }
    },
}
