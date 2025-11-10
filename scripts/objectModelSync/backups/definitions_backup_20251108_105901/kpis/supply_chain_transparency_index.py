from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainTransparencyIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_TRANSPARENCY_INDEX",
            name_="Supply Chain Transparency Index",
            description_="A measure of the visibility and traceability of products and materials throughout the supply chain, as recommended by ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Product'],
            formula_="(Sum of Transparency Criteria Met) / (Total Number of Transparency Criteria) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
