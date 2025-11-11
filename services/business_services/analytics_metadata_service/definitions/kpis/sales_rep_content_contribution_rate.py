"""
Sales Rep Content Contribution Rate

The percentage of sales content that is contributed by sales representatives, encouraging involvement and tailored content.
"""

SALES_REP_CONTENT_CONTRIBUTION_RATE = {
    "code": "SALES_REP_CONTENT_CONTRIBUTION_RATE",
    "name": "Sales Rep Content Contribution Rate",
    "description": "The percentage of sales content that is contributed by sales representatives, encouraging involvement and tailored content.",
    "formula": "(Number of Rep Contributions / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Rep Contributions / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Rep Content Contribution Rate to be added.",
    "trend_analysis": """



    * An increasing sales rep content contribution rate may indicate a more engaged sales team and better alignment with customer needs.
    * A decreasing rate could signal disengagement or a lack of focus on creating tailored content for specific customer segments.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales reps consistently contributing high-quality content, and if so, what can be learned from their approach?
    * How does the content contributed by sales reps align with the overall sales strategy and customer preferences?
    
    
    
    """,
    "actionable_tips": """



    * Provide training and resources to help sales reps understand the types of content that resonate with different customer personas.
    * Implement a content review process to ensure that contributed materials meet quality standards and align with the sales strategy.
    * Encourage collaboration between sales and marketing teams to develop content that addresses specific customer pain points and objections.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the contribution rate over time for individual sales reps or teams.
    * Pie charts illustrating the distribution of content contributions by sales reps across different customer segments or product lines.
    
    
    
    """,
    "risk_warnings": """



    * A low sales rep content contribution rate may result in generic, less effective sales materials that do not resonate with customers.
    * Over-reliance on a few sales reps for content contribution can lead to burnout and uneven distribution of workload.
    
    
    
    """,
    "tracking_tools": """



    * Content management systems like HubSpot or Salesforce to track and analyze the content contributed by sales reps.
    * Sales enablement platforms that provide templates and guidance for creating tailored content based on customer insights.
    
    
    
    """,
    "integration_points": """



    * Integrate the sales rep content contribution rate with customer relationship management (CRM) systems to understand how content impacts customer interactions and conversions.
    * Linking content contribution with sales performance metrics to assess the effectiveness of tailored content in driving revenue.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the sales rep content contribution rate can lead to more personalized and effective sales interactions, potentially increasing conversion rates and customer satisfaction.
    * Conversely, a low contribution rate may result in missed opportunities to address customer needs and differentiate from competitors, impacting overall sales performance.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.480356"},
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
                        49.16,
                        41.25,
                        57.29,
                        52.01,
                        55.24,
                        49.72,
                        44.96,
                        53.23,
                        46.81,
                        59.17,
                        57.85,
                        57.16
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.16,
                "unit": "%",
                "change": -0.69,
                "change_percent": -1.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 51.99,
                "min": 41.25,
                "max": 59.17,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 12.44,
                        "percentage": 21.8
                },
                {
                        "category": "Channel Sales",
                        "value": 7.69,
                        "percentage": 13.5
                },
                {
                        "category": "Online Sales",
                        "value": 11.65,
                        "percentage": 20.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.03,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 22.35,
                        "percentage": 39.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.152586",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Rep Content Contribution Rate"
        }
    },
}
