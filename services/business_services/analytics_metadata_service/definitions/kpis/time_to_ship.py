from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TimeToShip(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TIME_TO_SHIP",
            name_="Time to Ship",
            description_="The time it takes from receiving an order to shipping it out.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order'],
            formula_="Total Time Taken for Shipping / Total Number of Orders Shipped",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
