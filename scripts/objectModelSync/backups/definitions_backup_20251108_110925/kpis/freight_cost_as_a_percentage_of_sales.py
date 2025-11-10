from analytics_models.definitions.kpis.base_kpi import BaseKPI

class FreightCostAsAPercentageOfSales(BaseKPI):
    def __init__(self):
        super().__init__(
            code="FREIGHT_COST_AS_A_PERCENTAGE_OF_SALES",
            name_="Freight Cost as a Percentage of Sales",
            description_="The cost of transportation and logistics as a percentage of total sales, indicating the cost efficiency of logistics.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder'],
            formula_="(Total Freight Costs / Total Sales Revenue) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
