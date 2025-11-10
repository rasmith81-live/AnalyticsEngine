from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CarrierComplianceRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CARRIER_COMPLIANCE_RATE",
            name_="Carrier Compliance Rate",
            description_="The percentage of deliveries that comply with the carrier’s requirements and standards.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Shipment'],
            formula_="(Number of Compliant Shipments by Carrier / Total Number of Shipments by Carrier) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
