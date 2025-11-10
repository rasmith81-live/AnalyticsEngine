from analytics_models.definitions.kpis.base_kpi import BaseKPI

class GreenProcurementSpendShare(BaseKPI):
    def __init__(self):
        super().__init__(
            code="GREEN_PROCUREMENT_SPEND_SHARE",
            name_="Green Procurement Spend Share",
            description_="The share of total procurement spend that goes towards environmentally friendly products and services, as guided by ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Product'],
            formula_="(Green Procurement Spend / Total Procurement Spend) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
