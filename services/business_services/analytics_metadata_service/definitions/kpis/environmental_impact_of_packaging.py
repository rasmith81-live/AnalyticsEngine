from analytics_models.definitions.kpis.base_kpi import BaseKPI

class EnvironmentalImpactOfPackaging(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ENVIRONMENTAL_IMPACT_OF_PACKAGING",
            name_="Environmental Impact of Packaging",
            description_="A measure of the environmental footprint of packaging materials, assessing sustainability practices in the supply chain.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="Total Environmental Impact Score / Total Packaging Units",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
