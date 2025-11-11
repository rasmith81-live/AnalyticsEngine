"""
Sales Opportunity Scorecard

A tool that evaluates and scores sales opportunities based on various criteria like deal size, likelihood of close, etc.
"""

SALES_OPPORTUNITY_SCORECARD = {
    "code": "SALES_OPPORTUNITY_SCORECARD",
    "name": "Sales Opportunity Scorecard",
    "description": "A tool that evaluates and scores sales opportunities based on various criteria like deal size, likelihood of close, etc.",
    "formula": "Custom scoring based on criteria like budget, decision-maker accessibility, timeline, etc.",
    "calculation_formula": "Custom scoring based on criteria like budget, decision-maker accessibility, timeline, etc.",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Opportunity Scorecard to be added.",
    "trend_analysis": """

    * Increasing sales opportunity scores may indicate a more effective sales process or a higher quality of leads.
    * Decreasing scores could signal a need for sales team training or a shift in the market that requires a different approach.
    
    """,
    "diagnostic_questions": """

    * Are there common characteristics among opportunities with high scores?
    * What factors have historically led to successful closures of high-scoring opportunities?
    
    """,
    "actionable_tips": """

    * Regularly review and update the criteria used to score sales opportunities to ensure they align with current market conditions and customer needs.
    * Provide ongoing training and support for the sales team to improve their ability to identify and pursue high-scoring opportunities.
    * Implement a lead nurturing strategy to increase the likelihood of closing opportunities with lower scores.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average opportunity score over time to identify trends.
    * Pie charts to compare the distribution of scores across different sales territories or product lines.
    
    """,
    "risk_warnings": """

    * Over-reliance on the opportunity score without considering other factors may result in missed opportunities or lost revenue.
    * Inaccurate scoring criteria could lead to misallocation of resources and ineffective sales efforts.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software with built-in opportunity scoring functionality.
    * Data analytics tools to identify patterns and correlations between opportunity scores and eventual outcomes.
    
    """,
    "integration_points": """

    * Integrate sales opportunity scoring with performance management systems to align sales team incentives with the pursuit of high-scoring opportunities.
    * Link opportunity scoring with marketing automation platforms to ensure a consistent approach to lead qualification and nurturing.
    
    """,
    "change_impact_analysis": """

    * Improving opportunity scores can lead to increased revenue and market share, but may also require adjustments in resource allocation and sales strategies.
    * Lowering opportunity scores may indicate a need to realign sales and marketing efforts, potentially impacting short-term performance.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Deal", "Deal", "Expansion Opportunity", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Scorecard", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.455789"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
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
                        70.9,
                        72.1,
                        66.6,
                        76.8,
                        77.0,
                        70.7,
                        75.2,
                        70.1,
                        67.6,
                        74.4,
                        66.3,
                        71.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 71.6,
                "unit": "score",
                "change": 5.3,
                "change_percent": 8.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.61,
                "min": 66.3,
                "max": 77.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.97,
                        "percentage": 23.7
                },
                {
                        "category": "Category B",
                        "value": 18.84,
                        "percentage": 26.3
                },
                {
                        "category": "Category C",
                        "value": 9.21,
                        "percentage": 12.9
                },
                {
                        "category": "Category D",
                        "value": 7.61,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 18.97,
                        "percentage": 26.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.455789",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Opportunity Scorecard"
        }
    },
}
