"""
Sales Conversion Rate

The percentage of opportunities that are converted to closed deals.
"""

SALES_CONVERSION_RATE = {
    "code": "SALES_CONVERSION_RATE",
    "name": "Sales Conversion Rate",
    "description": "The percentage of opportunities that are converted to closed deals.",
    "formula": "(Number of Sales / Total Number of Leads) * 100",
    "calculation_formula": "(Number of Sales / Total Number of Leads) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Conversion Rate to be added.",
    "trend_analysis": """

    * An increasing sales conversion rate may indicate improved sales strategies or a growing market demand.
    * A decreasing rate could signal ineffective sales processes or a decline in customer interest.
    
    """,
    "diagnostic_questions": """

    * Are there specific stages in the sales funnel where conversion rates drop significantly?
    * How does our sales conversion rate compare with industry benchmarks or competitor performance?
    
    """,
    "actionable_tips": """

    * Provide additional sales training and support for the sales team to improve their closing techniques.
    * Implement customer relationship management (CRM) software to better track and manage sales opportunities.
    * Analyze and optimize the sales process to identify and address any bottlenecks or inefficiencies.
    
    """,
    "visualization_suggestions": """

    * Funnel charts to visualize the conversion rates at each stage of the sales process.
    * Line graphs to track the trend of conversion rates over time.
    
    """,
    "risk_warnings": """

    * Low sales conversion rates can lead to missed revenue opportunities and reduced profitability.
    * Consistently low conversion rates may indicate a need for a fundamental shift in sales strategy or targeting.
    
    """,
    "tracking_tools": """

    * CRM systems like Salesforce or HubSpot for tracking and managing sales opportunities.
    * Sales analytics tools to gain insights into the factors affecting conversion rates.
    
    """,
    "integration_points": """

    * Integrate sales conversion rate data with marketing analytics to understand the impact of marketing efforts on conversion.
    * Link with customer relationship management systems to track the entire customer journey from lead to conversion.
    
    """,
    "change_impact_analysis": """

    * Improving the sales conversion rate can lead to increased revenue and improved overall sales performance.
    * However, a significant increase in conversion rate may also put pressure on fulfillment and delivery processes, requiring operational adjustments.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.207427"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_OPERATIONS"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        50.0,
                        57.44,
                        45.04,
                        60.39,
                        57.69,
                        56.92,
                        54.79,
                        47.61,
                        56.35,
                        48.08,
                        54.58,
                        58.01
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.01,
                "unit": "%",
                "change": 3.43,
                "change_percent": 6.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 53.91,
                "min": 45.04,
                "max": 60.39,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.24,
                        "percentage": 34.9
                },
                {
                        "category": "Category B",
                        "value": 9.34,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 5.19,
                        "percentage": 8.9
                },
                {
                        "category": "Category D",
                        "value": 3.1,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 20.14,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.207427",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Conversion Rate"
        }
    },
}
