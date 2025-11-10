from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SustainableProcurementCostSavings(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUSTAINABLE_PROCUREMENT_COST_SAVINGS",
            name_="Sustainable Procurement Cost Savings",
            description_="The cost savings achieved by implementing sustainable procurement practices in line with ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=[],
            formula_="(Cost Before Sustainable Procurement - Cost After Sustainable Procurement)",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
