from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainVisibilityIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_VISIBILITY_INDEX",
            name_="Supply Chain Visibility Index",
            description_="The degree to which the organization has visibility over its entire supply chain, which is critical for identifying and mitigating security risks.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Sum of Visibility Metrics Scores) / (Total Number of Visibility Metrics)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
