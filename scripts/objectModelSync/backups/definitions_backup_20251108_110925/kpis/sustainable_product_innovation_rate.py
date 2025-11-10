from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SustainableProductInnovationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUSTAINABLE_PRODUCT_INNOVATION_RATE",
            name_="Sustainable Product Innovation Rate",
            description_="The rate at which new products or services are developed that meet sustainability criteria outlined in ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Product'],
            formula_="(Number of Sustainable Products Developed / Total Number of Products Developed) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
