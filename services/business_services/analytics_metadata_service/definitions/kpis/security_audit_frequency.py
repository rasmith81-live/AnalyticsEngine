from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SecurityAuditFrequency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_AUDIT_FREQUENCY",
            name_="Security Audit Frequency",
            description_="The number of security audits conducted in a given period, which assesses the regularity of security evaluations within the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="Total Number of Security Audits / Time Period",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
