import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class StakeholderSecurityConfidenceIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STAKEHOLDER_SECURITY_CONFIDENCE_INDEX",
            name_="Stakeholder Security Confidence Index",
            description_="A measure of stakeholders' confidence in the organization's supply chain security, derived from surveys or feedback mechanisms.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Sum of Stakeholder Confidence Ratings) / (Number of Stakeholders)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
