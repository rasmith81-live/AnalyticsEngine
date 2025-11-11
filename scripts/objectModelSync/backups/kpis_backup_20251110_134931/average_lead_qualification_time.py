"""
Average Lead Qualification Time

The average time taken to assess and qualify a new sales lead.
"""

AVERAGE_LEAD_QUALIFICATION_TIME = {
    "code": "AVERAGE_LEAD_QUALIFICATION_TIME",
    "name": "Average Lead Qualification Time",
    "description": "The average time taken to assess and qualify a new sales lead.",
    "formula": "Total Time to Qualify Leads / Total Number of Qualified Leads",
    "calculation_formula": "Total Time to Qualify Leads / Total Number of Qualified Leads",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Lead Qualification Time to be added.",
    "trend_analysis": """

    * Shortening lead qualification times may indicate improved efficiency in the sales process or better targeting of potential leads.
    * An increasing average lead qualification time could signal issues with lead quality, sales team capacity, or changes in market dynamics.
    
    """,
    "diagnostic_questions": """

    * Are there specific criteria or benchmarks used to qualify leads, and are they still relevant and effective?
    * How does the lead qualification time vary across different sales reps or regions, and what factors contribute to these differences?
    
    """,
    "actionable_tips": """

    * Implement lead scoring systems to prioritize high-quality leads and reduce time spent on low-potential prospects.
    * Provide ongoing training and support for sales reps to improve their ability to quickly assess lead potential.
    * Regularly review and update lead qualification criteria to ensure they align with changing market conditions and customer needs.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average lead qualification time over time to identify trends and potential seasonality.
    * Comparison bar charts to visualize lead qualification times across different sales reps or territories.
    
    """,
    "risk_warnings": """

    * Long lead qualification times can result in missed opportunities and decreased conversion rates.
    * Rapidly decreasing lead qualification times may indicate a drop in lead quality or insufficient attention to thorough qualification processes.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software with lead tracking and scoring capabilities to streamline lead qualification processes.
    * Sales analytics tools to identify patterns and bottlenecks in the lead qualification process.
    
    """,
    "integration_points": """

    * Integrate lead qualification time data with sales performance metrics to understand the impact of lead quality on overall sales results.
    * Link lead qualification time with marketing campaign data to assess the effectiveness of lead generation efforts.
    
    """,
    "change_impact_analysis": """

    * Reducing lead qualification time can lead to increased sales productivity and potentially higher revenue.
    * However, a significant decrease in lead qualification time without proper lead quality assessment may result in increased customer dissatisfaction and higher churn rates.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.022379"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        378,
                        368,
                        377,
                        370,
                        374,
                        408,
                        409,
                        399,
                        409,
                        392,
                        368,
                        404
                ],
                "unit": "count"
        },
        "current": {
                "value": 404,
                "unit": "count",
                "change": 36,
                "change_percent": 9.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 388.0,
                "min": 368,
                "max": 409,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 72.74,
                        "percentage": 18.0
                },
                {
                        "category": "Category B",
                        "value": 105.27,
                        "percentage": 26.1
                },
                {
                        "category": "Category C",
                        "value": 52.03,
                        "percentage": 12.9
                },
                {
                        "category": "Category D",
                        "value": 44.66,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 129.3,
                        "percentage": 32.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.022379",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Lead Qualification Time"
        }
    },
}
