from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderCycleTimeVariability(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_CYCLE_TIME_VARIABILITY",
            name_="Order Cycle Time Variability",
            description_="The variation in the time it takes to complete different orders, indicating the consistency of the buying process.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order'],
            formula_="Standard Deviation of Order Cycle Time / Average Order Cycle Time",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
