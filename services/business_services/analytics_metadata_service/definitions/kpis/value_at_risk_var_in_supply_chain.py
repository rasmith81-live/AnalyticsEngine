import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ValueAtRiskVarInSupplyChain(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VALUE_AT_RISK_VAR_IN_SUPPLY_CHAIN",
            name_="Value at Risk (VaR) in Supply Chain",
            description_="The potential loss in value of the supply chain due to risks within a specified time frame, used for risk assessment and management.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['PurchaseOrder'],
            formula_="VaR Model Calculation (historical simulation, variance-covariance, or Monte Carlo simulation)",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
