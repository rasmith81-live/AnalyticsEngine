from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OpportunityPipeline(BaseKPI):
    def __init__(self):
        super().__init__(
            code="OPPORTUNITY_PIPELINE",
            name_="Opportunity Pipeline",
            description_="The number of opportunities in the pipeline and their value.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Opportunity', 'PurchaseOrder'],
            formula_="Sum of All Opportunities at Various Stages of the Sales Cycle",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
