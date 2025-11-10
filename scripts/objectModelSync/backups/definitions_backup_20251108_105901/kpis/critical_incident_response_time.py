from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CriticalIncidentResponseTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CRITICAL_INCIDENT_RESPONSE_TIME",
            name_="Critical Incident Response Time",
            description_="The time taken to respond to and address critical incidents in the supply chain, affecting continuity and resilience.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['PurchaseOrder'],
            formula_="Time of Incident Resolution - Time of Incident Identification",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
