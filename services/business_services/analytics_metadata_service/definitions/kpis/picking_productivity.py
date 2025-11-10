import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PickingProductivity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PICKING_PRODUCTIVITY",
            name_="Picking Productivity",
            description_="The rate at which items are picked and processed for orders.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Product'],
            formula_="Total Items Picked / Total Picking Hours",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
