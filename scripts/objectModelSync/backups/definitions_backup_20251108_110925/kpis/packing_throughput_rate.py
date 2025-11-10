from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingThroughputRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_THROUGHPUT_RATE",
            name_="Packing Throughput Rate",
            description_="The number of units packed over a specific period, indicating the volume and efficiency of packing operations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order'],
            formula_="Total Orders Packed / Total Packing Time",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
