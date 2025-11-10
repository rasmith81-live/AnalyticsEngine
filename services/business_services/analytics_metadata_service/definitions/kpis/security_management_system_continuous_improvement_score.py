import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SecurityManagementSystemContinuousImprovementScore(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_MANAGEMENT_SYSTEM_CONTINUOUS_IMPROVEMENT_SCORE",
            name_="Security Management System Continuous Improvement Score",
            description_="A score that evaluates the extent of continuous improvement efforts applied to the security management system within the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Total Improvement Actions Successfully Implemented / Total Improvement Actions Identified) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
