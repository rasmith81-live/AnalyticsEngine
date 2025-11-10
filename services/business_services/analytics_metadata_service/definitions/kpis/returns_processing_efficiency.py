from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ReturnsProcessingEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="RETURNS_PROCESSING_EFFICIENCY",
            name_="Returns Processing Efficiency",
            description_="The effectiveness of handling and processing returned items.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Product', 'Return'],
            formula_="Total Time Taken for Processing Returns / Total Number of Returned Items",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
