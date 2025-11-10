import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LostDealAnalysis(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LOST_DEAL_ANALYSIS",
            name_="Lost Deal Analysis",
            description_="The systematic examination of lost deals to understand why they were not won and to implement improvements.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal'],
            formula_="(Qualitative analysis based on deal feedback and data)",
            aggregation_methods=['min'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
