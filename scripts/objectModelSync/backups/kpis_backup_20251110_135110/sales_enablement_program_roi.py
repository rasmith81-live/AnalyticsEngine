"""
Sales Enablement Program Roi

The return on investment of the sales enablement program in terms of revenue generated, cost savings, and productivity improvements.
"""

SALES_ENABLEMENT_PROGRAM_ROI = {
    "code": "SALES_ENABLEMENT_PROGRAM_ROI",
    "name": "Sales Enablement Program Roi",
    "description": "The return on investment of the sales enablement program in terms of revenue generated, cost savings, and productivity improvements.",
    "formula": "(Revenue Attributable to Sales Enablement - Cost of Sales Enablement) / Cost of Sales Enablement",
    "calculation_formula": "(Revenue Attributable to Sales Enablement - Cost of Sales Enablement) / Cost of Sales Enablement",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Enablement Program Roi to be added.",
    "trend_analysis": """


    * Increasing revenue generated from the sales enablement program may indicate positive performance shifts.
    * Decreasing cost savings or productivity improvements could signal negative performance trends.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales enablement initiatives that have consistently led to revenue growth?
    * How does the cost savings and productivity improvements from the program compare with initial expectations?
    
    
    """,
    "actionable_tips": """


    * Regularly review and optimize the sales enablement content and training materials to ensure relevance and effectiveness.
    * Implement feedback mechanisms to gather insights from the sales team on the impact of the program on their performance.
    * Invest in technology that can automate and streamline sales enablement processes to improve efficiency.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of revenue generated over time.
    * Stacked bar charts comparing the cost savings and productivity improvements achieved each quarter.
    
    
    """,
    "risk_warnings": """


    * Failure to generate sufficient revenue from the program may lead to questions about its effectiveness and ROI.
    * Overemphasis on cost savings without considering the impact on sales team productivity and effectiveness.
    
    
    """,
    "tracking_tools": """


    * Sales enablement platforms like Highspot or Seismic for content management and analytics.
    * CRM systems with integrated sales enablement features to track the impact on revenue and productivity.
    
    
    """,
    "integration_points": """


    * Integrate sales enablement data with sales performance management systems to analyze the correlation between enablement efforts and sales results.
    * Link the program with customer relationship management (CRM) systems to understand the impact on customer acquisition and retention.
    
    
    """,
    "change_impact_analysis": """


    * Improving revenue generated from the program can positively impact overall sales team motivation and performance.
    * However, focusing solely on cost savings may lead to reduced investment in critical sales enablement resources and tools.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Enablement Feedback", "Enablement Platform", "Loyalty Program", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.421360"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        781.94,
                        850.15,
                        760.5,
                        732.66,
                        721.75,
                        816.29,
                        804.74,
                        779.21,
                        770.78,
                        753.42,
                        798.57,
                        812.5
                ],
                "unit": "units"
        },
        "current": {
                "value": 812.5,
                "unit": "units",
                "change": 13.93,
                "change_percent": 1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 781.88,
                "min": 721.75,
                "max": 850.15,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 246.27,
                        "percentage": 30.3
                },
                {
                        "category": "Category B",
                        "value": 155.96,
                        "percentage": 19.2
                },
                {
                        "category": "Category C",
                        "value": 92.1,
                        "percentage": 11.3
                },
                {
                        "category": "Category D",
                        "value": 55.44,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 262.73,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.389108",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Enablement Program Roi"
        }
    },
}
