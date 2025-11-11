"""
Sales Channel Efficiency

The efficiency of different sales channels assessed by metrics such as sales volume, customer reach, and conversion rates.
"""

SALES_CHANNEL_EFFICIENCY = {
    "code": "SALES_CHANNEL_EFFICIENCY",
    "name": "Sales Channel Efficiency",
    "description": "The efficiency of different sales channels assessed by metrics such as sales volume, customer reach, and conversion rates.",
    "formula": "Revenue or Performance Metric Specific to Sales Channel",
    "calculation_formula": "Revenue or Performance Metric Specific to Sales Channel",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Channel Efficiency to be added.",
    "trend_analysis": """


    * Increasing sales channel efficiency may indicate better targeting of potential customers or improved conversion strategies.
    * Decreasing efficiency could signal market saturation or ineffective sales tactics.
    
    
    """,
    "diagnostic_questions": """


    * Which sales channels are performing best and why?
    * Are there specific customer segments that certain channels are not reaching effectively?
    
    
    """,
    "actionable_tips": """


    * Regularly analyze and optimize the performance of each sales channel.
    * Invest in training and support for sales teams to improve their effectiveness in different channels.
    * Consider diversifying sales channels to reach new customer segments or markets.
    
    
    """,
    "visualization_suggestions": """


    * Line charts to track sales volume and conversion rates over time for each channel.
    * Pie charts to compare the contribution of each channel to overall sales volume.
    
    
    """,
    "risk_warnings": """


    * Over-reliance on a single sales channel can create vulnerability to market changes or disruptions.
    * Ignoring underperforming channels may lead to missed opportunities for growth.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track customer interactions and sales performance across channels.
    * Marketing automation tools to streamline and optimize multichannel campaigns.
    
    
    """,
    "integration_points": """


    * Integrate sales channel data with customer feedback and satisfaction metrics to understand the impact of each channel on customer experience.
    * Link sales channel performance with inventory and supply chain systems to ensure seamless order fulfillment.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales channel efficiency can lead to increased revenue and market share.
    * However, changes in sales channels may require adjustments in marketing budgets and resource allocation.
    
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.385762"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        563.38,
                        535.97,
                        557.38,
                        582.35,
                        625.6,
                        521.42,
                        608.4,
                        497.77,
                        625.35,
                        490.39,
                        542.71,
                        609.41
                ],
                "unit": "units"
        },
        "current": {
                "value": 609.41,
                "unit": "units",
                "change": 66.7,
                "change_percent": 12.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 563.34,
                "min": 490.39,
                "max": 625.6,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 205.42,
                        "percentage": 33.7
                },
                {
                        "category": "Category B",
                        "value": 96.9,
                        "percentage": 15.9
                },
                {
                        "category": "Category C",
                        "value": 81.68,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 23.55,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 201.86,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.169976",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Channel Efficiency"
        }
    },
}
