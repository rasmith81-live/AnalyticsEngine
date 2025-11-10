from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderPackingCapacity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_PACKING_CAPACITY",
            name_="Order Packing Capacity",
            description_="The maximum number of orders that can be packed within a given time frame, indicating the capability of packing operations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order'],
            formula_="Total Orders Packed / Total Packing Time",
            aggregation_methods=['sum', 'max', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
