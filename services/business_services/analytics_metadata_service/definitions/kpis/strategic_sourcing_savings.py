from analytics_models.definitions.kpis.base_kpi import BaseKPI

class StrategicSourcingSavings(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STRATEGIC_SOURCING_SAVINGS",
            name_="Strategic Sourcing Savings",
            description_="The cost savings achieved through the strategic sourcing process by optimizing supplier selection and procurement practices.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Supplier'],
            formula_="(Cost Before Strategic Sourcing - Cost After Strategic Sourcing) / Cost Before Strategic Sourcing * 100",
            aggregation_methods=['average'],
            time_periods=['quarterly', 'annually']
        )
