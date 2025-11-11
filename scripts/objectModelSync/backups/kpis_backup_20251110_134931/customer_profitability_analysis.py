"""
Customer Profitability Analysis

The analysis of the profit contribution of individual customers or customer segments.
"""

CUSTOMER_PROFITABILITY_ANALYSIS = {
    "code": "CUSTOMER_PROFITABILITY_ANALYSIS",
    "name": "Customer Profitability Analysis",
    "description": "The analysis of the profit contribution of individual customers or customer segments.",
    "formula": "Total Revenue from Customer - Total Costs Associated with Customer",
    "calculation_formula": "Total Revenue from Customer - Total Costs Associated with Customer",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Profitability Analysis to be added.",
    "trend_analysis": """

    * Customer profitability may show an upward trend due to increased customer retention and repeat purchases.
    * A declining trend could indicate pricing issues, increased competition, or declining customer satisfaction.
    
    """,
    "diagnostic_questions": """

    * What are the main drivers of profitability for our top customers?
    * Are there specific customer segments that are consistently less profitable?
    
    """,
    "actionable_tips": """

    * Implement customer segmentation to better understand and cater to the needs of different customer groups.
    * Regularly review pricing strategies to ensure they align with customer value and market conditions.
    * Invest in customer relationship management (CRM) systems to track and manage customer interactions and preferences.
    
    """,
    "visualization_suggestions": """

    * Pareto charts to identify the most profitable customers or segments.
    * Profitability trend lines over time to visualize changes in customer profitability.
    
    """,
    "risk_warnings": """

    * Over-reliance on a small number of highly profitable customers can pose a risk if they are lost.
    * Ignoring less profitable customer segments may lead to missed opportunities for improvement.
    
    """,
    "tracking_tools": """

    * Customer profitability analysis modules within ERP systems like SAP or Oracle.
    * Business intelligence tools for in-depth analysis and reporting on customer profitability.
    
    """,
    "integration_points": """

    * Integrate customer profitability data with sales and marketing systems to align efforts with the most profitable customers.
    * Link customer profitability analysis with customer service platforms to tailor service levels based on customer value.
    
    """,
    "change_impact_analysis": """

    * Improving customer profitability can lead to increased revenue and overall business growth.
    * However, changes in pricing or service levels may impact customer satisfaction and retention.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:43:23.330730"},
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
                        302.27,
                        421.98,
                        389.57,
                        416.77,
                        365.83,
                        349.69,
                        416.11,
                        399.4,
                        346.6,
                        337.8,
                        367.32,
                        343.37
                ],
                "unit": "units"
        },
        "current": {
                "value": 343.37,
                "unit": "units",
                "change": -23.95,
                "change_percent": -6.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 371.39,
                "min": 302.27,
                "max": 421.98,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 95.06,
                        "percentage": 27.7
                },
                {
                        "category": "Category B",
                        "value": 56.79,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 56.51,
                        "percentage": 16.5
                },
                {
                        "category": "Category D",
                        "value": 39.19,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 95.82,
                        "percentage": 27.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.330730",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Profitability Analysis"
        }
    },
}
