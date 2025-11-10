import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainPackingCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_PACKING_CYCLE_TIME",
            name_="Supply Chain Packing Cycle Time",
            description_="The total time from order placement to packing completion in the supply chain, providing a measure of packing speed and responsiveness.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Total Packing Cycle Time / Total Orders Packed",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
