from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_CYCLE_TIME",
            name_="Total Order Cycle Time",
            description_="The total time from when an order is placed until it's delivered to the customer.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Customer', 'Delivery', 'Order'],
            formula_="Sum of Time from Order Placement to Order Delivery / Total Number of Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
