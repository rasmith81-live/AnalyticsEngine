from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainSustainabilityIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_SUSTAINABILITY_INDEX",
            name_="Supply Chain Sustainability Index",
            description_="A composite metric that evaluates the environmental and social performance of the supply chain operations.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['PurchaseOrder'],
            formula_="Sustainability Score based on predefined criteria",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
