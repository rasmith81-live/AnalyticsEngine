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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.863519"},
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
                        828.36,
                        880.3,
                        843.97,
                        895.73,
                        784.2,
                        859.22,
                        869.09,
                        804.03,
                        868.01,
                        873.8,
                        823.86,
                        789.39
                ],
                "unit": "units"
        },
        "current": {
                "value": 789.39,
                "unit": "units",
                "change": -34.47,
                "change_percent": -4.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 843.33,
                "min": 784.2,
                "max": 895.73,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 216.34,
                        "percentage": 27.4
                },
                {
                        "category": "Existing Customers",
                        "value": 91.53,
                        "percentage": 11.6
                },
                {
                        "category": "VIP Customers",
                        "value": 136.84,
                        "percentage": 17.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 96.38,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 248.3,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.761713",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Profitability Analysis"
        }
    },
}
