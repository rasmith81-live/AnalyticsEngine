"""
Deal Slippage Rate

The rate at which deals slip past their expected close date.
"""

DEAL_SLIPPAGE_RATE = {
    "code": "DEAL_SLIPPAGE_RATE",
    "name": "Deal Slippage Rate",
    "description": "The rate at which deals slip past their expected close date.",
    "formula": "(Number of Deals Slipped / Total Number of Deals Expected to Close) * 100",
    "calculation_formula": "(Number of Deals Slipped / Total Number of Deals Expected to Close) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Slippage Rate to be added.",
    "trend_analysis": """



    * Increasing deal slippage rate may indicate issues with sales forecasting or longer sales cycles.
    * A decreasing rate could signal improved sales pipeline management or more accurate sales projections.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common factors causing deals to slip, such as specific customer objections or internal process bottlenecks?
    * How does our deal slippage rate compare with industry averages or benchmarks for similar products or services?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular pipeline reviews to identify potential deal slippage early and take proactive measures.
    * Provide additional sales training or resources to address common reasons for deal slippage.
    * Consider adjusting sales projections and timelines based on historical deal slippage patterns.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of deal slippage rate over time.
    * Pareto charts to identify the most common reasons for deal slippage.
    
    
    
    """,
    "risk_warnings": """



    * High deal slippage rates can lead to missed revenue targets and impact overall sales performance.
    * Consistently high deal slippage may indicate underlying issues in the sales process that need to be addressed.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with robust pipeline management and forecasting capabilities to track deal progress and identify potential slippage.
    * Sales analytics platforms to analyze historical data and identify patterns leading to deal slippage.
    
    
    
    """,
    "integration_points": """



    * Integrate deal slippage rate tracking with sales performance management systems to align incentives with timely deal closures.
    * Link with customer relationship management systems to communicate transparently with customers about potential delays.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing deal slippage can lead to improved revenue predictability and better resource allocation.
    * However, overly aggressive measures to reduce deal slippage may put undue pressure on sales teams and impact morale.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.917392"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "SALES_OPERATIONS"],
    "module_code": "INSIDE_SALES",
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
                        72.07,
                        60.86,
                        63.03,
                        65.42,
                        69.73,
                        76.46,
                        59.85,
                        67.02,
                        69.99,
                        61.49,
                        74.55,
                        71.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.33,
                "unit": "%",
                "change": -3.22,
                "change_percent": -4.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 67.65,
                "min": 59.85,
                "max": 76.46,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.87,
                        "percentage": 26.5
                },
                {
                        "category": "Segment B",
                        "value": 10.15,
                        "percentage": 14.2
                },
                {
                        "category": "Segment C",
                        "value": 11.74,
                        "percentage": 16.5
                },
                {
                        "category": "Segment D",
                        "value": 7.64,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 22.93,
                        "percentage": 32.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.895382",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Deal Slippage Rate"
        }
    },
}
