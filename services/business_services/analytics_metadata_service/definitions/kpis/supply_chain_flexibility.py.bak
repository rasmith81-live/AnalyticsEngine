import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainFlexibility(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_FLEXIBILITY",
            name_="Supply Chain Flexibility",
            description_="The ability of the supply chain to adapt to changes in demand, supply, and market conditions without significant performance degradation.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=[],
            formula_="Scored on a predetermined flexibility scale",
            aggregation_methods=['min'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
