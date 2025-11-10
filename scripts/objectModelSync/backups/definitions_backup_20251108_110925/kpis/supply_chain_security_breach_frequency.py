from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainSecurityBreachFrequency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_SECURITY_BREACH_FREQUENCY",
            name_="Supply Chain Security Breach Frequency",
            description_="The number of times the security of the supply chain is breached within a given period, indicating the effectiveness of security measures in place.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="Total Number of Supply Chain Security Breaches / Time Period",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
