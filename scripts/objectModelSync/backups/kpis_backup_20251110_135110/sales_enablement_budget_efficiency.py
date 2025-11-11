"""
Sales Enablement Budget Efficiency

The efficiency of the sales enablement budget, measured by the ROI generated per dollar spent.
"""

SALES_ENABLEMENT_BUDGET_EFFICIENCY = {
    "code": "SALES_ENABLEMENT_BUDGET_EFFICIENCY",
    "name": "Sales Enablement Budget Efficiency",
    "description": "The efficiency of the sales enablement budget, measured by the ROI generated per dollar spent.",
    "formula": "(Sales Growth Attributed to Sales Enablement / Sales Enablement Budget Spent)",
    "calculation_formula": "(Sales Growth Attributed to Sales Enablement / Sales Enablement Budget Spent)",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Enablement Budget Efficiency to be added.",
    "trend_analysis": """


    * An increasing ROI per dollar spent may indicate that sales enablement initiatives are effectively driving revenue growth.
    * A decreasing ROI could signal inefficiencies in the sales enablement budget allocation or a lack of impact from the initiatives.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales enablement activities or programs that consistently deliver higher ROI?
    * How does the ROI from the sales enablement budget compare with industry benchmarks or with previous periods?
    
    
    """,
    "actionable_tips": """


    * Regularly assess the performance of sales enablement initiatives and reallocate budget to activities with higher ROI.
    * Invest in training and development programs to enhance the effectiveness of the sales team, thus improving the ROI of sales enablement efforts.
    * Utilize technology to automate repetitive tasks and streamline sales processes, maximizing the impact of the sales enablement budget.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of ROI generated per dollar spent over time.
    * Pareto charts to identify the sales enablement activities that contribute the most to ROI.
    
    
    """,
    "risk_warnings": """


    * Low ROI from the sales enablement budget may lead to decreased motivation and engagement among the sales team.
    * A consistently declining ROI could indicate a need for a fundamental reevaluation of sales enablement strategies and budget allocation.
    
    
    """,
    "tracking_tools": """


    * Sales enablement platforms like Highspot or Seismic to track the impact of enablement activities on revenue generation.
    * CRM systems such as Salesforce or HubSpot to analyze the correlation between sales enablement efforts and actual sales performance.
    
    
    """,
    "integration_points": """


    * Integrate ROI data from the sales enablement budget with financial reporting systems to provide a comprehensive view of overall business performance.
    * Link sales enablement ROI with sales performance metrics to understand the direct impact of enablement efforts on sales outcomes.
    
    
    """,
    "change_impact_analysis": """


    * Improving the ROI of the sales enablement budget can lead to increased sales productivity and revenue growth.
    * Conversely, a declining ROI may result in missed sales opportunities and reduced competitiveness in the market.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.411509"},
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
                        778.14,
                        759.79,
                        745.13,
                        736.18,
                        851.25,
                        826.93,
                        787.01,
                        758.08,
                        870.18,
                        851.5,
                        789.45,
                        726.86
                ],
                "unit": "units"
        },
        "current": {
                "value": 726.86,
                "unit": "units",
                "change": -62.59,
                "change_percent": -7.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 790.04,
                "min": 726.86,
                "max": 870.18,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 170.93,
                        "percentage": 23.5
                },
                {
                        "category": "Category B",
                        "value": 152.18,
                        "percentage": 20.9
                },
                {
                        "category": "Category C",
                        "value": 131.19,
                        "percentage": 18.0
                },
                {
                        "category": "Category D",
                        "value": 48.2,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 224.36,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.369973",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Enablement Budget Efficiency"
        }
    },
}
