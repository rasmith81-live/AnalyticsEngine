from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TransportationCostPerUnit(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TRANSPORTATION_COST_PER_UNIT",
            name_="Transportation Cost per Unit",
            description_="The cost of transportation per unit of product shipped. A lower cost indicates more efficient transportation operations.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Product', 'PurchaseOrder'],
            formula_="Total Transportation Costs / Total Number of Units Shipped",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
