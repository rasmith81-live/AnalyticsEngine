from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_EFFICIENCY",
            name_="Packing Efficiency",
            description_="The speed and accuracy with which items are packed for shipment.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Product', 'Shipment'],
            formula_="Total Time Taken for Packing / Total Number of Orders Packed",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
