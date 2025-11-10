from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ClaimsPercentage(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CLAIMS_PERCENTAGE",
            name_="Claims Percentage",
            description_="The percentage of shipments that result in claims for loss or damage.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Shipment'],
            formula_="(Number of Claims / Total Number of Shipments) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
