"""
Average Purchase Value

The average amount of money spent by customers per transaction.
"""

AVERAGE_PURCHASE_VALUE = {
    "code": "AVERAGE_PURCHASE_VALUE",
    "name": "Average Purchase Value",
    "description": "The average amount of money spent by customers per transaction.",
    "formula": "Total Revenue / Total Number of Purchases",
    "calculation_formula": "Total Revenue / Total Number of Purchases",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Purchase Value to be added.",
    "trend_analysis": """

    * The average purchase value may increase over time due to inflation or changes in customer spending habits.
    * A decreasing average purchase value could indicate pricing pressure, changes in product mix, or declining customer satisfaction.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or categories driving the changes in average purchase value?
    * How does the average purchase value compare with industry benchmarks or historical data?
    
    """,
    "actionable_tips": """

    * Implement upselling and cross-selling strategies to increase the average purchase value.
    * Offer bundled discounts or loyalty programs to encourage higher spending per transaction.
    * Regularly review and adjust pricing strategies to maintain or increase the average purchase value.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average purchase value over time.
    * Pie charts to visualize the distribution of purchase values across different customer segments or product categories.
    
    """,
    "risk_warnings": """

    * A declining average purchase value may lead to reduced revenue and profitability.
    * An excessively high average purchase value may indicate a lack of customer diversity or potential pricing issues.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems to track customer purchasing behavior and preferences.
    * Point-of-sale (POS) systems with reporting capabilities to analyze transaction data and identify opportunities for increasing purchase value.
    
    """,
    "integration_points": """

    * Integrate average purchase value tracking with marketing automation platforms to personalize offers and promotions based on customer spending patterns.
    * Link with inventory management systems to ensure adequate stock levels for high-value items and optimize product mix.
    
    """,
    "change_impact_analysis": """

    * Increasing the average purchase value can lead to higher revenue and improved customer lifetime value.
    * However, aggressive tactics to raise the average purchase value may negatively impact customer satisfaction and retention.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Purchase History", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.029242"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        276,
                        246,
                        237,
                        265,
                        264,
                        278,
                        278,
                        242,
                        276,
                        268,
                        233,
                        230
                ],
                "unit": "count"
        },
        "current": {
                "value": 230,
                "unit": "count",
                "change": -3,
                "change_percent": -1.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 257.75,
                "min": 230,
                "max": 278,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 76.03,
                        "percentage": 33.1
                },
                {
                        "category": "Category B",
                        "value": 50.11,
                        "percentage": 21.8
                },
                {
                        "category": "Category C",
                        "value": 29.04,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 14.85,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 59.97,
                        "percentage": 26.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.029242",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Purchase Value"
        }
    },
}
