from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DockToStockCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DOCK_TO_STOCK_CYCLE_TIME",
            name_="Dock-to-stock Cycle Time",
            description_="The time taken to move goods from the receiving dock to the storage area.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Inventory', 'Warehouse'],
            formula_="Average Time from Goods Receipt to Warehouse Stocking",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
