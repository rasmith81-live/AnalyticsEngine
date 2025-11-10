from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerOrderCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_ORDER_CYCLE_TIME",
            name_="Customer Order Cycle Time",
            description_="The total time taken from receiving a customer order to delivering the product or service, reflecting the speed of the supply chain.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Customer', 'Delivery', 'Order', 'Product'],
            formula_="Time of Order Delivery - Time of Order Placement",
            aggregation_methods=['sum'],
            time_periods=['custom']
        )
