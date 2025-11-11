import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CustomerOnboardingEfficacy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_ONBOARDING_EFFICACY",
            name_="Customer Onboarding Efficacy",
            description_="The effectiveness of the onboarding process for new customers, measured by their time to value and overall satisfaction.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="(Number of Successfully Onboarded Customers / Total Number of New Customers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
