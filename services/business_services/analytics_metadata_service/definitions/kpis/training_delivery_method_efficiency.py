"""
Training Delivery Method Efficiency

An evaluation of the effectiveness of different training delivery methods (e.g., in-person, online, blended learning).
"""

TRAINING_DELIVERY_METHOD_EFFICIENCY = {
    "code": "TRAINING_DELIVERY_METHOD_EFFICIENCY",
    "name": "Training Delivery Method Efficiency",
    "description": "An evaluation of the effectiveness of different training delivery methods (e.g., in-person, online, blended learning).",
    "formula": "Efficiency Rating Based on Performance Improvements Post-Training",
    "calculation_formula": "Efficiency Rating Based on Performance Improvements Post-Training",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Delivery Method Efficiency to be added.",
    "trend_analysis": """



    * Increased utilization of online training methods may indicate a shift towards remote work and virtual learning.
    * A decline in in-person training effectiveness could signal a need for updated content or more engaging delivery methods.
    
    
    
    """,
    "diagnostic_questions": """



    * Are certain topics or skills better suited for specific training delivery methods?
    * How do participant feedback and performance metrics differ across different training delivery methods?
    
    
    
    """,
    "actionable_tips": """



    * Customize training content to fit the delivery method, ensuring it is engaging and interactive.
    * Regularly assess and update online training platforms to incorporate new technologies and learning trends.
    * Provide options for blended learning to cater to different learning styles and preferences.
    
    
    
    """,
    "visualization_suggestions": """



    * Line graphs showing the effectiveness of different training delivery methods over time.
    * Comparison charts displaying participant feedback and performance metrics for each delivery method.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on a single delivery method may lead to disengagement and reduced effectiveness of training.
    * Ignoring participant feedback on delivery methods can result in decreased learning outcomes and knowledge retention.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) with analytics capabilities to track participant engagement and performance across different delivery methods.
    * Virtual reality (VR) and augmented reality (AR) technologies for immersive online training experiences.
    
    
    
    """,
    "integration_points": """



    * Integrate training delivery method data with HR systems to align learning strategies with employee development goals.
    * Link participant feedback from different delivery methods with performance management systems to identify correlations with job performance.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the effectiveness of training delivery methods can lead to better knowledge retention and application in the workplace.
    * However, changes in delivery methods may require additional resources and time for content development and implementation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.736599"},
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
                        122.02,
                        168.7,
                        139.42,
                        91.51,
                        87.5,
                        186.34,
                        153.39,
                        174.91,
                        122.81,
                        183.19,
                        167.21,
                        214.15
                ],
                "unit": "units"
        },
        "current": {
                "value": 214.15,
                "unit": "units",
                "change": 46.94,
                "change_percent": 28.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 150.93,
                "min": 87.5,
                "max": 214.15,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 56.48,
                        "percentage": 26.4
                },
                {
                        "category": "Segment B",
                        "value": 32.13,
                        "percentage": 15.0
                },
                {
                        "category": "Segment C",
                        "value": 30.7,
                        "percentage": 14.3
                },
                {
                        "category": "Segment D",
                        "value": 27.6,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 67.24,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.836137",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Training Delivery Method Efficiency"
        }
    },
}
