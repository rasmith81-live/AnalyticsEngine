from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ContainerSecurityDeviceUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CONTAINER_SECURITY_DEVICE_UTILIZATION_RATE",
            name_="Container Security Device Utilization Rate",
            description_="The percentage of containers equipped with security devices, indicating the level of technology adoption to enhance shipment security.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Shipment'],
            formula_="(Number of Containers with Security Devices / Total Number of Containers Shipped) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
