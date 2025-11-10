import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SocialResponsibilityIndexInProcurement(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SOCIAL_RESPONSIBILITY_INDEX_IN_PROCUREMENT",
            name_="Social Responsibility Index in Procurement",
            description_="The index measuring the consideration of social responsibility in procurement decisions, aligning with ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['PurchaseOrder'],
            formula_="(Sum of Social Responsibility Scores) / (Total Number of Procurement Activities * Maximum Score per Activity)",
            aggregation_methods=['sum', 'max', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
