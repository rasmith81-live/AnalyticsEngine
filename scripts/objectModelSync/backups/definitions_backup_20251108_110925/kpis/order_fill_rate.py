from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderFillRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_FILL_RATE",
            name_="Order Fill Rate",
            description_="The percentage of orders that are filled completely and on time. A high fill rate indicates good relationships with suppliers and efficient order processing.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'Supplier'],
            formula_="(Number of Orders Completely Filled / Total Number of Orders) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
