from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DealDiscount(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DEAL_DISCOUNT",
            name_="Average Deal Discount",
            description_="The average percentage discount applied to deals, which can reflect the sales team's negotiation skills and pricing strategy.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal'],
            formula_="(Total Discounts Given / Number of Deals Closed) * 100",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
