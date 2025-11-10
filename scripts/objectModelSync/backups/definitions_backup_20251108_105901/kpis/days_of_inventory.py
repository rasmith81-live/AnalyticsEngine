from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DaysOfInventory(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DAYS_OF_INVENTORY",
            name_="Days of Inventory",
            description_="How many days of sales the inventory can support. The KPI is calculated as the average inventory value over a period of time divided by the average daily cost of goods sold.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'PurchaseOrder'],
            formula_="(Average Inventory Value / Cost of Goods Sold) * Number of Days in Period",
            aggregation_methods=['average', 'count'],
            time_periods=['daily']
        )
