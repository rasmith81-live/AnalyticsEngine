from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainRedundancyLevel(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_REDUNDANCY_LEVEL",
            name_="Supply Chain Redundancy Level",
            description_="The level of redundancy built into the supply chain to ensure continuity in the event of a disruption or security breach.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Number of Redundant Supply Chain Elements / Total Supply Chain Elements) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
