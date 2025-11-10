from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerEffortScoreCes(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_EFFORT_SCORE_CES",
            name_="Customer Effort Score (CES)",
            description_="A metric that measures the ease with which customers can interact with the company and its services.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="Sum of All Customer Effort Ratings / Number of Ratings",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
