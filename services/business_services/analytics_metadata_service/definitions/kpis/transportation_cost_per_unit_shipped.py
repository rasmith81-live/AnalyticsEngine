import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class TransportationCostPerUnitShipped(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TRANSPORTATION_COST_PER_UNIT_SHIPPED",
            name_="Transportation Cost per Unit Shipped",
            description_="The average cost associated with transporting a single unit of product, with lower costs indicating a more efficient transportation strategy.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Product', 'PurchaseOrder'],
            formula_="Total Transportation Costs / Total Units Shipped",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
