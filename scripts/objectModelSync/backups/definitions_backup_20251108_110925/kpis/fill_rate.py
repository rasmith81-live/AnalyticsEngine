from analytics_models.definitions.kpis.base_kpi import BaseKPI

class FillRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="FILL_RATE",
            name_="Fill Rate",
            description_="The percentage of customer orders that are filled completely and on time. The KPI is calculated as the number of items shipped on time divided by the total number of items ordered.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Customer', 'Order', 'Product'],
            formula_="(Total Orders Fulfilled Without Backorders / Total Orders Placed) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
