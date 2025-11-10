from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingQualityControlRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_QUALITY_CONTROL_RATE",
            name_="Packing Quality Control Rate",
            description_="The percentage of packed items that pass quality control checks, ensuring product integrity and customer satisfaction.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Customer', 'Order', 'Product', 'QualityMetric'],
            formula_="(Total Passed QC Orders / Total Orders Packed) * 100",
            aggregation_methods=['sum'],
            time_periods=['custom']
        )
