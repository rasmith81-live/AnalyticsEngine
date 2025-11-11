"""
Customer Lifetime Profitability

The total profit a company expects to earn over the entirety of its business relationship with a customer.
"""

CUSTOMER_LIFETIME_PROFITABILITY = {
    "code": "CUSTOMER_LIFETIME_PROFITABILITY",
    "name": "Customer Lifetime Profitability",
    "description": "The total profit a company expects to earn over the entirety of its business relationship with a customer.",
    "formula": "Sum of Customer\u2019s Lifetime Value - Sum of Customer\u2019s Lifetime Costs",
    "calculation_formula": "Sum of Customer\u2019s Lifetime Value - Sum of Customer\u2019s Lifetime Costs",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Lifetime Profitability to be added.",
    "trend_analysis": """



    * Increasing customer lifetime profitability may indicate successful upselling or cross-selling efforts.
    * Decreasing profitability could signal customer dissatisfaction or increased competition impacting repeat business.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors contribute to the increase or decrease in customer lifetime profitability?
    * How does our customer lifetime profitability compare to industry benchmarks or customer segments?
    
    
    
    """,
    "actionable_tips": """



    * Focus on building long-term customer relationships through personalized service and tailored solutions.
    * Regularly review customer feedback and adjust strategies to meet evolving needs and expectations.
    * Implement loyalty programs to encourage repeat purchases and increase customer lifetime value.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of customer lifetime profitability over time.
    * Pareto charts to identify the most profitable customers and prioritize retention efforts.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on a small number of high-profit customers can pose a risk if their business is lost.
    * Ignoring declining profitability may lead to customer churn and revenue loss.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track customer interactions and preferences.
    * Business intelligence tools for analyzing customer data and identifying opportunities for increasing profitability.
    
    
    
    """,
    "integration_points": """



    * Integrate customer profitability data with sales and marketing systems to align efforts with high-value customers.
    * Link profitability metrics with customer service platforms to ensure consistent experience across all touchpoints.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving customer lifetime profitability may require investment in customer service and relationship management.
    * Decreasing profitability can impact overall revenue and long-term business sustainability.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.843488"},
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
                        23.4,
                        28.7,
                        29.5,
                        30.0,
                        29.5,
                        25.2,
                        24.8,
                        28.5,
                        30.0,
                        24.5,
                        27.0,
                        26.4
                ],
                "unit": "days"
        },
        "current": {
                "value": 26.4,
                "unit": "days",
                "change": -0.6,
                "change_percent": -2.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 27.29,
                "min": 23.4,
                "max": 30.0,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 5.31,
                        "percentage": 20.1
                },
                {
                        "category": "Existing Customers",
                        "value": 3.75,
                        "percentage": 14.2
                },
                {
                        "category": "VIP Customers",
                        "value": 3.55,
                        "percentage": 13.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 2.52,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 11.27,
                        "percentage": 42.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.711852",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Customer Lifetime Profitability"
        }
    },
}
