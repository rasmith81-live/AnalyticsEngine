"""
Annual Recurring Revenue (ARR)

The amount of revenue that the outside sales team generates annually through renewals, upgrades, and new sales.
"""

ANNUAL_RECURRING_REVENUE_ARR = {
    "code": "ANNUAL_RECURRING_REVENUE_ARR",
    "name": "Annual Recurring Revenue (ARR)",
    "description": "The amount of revenue that the outside sales team generates annually through renewals, upgrades, and new sales.",
    "formula": "Sum of all recurring revenue from customers in one year",
    "calculation_formula": "Sum of all recurring revenue from customers in one year",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Annual Recurring Revenue (ARR) to be added.",
    "trend_analysis": """


    * Increasing ARR may indicate successful customer retention and upselling efforts.
    * Decreasing ARR could signal customer churn or a decline in the value of sales.
    
    
    """,
    "diagnostic_questions": """


    * What percentage of the ARR comes from renewals versus new sales?
    * Are there specific customer segments or products that contribute significantly to the ARR?
    
    
    """,
    "actionable_tips": """


    * Implement customer success programs to improve retention and upsell opportunities.
    * Focus on identifying and targeting high-value customer segments for new sales.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of ARR over time.
    * Pie charts to illustrate the contribution of renewals, upgrades, and new sales to the overall ARR.
    
    
    """,
    "risk_warnings": """


    * Dependence on a few key accounts for a large portion of the ARR can pose a risk if those accounts are lost.
    * Failure to adapt to changing customer needs and market trends may lead to declining ARR.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track customer interactions and identify upsell opportunities.
    * Business intelligence tools for analyzing customer behavior and identifying opportunities for increasing ARR.
    
    
    """,
    "integration_points": """


    * Integrate ARR tracking with sales and marketing systems to align efforts towards increasing recurring revenue.
    * Link ARR data with customer support systems to identify opportunities for upselling or cross-selling.
    
    
    """,
    "change_impact_analysis": """


    * Increasing ARR can lead to higher customer lifetime value and overall revenue growth.
    * However, focusing solely on ARR may neglect the importance of new customer acquisition and market expansion.
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.641418"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_OPERATIONS"],
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
                        18251.62,
                        14691.26,
                        27439.19,
                        25203.44,
                        24416.69,
                        17056.47,
                        13861.47,
                        16142.68,
                        18879.35,
                        13336.61,
                        20904.79,
                        27459.95
                ],
                "unit": "$"
        },
        "current": {
                "value": 27459.95,
                "unit": "$",
                "change": 6555.16,
                "change_percent": 31.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 19803.63,
                "min": 13336.61,
                "max": 27459.95,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7492.89,
                        "percentage": 27.3
                },
                {
                        "category": "Category B",
                        "value": 4608.47,
                        "percentage": 16.8
                },
                {
                        "category": "Category C",
                        "value": 5177.67,
                        "percentage": 18.9
                },
                {
                        "category": "Category D",
                        "value": 2834.25,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 7346.67,
                        "percentage": 26.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.010774",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Annual Recurring Revenue (ARR)"
        }
    },
}
