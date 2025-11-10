from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierQualityRating(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_QUALITY_RATING",
            name_="Supplier Quality Rating",
            description_="The average score of suppliers' performance based on quality metrics, reflecting the ability to meet or exceed quality expectations.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['QualityMetric', 'Supplier'],
            formula_="Sum of Supplier Quality Scores / Number of Suppliers",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
