"""
Partner Retention Rate

The percentage of channel partners that continue their relationship with the company over a given period, indicating partner satisfaction and stability in the channel network.
"""

PARTNER_RETENTION_RATE = {
    "code": "PARTNER_RETENTION_RATE",
    "name": "Partner Retention Rate",
    "description": "The percentage of channel partners that continue their relationship with the company over a given period, indicating partner satisfaction and stability in the channel network.",
    "formula": "(Number of Partners at End of Period - Number of New Partners Acquired) / Number of Partners at Start of Period * 100",
    "calculation_formula": "(Number of Partners at End of Period - Number of New Partners Acquired) / Number of Partners at Start of Period * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Retention Rate to be added.",
    "trend_analysis": """



    * An increasing partner retention rate may indicate improved partner support and satisfaction with the company's products or services.
    * A decreasing rate could signal issues with communication, product quality, or changes in the competitive landscape.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific factors contribute to our channel partners' decision to continue or discontinue their relationship with us?
    * How does our partner retention rate compare with industry benchmarks or with our competitors?
    
    
    
    """,
    "actionable_tips": """



    * Regularly gather feedback from channel partners to understand their needs and concerns, and take action based on their input.
    * Provide training and resources to help partners effectively sell and support the company's products or services.
    * Develop and maintain strong relationships with channel partners to build trust and loyalty.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of partner retention rate over time.
    * Pie charts to compare the distribution of retained and lost partners by region or product line.
    
    
    
    """,
    "risk_warnings": """



    * A declining partner retention rate can lead to a loss of market share and revenue as partners seek out other companies to work with.
    * High partner turnover can indicate issues with the company's channel program, potentially leading to negative word-of-mouth and reputation damage.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track partner interactions and manage partner relationships effectively.
    * Partner portal platforms to provide partners with easy access to resources, training, and support.
    
    
    
    """,
    "integration_points": """



    * Integrate partner retention rate data with sales performance metrics to understand the impact of partner stability on overall sales results.
    * Link partner retention rate with customer satisfaction data to identify potential correlations between partner stability and customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving partner retention can lead to increased sales and market share, but may also require investment in partner support and resources.
    * A declining partner retention rate can negatively impact customer satisfaction and brand reputation, affecting long-term business performance.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.216012"},
    "required_objects": [],
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
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
                        61.67,
                        53.01,
                        60.14,
                        71.7,
                        69.05,
                        70.4,
                        63.98,
                        66.65,
                        59.99,
                        59.61,
                        56.04,
                        69.78
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.78,
                "unit": "%",
                "change": 13.74,
                "change_percent": 24.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.5,
                "min": 53.01,
                "max": 71.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.28,
                        "percentage": 23.3
                },
                {
                        "category": "Segment B",
                        "value": 15.32,
                        "percentage": 22.0
                },
                {
                        "category": "Segment C",
                        "value": 7.38,
                        "percentage": 10.6
                },
                {
                        "category": "Segment D",
                        "value": 8.49,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 22.31,
                        "percentage": 32.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.518238",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Retention Rate"
        }
    },
}
