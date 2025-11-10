from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WaterUsageReductionInSupplyChain(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WATER_USAGE_REDUCTION_IN_SUPPLY_CHAIN",
            name_="Water Usage Reduction in Supply Chain",
            description_="The percentage reduction in water usage throughout the supply chain, demonstrating commitment to the ISO 20400 standard.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=[],
            formula_="(Water Usage Before Initiatives - Water Usage After Initiatives) / Water Usage Before Initiatives",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
