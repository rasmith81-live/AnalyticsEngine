from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TimeToReceive(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TIME_TO_RECEIVE",
            name_="Time to Receive",
            description_="The time it takes to accept, process, and store incoming goods.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=[],
            formula_="Total Time Taken for Receiving / Total Number of Deliveries",
            aggregation_methods=['sum', 'min', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
