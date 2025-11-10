import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingCostVariance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_COST_VARIANCE",
            name_="Packing Cost Variance",
            description_="The difference between projected and actual packing costs, important for budget management and cost control.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['PurchaseOrder'],
            formula_="Actual Packing Costs - Budgeted Packing Costs",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
