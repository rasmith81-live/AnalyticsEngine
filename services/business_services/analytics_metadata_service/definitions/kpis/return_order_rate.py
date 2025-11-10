from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ReturnOrderRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="RETURN_ORDER_RATE",
            name_="Return Order Rate",
            description_="The percentage of orders that are returned by customers.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Customer', 'Order', 'Return'],
            formula_="(Number of Returned Orders / Total Number of Orders) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
