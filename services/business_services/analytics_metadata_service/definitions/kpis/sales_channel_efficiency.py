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
                        997.98,
                        858.06,
                        906.49,
                        945.55,
                        966.24,
                        916.26,
                        934.09,
                        965.91,
                        904.7,
                        851.43,
                        902.07,
                        956.74
                ],
                "unit": "units"
        },
        "current": {
                "value": 956.74,
                "unit": "units",
                "change": 54.67,
                "change_percent": 6.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 925.46,
                "min": 851.43,
                "max": 997.98,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 330.15,
                        "percentage": 34.5
                },
                {
                        "category": "Channel Sales",
                        "value": 205.19,
                        "percentage": 21.4
                },
                {
                        "category": "Online Sales",
                        "value": 108.73,
                        "percentage": 11.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 43.45,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 269.22,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.891448",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Channel Efficiency"
        }
    },
}
