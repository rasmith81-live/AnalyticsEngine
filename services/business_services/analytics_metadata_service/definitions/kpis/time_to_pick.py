from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TimeToPick(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TIME_TO_PICK",
            name_="Time to Pick",
            description_="The time it takes to collect items for an order from the warehouse.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Product', 'Warehouse'],
            formula_="Total Time Taken for Picking / Total Number of Orders Picked",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
