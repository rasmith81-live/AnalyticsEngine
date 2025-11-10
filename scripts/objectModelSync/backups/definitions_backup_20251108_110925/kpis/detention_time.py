from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DetentionTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DETENTION_TIME",
            name_="Detention Time",
            description_="The time a vehicle spends waiting at a facility beyond the expected loading or unloading time.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=[],
            formula_="Total Detention Time / Number of Deliveries",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
