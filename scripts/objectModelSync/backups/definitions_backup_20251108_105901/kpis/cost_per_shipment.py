from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostPerShipment(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_SHIPMENT",
            name_="Cost per Shipment",
            description_="The total cost divided by the number of shipments.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Shipment'],
            formula_="Total Shipping Costs / Total Number of Shipments",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
