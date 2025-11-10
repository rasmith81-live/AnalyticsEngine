"""
Worker Safety Incident Rate KPI

SCOR Metric: SC.1.1
Performance Attribute: Social
Level: Level 1 - Strategic

Number of recordable safety incidents per 100 workers

Formula:
(Number of Recordable Incidents / Total Hours Worked) * 200,000

Calculation Details:

        TRIR = Total Recordable Incident Rate
        OSHA standard calculation
        200,000 = hours for 100 workers (50 weeks * 40 hours)
        Includes: Injuries, illnesses requiring medical treatment
        

Required Objects: SafetyIncident, Employee, WorkHours
"""

from analytics_models import KPI

WORKER_SAFETY_INCIDENT_RATE = KPI(
    code="WORKER_SAFETY_INCIDENT_RATE",
    name="Worker Safety Incident Rate",
    category="Supply Chain Social",
    description="Number of recordable safety incidents per 100 workers",
    
    formula="""
(Number of Recordable Incidents / Total Hours Worked) * 200,000
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "SC.1.1",
            "performance_attribute": "Social",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["SafetyIncident", "Employee", "WorkHours"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "incidents_per_100_workers",
        "aggregation_methods": ["rate"],
        "time_periods": ["monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["facility", "department", "shift", "incident_type"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 0.5,
            "advantage": 1.0,
            "parity": 2.0,
            "disadvantage": 3.0
        },
        
        # Calculation Details
        "calculation_detail": """

        TRIR = Total Recordable Incident Rate
        OSHA standard calculation
        200,000 = hours for 100 workers (50 weeks * 40 hours)
        Includes: Injuries, illnesses requiring medical treatment
        
        """,
        
        # Data Quality
        "data_quality_requirements": {
            "completeness": 0.95,
            "accuracy": 0.98,
            "timeliness": "daily"
        },
        
        # Reporting
        "reporting_frequency": ["daily", "weekly", "monthly", "quarterly", "annually"],
        "dashboard_priority": "high",
        "executive_visibility": True
    }
)
