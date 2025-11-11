"""
Sales Coverage Ratio

The ratio of sales representatives to the potential market or number of accounts, indicating potential market reach.
"""

SALES_COVERAGE_RATIO = {
    "code": "SALES_COVERAGE_RATIO",
    "name": "Sales Coverage Ratio",
    "description": "The ratio of sales representatives to the potential market or number of accounts, indicating potential market reach.",
    "formula": "Number of Sales Representatives / Number of Accounts or Sales Territories",
    "calculation_formula": "Number of Sales Representatives / Number of Accounts or Sales Territories",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Coverage Ratio to be added.",
    "trend_analysis": """



    * An increasing sales coverage ratio may indicate a growing sales team or expansion into new markets.
    * A decreasing ratio could signal a need for more sales representatives to effectively cover the potential market.
    
    
    
    """,
    "diagnostic_questions": """



    * How does the current sales coverage ratio align with our sales strategy and target market segments?
    * Are there specific regions or customer segments that are underrepresented in our current sales coverage?
    
    
    
    """,
    "actionable_tips": """



    * Regularly assess and adjust the sales coverage ratio based on changes in the potential market and customer demand.
    * Invest in sales training and development to ensure existing representatives can effectively cover the potential market.
    * Utilize sales territory mapping and optimization tools to maximize the efficiency of sales coverage.
    
    
    
    """,
    "visualization_suggestions": """



    * Map visualizations showing the geographical distribution of sales representatives compared to the potential market.
    * Line charts tracking the sales coverage ratio over time to identify any significant shifts or trends.
    
    
    
    """,
    "risk_warnings": """



    * A low sales coverage ratio may result in missed opportunities and decreased market penetration.
    * An excessively high ratio could lead to inefficiencies and decreased effectiveness of individual sales representatives.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software with territory management features to optimize sales coverage.
    * Geospatial analytics tools to visualize and analyze the distribution of potential customers relative to sales representatives.
    
    
    
    """,
    "integration_points": """



    * Integrate sales coverage data with customer relationship management systems to align sales efforts with customer needs and preferences.
    * Link sales coverage metrics with sales performance data to assess the impact of coverage on actual sales results.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing the sales coverage ratio may lead to higher customer acquisition but could also require additional resources and support.
    * Decreasing the ratio may reduce costs but could limit the organization's ability to reach new customers and expand market share.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Channel Market", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.403154"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
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
                        49.33,
                        58.17,
                        61.88,
                        45.8,
                        57.87,
                        50.47,
                        59.49,
                        49.31,
                        47.38,
                        51.89,
                        53.0,
                        46.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.33,
                "unit": "%",
                "change": -6.67,
                "change_percent": -12.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 52.58,
                "min": 45.8,
                "max": 61.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 10.88,
                        "percentage": 23.5
                },
                {
                        "category": "Mid-Market",
                        "value": 9.53,
                        "percentage": 20.6
                },
                {
                        "category": "Small Business",
                        "value": 8.45,
                        "percentage": 18.2
                },
                {
                        "category": "Strategic Partners",
                        "value": 2.89,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 14.58,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.935191",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Coverage Ratio"
        }
    },
}
