import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

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
