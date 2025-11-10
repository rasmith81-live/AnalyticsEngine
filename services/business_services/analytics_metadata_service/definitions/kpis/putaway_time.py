import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PutawayTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PUTAWAY_TIME",
            name_="Putaway Time",
            description_="The time it takes to store goods in their designated location after receipt.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Product'],
            formula_="Total Time Taken for Putaway / Total Number of Items Putaway",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
