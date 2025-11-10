from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderToDeliveryLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_TO_DELIVERY_LEAD_TIME",
            name_="Order to Delivery Lead Time",
            description_="The total time taken from when an order is placed to when it is delivered.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'Lead', 'Order'],
            formula_="Average Time from Order Placement to Delivery",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
