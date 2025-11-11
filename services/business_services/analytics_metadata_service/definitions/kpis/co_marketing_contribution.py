"""
Co-Marketing Contribution

The contribution of channel partners to joint marketing efforts and the effectiveness of those efforts in generating leads and sales.
"""

CO_MARKETING_CONTRIBUTION = {
    "code": "CO_MARKETING_CONTRIBUTION",
    "name": "Co-Marketing Contribution",
    "description": "The contribution of channel partners to joint marketing efforts and the effectiveness of those efforts in generating leads and sales.",
    "formula": "Total Revenue from Co-Marketing Campaigns / Total Co-Marketing Investment",
    "calculation_formula": "Total Revenue from Co-Marketing Campaigns / Total Co-Marketing Investment",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Co-Marketing Contribution to be added.",
    "trend_analysis": """



    * An increasing co-marketing contribution may indicate stronger collaboration with channel partners and more effective joint marketing efforts.
    * A decreasing co-marketing contribution could signal a lack of engagement from channel partners or ineffective marketing strategies.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific marketing activities that have shown better results in generating leads and sales?
    * How do our co-marketing efforts compare with industry benchmarks or with those of our competitors?
    
    
    
    """,
    "actionable_tips": """



    * Provide training and resources to channel partners to improve their marketing capabilities.
    * Regularly review and optimize joint marketing strategies to ensure they are aligned with the needs and preferences of the target audience.
    * Establish clear goals and expectations for co-marketing efforts to ensure accountability and effectiveness.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of leads and sales generated from co-marketing activities over time.
    * Pie charts illustrating the distribution of leads and sales by channel partner or marketing activity.
    
    
    
    """,
    "risk_warnings": """



    * A low co-marketing contribution may result in missed opportunities for lead generation and sales growth.
    * Over-reliance on a few channel partners for co-marketing efforts can create vulnerability if those partners disengage or underperform.
    
    
    
    """,
    "tracking_tools": """



    * Marketing automation platforms to streamline joint marketing campaigns and track their performance.
    * Collaboration tools for effective communication and resource sharing with channel partners.
    
    
    
    """,
    "integration_points": """



    * Integrate co-marketing contribution data with CRM systems to track the impact on lead conversion and sales pipeline.
    * Link co-marketing efforts with sales performance metrics to assess the direct influence on revenue generation.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving co-marketing contribution can lead to increased brand visibility and market share, but may also require additional investment in resources and support for channel partners.
    * A decrease in co-marketing contribution may negatively impact overall sales performance and the strength of the channel partner relationships.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Co-Marketing Campaign", "Customer", "Lead", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.701138"},
    "required_objects": [],
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
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
                        773.62,
                        744.85,
                        846.01,
                        800.97,
                        809.16,
                        753.28,
                        755.04,
                        768.98,
                        866.0,
                        769.38,
                        855.59,
                        873.11
                ],
                "unit": "units"
        },
        "current": {
                "value": 873.11,
                "unit": "units",
                "change": 17.52,
                "change_percent": 2.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 801.33,
                "min": 744.85,
                "max": 873.11,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 167.32,
                        "percentage": 19.2
                },
                {
                        "category": "Segment B",
                        "value": 167.79,
                        "percentage": 19.2
                },
                {
                        "category": "Segment C",
                        "value": 174.54,
                        "percentage": 20.0
                },
                {
                        "category": "Segment D",
                        "value": 84.66,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 278.8,
                        "percentage": 31.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.481246",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Co-Marketing Contribution"
        }
    },
}
