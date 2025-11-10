from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierRiskAssessmentRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_RISK_ASSESSMENT_RATE",
            name_="Supplier Risk Assessment Rate",
            description_="The frequency at which suppliers are evaluated for risks such as financial stability, geopolitical factors, and natural disasters.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Number of Assessments Conducted / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
