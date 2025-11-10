from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WarehouseSafetyIncidentsRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_SAFETY_INCIDENTS_RATE",
            name_="Warehouse Safety Incidents Rate",
            description_="The number of safety incidents recorded in a warehouse per time unit.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Warehouse'],
            formula_="(Total Number of Safety Incidents / Total Warehouse Hours Worked) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
