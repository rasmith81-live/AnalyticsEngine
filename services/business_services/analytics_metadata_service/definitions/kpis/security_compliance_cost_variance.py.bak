import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SecurityComplianceCostVariance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_COMPLIANCE_COST_VARIANCE",
            name_="Security Compliance Cost Variance",
            description_="The variance between budgeted and actual costs of maintaining compliance with security standards, which reflects financial management efficiency in security matters.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Actual Security Compliance Costs - Budgeted Security Compliance Costs) / Budgeted Security Compliance Costs * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
