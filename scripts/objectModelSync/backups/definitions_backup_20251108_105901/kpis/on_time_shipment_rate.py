from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OnTimeShipmentRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ON_TIME_SHIPMENT_RATE",
            name_="On-time Shipment Rate",
            description_="The percentage of orders shipped on or before the requested ship date.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Shipment'],
            formula_="(Total On-Time Shipments / Total Shipments) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
