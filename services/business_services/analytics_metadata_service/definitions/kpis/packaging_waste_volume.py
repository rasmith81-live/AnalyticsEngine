from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackagingWasteVolume(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_WASTE_VOLUME",
            name_="Packaging Waste Volume",
            description_="The total volume of waste generated from packaging materials, highlighting opportunities for waste reduction and recycling.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['PurchaseOrder'],
            formula_="Total Waste Volume / Total Packaging Units",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
