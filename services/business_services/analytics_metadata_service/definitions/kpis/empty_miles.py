from analytics_models.definitions.kpis.base_kpi import BaseKPI

class EmptyMiles(BaseKPI):
    def __init__(self):
        super().__init__(
            code="EMPTY_MILES",
            name_="Empty Miles",
            description_="The number of miles a vehicle travels empty without carrying any load.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=[],
            formula_="(Total Empty Miles / Total Miles Driven) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
