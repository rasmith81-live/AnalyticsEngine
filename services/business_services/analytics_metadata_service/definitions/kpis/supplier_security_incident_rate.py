from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierSecurityIncidentRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_SECURITY_INCIDENT_RATE",
            name_="Supplier Security Incident Rate",
            description_="The frequency of security incidents originating from suppliers, indicating the security performance of upstream supply chain partners.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Supplier'],
            formula_="(Number of Security Incidents Involving Suppliers / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
