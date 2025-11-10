from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ShipmentIntegrityIncidents(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SHIPMENT_INTEGRITY_INCIDENTS",
            name_="Shipment Integrity Incidents",
            description_="The number of incidents where a shipment's integrity was compromised, indicating potential security issues in the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder', 'Shipment'],
            formula_="Total Number of Shipment Integrity Incidents",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
