from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierRiskAssessment(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_RISK_ASSESSMENT",
            name_="Supplier Risk Assessment",
            description_="The identification and evaluation of risks associated with a supplier's ability to deliver goods or services.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Supplier'],
            formula_="Qualitative Risk Score based on Predefined Risk Criteria",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
