"""
Service Level Agreement (SLA) Compliance Rate

The rate at which the customer success team adheres to the agreed-upon service levels in SLAs with customers.
"""

SERVICE_LEVEL_AGREEMENT_SLA_COMPLIANCE_RATE = {
    "code": "SERVICE_LEVEL_AGREEMENT_SLA_COMPLIANCE_RATE",
    "name": "Service Level Agreement (SLA) Compliance Rate",
    "description": "The rate at which the customer success team adheres to the agreed-upon service levels in SLAs with customers.",
    "formula": "(Number of SLA Compliant Resolutions / Total Number of SLA Bound Requests) * 100",
    "calculation_formula": "(Number of SLA Compliant Resolutions / Total Number of SLA Bound Requests) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Service Level Agreement (SLA) Compliance Rate to be added.",
    "trend_analysis": """



    * An increasing SLA compliance rate may indicate improved customer success processes and better alignment with customer needs.
    * A decreasing rate could signal issues in resource allocation, communication, or customer expectations management.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific SLAs or customer segments where compliance is consistently lower?
    * How do our SLA compliance rates compare with industry benchmarks or customer feedback?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and update SLAs to ensure they reflect current customer needs and the capabilities of the customer success team.
    * Invest in training and resources for the customer success team to better meet SLA requirements.
    * Implement automated systems for tracking and managing SLA compliance to reduce manual errors and delays.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of SLA compliance rates over time.
    * Pie charts comparing SLA compliance rates across different customer segments or service offerings.
    
    
    
    """,
    "risk_warnings": """



    * Low SLA compliance rates can lead to customer dissatisfaction and potential churn.
    * Consistently high compliance rates may indicate overcommitment or underutilization of resources.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems with built-in SLA tracking and reporting capabilities.
    * Workflow automation tools to streamline and standardize the process of managing and fulfilling SLAs.
    
    
    
    """,
    "integration_points": """



    * Integrate SLA compliance data with customer feedback and satisfaction metrics to understand the impact on overall customer experience.
    * Link SLA compliance tracking with resource management systems to ensure adequate allocation of personnel and resources.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving SLA compliance can enhance customer satisfaction and loyalty, leading to increased customer lifetime value.
    * However, overcommitting to SLAs without the necessary resources can strain the customer success team and impact employee morale.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Product", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.564565"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
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
                        59.1,
                        45.55,
                        46.14,
                        57.8,
                        48.2,
                        61.75,
                        63.01,
                        45.08,
                        50.46,
                        57.79,
                        51.21,
                        58.92
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.92,
                "unit": "%",
                "change": 7.71,
                "change_percent": 15.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 53.75,
                "min": 45.08,
                "max": 63.01,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20.29,
                        "percentage": 34.4
                },
                {
                        "category": "Segment B",
                        "value": 12.57,
                        "percentage": 21.3
                },
                {
                        "category": "Segment C",
                        "value": 9.03,
                        "percentage": 15.3
                },
                {
                        "category": "Segment D",
                        "value": 2.6,
                        "percentage": 4.4
                },
                {
                        "category": "Other",
                        "value": 14.43,
                        "percentage": 24.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.359399",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Service Level Agreement (SLA) Compliance Rate"
        }
    },
}
