from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OutboundOrdersProcessedPerHour(BaseKPI):
    def __init__(self):
        super().__init__(
            code="OUTBOUND_ORDERS_PROCESSED_PER_HOUR",
            name_="Outbound Orders Processed per Hour",
            description_="The number of outbound orders processed per hour.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order'],
            formula_="Total Outbound Orders Processed / Total Hours Worked",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
