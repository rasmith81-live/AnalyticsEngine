from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierOnTimeDeliveryRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_ON_TIME_DELIVERY_RATE",
            name_="Supplier On-time Delivery Rate",
            description_="The percentage of orders delivered by suppliers on or before the promised delivery date, indicating their reliability and efficiency.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Delivery', 'Order', 'Supplier'],
            formula_="(Number of On-time Deliveries / Total Deliveries) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
