"""
Customer Onboarding Time

The time taken to fully onboard a new customer so they are utilizing the product or service effectively.
"""

CUSTOMER_ONBOARDING_TIME = {
    "code": "CUSTOMER_ONBOARDING_TIME",
    "name": "Customer Onboarding Time",
    "description": "The time taken to fully onboard a new customer so they are utilizing the product or service effectively.",
    "formula": "Average Time Taken From Signup to Achieving First Value Milestone",
    "calculation_formula": "Average Time Taken From Signup to Achieving First Value Milestone",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Onboarding Time to be added.",
    "trend_analysis": """



    * Decreasing customer onboarding time may indicate improved onboarding processes or better product usability.
    * An increasing onboarding time could signal issues with training, product complexity, or resource constraints.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific steps in the onboarding process that consistently take longer than expected?
    * How does our onboarding time compare with industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Streamline onboarding processes by creating standardized templates and resources.
    * Invest in training and support resources to help customers get up to speed more quickly.
    * Utilize customer feedback to identify areas of improvement in the onboarding experience.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average onboarding time over different time periods.
    * Stacked bar charts comparing onboarding times for different customer segments or product lines.
    
    
    
    """,
    "risk_warnings": """



    * Long onboarding times can lead to customer frustration and potential churn.
    * Rapidly increasing onboarding times may indicate scalability issues with current processes.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track onboarding progress and customer interactions.
    * Learning management systems (LMS) for creating and delivering training materials.
    
    
    
    """,
    "integration_points": """



    * Integrate onboarding time data with customer satisfaction metrics to understand the impact of onboarding on overall customer experience.
    * Link onboarding time with sales performance data to assess the impact of onboarding on customer lifetime value.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing onboarding time can lead to increased customer satisfaction and potentially higher retention rates.
    * However, rapid onboarding may also lead to lower product adoption and usage if customers feel overwhelmed.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.856892"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        24.1,
                        25.8,
                        28.8,
                        26.3,
                        30.0,
                        24.9,
                        29.9,
                        29.7,
                        28.3,
                        24.9,
                        29.9,
                        30.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 30.5,
                "unit": "days",
                "change": 0.6,
                "change_percent": 2.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 27.76,
                "min": 24.1,
                "max": 30.5,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 6.37,
                        "percentage": 20.9
                },
                {
                        "category": "Existing Customers",
                        "value": 3.67,
                        "percentage": 12.0
                },
                {
                        "category": "VIP Customers",
                        "value": 3.27,
                        "percentage": 10.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 2.73,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 14.46,
                        "percentage": 47.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.744054",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Customer Onboarding Time"
        }
    },
}
