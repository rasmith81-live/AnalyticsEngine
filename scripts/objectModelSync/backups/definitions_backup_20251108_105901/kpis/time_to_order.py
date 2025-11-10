from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TimeToOrder(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TIME_TO_ORDER",
            name_="Time-to-order",
            description_="The time it takes for the buying function to process a purchase request and place an order with a supplier. A shorter time-to-order indicates more efficient processing of requests.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'Supplier'],
            formula_="Total Time for All Identified Needs to Order Placement / Number of Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
