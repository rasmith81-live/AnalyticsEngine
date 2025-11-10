from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierRiskAssessmentCoverage(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_RISK_ASSESSMENT_COVERAGE",
            name_="Supplier Risk Assessment Coverage",
            description_="The extent to which the supply base has been assessed for risks related to social, environmental, and economic factors as per ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Supplier'],
            formula_="(Number of Suppliers Assessed for Risk / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
