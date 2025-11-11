"""
Customer Satisfaction Score (CSAT)

A metric that assesses how satisfied customers are with a company's products or services.
"""

CUSTOMER_SATISFACTION_SCORE_CSAT = {
    "code": "CUSTOMER_SATISFACTION_SCORE_CSAT",
    "name": "Customer Satisfaction Score (CSAT)",
    "description": "A metric that assesses how satisfied customers are with a company's products or services.",
    "formula": "Average of Customer Satisfaction Ratings on a Scale (e.g., 1-5)",
    "calculation_formula": "Average of Customer Satisfaction Ratings on a Scale (e.g., 1-5)",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Satisfaction Score (CSAT) to be added.",
    "trend_analysis": """



    * Increasing CSAT scores may indicate improved product quality or customer service.
    * Decreasing scores could signal issues with product performance, customer support, or overall satisfaction.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific aspects of our products or services are contributing to higher or lower CSAT scores?
    * Are there common themes or patterns in customer feedback that correlate with changes in CSAT scores?
    
    
    
    """,
    "actionable_tips": """



    * Regularly solicit and act on customer feedback to address pain points and improve satisfaction.
    * Invest in training and development for customer-facing teams to enhance service quality.
    * Implement quality control measures to ensure products meet or exceed customer expectations.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing CSAT scores over time to identify trends and fluctuations.
    * Pie charts to visualize the distribution of satisfaction levels across different products or services.
    
    
    
    """,
    "risk_warnings": """



    * Low CSAT scores can lead to customer churn and negative word-of-mouth, impacting revenue and brand reputation.
    * Ignoring or neglecting customer feedback can result in missed opportunities for improvement and long-term success.
    
    
    
    """,
    "tracking_tools": """



    * Customer feedback and survey platforms like SurveyMonkey or Qualtrics for collecting and analyzing satisfaction data.
    * CRM systems with built-in CSAT tracking and reporting capabilities for seamless integration with customer interactions.
    
    
    
    """,
    "integration_points": """



    * Integrate CSAT data with customer relationship management systems to personalize interactions and address individual satisfaction concerns.
    * Link CSAT scores with product development and quality assurance processes to align improvements with customer needs.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving CSAT scores can lead to increased customer loyalty and lifetime value, offsetting initial investment costs.
    * Conversely, declining CSAT scores may result in higher customer acquisition costs as a result of churn and negative reviews.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.876796"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
    "module_code": "CUSTOMER_RETENTION",
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
                        72.7,
                        79.9,
                        72.3,
                        77.1,
                        80.3,
                        77.7,
                        74.3,
                        76.3,
                        82.3,
                        72.8,
                        80.4,
                        80.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 80.6,
                "unit": "score",
                "change": 0.2,
                "change_percent": 0.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 77.22,
                "min": 72.3,
                "max": 82.3,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 21.64,
                        "percentage": 26.8
                },
                {
                        "category": "Existing Customers",
                        "value": 11.75,
                        "percentage": 14.6
                },
                {
                        "category": "VIP Customers",
                        "value": 10.02,
                        "percentage": 12.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 7.95,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 29.24,
                        "percentage": 36.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.793325",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Customer Satisfaction Score (CSAT)"
        }
    },
}
