from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplyChainSecurityInvestmentRoi(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_SECURITY_INVESTMENT_ROI",
            name_="Supply Chain Security Investment ROI",
            description_="The return on investment for security measures implemented within the supply chain, demonstrating the financial impact of security investments.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Return'],
            formula_="(Gains from Security Investments - Cost of Security Investments) / Cost of Security Investments * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
