from analytics_models.definitions.kpis.base_kpi import BaseKPI

class MaterialUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="MATERIAL_UTILIZATION_RATE",
            name_="Material Utilization Rate",
            description_="The percentage of packaging materials that are optimally used without excess waste, reflecting sustainable packaging practices.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Material Used / Total Material Available) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
