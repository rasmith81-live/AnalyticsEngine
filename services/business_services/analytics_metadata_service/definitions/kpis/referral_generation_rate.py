"""
Referral Generation Rate

The rate at which the sales team generates new leads through referrals from existing customers.
"""

REFERRAL_GENERATION_RATE = {
    "code": "REFERRAL_GENERATION_RATE",
    "name": "Referral Generation Rate",
    "description": "The rate at which the sales team generates new leads through referrals from existing customers.",
    "formula": "(Number of Customers Acquired through Referrals / Total Number of New Customers) * 100",
    "calculation_formula": "(Number of Customers Acquired through Referrals / Total Number of New Customers) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Referral Generation Rate to be added.",
    "trend_analysis": """



    * An increasing referral generation rate may indicate a high level of customer satisfaction and loyalty, leading to more referrals.
    * A decreasing rate could signal a lack of engagement with existing customers or a decline in the quality of products/services.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or products that consistently generate more referrals?
    * How does our referral generation rate compare with industry benchmarks or with historical data?
    
    
    
    """,
    "actionable_tips": """



    * Implement a formal referral program to incentivize existing customers to refer new leads.
    * Provide training and resources to the sales team to effectively ask for referrals and follow up on leads.
    * Regularly communicate with existing customers to maintain engagement and encourage referrals.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of referral generation rate over time.
    * Pie charts to visualize the distribution of new leads by referral source.
    
    
    
    """,
    "risk_warnings": """



    * A low referral generation rate may lead to increased customer acquisition costs and reduced sales opportunities.
    * Dependence on referrals without diversifying lead generation sources can lead to vulnerability if the referral network diminishes.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and manage referral sources and leads.
    * Social media monitoring tools to identify and engage with potential referral sources online.
    
    
    
    """,
    "integration_points": """



    * Integrate referral generation data with customer satisfaction metrics to understand the correlation between satisfaction and referrals.
    * Link referral data with sales performance to measure the conversion rate of referred leads.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in referral generation rate can lead to a more sustainable and cost-effective sales pipeline.
    * However, a decrease in the rate may require additional investments in marketing and lead generation activities.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Quarterly Business Review", "Referral", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.321101"},
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
                        59.63,
                        71.32,
                        65.83,
                        58.55,
                        71.51,
                        66.5,
                        64.06,
                        74.26,
                        67.78,
                        60.8,
                        59.9,
                        75.42
                ],
                "unit": "%"
        },
        "current": {
                "value": 75.42,
                "unit": "%",
                "change": 15.52,
                "change_percent": 25.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.3,
                "min": 58.55,
                "max": 75.42,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 14.79,
                        "percentage": 19.6
                },
                {
                        "category": "Existing Customers",
                        "value": 14.73,
                        "percentage": 19.5
                },
                {
                        "category": "VIP Customers",
                        "value": 7.57,
                        "percentage": 10.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 10.87,
                        "percentage": 14.4
                },
                {
                        "category": "Other",
                        "value": 27.46,
                        "percentage": 36.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.757884",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Referral Generation Rate"
        }
    },
}
