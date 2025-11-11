"""
Channel Margin

A measure of the profit margin a company achieves on sales made through channel partners.
"""

CHANNEL_MARGIN = {
    "code": "CHANNEL_MARGIN",
    "name": "Channel Margin",
    "description": "A measure of the profit margin a company achieves on sales made through channel partners.",
    "formula": "(Sales Price - Cost of Procurement) / Sales Price * 100",
    "calculation_formula": "(Sales Price - Cost of Procurement) / Sales Price * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Channel Margin to be added.",
    "trend_analysis": """

    * Increasing channel margin may indicate successful negotiation of better terms with channel partners or a shift towards higher-margin products.
    * Decreasing channel margin could signal increased competition, pricing pressures, or inefficiencies in the channel sales process.
    
    """,
    "diagnostic_questions": """

    * What factors are contributing to changes in channel margin, such as product mix, pricing strategies, or partner performance?
    * Are there specific channel partners or regions where channel margin is consistently higher or lower, and what factors may be influencing this?
    
    """,
    "actionable_tips": """

    * Regularly review and renegotiate terms with channel partners to ensure margins are competitive and sustainable.
    * Provide training and support to channel partners to help them sell higher-margin products or services effectively.
    * Implement pricing strategies that incentivize channel partners to focus on higher-margin offerings.
    
    """,
    "visualization_suggestions": """

    * Line charts showing channel margin trends over time, segmented by product category or partner type.
    * Pareto charts to identify the most significant channel partners contributing to overall margin performance.
    
    """,
    "risk_warnings": """

    * Declining channel margins may lead to reduced profitability and financial instability for the organization.
    * High channel margins in certain regions or with specific partners may indicate potential pricing inefficiencies or missed opportunities for growth.
    
    """,
    "tracking_tools": """

    * Financial analysis and reporting software to track and analyze channel margin data in real-time.
    * Partner relationship management (PRM) platforms to monitor and optimize partner performance and margin contributions.
    
    """,
    "integration_points": """

    * Integrate channel margin data with sales and marketing systems to align strategies with margin performance and optimize resource allocation.
    * Link channel margin analysis with supply chain and inventory management systems to ensure efficient fulfillment and minimize margin erosion due to stockouts or overstock situations.
    
    """,
    "change_impact_analysis": """

    * Improving channel margin can positively impact overall profitability and financial health, but may require initial investments in partner enablement and relationship management.
    * Conversely, declining channel margin can lead to reduced resources for innovation and growth, impacting long-term competitiveness and market position.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.088157"},
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
                        33297.68,
                        33515.14,
                        35001.35,
                        36985.71,
                        29742.22,
                        39890.17,
                        35198.55,
                        40876.07,
                        34476.06,
                        37515.01,
                        38352.3,
                        37753.79
                ],
                "unit": "$"
        },
        "current": {
                "value": 37753.79,
                "unit": "$",
                "change": -598.51,
                "change_percent": -1.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 36050.34,
                "min": 29742.22,
                "max": 40876.07,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9072.75,
                        "percentage": 24.0
                },
                {
                        "category": "Category B",
                        "value": 8509.52,
                        "percentage": 22.5
                },
                {
                        "category": "Category C",
                        "value": 3748.59,
                        "percentage": 9.9
                },
                {
                        "category": "Category D",
                        "value": 4418.59,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 12004.34,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.088157",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Channel Margin"
        }
    },
}
