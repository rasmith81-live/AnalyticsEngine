from analytics_models.definitions.kpis.base_kpi import BaseKPI

class MaterialPriceVariance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="MATERIAL_PRICE_VARIANCE",
            name_="Material Price Variance",
            description_="The difference between the actual cost of materials and the standard cost, indicating how well costs are controlled.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=[],
            formula_="(Actual Price - Standard Price) * Quantity Purchased",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
