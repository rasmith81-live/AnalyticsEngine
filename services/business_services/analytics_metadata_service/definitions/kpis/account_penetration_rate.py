from analytics_models.definitions.kpis.base_kpi import BaseKPI

class AccountPenetrationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ACCOUNT_PENETRATION_RATE",
            name_="Account Penetration Rate",
            description_="The percentage of a customer account's potential that has been realized by the sales team, indicating the depth of the relationship.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product', 'PurchaseOrder'],
            formula_="(Number of Products or Services Sold to an Account / Total Number of Available Offerings) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
