from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierQualityIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_QUALITY_INDEX",
            name_="Supplier Quality Index",
            description_="A composite score reflecting the quality of products or services provided by suppliers.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Product', 'PurchaseOrder', 'QualityMetric', 'Supplier'],
            formula_="Sum of Weighted Quality Metrics / Total Number of Quality Metrics",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
