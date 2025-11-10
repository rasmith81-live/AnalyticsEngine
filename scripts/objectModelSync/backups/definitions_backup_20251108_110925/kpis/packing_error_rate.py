from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingErrorRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_ERROR_RATE",
            name_="Packing Error Rate",
            description_="The ratio of incorrectly packed items to the total number of items packed, highlighting the accuracy of the packing process.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order', 'Product'],
            formula_="(Total Packing Errors / Total Orders Packed) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
