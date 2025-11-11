"""
Long-term Training ROI

The return on investment for sales training calculated over a longer period to gauge sustained impact.
"""

LONG_TERM_TRAINING_ROI = {
    "code": "LONG_TERM_TRAINING_ROI",
    "name": "Long-term Training ROI",
    "description": "The return on investment for sales training calculated over a longer period to gauge sustained impact.",
    "formula": "(Gain from Investment in Training - Cost of Training) / Cost of Training",
    "calculation_formula": "(Gain from Investment in Training - Cost of Training) / Cost of Training",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Long-term Training ROI to be added.",
    "trend_analysis": """

    * Long-term training ROI may show an initial dip as the investment in training takes time to yield results, followed by a gradual increase as the impact of training becomes evident.
    * A declining trend could indicate a need for updated training methods or a shift in market dynamics that require different skill sets.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales teams or individuals that have shown sustained improvement in performance after training?
    * How does the long-term training ROI compare with industry benchmarks or competitors' performance?
    
    """,
    "actionable_tips": """

    * Regularly assess the relevance of training content and methods to ensure they align with evolving market needs.
    * Provide ongoing coaching and reinforcement to ensure that training outcomes are sustained over the long term.
    * Encourage a culture of continuous learning and skill development to maximize the long-term impact of training.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of training ROI over multiple years.
    * Comparison graphs to visualize the ROI of different training programs or approaches.
    
    """,
    "risk_warnings": """

    * A consistently low long-term training ROI may indicate a need for a fundamental shift in training strategies or resource allocation.
    * High variability in training ROI over time may point to inconsistent training quality or effectiveness.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and analyze the long-term impact of different training programs.
    * Performance management software to correlate training ROI with individual and team sales performance.
    
    """,
    "integration_points": """

    * Integrate long-term training ROI analysis with HR systems to align training efforts with talent development and retention strategies.
    * Link training ROI data with sales performance metrics to understand the direct impact of training on revenue generation.
    
    """,
    "change_impact_analysis": """

    * Improving long-term training ROI can lead to a more skilled and motivated sales force, potentially increasing overall sales performance and customer satisfaction.
    * Conversely, a declining long-term training ROI may signal a need for significant changes in training approaches to avoid negative impacts on sales effectiveness and employee morale.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.616976"},
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
                        432.7,
                        374.52,
                        338.84,
                        385.95,
                        464.2,
                        345.27,
                        417.86,
                        323.97,
                        448.23,
                        416.63,
                        412.75,
                        354.25
                ],
                "unit": "units"
        },
        "current": {
                "value": 354.25,
                "unit": "units",
                "change": -58.5,
                "change_percent": -14.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 392.93,
                "min": 323.97,
                "max": 464.2,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 66.13,
                        "percentage": 18.7
                },
                {
                        "category": "Category B",
                        "value": 98.07,
                        "percentage": 27.7
                },
                {
                        "category": "Category C",
                        "value": 65.44,
                        "percentage": 18.5
                },
                {
                        "category": "Category D",
                        "value": 29.42,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 95.19,
                        "percentage": 26.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.616976",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Long-term Training ROI"
        }
    },
}
