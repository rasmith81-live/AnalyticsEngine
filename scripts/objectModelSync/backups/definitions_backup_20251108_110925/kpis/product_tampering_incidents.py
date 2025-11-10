from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ProductTamperingIncidents(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PRODUCT_TAMPERING_INCIDENTS",
            name_="Product Tampering Incidents",
            description_="The number of product tampering incidents detected, which affects consumer safety and brand reputation.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Product'],
            formula_="Total Number of Product Tampering Incidents",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
