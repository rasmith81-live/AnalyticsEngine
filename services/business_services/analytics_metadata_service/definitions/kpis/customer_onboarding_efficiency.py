"""
Customer Onboarding Efficiency

Measurement of the speed and effectiveness of the process that gets new customers or clients acclimated to the company's products or services.
"""

CUSTOMER_ONBOARDING_EFFICIENCY = {
    "code": "CUSTOMER_ONBOARDING_EFFICIENCY",
    "name": "Customer Onboarding Efficiency",
    "description": "Measurement of the speed and effectiveness of the process that gets new customers or clients acclimated to the company's products or services.",
    "formula": "Total Onboarding Time for All Customers / Number of Customers Onboarded",
    "calculation_formula": "Total Onboarding Time for All Customers / Number of Customers Onboarded",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Onboarding Efficiency to be added.",
    "trend_analysis": """



    * An increasing customer onboarding efficiency may indicate improved processes or better alignment with customer needs.
    * A decreasing efficiency could signal issues with training, product complexity, or organizational changes.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific stages in the onboarding process where customers tend to get stuck or require additional support?
    * How does our customer onboarding efficiency compare with industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Streamline onboarding processes by automating repetitive tasks or providing self-service resources.
    * Invest in training and support resources to ensure customers are well-equipped to use the products or services effectively.
    * Regularly gather feedback from new customers to identify areas for improvement in the onboarding process.
    
    
    
    """,
    "visualization_suggestions": """



    * Flowcharts or process maps to visualize the customer onboarding journey and identify bottlenecks.
    * Time-series line charts to track the efficiency of onboarding over time.
    
    
    
    """,
    "risk_warnings": """



    * Low customer onboarding efficiency can lead to customer frustration and increased churn rates.
    * Complex or lengthy onboarding processes may deter potential customers from making a purchase.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track customer interactions and progress through the onboarding process.
    * Customer feedback and survey tools to gather insights on the onboarding experience.
    
    
    
    """,
    "integration_points": """



    * Integrate customer onboarding data with sales and marketing systems to understand the impact of onboarding on customer acquisition and retention.
    * Link onboarding efficiency with customer support systems to ensure a seamless transition from onboarding to ongoing assistance.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving customer onboarding efficiency can lead to higher customer satisfaction and retention rates.
    * However, rapid changes in onboarding processes may require additional resources and could impact initial sales velocity.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Product", "Renewal Management", "Sales Process Workflow"], "last_validated": "2025-11-10T13:49:32.854548"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        397,
                        396,
                        407,
                        385,
                        426,
                        382,
                        386,
                        390,
                        413,
                        399,
                        415,
                        392
                ],
                "unit": "count"
        },
        "current": {
                "value": 392,
                "unit": "count",
                "change": -23,
                "change_percent": -5.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 399.0,
                "min": 382,
                "max": 426,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 127.8,
                        "percentage": 32.6
                },
                {
                        "category": "Existing Customers",
                        "value": 60.47,
                        "percentage": 15.4
                },
                {
                        "category": "VIP Customers",
                        "value": 64.62,
                        "percentage": 16.5
                },
                {
                        "category": "At-Risk Customers",
                        "value": 35.46,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 103.65,
                        "percentage": 26.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.735810",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Onboarding Efficiency"
        }
    },
}
