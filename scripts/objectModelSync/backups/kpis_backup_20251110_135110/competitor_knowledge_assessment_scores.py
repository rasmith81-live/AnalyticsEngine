"""
Competitor Knowledge Assessment Scores

The scores achieved by sales representatives on assessments regarding competitors' offerings and strategies.
"""

COMPETITOR_KNOWLEDGE_ASSESSMENT_SCORES = {
    "code": "COMPETITOR_KNOWLEDGE_ASSESSMENT_SCORES",
    "name": "Competitor Knowledge Assessment Scores",
    "description": "The scores achieved by sales representatives on assessments regarding competitors' offerings and strategies.",
    "formula": "Average Score on Competitor Knowledge Assessments",
    "calculation_formula": "Average Score on Competitor Knowledge Assessments",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Competitor Knowledge Assessment Scores to be added.",
    "trend_analysis": """


    * Increasing competitor knowledge assessment scores may indicate improved training programs or a deeper understanding of the market.
    * Decreasing scores could signal a lack of focus on competitive intelligence or a shift in the competitive landscape that is not being addressed.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific competitors or product segments where our sales representatives consistently score lower?
    * How do our competitor knowledge assessment scores compare with industry benchmarks or with our own historical data?
    
    
    """,
    "actionable_tips": """


    * Provide regular updates on competitor strategies and offerings through internal communications or training sessions.
    * Encourage sales representatives to actively engage with industry news, attend conferences, and participate in webinars to stay updated on competitors.
    * Implement gamification or rewards for sales reps who demonstrate strong competitor knowledge in their sales pitches or interactions.
    
    
    """,
    "visualization_suggestions": """


    * Radar charts comparing sales representatives' scores on different aspects of competitor knowledge.
    * Line graphs showing the trend of average competitor knowledge assessment scores over time.
    
    
    """,
    "risk_warnings": """


    * Low competitor knowledge assessment scores may result in ineffective sales strategies and missed opportunities.
    * Overemphasis on competitor knowledge without a focus on product knowledge or customer needs can lead to a misalignment in sales approaches.
    
    
    """,
    "tracking_tools": """


    * Competitor tracking software like Crayon or Kompyte to monitor and analyze competitors' offerings and strategies.
    * Sales enablement platforms with built-in competitor intelligence modules to integrate competitor knowledge assessment with sales processes.
    
    
    """,
    "integration_points": """


    * Integrate competitor knowledge assessment scores with performance management systems to align training and coaching efforts with individual sales representatives' needs.
    * Link competitor knowledge assessment with CRM systems to provide sales reps with real-time competitor insights during customer interactions.
    
    
    """,
    "change_impact_analysis": """


    * Improving competitor knowledge assessment scores can lead to more effective sales pitches, better objection handling, and increased win rates.
    * However, a singular focus on competitor knowledge may lead to neglect of other critical sales skills and customer-centric approaches.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Knowledge Base", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.710139"},
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
                        92.2,
                        83.9,
                        91.1,
                        85.3,
                        81.9,
                        81.3,
                        83.4,
                        92.4,
                        88.2,
                        79.9,
                        92.2,
                        84.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 84.6,
                "unit": "score",
                "change": -7.6,
                "change_percent": -8.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 86.37,
                "min": 79.9,
                "max": 92.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 25.31,
                        "percentage": 29.9
                },
                {
                        "category": "Category B",
                        "value": 14.0,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 10.89,
                        "percentage": 12.9
                },
                {
                        "category": "Category D",
                        "value": 4.25,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 30.15,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.136319",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Competitor Knowledge Assessment Scores"
        }
    },
}
