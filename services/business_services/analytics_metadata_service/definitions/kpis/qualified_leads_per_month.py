from analytics_models.definitions.kpis.base_kpi import BaseKPI

class QualifiedLeadsPerMonth(BaseKPI):
    def __init__(self):
        super().__init__(
            code="QUALIFIED_LEADS_PER_MONTH",
            name_="Qualified Leads per Month",
            description_="The number of leads that meet certain criteria set by the sales team, indicating a higher probability of converting into customers.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Lead'],
            formula_="Total Number of Qualified Leads in a Month",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
