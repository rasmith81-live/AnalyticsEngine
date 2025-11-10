from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DriverRetentionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DRIVER_RETENTION_RATE",
            name_="Driver Retention Rate",
            description_="The rate at which a company retains its drivers over a period.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=[],
            formula_="(Number of Drivers at End of Period - Number of New Drivers During Period) / Number of Drivers at Start of Period * 100",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
