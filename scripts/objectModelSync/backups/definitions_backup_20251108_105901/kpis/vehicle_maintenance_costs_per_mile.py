from analytics_models.definitions.kpis.base_kpi import BaseKPI

class VehicleMaintenanceCostsPerMile(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VEHICLE_MAINTENANCE_COSTS_PER_MILE",
            name_="Vehicle Maintenance Costs per Mile",
            description_="The cost incurred for maintaining a vehicle per mile driven.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=[],
            formula_="Total Vehicle Maintenance Costs / Total Miles Driven",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
