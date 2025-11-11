import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class FirstContactResolutionFcr(BaseKPI):
    def __init__(self):
        super().__init__(
            code="FIRST_CONTACT_RESOLUTION_FCR",
            name_="First Contact Resolution (FCR)",
            description_="The percentage of sales inquiries or issues that are resolved upon first interaction with a customer, indicating the efficacy of the sales team's problem-solving skills.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'PurchaseOrder'],
            formula_="(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
