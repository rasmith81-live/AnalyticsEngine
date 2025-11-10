import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SecurityRiskMitigationEffectiveness(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_RISK_MITIGATION_EFFECTIVENESS",
            name_="Security Risk Mitigation Effectiveness",
            description_="The effectiveness of implemented measures to reduce supply chain security risks, measured by the reduction in identified risks over time.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="(Risk Exposure Before Mitigation - Risk Exposure After Mitigation) / Risk Exposure Before Mitigation * 100",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
