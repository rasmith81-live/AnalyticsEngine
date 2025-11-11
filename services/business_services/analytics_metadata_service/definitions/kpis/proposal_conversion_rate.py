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
                        46.47,
                        47.13,
                        52.41,
                        50.95,
                        65.25,
                        58.79,
                        54.85,
                        60.9,
                        52.54,
                        57.91,
                        55.58,
                        61.07
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.07,
                "unit": "%",
                "change": 5.49,
                "change_percent": 9.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 55.32,
                "min": 46.47,
                "max": 65.25,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 19.61,
                        "percentage": 32.1
                },
                {
                        "category": "Channel Sales",
                        "value": 13.01,
                        "percentage": 21.3
                },
                {
                        "category": "Online Sales",
                        "value": 8.32,
                        "percentage": 13.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.34,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 14.79,
                        "percentage": 24.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.678532",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Proposal Conversion Rate"
        }
    },
}
