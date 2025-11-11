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
                        345,
                        351,
                        317,
                        329,
                        358,
                        342,
                        319,
                        338,
                        318,
                        323,
                        337,
                        316
                ],
                "unit": "count"
        },
        "current": {
                "value": 316,
                "unit": "count",
                "change": -21,
                "change_percent": -6.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 332.75,
                "min": 316,
                "max": 358,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 68.94,
                        "percentage": 21.8
                },
                {
                        "category": "Category B",
                        "value": 83.64,
                        "percentage": 26.5
                },
                {
                        "category": "Category C",
                        "value": 37.52,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 36.51,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 89.39,
                        "percentage": 28.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.965985",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Product Knowledge Competency"
        }
    },
}
