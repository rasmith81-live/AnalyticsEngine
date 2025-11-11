"""
Customer Lifetime Value (CLTV)

The total amount of revenue a customer is expected to generate over the course of their relationship with the company. This KPI measures the impact of the Customer Success Team's efforts on revenue.
"""

CUSTOMER_LIFETIME_VALUE_CLTV = {
    "code": "CUSTOMER_LIFETIME_VALUE_CLTV",
    "name": "Customer Lifetime Value (CLTV)",
    "description": "The total amount of revenue a customer is expected to generate over the course of their relationship with the company. This KPI measures the impact of the Customer Success Team's efforts on revenue.",
    "formula": "(Average Revenue Per Account * Customer Relationship Duration) - Acquisition and Service Costs",
    "calculation_formula": "(Average Revenue Per Account * Customer Relationship Duration) - Acquisition and Service Costs",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Lifetime Value (CLTV) to be added.",
    "trend_analysis": """



    * Increasing CLTV may indicate successful upselling or cross-selling efforts.
    * Decreasing CLTV could signal poor customer retention or dissatisfaction.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments with significantly higher or lower CLTV?
    * What factors contribute to the decline or growth of CLTV for different customer groups?
    
    
    
    """,
    "actionable_tips": """



    * Focus on improving customer satisfaction and loyalty through better service and support.
    * Implement targeted marketing campaigns to increase customer engagement and repeat purchases.
    * Personalize the customer experience to build long-term relationships and maximize CLTV.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing CLTV trends over time for different customer segments.
    * Pareto charts to identify the most valuable customer segments contributing to overall CLTV.
    
    
    
    """,
    "risk_warnings": """



    * Low CLTV may indicate a need for improved product quality or customer experience.
    * High CLTV from a few customers may pose a risk if those customers are lost.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track customer interactions and behavior.
    * Analytics tools to analyze customer data and identify opportunities for increasing CLTV.
    
    
    
    """,
    "integration_points": """



    * Integrate CLTV tracking with sales and marketing systems to align efforts towards maximizing customer value.
    * Link CLTV with customer feedback and satisfaction metrics to understand the impact of customer experience on value.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving CLTV may require investment in customer service and product development.
    * Reducing CLTV could impact revenue and profitability in the long run.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Product", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.844542"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"],
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
                        476,
                        462,
                        454,
                        472,
                        454,
                        465,
                        485,
                        487,
                        459,
                        476,
                        456,
                        478
                ],
                "unit": "count"
        },
        "current": {
                "value": 478,
                "unit": "count",
                "change": 22,
                "change_percent": 4.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 468.67,
                "min": 454,
                "max": 487,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 102.84,
                        "percentage": 21.5
                },
                {
                        "category": "Mid-Market",
                        "value": 83.2,
                        "percentage": 17.4
                },
                {
                        "category": "Small Business",
                        "value": 76.98,
                        "percentage": 16.1
                },
                {
                        "category": "Strategic Partners",
                        "value": 33.48,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 181.5,
                        "percentage": 38.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.715485",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Lifetime Value (CLTV)"
        }
    },
}
