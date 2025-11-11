"""
Number of Qualified Leads

The total number of leads that meet certain predefined criteria and are considered likely to become customers.
"""

NUMBER_OF_QUALIFIED_LEADS = {
    "code": "NUMBER_OF_QUALIFIED_LEADS",
    "name": "Number of Qualified Leads",
    "description": "The total number of leads that meet certain predefined criteria and are considered likely to become customers.",
    "formula": "Sum of all Qualified Leads",
    "calculation_formula": "Sum of all Qualified Leads",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Qualified Leads to be added.",
    "trend_analysis": """

    * An increasing number of qualified leads may indicate improved marketing strategies or increased demand for the product or service.
    * A decreasing number of qualified leads could signal a need for reevaluation of lead generation tactics or a decline in market interest.
    
    """,
    "diagnostic_questions": """

    * What specific criteria are being used to qualify leads, and are they still relevant to the target customer base?
    * How do the conversion rates from qualified leads to customers compare to historical data or industry benchmarks?
    
    """,
    "actionable_tips": """

    * Regularly review and update the criteria for qualified leads to ensure they align with the changing market and customer needs.
    * Implement lead nurturing strategies to further qualify and engage potential customers before passing them to the sales team.
    * Provide ongoing training and support to the sales team to effectively convert qualified leads into customers.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of qualified leads over time.
    * Pie charts to visualize the distribution of qualified leads by source or criteria.
    
    """,
    "risk_warnings": """

    * A low number of qualified leads may lead to missed sales opportunities and revenue growth.
    * Overly strict criteria for qualified leads could result in a limited pool of potential customers and hinder business expansion.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and manage qualified leads throughout the sales process.
    * Marketing automation tools to streamline lead qualification and nurturing processes.
    
    """,
    "integration_points": """

    * Integrate qualified lead data with sales performance metrics to analyze the effectiveness of lead qualification in driving actual sales.
    * Link qualified lead information with customer relationship management systems to ensure a seamless transition from marketing to sales activities.
    
    """,
    "change_impact_analysis": """

    * An increase in the number of qualified leads can positively impact sales revenue and market share.
    * However, a decrease in qualified leads may require adjustments in marketing and sales strategies to maintain business growth.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Lead Qualification", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.715838"},
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
                        624.5,
                        553.35,
                        602.78,
                        619.29,
                        531.05,
                        519.83,
                        633.47,
                        521.36,
                        514.81,
                        526.35,
                        526.17,
                        503.54
                ],
                "unit": "units"
        },
        "current": {
                "value": 503.54,
                "unit": "units",
                "change": -22.63,
                "change_percent": -4.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 556.38,
                "min": 503.54,
                "max": 633.47,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 171.02,
                        "percentage": 34.0
                },
                {
                        "category": "Category B",
                        "value": 52.18,
                        "percentage": 10.4
                },
                {
                        "category": "Category C",
                        "value": 97.2,
                        "percentage": 19.3
                },
                {
                        "category": "Category D",
                        "value": 47.5,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 135.64,
                        "percentage": 26.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.715838",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Number of Qualified Leads"
        }
    },
}
