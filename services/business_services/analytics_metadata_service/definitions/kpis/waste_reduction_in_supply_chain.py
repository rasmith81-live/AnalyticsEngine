from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WasteReductionInSupplyChain(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WASTE_REDUCTION_IN_SUPPLY_CHAIN",
            name_="Waste Reduction in Supply Chain",
            description_="The percentage reduction of waste generated throughout the supply chain, aligning with ISO 20400's focus on sustainable practices.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=[],
            formula_="(Waste Output Before Initiatives - Waste Output After Initiatives) / Waste Output Before Initiatives",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
