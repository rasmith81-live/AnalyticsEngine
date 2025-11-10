from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DeliveryDistance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DELIVERY_DISTANCE",
            name_="Average Delivery Distance",
            description_="The average distance covered per delivery.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery'],
            formula_="Total Distance for All Deliveries / Number of Deliveries",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
