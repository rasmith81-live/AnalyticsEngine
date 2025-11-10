from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierComplianceRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_COMPLIANCE_RATE",
            name_="Supplier Compliance Rate",
            description_="The percentage of suppliers that comply with the sustainability standards and requirements set out in ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Supplier'],
            formula_="(Number of Compliant Suppliers / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
