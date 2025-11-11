"""
Sales Revenue Growth

The growth in sales revenue over a specific period. A higher growth rate indicates effective training and coaching.
"""

SALES_REVENUE_GROWTH = {
    "code": "SALES_REVENUE_GROWTH",
    "name": "Sales Revenue Growth",
    "description": "The growth in sales revenue over a specific period. A higher growth rate indicates effective training and coaching.",
    "formula": "(Sales Revenue Post-Training - Sales Revenue Pre-Training) / Sales Revenue Pre-Training * 100",
    "calculation_formula": "(Sales Revenue Post-Training - Sales Revenue Pre-Training) / Sales Revenue Pre-Training * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Revenue Growth to be added.",
    "trend_analysis": """


    * A steady increase in sales revenue growth may indicate effective training and coaching methods that are positively impacting the sales team's performance.
    * An inconsistent or declining growth rate could signal a need for adjustments in the training and coaching strategies to better support the sales team.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales territories or product lines that are driving the majority of the sales revenue growth?
    * How do the sales revenue growth trends align with the implementation of new training and coaching initiatives?
    
    
    """,
    "actionable_tips": """


    * Regularly assess and update the training and coaching programs to ensure they are aligned with the evolving needs of the sales team.
    * Provide ongoing support and resources to sales managers to effectively implement the training and coaching strategies with their teams.
    * Encourage a culture of continuous learning and skill development within the sales team to drive sustained sales revenue growth.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the sales revenue growth over time to identify any consistent patterns or fluctuations.
    * Comparative bar charts to visualize the sales revenue growth across different sales territories or product categories.
    
    
    """,
    "risk_warnings": """


    * Overreliance on a few high-performing sales representatives may lead to inconsistent or unsustainable sales revenue growth.
    * Inadequate training and coaching may result in missed sales opportunities and hinder overall sales revenue growth.
    
    
    """,
    "tracking_tools": """


    * Sales performance management software to track individual and team sales metrics and identify areas for improvement.
    * Customer relationship management (CRM) systems to analyze customer interactions and identify potential sales opportunities for revenue growth.
    
    
    """,
    "integration_points": """


    * Integrate sales revenue growth data with marketing analytics to understand the impact of marketing efforts on driving sales.
    * Align sales revenue growth with financial reporting systems to track the overall impact on the organization's bottom line.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales revenue growth can lead to increased profitability and overall business success.
    * However, rapid sales revenue growth may also strain operational resources and require adjustments in production or service delivery to meet increased demand.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.493525"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        45751.45,
                        48261.65,
                        42508.61,
                        47659.26,
                        47421.93,
                        39635.65,
                        44909.63,
                        38113.19,
                        43128.1,
                        41318.99,
                        39949.47,
                        38089.69
                ],
                "unit": "$"
        },
        "current": {
                "value": 38089.69,
                "unit": "$",
                "change": -1859.78,
                "change_percent": -4.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 43062.3,
                "min": 38089.69,
                "max": 48261.65,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11758.12,
                        "percentage": 30.9
                },
                {
                        "category": "Category B",
                        "value": 8024.05,
                        "percentage": 21.1
                },
                {
                        "category": "Category C",
                        "value": 3466.88,
                        "percentage": 9.1
                },
                {
                        "category": "Category D",
                        "value": 2242.02,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 12598.62,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.596794",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Sales Revenue Growth"
        }
    },
}
