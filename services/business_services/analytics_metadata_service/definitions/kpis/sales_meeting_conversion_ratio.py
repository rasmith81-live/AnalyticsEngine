from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SalesMeetingConversionRatio(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_MEETING_CONVERSION_RATIO",
            name_="Sales Meeting Conversion Ratio",
            description_="The proportion of sales meetings or presentations that result in a sale or movement to the next stage of the buying process.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['PurchaseOrder'],
            formula_="(Number of Meetings Resulting in a Next Step / Total Number of Sales Meetings) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
