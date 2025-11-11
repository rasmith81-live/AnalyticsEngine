"""
Quarterly Business Review (QBR) Completion Rate

The percentage of QBRs conducted with customers as planned on a quarterly basis.
"""

QUARTERLY_BUSINESS_REVIEW_QBR_COMPLETION_RATE = {
    "code": "QUARTERLY_BUSINESS_REVIEW_QBR_COMPLETION_RATE",
    "name": "Quarterly Business Review (QBR) Completion Rate",
    "description": "The percentage of QBRs conducted with customers as planned on a quarterly basis.",
    "formula": "(Number of Completed QBRs / Total Scheduled QBRs) * 100",
    "calculation_formula": "(Number of Completed QBRs / Total Scheduled QBRs) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Quarterly Business Review (QBR) Completion Rate to be added.",
    "trend_analysis": """



    * An increasing QBR completion rate may indicate improved customer engagement and satisfaction.
    * A decreasing rate could signal challenges in scheduling or conducting QBRs, potentially leading to missed opportunities for upselling or addressing customer needs.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or regions where QBR completion rates are consistently low?
    * How does the QBR completion rate correlate with customer retention and expansion metrics?
    
    
    
    """,
    "actionable_tips": """



    * Implement automated scheduling and reminder systems for QBRs to ensure timely completion.
    * Provide training and resources for sales teams to effectively conduct QBRs and extract valuable insights from customer interactions.
    * Incentivize customers to participate in QBRs by offering exclusive benefits or discounts tied to the review process.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the quarterly trend in QBR completion rates.
    * Pie charts comparing completion rates across different customer segments or industries.
    
    
    
    """,
    "risk_warnings": """



    * Low QBR completion rates may indicate a lack of customer engagement and could lead to increased churn or loss of revenue opportunities.
    * Missed QBRs may result in unaddressed customer issues or unmet needs, impacting overall customer satisfaction and loyalty.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software with built-in QBR scheduling and tracking capabilities.
    * Survey and feedback tools to gather insights from customers about their QBR experience and identify areas for improvement.
    
    
    
    """,
    "integration_points": """



    * Integrate QBR completion data with customer success platforms to align sales and customer success efforts in addressing customer needs.
    * Link QBR completion rates with sales forecasting and pipeline management to identify potential revenue opportunities and risks.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving QBR completion rates can lead to better customer understanding and relationship management, potentially increasing customer lifetime value.
    * Conversely, low completion rates may result in missed opportunities for upselling, cross-selling, and addressing customer concerns, impacting overall sales performance and customer satisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review", "Strategic Review"], "last_validated": "2025-11-10T13:49:33.309978"},
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
                        57.91,
                        71.62,
                        72.2,
                        73.92,
                        68.34,
                        56.41,
                        58.03,
                        68.0,
                        74.68,
                        71.33,
                        73.04,
                        74.12
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.12,
                "unit": "%",
                "change": 1.08,
                "change_percent": 1.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 68.3,
                "min": 56.41,
                "max": 74.68,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.37,
                        "percentage": 22.1
                },
                {
                        "category": "Segment B",
                        "value": 15.23,
                        "percentage": 20.5
                },
                {
                        "category": "Segment C",
                        "value": 12.3,
                        "percentage": 16.6
                },
                {
                        "category": "Segment D",
                        "value": 6.34,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 23.88,
                        "percentage": 32.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.726392",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Quarterly Business Review (QBR) Completion Rate"
        }
    },
}
