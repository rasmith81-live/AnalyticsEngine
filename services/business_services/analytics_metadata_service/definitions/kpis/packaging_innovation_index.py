from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackagingInnovationIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_INNOVATION_INDEX",
            name_="Packaging Innovation Index",
            description_="A measure of the adoption and implementation of innovative packaging solutions, highlighting competitiveness and adaptability.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Innovations Implemented / Total Packaging Solutions) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
