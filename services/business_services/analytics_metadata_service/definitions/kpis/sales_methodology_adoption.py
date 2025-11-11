"""
Sales Methodology Adoption

How well and quickly sales reps adopt and implement the sales methodology taught during training.
"""

SALES_METHODOLOGY_ADOPTION = {
    "code": "SALES_METHODOLOGY_ADOPTION",
    "name": "Sales Methodology Adoption",
    "description": "How well and quickly sales reps adopt and implement the sales methodology taught during training.",
    "formula": "(Number of Reps Using the New Methodology / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Reps Using the New Methodology / Total Number of Sales Reps) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Methodology Adoption to be added.",
    "trend_analysis": """



    * Increasing adoption rates may indicate effective training and coaching methods.
    * Decreasing adoption rates could signal a need for reinforcement or adjustments to the sales methodology.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales reps or teams that are struggling to adopt the new methodology?
    * What feedback have sales reps provided about the effectiveness of the training in implementing the new methodology?
    
    
    
    """,
    "actionable_tips": """



    * Provide ongoing coaching and support to reinforce the new methodology.
    * Incorporate the new methodology into regular sales meetings and performance evaluations.
    * Offer incentives for sales reps who demonstrate strong adoption and implementation of the new methodology.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the adoption rates over time for different sales teams or regions.
    * Comparison bar charts to visualize the differences in adoption rates between the new and old methodologies.
    
    
    
    """,
    "risk_warnings": """



    * Low adoption rates may lead to missed sales opportunities and decreased revenue.
    * Inconsistent adoption across the sales team can result in a lack of uniformity in sales approaches and customer experiences.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with built-in sales methodology tracking and reporting capabilities.
    * Sales enablement platforms that offer content and training materials aligned with the new methodology.
    
    
    
    """,
    "integration_points": """



    * Integrate sales methodology adoption data with performance management systems to assess the impact on individual and team sales results.
    * Link adoption rates with customer feedback and satisfaction metrics to understand the correlation between methodology implementation and customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving adoption rates can lead to more consistent sales processes and potentially higher customer satisfaction.
    * However, rapid changes in the methodology may initially impact sales productivity as reps adjust to the new approach.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.440890"},
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
                        66.38,
                        53.92,
                        61.51,
                        61.86,
                        56.42,
                        63.07,
                        58.87,
                        60.59,
                        53.45,
                        65.77,
                        66.4,
                        50.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.89,
                "unit": "%",
                "change": -15.51,
                "change_percent": -23.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 59.93,
                "min": 50.89,
                "max": 66.4,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 13.54,
                        "percentage": 26.6
                },
                {
                        "category": "Channel Sales",
                        "value": 7.86,
                        "percentage": 15.4
                },
                {
                        "category": "Online Sales",
                        "value": 6.94,
                        "percentage": 13.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.19,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 18.36,
                        "percentage": 36.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.037027",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Methodology Adoption"
        }
    },
}
