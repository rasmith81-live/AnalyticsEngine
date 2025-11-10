from analytics_models.definitions.kpis.base_kpi import BaseKPI

class AccountCoverageRatio(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ACCOUNT_COVERAGE_RATIO",
            name_="Account Coverage Ratio",
            description_="The ratio of accounts actively managed by the sales team compared to the total number of target accounts.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Number of Accounts Managed by Sales Rep / Total Target Accounts) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
