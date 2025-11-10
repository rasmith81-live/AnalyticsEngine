from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CrossDockingEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CROSS_DOCKING_EFFICIENCY",
            name_="Cross-docking Efficiency",
            description_="The effectiveness of moving incoming goods directly to outbound shipping with no storage time.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Product'],
            formula_="(Total Number of Cross-Docked Items / Total Number of Items Received) * 100",
            aggregation_methods=['sum', 'min', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
