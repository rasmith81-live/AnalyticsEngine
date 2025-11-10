import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingMaterialCostVariability(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_MATERIAL_COST_VARIABILITY",
            name_="Packing Material Cost Variability",
            description_="The fluctuation in the cost of packing materials over time, affecting budgeting and cost management.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Max Material Cost - Min Material Cost) / Average Material Cost",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
