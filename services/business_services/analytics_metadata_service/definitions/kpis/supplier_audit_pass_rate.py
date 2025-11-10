from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierAuditPassRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_AUDIT_PASS_RATE",
            name_="Supplier Audit Pass Rate",
            description_="The rate at which suppliers pass sustainability audits based on criteria established in ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Supplier'],
            formula_="(Number of Supplier Audits Passed / Total Number of Supplier Audits Conducted) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
