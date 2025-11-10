from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ContractRenewalRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CONTRACT_RENEWAL_RATE",
            name_="Contract Renewal Rate",
            description_="The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Contract', 'Customer'],
            formula_="(Number of Contracts Renewed / Number of Contracts Up for Renewal) * 100",
            aggregation_methods=['count'],
            time_periods=['custom']
        )
