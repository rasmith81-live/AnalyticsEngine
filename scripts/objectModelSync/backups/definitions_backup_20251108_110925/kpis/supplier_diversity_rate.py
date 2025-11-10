from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierDiversityRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_DIVERSITY_RATE",
            name_="Supplier Diversity Rate",
            description_="The percentage of the supplier base that is composed of diverse businesses, promoting diversity as per ISO 20400's sustainable procurement guidelines.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Number of Diverse Suppliers / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
