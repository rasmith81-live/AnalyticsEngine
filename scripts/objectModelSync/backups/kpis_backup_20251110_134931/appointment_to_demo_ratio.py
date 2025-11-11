"""
Appointment-to-Demo Ratio

The ratio of sales appointments to the number of product or service demos given.
"""

APPOINTMENT_TO_DEMO_RATIO = {
    "code": "APPOINTMENT_TO_DEMO_RATIO",
    "name": "Appointment-to-Demo Ratio",
    "description": "The ratio of sales appointments to the number of product or service demos given.",
    "formula": "Number of Demos Conducted / Number of Appointments Scheduled * 100",
    "calculation_formula": "Number of Demos Conducted / Number of Appointments Scheduled * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Appointment-to-Demo Ratio to be added.",
    "trend_analysis": """

    * An increasing appointment-to-demo ratio may indicate a lack of qualified leads or ineffective sales prospecting.
    * A decreasing ratio could signal improved lead quality or more efficient sales processes.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales channels or sources that consistently lead to higher appointment-to-demo ratios?
    * How does our appointment-to-demo ratio compare with industry benchmarks or with different sales teams within the organization?
    
    """,
    "actionable_tips": """

    * Implement lead scoring to prioritize high-quality leads for appointments.
    * Provide additional sales training to improve the effectiveness of product or service demos.
    * Regularly review and refine the sales prospecting process to attract more qualified leads.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of appointment-to-demo ratios over time.
    * Comparison bar charts to visualize the appointment-to-demo ratios across different sales channels or teams.
    
    """,
    "risk_warnings": """

    * A consistently low appointment-to-demo ratio may lead to wasted resources and inefficiencies in the sales process.
    * A high ratio may indicate a lack of proactive sales prospecting and lead generation.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and analyze lead sources and appointment outcomes.
    * Sales enablement platforms to streamline the demo process and provide sales reps with the necessary tools and materials.
    
    """,
    "integration_points": """

    * Integrate appointment-to-demo ratio tracking with marketing automation systems to align lead generation efforts with sales activities.
    * Link with customer feedback systems to gather insights on the quality of demos and potential areas for improvement.
    
    """,
    "change_impact_analysis": """

    * Improving the appointment-to-demo ratio can lead to more efficient use of sales resources and potentially higher conversion rates.
    * However, a significant increase in the ratio may also indicate a need for more aggressive lead generation efforts to maintain a healthy pipeline.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Appointment", "Demo", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.014417"},
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
                        35.65,
                        34.6,
                        44.79,
                        43.87,
                        39.15,
                        38.49,
                        50.62,
                        52.46,
                        41.61,
                        40.87,
                        33.23,
                        37.11
                ],
                "unit": "%"
        },
        "current": {
                "value": 37.11,
                "unit": "%",
                "change": 3.88,
                "change_percent": 11.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 41.04,
                "min": 33.23,
                "max": 52.46,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.62,
                        "percentage": 31.3
                },
                {
                        "category": "Category B",
                        "value": 4.36,
                        "percentage": 11.7
                },
                {
                        "category": "Category C",
                        "value": 4.55,
                        "percentage": 12.3
                },
                {
                        "category": "Category D",
                        "value": 4.86,
                        "percentage": 13.1
                },
                {
                        "category": "Other",
                        "value": 11.72,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.014417",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Appointment-to-Demo Ratio"
        }
    },
}
