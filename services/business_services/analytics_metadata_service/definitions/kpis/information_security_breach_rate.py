from analytics_models.definitions.kpis.base_kpi import BaseKPI

class InformationSecurityBreachRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INFORMATION_SECURITY_BREACH_RATE",
            name_="Information Security Breach Rate",
            description_="The frequency of breaches in information security within the supply chain, hinting at the robustness of cybersecurity measures.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Number of Information Security Breaches / Time Period) * 100",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
