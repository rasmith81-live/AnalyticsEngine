import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LossPreventionCostSavings(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LOSS_PREVENTION_COST_SAVINGS",
            name_="Loss Prevention Cost Savings",
            description_="The cost savings realized from loss prevention strategies and security measures within the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Costs Without Loss Prevention Measures - Costs With Loss Prevention Measures)",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
