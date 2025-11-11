"""
Partner Sales Training Efficacy

A measure of how effective sales training provided to partners is in improving their performance.
"""

PARTNER_SALES_TRAINING_EFFICACY = {
    "code": "PARTNER_SALES_TRAINING_EFFICACY",
    "name": "Partner Sales Training Efficacy",
    "description": "A measure of how effective sales training provided to partners is in improving their performance.",
    "formula": "Percentage Increase in Sales Post-Training vs. Pre-Training",
    "calculation_formula": "Percentage Increase in Sales Post-Training vs. Pre-Training",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Sales Training Efficacy to be added.",
    "trend_analysis": """



    * An increasing efficacy in partner sales training may indicate improved sales performance and increased revenue from partner channels.
    * A decreasing efficacy could signal a need for reevaluation of the training content and methods, as well as potential impact on partner relationships and sales outcomes.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas or topics in the sales training that partners struggle with the most?
    * How do partners perceive the effectiveness of the sales training they receive, and what feedback do they provide?
    
    
    
    """,
    "actionable_tips": """



    * Regularly gather feedback from partners to understand which aspects of the training are most beneficial and which need improvement.
    * Customize sales training content to align with the unique needs and challenges of different partner organizations.
    * Provide ongoing support and resources to reinforce and apply the training concepts in real-world sales scenarios.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of partner sales performance alongside the efficacy of sales training over time.
    * Comparison bar charts displaying the performance of partners who have received different levels of sales training.
    
    
    
    """,
    "risk_warnings": """



    * Low efficacy in partner sales training may lead to missed sales opportunities and decreased partner satisfaction.
    * Failure to address training efficacy issues could result in disengagement from partners and a negative impact on overall channel sales performance.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to deliver, track, and assess the effectiveness of sales training content for partners.
    * Feedback and survey tools to gather insights from partners about the relevance and impact of the sales training they receive.
    
    
    
    """,
    "integration_points": """



    * Integrate partner sales training efficacy data with sales performance metrics to understand the direct impact of training on revenue generation.
    * Link training efficacy with partner relationship management systems to identify correlations between training satisfaction and partner engagement.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving partner sales training efficacy can lead to increased partner loyalty, stronger sales relationships, and higher overall channel sales performance.
    * Conversely, a decline in training efficacy may result in decreased partner trust, reduced sales effectiveness, and potential loss of market share within partner channels.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.218576"},
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
                        62.76,
                        65.21,
                        66.94,
                        61.73,
                        69.72,
                        64.46,
                        66.14,
                        65.14,
                        77.49,
                        61.5,
                        74.68,
                        62.2
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.2,
                "unit": "%",
                "change": -12.48,
                "change_percent": -16.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.5,
                "min": 61.5,
                "max": 77.49,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 10.52,
                        "percentage": 16.9
                },
                {
                        "category": "Channel Sales",
                        "value": 15.06,
                        "percentage": 24.2
                },
                {
                        "category": "Online Sales",
                        "value": 9.08,
                        "percentage": 14.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.19,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 20.35,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.522265",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner Sales Training Efficacy"
        }
    },
}
