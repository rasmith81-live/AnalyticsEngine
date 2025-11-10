from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DeliveryRouteOptimizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DELIVERY_ROUTE_OPTIMIZATION_RATE",
            name_="Delivery Route Optimization Rate",
            description_="The percentage of delivery routes that are optimized for cost, time, and fuel efficiency.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery'],
            formula_="(Number of Optimized Routes / Total Number of Routes) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
