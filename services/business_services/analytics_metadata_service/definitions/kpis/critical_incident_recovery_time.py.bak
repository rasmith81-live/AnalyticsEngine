import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CriticalIncidentRecoveryTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CRITICAL_INCIDENT_RECOVERY_TIME",
            name_="Critical Incident Recovery Time",
            description_="The average time it takes to recover from a critical security incident in the supply chain, demonstrating the resilience of the supply chain operations.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="Sum of Recovery Times for Critical Incidents / Number of Critical Incidents",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
