from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostPerDeliveryPoint(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_DELIVERY_POINT",
            name_="Cost per Delivery Point",
            description_="The cost incurred for delivering goods to each individual point.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'PurchaseOrder'],
            formula_="Total Delivery Costs / Total Number of Delivery Points",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
