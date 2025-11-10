from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PostSaleFollowUpRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="POST_SALE_FOLLOW_UP_RATE",
            name_="Post-Sale Follow-Up Rate",
            description_="The rate at which the sales team follows up with customers after a sale has been completed, which can impact customer retention and repeat business.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'PurchaseOrder'],
            formula_="(Number of Completed Sales with Follow-Up / Total Number of Completed Sales) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
