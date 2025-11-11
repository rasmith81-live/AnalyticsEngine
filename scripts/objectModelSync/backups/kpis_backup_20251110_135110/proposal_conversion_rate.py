"""
Proposal Conversion Rate

The percentage of proposals or quotes that result in a sale.
"""

PROPOSAL_CONVERSION_RATE = {
    "code": "PROPOSAL_CONVERSION_RATE",
    "name": "Proposal Conversion Rate",
    "description": "The percentage of proposals or quotes that result in a sale.",
    "formula": "(Total Number of Sales / Total Number of Proposals Sent) * 100",
    "calculation_formula": "(Total Number of Sales / Total Number of Proposals Sent) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Proposal Conversion Rate to be added.",
    "trend_analysis": """


    * An increasing proposal conversion rate may indicate improved sales strategies or a higher quality of leads.
    * A decreasing rate could signal issues with the sales process, pricing, or product quality.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products or services with consistently high or low proposal conversion rates?
    * How does our proposal conversion rate compare with industry benchmarks or competitors?
    
    
    """,
    "actionable_tips": """


    * Provide sales teams with additional training and resources to improve their ability to close deals.
    * Regularly review and update pricing strategies to ensure competitiveness and value perception.
    * Implement customer feedback mechanisms to understand reasons for lost proposals and address any recurring issues.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of proposal conversion rates over time.
    * Pie charts to compare proposal conversion rates for different products or services.
    
    
    """,
    "risk_warnings": """


    * A consistently low proposal conversion rate may lead to decreased revenue and market share.
    * An excessively high conversion rate may indicate underpricing or missed revenue opportunities.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track and analyze proposal outcomes.
    * Sales enablement platforms to provide sales teams with the necessary resources and content for effective selling.
    
    
    """,
    "integration_points": """


    * Integrate proposal conversion rate data with marketing analytics to understand the quality of leads generated.
    * Link with customer relationship management systems to track the entire sales process from lead to conversion.
    
    
    """,
    "change_impact_analysis": """


    * Improving the proposal conversion rate can lead to increased revenue and customer satisfaction.
    * However, a significant increase in conversion rate may also lead to capacity constraints and the need for additional resources to fulfill orders.
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Lost Sale", "Opportunity", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.289049"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT", "SALES_OPERATIONS"],
    "module_code": "SALES_DEVELOPMENT",
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
                        58.98,
                        53.92,
                        45.8,
                        50.64,
                        54.42,
                        47.55,
                        56.4,
                        55.84,
                        41.77,
                        55.2,
                        46.68,
                        58.58
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.58,
                "unit": "%",
                "change": 11.9,
                "change_percent": 25.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 52.15,
                "min": 41.77,
                "max": 58.98,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.7,
                        "percentage": 20.0
                },
                {
                        "category": "Category B",
                        "value": 7.66,
                        "percentage": 13.1
                },
                {
                        "category": "Category C",
                        "value": 10.5,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 3.48,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 25.24,
                        "percentage": 43.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.999482",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Proposal Conversion Rate"
        }
    },
}
