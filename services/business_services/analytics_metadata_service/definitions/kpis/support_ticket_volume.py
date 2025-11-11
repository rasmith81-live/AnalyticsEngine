"""
Support Ticket Volume

The number of customer support tickets or inquiries received over a certain period of time.
"""

SUPPORT_TICKET_VOLUME = {
    "code": "SUPPORT_TICKET_VOLUME",
    "name": "Support Ticket Volume",
    "description": "The number of customer support tickets or inquiries received over a certain period of time.",
    "formula": "Total Number of Support Tickets Received",
    "calculation_formula": "Total Number of Support Tickets Received",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Support Ticket Volume to be added.",
    "trend_analysis": """



    * An increasing support ticket volume may indicate product or service issues that need to be addressed.
    * A decreasing volume could signal improved product quality or customer education leading to fewer inquiries.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that are generating a disproportionate number of support tickets?
    * How does our support ticket volume compare with industry benchmarks or with previous periods?
    
    
    
    """,
    "actionable_tips": """



    * Invest in product or service improvements based on common support ticket themes.
    * Provide additional customer education or resources to address recurring support ticket topics.
    * Implement proactive customer outreach to address potential support issues before they become tickets.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing support ticket volume over time to identify trends and patterns.
    * Pie charts to visualize the distribution of support tickets by product or service category.
    
    
    
    """,
    "risk_warnings": """



    * High support ticket volume can lead to customer frustration and dissatisfaction.
    * Chronic support ticket issues may indicate underlying product or service quality problems.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and manage support tickets.
    * Help desk software to streamline ticket resolution processes and identify common issues.
    
    
    
    """,
    "integration_points": """



    * Integrate support ticket data with product development teams to address recurring issues.
    * Link support ticket volume with customer satisfaction metrics to understand the impact on overall customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing support ticket volume can lead to cost savings and improved customer satisfaction.
    * However, a sudden decrease in support ticket volume may also indicate a decline in customer engagement or feedback, which could impact product development and innovation.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.692108"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        378,
                        377,
                        396,
                        385,
                        412,
                        379,
                        397,
                        367,
                        395,
                        399,
                        378,
                        401
                ],
                "unit": "count"
        },
        "current": {
                "value": 401,
                "unit": "count",
                "change": 23,
                "change_percent": 6.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 388.67,
                "min": 367,
                "max": 412,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 117.26,
                        "percentage": 29.2
                },
                {
                        "category": "Segment B",
                        "value": 60.39,
                        "percentage": 15.1
                },
                {
                        "category": "Segment C",
                        "value": 64.36,
                        "percentage": 16.0
                },
                {
                        "category": "Segment D",
                        "value": 42.59,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 116.4,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.710134",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Support Ticket Volume"
        }
    },
}
