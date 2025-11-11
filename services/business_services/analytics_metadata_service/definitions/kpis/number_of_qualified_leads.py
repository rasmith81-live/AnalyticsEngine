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
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Lead Qualification", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.095615"},
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
                        1046.8,
                        922.35,
                        996.42,
                        997.81,
                        915.67,
                        930.28,
                        1043.16,
                        928.37,
                        1019.82,
                        915.7,
                        972.56,
                        1025.25
                ],
                "unit": "units"
        },
        "current": {
                "value": 1025.25,
                "unit": "units",
                "change": 52.69,
                "change_percent": 5.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 976.18,
                "min": 915.67,
                "max": 1046.8,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 272.75,
                        "percentage": 26.6
                },
                {
                        "category": "Segment B",
                        "value": 119.05,
                        "percentage": 11.6
                },
                {
                        "category": "Segment C",
                        "value": 145.76,
                        "percentage": 14.2
                },
                {
                        "category": "Segment D",
                        "value": 83.2,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 404.49,
                        "percentage": 39.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.275602",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Number of Qualified Leads"
        }
    },
}
