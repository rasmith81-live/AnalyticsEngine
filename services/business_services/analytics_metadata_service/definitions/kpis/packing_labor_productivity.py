import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingLaborProductivity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_LABOR_PRODUCTIVITY",
            name_="Packing Labor Productivity",
            description_="The amount of output (packed items) achieved per labor hour, indicating the efficiency of labor in packing operations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order', 'Product'],
            formula_="Total Orders Packed / Total Labor Hours",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
