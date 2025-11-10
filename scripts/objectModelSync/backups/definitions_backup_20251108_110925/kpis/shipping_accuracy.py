from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ShippingAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SHIPPING_ACCURACY",
            name_="Shipping Accuracy",
            description_="The percentage of shipments that are correct per the shipping documentation.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Shipment'],
            formula_="(Total Accurate Shipments / Total Shipments) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
