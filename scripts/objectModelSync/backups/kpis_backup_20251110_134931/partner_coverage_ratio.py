"""
Partner Coverage Ratio

The ratio of the number of active channel partners to the total addressable market, indicating the extent of market coverage through partners.
"""

PARTNER_COVERAGE_RATIO = {
    "code": "PARTNER_COVERAGE_RATIO",
    "name": "Partner Coverage Ratio",
    "description": "The ratio of the number of active channel partners to the total addressable market, indicating the extent of market coverage through partners.",
    "formula": "Number of Market Areas or Customer Segments / Number of Active Partners",
    "calculation_formula": "Number of Market Areas or Customer Segments / Number of Active Partners",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Coverage Ratio to be added.",
    "trend_analysis": """

    * An increasing partner coverage ratio may indicate successful onboarding of new partners or expansion into new markets.
    * A decreasing ratio could signal partner attrition or a lack of focus on partner enablement and support.
    
    """,
    "diagnostic_questions": """

    * Are there specific regions or segments of the market where we have a low partner coverage ratio?
    * What are the main reasons for partners leaving or becoming inactive, and how can we address these issues?
    
    """,
    "actionable_tips": """

    * Invest in partner training and enablement programs to ensure partners are equipped to effectively cover the market.
    * Regularly assess the performance and engagement of existing partners to identify areas for improvement or expansion.
    * Implement a structured partner recruitment strategy to fill gaps in market coverage.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of partner coverage ratio over time.
    * Geospatial maps to visualize the distribution of partners across different regions.
    
    """,
    "risk_warnings": """

    * A low partner coverage ratio may result in missed opportunities and reduced market penetration.
    * Over-reliance on a small number of partners can create vulnerability to market changes or partner turnover.
    
    """,
    "tracking_tools": """

    * Partner relationship management (PRM) software to track partner performance and engagement.
    * Market analysis tools to identify potential areas for partner expansion based on market demand.
    
    """,
    "integration_points": """

    * Integrate partner coverage data with sales and marketing systems to align partner efforts with overall go-to-market strategies.
    * Link partner coverage metrics with customer relationship management (CRM) systems to understand the impact on customer reach and engagement.
    
    """,
    "change_impact_analysis": """

    * Improving partner coverage can lead to increased market share and revenue, but may also require additional resources for partner support and management.
    * A decrease in partner coverage ratio can negatively impact sales performance and market competitiveness.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Market Segment", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.857585"},
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
                        33.88,
                        45.02,
                        33.9,
                        50.73,
                        36.42,
                        47.21,
                        34.39,
                        41.62,
                        47.45,
                        36.66,
                        50.37,
                        36.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 36.33,
                "unit": "%",
                "change": -14.04,
                "change_percent": -27.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 41.16,
                "min": 33.88,
                "max": 50.73,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.32,
                        "percentage": 33.9
                },
                {
                        "category": "Category B",
                        "value": 5.79,
                        "percentage": 15.9
                },
                {
                        "category": "Category C",
                        "value": 3.52,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 2.88,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 11.82,
                        "percentage": 32.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.857585",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Coverage Ratio"
        }
    },
}
