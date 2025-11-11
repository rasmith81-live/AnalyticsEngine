"""
Average Sales Call Duration

The average length of time of a sales call.
"""

AVERAGE_SALES_CALL_DURATION = {
    "code": "AVERAGE_SALES_CALL_DURATION",
    "name": "Average Sales Call Duration",
    "description": "The average length of time of a sales call.",
    "formula": "Total Time of Sales Calls / Number of Sales Calls",
    "calculation_formula": "Total Time of Sales Calls / Number of Sales Calls",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Sales Call Duration to be added.",
    "trend_analysis": """

    * An increasing average sales call duration may indicate more in-depth conversations with potential customers, potentially leading to higher quality leads and better conversion rates.
    * A decreasing duration could signal a more efficient sales process, but it may also indicate rushed or incomplete interactions with prospects.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales reps or teams that consistently have longer or shorter call durations?
    * How does the average call duration correlate with the conversion rates and overall sales performance?
    
    """,
    "actionable_tips": """

    * Provide sales training and coaching to help reps engage in more effective and efficient conversations with prospects.
    * Implement call monitoring and analysis tools to identify areas for improvement in sales call quality and duration.
    * Encourage sales reps to focus on active listening and asking relevant, open-ended questions to keep the conversation engaging and productive.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average call duration over time for individual sales reps or teams.
    * Comparative bar charts displaying the average call duration for different product lines or customer segments.
    
    """,
    "risk_warnings": """

    * Excessively long call durations may lead to decreased productivity and missed opportunities to engage with other prospects.
    * Very short call durations could indicate a lack of thoroughness in the sales process, potentially resulting in lost sales opportunities.
    
    """,
    "tracking_tools": """

    * CRM systems with call tracking and recording capabilities to analyze and improve sales call effectiveness.
    * Sales engagement platforms that provide insights into prospect behavior and interaction patterns during sales calls.
    
    """,
    "integration_points": """

    * Integrate average call duration data with customer relationship management (CRM) systems to understand the impact of call length on customer relationships and sales outcomes.
    * Link call duration metrics with sales performance data to identify correlations between call quality and conversion rates.
    
    """,
    "change_impact_analysis": """

    * Improving average call duration can lead to better customer relationships and higher conversion rates, but it may also require additional resources for training and technology.
    * Significantly reducing call durations without maintaining quality could lead to missed opportunities and decreased sales effectiveness.
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Deal", "Lead", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.039052"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
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
                        64.85,
                        65.08,
                        46.92,
                        46.58,
                        59.9,
                        50.28,
                        54.9,
                        56.74,
                        59.06,
                        61.24,
                        63.54,
                        59.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.33,
                "unit": "%",
                "change": -4.21,
                "change_percent": -6.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 57.37,
                "min": 46.58,
                "max": 65.08,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.03,
                        "percentage": 28.7
                },
                {
                        "category": "Category B",
                        "value": 11.79,
                        "percentage": 19.9
                },
                {
                        "category": "Category C",
                        "value": 5.44,
                        "percentage": 9.2
                },
                {
                        "category": "Category D",
                        "value": 6.29,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 18.78,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.039052",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Average Sales Call Duration"
        }
    },
}
