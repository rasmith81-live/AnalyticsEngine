import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class TimeToPackPerOrder(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TIME_TO_PACK_PER_ORDER",
            name_="Time to Pack per Order",
            description_="The average time taken to pack a single order, providing insight into the speed and efficiency of packing operations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order'],
            formula_="Total Packing Time / Total Orders Packed",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
