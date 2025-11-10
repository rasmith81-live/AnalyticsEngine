"""
Carbon Emissions per Unit KPI

SCOR Metric: EV.1.1
Performance Attribute: Environmental
Level: Level 1 - Strategic

Total greenhouse gas emissions per unit produced/delivered

Formula:
Total CO2 Equivalent Emissions / Units Produced

Calculation Details:

        Carbon Footprint = GHG emissions per unit
        Includes: Scope 1, 2, and 3 emissions
        - Scope 1: Direct emissions (manufacturing)
        - Scope 2: Indirect (electricity, heating)
        - Scope 3: Supply chain (suppliers, logistics)
        

Required Objects: Emission, Production, Energy, Transportation
"""

from analytics_models import KPI

CARBON_EMISSIONS_PER_UNIT = KPI(
    code="CARBON_EMISSIONS_PER_UNIT",
    name="Carbon Emissions per Unit",
    category="Supply Chain Environmental",
    description="Total greenhouse gas emissions per unit produced/delivered",
    
    formula="""
Total CO2 Equivalent Emissions / Units Produced
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "EV.1.1",
            "performance_attribute": "Environmental",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Emission", "Production", "Energy", "Transportation"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "kg_co2e",
        "aggregation_methods": ["average", "sum"],
        "time_periods": ["monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["product_line", "facility", "scope", "source"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": "< 5 kg CO2e/unit",
            "advantage": "5-10 kg CO2e/unit",
            "parity": "10-20 kg CO2e/unit",
            "disadvantage": "> 20 kg CO2e/unit"
        },
        
        # Calculation Details
        "calculation_detail": """

        Carbon Footprint = GHG emissions per unit
        Includes: Scope 1, 2, and 3 emissions
        - Scope 1: Direct emissions (manufacturing)
        - Scope 2: Indirect (electricity, heating)
        - Scope 3: Supply chain (suppliers, logistics)
        
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
