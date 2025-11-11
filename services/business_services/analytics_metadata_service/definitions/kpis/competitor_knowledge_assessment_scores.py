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
                        61.6,
                        58.7,
                        66.3,
                        64.7,
                        57.5,
                        65.0,
                        69.8,
                        60.2,
                        60.2,
                        59.7,
                        65.3,
                        69.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 69.4,
                "unit": "score",
                "change": 4.1,
                "change_percent": 6.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.2,
                "min": 57.5,
                "max": 69.8,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 23.81,
                        "percentage": 34.3
                },
                {
                        "category": "Segment B",
                        "value": 15.17,
                        "percentage": 21.9
                },
                {
                        "category": "Segment C",
                        "value": 5.82,
                        "percentage": 8.4
                },
                {
                        "category": "Segment D",
                        "value": 5.6,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 19.0,
                        "percentage": 27.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.501762",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Competitor Knowledge Assessment Scores"
        }
    },
}
