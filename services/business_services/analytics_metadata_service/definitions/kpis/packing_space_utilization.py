from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingSpaceUtilization(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_SPACE_UTILIZATION",
            name_="Packing Space Utilization",
            description_="The percentage of available packing space that is effectively used, highlighting space management efficiency in packing areas.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Used Packing Space / Total Available Packing Space) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
