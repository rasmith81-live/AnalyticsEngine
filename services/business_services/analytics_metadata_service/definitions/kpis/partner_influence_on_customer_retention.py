"""
Partner Influence on Customer Retention

The impact channel partners have on retaining customers, often measured by customer renewal rates or repeat purchases through partners.
"""

PARTNER_INFLUENCE_ON_CUSTOMER_RETENTION = {
    "code": "PARTNER_INFLUENCE_ON_CUSTOMER_RETENTION",
    "name": "Partner Influence on Customer Retention",
    "description": "The impact channel partners have on retaining customers, often measured by customer renewal rates or repeat purchases through partners.",
    "formula": "(Customer Retention Rate Attributable to Partners / Overall Customer Retention Rate) * 100",
    "calculation_formula": "(Customer Retention Rate Attributable to Partners / Overall Customer Retention Rate) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Influence on Customer Retention to be added.",
    "trend_analysis": """



    * Increasing partner influence on customer retention may indicate stronger relationships and better customer satisfaction.
    * A decreasing influence could signal dissatisfaction with partner performance or a shift in customer preferences.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services where partners have a particularly strong or weak impact on customer retention?
    * How do our partner-influenced customer retention rates compare with direct sales retention rates?
    
    
    
    """,
    "actionable_tips": """



    * Provide partners with additional training and resources to enhance their ability to retain customers.
    * Regularly review and assess partner performance to identify areas for improvement.
    * Implement customer feedback mechanisms to understand the impact of partners on retention.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing partner-influenced customer retention rates over time.
    * Comparative bar graphs displaying retention rates for customers acquired through partners versus other channels.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on partners for customer retention may lead to vulnerability if partner relationships sour.
    * Weak partner influence on retention could result in lost opportunities for repeat business.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and analyze customer retention data by channel.
    * Partner performance management software to assess and improve partner contributions to customer retention.
    
    
    
    """,
    "integration_points": """



    * Integrate partner-influenced customer retention data with sales performance metrics to understand the overall impact of partners on revenue.
    * Link customer feedback systems with partner management platforms to gather insights on partner-influenced retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving partner influence on customer retention can lead to increased customer lifetime value and overall revenue growth.
    * Conversely, a decline in partner influence may require adjustments in channel strategy and resource allocation.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Renewal Management", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.199963"},
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
                        81.07,
                        80.96,
                        70.49,
                        75.34,
                        71.06,
                        65.89,
                        72.19,
                        73.71,
                        73.28,
                        77.2,
                        77.03,
                        71.49
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.49,
                "unit": "%",
                "change": -5.54,
                "change_percent": -7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.14,
                "min": 65.89,
                "max": 81.07,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 24.29,
                        "percentage": 34.0
                },
                {
                        "category": "Existing Customers",
                        "value": 15.09,
                        "percentage": 21.1
                },
                {
                        "category": "VIP Customers",
                        "value": 11.21,
                        "percentage": 15.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.69,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 15.21,
                        "percentage": 21.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.480217",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner Influence on Customer Retention"
        }
    },
}
