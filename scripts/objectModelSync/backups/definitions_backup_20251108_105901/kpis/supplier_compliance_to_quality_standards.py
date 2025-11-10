from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierComplianceToQualityStandards(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS",
            name_="Supplier Compliance to Quality Standards",
            description_="The percentage of suppliers that comply with predefined quality standards, ensuring consistency and reliability in the supply chain.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['QualityMetric', 'Supplier'],
            formula_="(Number of Suppliers Meeting Quality Standards / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
