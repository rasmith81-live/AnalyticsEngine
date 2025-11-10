from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SecurityPolicyUpdateFrequency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_POLICY_UPDATE_FREQUENCY",
            name_="Security Policy Update Frequency",
            description_="The frequency with which security policies are reviewed and updated, showing the organization's adaptability to the changing security landscape.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="Total Number of Security Policy Updates / Time Period",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
