import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class StrategicInitiativeProgress(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STRATEGIC_INITIATIVE_PROGRESS",
            name_="Strategic Initiative Progress",
            description_="A measure of the progress of key business initiatives against strategic goals.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Sum of Completed Milestones or Objectives / Total Planned Milestones or Objectives) * 100",
            aggregation_methods=['sum'],
            time_periods=['quarterly', 'annually']
        )
