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
                        361.42,
                        398.1,
                        400.88,
                        404.32,
                        385.8,
                        380.29,
                        419.44,
                        360.02,
                        395.98,
                        364.5,
                        368.92,
                        362.22
                ],
                "unit": "units"
        },
        "current": {
                "value": 362.22,
                "unit": "units",
                "change": -6.7,
                "change_percent": -1.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 383.49,
                "min": 360.02,
                "max": 419.44,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 95.26,
                        "percentage": 26.3
                },
                {
                        "category": "Channel Sales",
                        "value": 43.99,
                        "percentage": 12.1
                },
                {
                        "category": "Online Sales",
                        "value": 53.57,
                        "percentage": 14.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 43.03,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 126.37,
                        "percentage": 34.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.981248",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Enablement Program Roi"
        }
    },
}
