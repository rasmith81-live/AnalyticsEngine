from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainResilienceIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_RESILIENCE_INDEX",
            name_="Supply Chain Resilience Index",
            description_="A measure of the supply chain's ability to withstand and recover from disruptions, maintaining operational continuity and mitigating risks.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=[],
            formula_="Supply Chain Resilience Score",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
