import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class FulfillmentCostPerOrder(BaseKPI):
    def __init__(self):
        super().__init__(
            code="FULFILLMENT_COST_PER_ORDER",
            name_="Fulfillment Cost per Order",
            description_="The total cost to fulfill an average order, including labor, materials, and overhead.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order'],
            formula_="Total Fulfillment Costs / Total Number of Orders Fulfilled",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
