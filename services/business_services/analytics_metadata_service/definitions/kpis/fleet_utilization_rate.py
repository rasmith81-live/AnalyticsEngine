from analytics_models.definitions.kpis.base_kpi import BaseKPI

class FleetUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="FLEET_UTILIZATION_RATE",
            name_="Fleet Utilization Rate",
            description_="The percentage of time a fleet is used compared to its availability for use.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder'],
            formula_="(Total Miles Driven / (Number of Vehicles * Maximum Possible Miles)) * 100",
            aggregation_methods=['sum', 'max', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
