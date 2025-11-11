"""
Sales to New Customers vs. Existing Customers

A comparison of sales made to new versus existing customers, indicating the balance between acquisition and retention efforts.
"""

SALES_TO_NEW_CUSTOMERS_VS_EXISTING_CUSTOMERS = {
    "code": "SALES_TO_NEW_CUSTOMERS_VS_EXISTING_CUSTOMERS",
    "name": "Sales to New Customers vs. Existing Customers",
    "description": "A comparison of sales made to new versus existing customers, indicating the balance between acquisition and retention efforts.",
    "formula": "Total Revenue from New Customers / Total Revenue from Existing Customers",
    "calculation_formula": "Total Revenue from New Customers / Total Revenue from Existing Customers",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales to New Customers vs. Existing Customers to be added.",
    "trend_analysis": """



    * An increasing ratio of sales to new customers may indicate successful acquisition efforts or a decline in repeat business.
    * A decreasing ratio could signal a focus on retention and customer loyalty, or a decline in new customer acquisition.
    
    
    
    """,
    "diagnostic_questions": """



    * What strategies or promotions have been implemented to attract new customers?
    * Are there specific products or services that are driving sales to existing customers?
    
    
    
    """,
    "actionable_tips": """



    * Implement targeted marketing campaigns to attract new customers.
    * Enhance customer loyalty programs to increase repeat business from existing customers.
    * Train sales teams to effectively cross-sell and upsell to existing customers.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts comparing the trend of sales to new and existing customers over time.
    * Pie charts showing the proportion of total sales attributed to new and existing customers.
    
    
    
    """,
    "risk_warnings": """



    * Overemphasis on acquiring new customers may lead to neglect of existing customer relationships.
    * Heavy reliance on existing customers may result in missed opportunities for growth and expansion.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track customer interactions and sales activities.
    * Data analytics tools to segment customer data and identify opportunities for new and repeat business.
    
    
    
    """,
    "integration_points": """



    * Integrate sales data with customer feedback and satisfaction metrics to understand the impact of sales efforts on customer relationships.
    * Link sales performance with marketing and advertising data to evaluate the effectiveness of customer acquisition campaigns.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in sales to new customers may lead to higher revenue but could also strain resources to support new customer onboarding and support.
    * A shift towards more sales to existing customers may improve customer retention and loyalty, but could limit overall business growth.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.521442"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        317.62,
                        437.82,
                        454.17,
                        425.21,
                        350.64,
                        322.91,
                        403.76,
                        327.07,
                        324.65,
                        341.96,
                        428.09,
                        427.06
                ],
                "unit": "units"
        },
        "current": {
                "value": 427.06,
                "unit": "units",
                "change": -1.03,
                "change_percent": -0.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 380.08,
                "min": 317.62,
                "max": 454.17,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 97.43,
                        "percentage": 22.8
                },
                {
                        "category": "Existing Customers",
                        "value": 73.55,
                        "percentage": 17.2
                },
                {
                        "category": "VIP Customers",
                        "value": 77.86,
                        "percentage": 18.2
                },
                {
                        "category": "At-Risk Customers",
                        "value": 17.9,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 160.32,
                        "percentage": 37.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.260572",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales to New Customers vs. Existing Customers"
        }
    },
}
