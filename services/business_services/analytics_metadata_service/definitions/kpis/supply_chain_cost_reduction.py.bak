import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainCostReduction(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_COST_REDUCTION",
            name_="Supply Chain Cost Reduction",
            description_="The amount of cost savings achieved through efficiency improvements in the supply chain operations.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=[],
            formula_="(Previous Period Costs - Current Period Costs) / Previous Period Costs * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
