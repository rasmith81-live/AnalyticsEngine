from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CybersecurityIncidentImpactReduction(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CYBERSECURITY_INCIDENT_IMPACT_REDUCTION",
            name_="Cybersecurity Incident Impact Reduction",
            description_="The reduction in impact from cybersecurity incidents due to proactive measures, reflecting the effectiveness of cybersecurity in the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Impact of Incidents in Previous Period - Impact of Incidents in Current Period) / Impact of Incidents in Previous Period * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
