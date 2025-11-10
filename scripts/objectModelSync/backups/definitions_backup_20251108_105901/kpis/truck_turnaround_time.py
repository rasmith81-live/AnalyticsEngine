from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TruckTurnaroundTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TRUCK_TURNAROUND_TIME",
            name_="Truck Turnaround Time",
            description_="The total time from when a truck arrives at a facility until it departs.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Return'],
            formula_="Average Time from Departure to Return for Each Truck",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
