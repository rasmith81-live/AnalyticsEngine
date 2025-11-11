import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingCostPerUnit(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_COST_PER_UNIT",
            name_="Packing Cost per Unit",
            description_="The average cost incurred to pack a single unit, helping to assess cost-efficiency in packing operations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="Total Packing Costs / Total Units Packed",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
