from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingProcessDowntime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_PROCESS_DOWNTIME",
            name_="Packing Process Downtime",
            description_="The total time when packing operations are halted due to equipment failure or other disruptions, impacting operational efficiency.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="Total Downtime / Total Packing Time",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
