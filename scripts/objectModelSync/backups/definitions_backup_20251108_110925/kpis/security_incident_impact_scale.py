from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SecurityIncidentImpactScale(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_INCIDENT_IMPACT_SCALE",
            name_="Security Incident Impact Scale",
            description_="A scale that rates the impact of security incidents, helping to prioritize response efforts and allocate resources effectively.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="(Sum of Incident Impact Scores) / (Total Number of Incidents)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
