import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class RiskAssessmentCoverageRatio(BaseKPI):
    def __init__(self):
        super().__init__(
            code="RISK_ASSESSMENT_COVERAGE_RATIO",
            name_="Risk Assessment Coverage Ratio",
            description_="The proportion of the supply chain that has undergone risk assessments, showing the extent of proactive security risk management.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="(Area of Supply Chain Assessed for Risks / Total Supply Chain Area) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
