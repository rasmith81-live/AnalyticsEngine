"""
Product Knowledge Competency

The level of understanding the sales team has regarding the products they sell.
"""

PRODUCT_KNOWLEDGE_COMPETENCY = {
    "code": "PRODUCT_KNOWLEDGE_COMPETENCY",
    "name": "Product Knowledge Competency",
    "description": "The level of understanding the sales team has regarding the products they sell.",
    "formula": "(Number of Correct Answers / Total Number of Questions) * 100",
    "calculation_formula": "(Number of Correct Answers / Total Number of Questions) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Knowledge Competency to be added.",
    "trend_analysis": """



    * An increasing product knowledge competency may indicate improved training programs or a focus on continuous learning within the sales team.
    * A decreasing competency could signal high turnover, lack of training resources, or a shift in product offerings that the team is not fully prepared for.
    
    
    
    """,
    "diagnostic_questions": """



    * How often do we assess the product knowledge of our sales team members?
    * What resources and training opportunities are available to improve product knowledge competency?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular product training sessions and assessments to ensure sales team members are up to date with product information.
    * Encourage collaboration between sales and product teams to share insights and updates on product features and benefits.
    * Utilize technology such as knowledge management systems to provide easy access to product information and resources for the sales team.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of product knowledge competency over time.
    * Radar charts comparing individual sales team members' product knowledge competency levels.
    
    
    
    """,
    "risk_warnings": """



    * Low product knowledge competency can lead to missed sales opportunities and decreased customer satisfaction.
    * High turnover within the sales team can negatively impact product knowledge competency and overall sales performance.
    
    
    
    """,
    "tracking_tools": """



    * Utilize learning management systems (LMS) to create and track product knowledge training modules.
    * Implement customer relationship management (CRM) systems with integrated product information to provide quick access for the sales team.
    
    
    
    """,
    "integration_points": """



    * Integrate product knowledge competency assessments with performance management systems to align individual goals with training needs.
    * Link product knowledge competency data with customer feedback and sales performance metrics to understand the impact on customer satisfaction and revenue.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving product knowledge competency can lead to increased sales effectiveness and customer trust, ultimately impacting revenue and market share.
    * However, investing in extensive training and resources for product knowledge may impact short-term costs and resource allocation.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Knowledge Base", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.262887"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
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
                        57.69,
                        48.71,
                        61.56,
                        48.98,
                        56.78,
                        62.88,
                        58.93,
                        55.51,
                        57.29,
                        54.83,
                        57.87,
                        54.82
                ],
                "unit": "%"
        },
        "current": {
                "value": 54.82,
                "unit": "%",
                "change": -3.05,
                "change_percent": -5.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.32,
                "min": 48.71,
                "max": 62.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 18.18,
                        "percentage": 33.2
                },
                {
                        "category": "Product Line B",
                        "value": 11.37,
                        "percentage": 20.7
                },
                {
                        "category": "Product Line C",
                        "value": 5.37,
                        "percentage": 9.8
                },
                {
                        "category": "Services",
                        "value": 3.45,
                        "percentage": 6.3
                },
                {
                        "category": "Other",
                        "value": 16.45,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.624547",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Product Knowledge Competency"
        }
    },
}
