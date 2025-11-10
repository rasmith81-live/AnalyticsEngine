from analytics_models.definitions.kpis.base_kpi import BaseKPI

class BackOrderRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="BACK_ORDER_RATE",
            name_="Back Order Rate",
            description_="The percentage of orders that cannot be filled at the time of customer order.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Customer', 'Order', 'Product'],
            formula_="(Number of Items on Backorder / Total Number of Items Ordered) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
