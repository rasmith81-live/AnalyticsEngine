import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CostPerOrder(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_ORDER",
            name_="Cost per Order",
            description_="The total cost of processing a purchase order, including any fees or charges associated with placing the order. A lower cost per order indicates more efficient use of resources.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Total Cost of Procurement Operations / Total Number of Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
