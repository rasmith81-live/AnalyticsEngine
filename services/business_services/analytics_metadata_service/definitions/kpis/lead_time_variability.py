from analytics_models.definitions.kpis.base_kpi import BaseKPI

class LeadTimeVariability(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_TIME_VARIABILITY",
            name_="Lead Time Variability",
            description_="The consistency of lead times provided by suppliers, with lower variability indicating more reliable delivery.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Delivery', 'Lead', 'Supplier'],
            formula_="Standard Deviation of Lead Times / Average Lead Time",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
