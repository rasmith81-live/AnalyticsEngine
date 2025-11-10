from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainTrainingInvestment(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_TRAINING_INVESTMENT",
            name_="Supply Chain Training Investment",
            description_="The amount invested in employee training to improve supply chain skills and knowledge, contributing to performance improvements.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Employee'],
            formula_="Total Spend on Supply Chain Training",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
