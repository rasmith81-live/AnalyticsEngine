from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TransportationOrderLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TRANSPORTATION_ORDER_LEAD_TIME",
            name_="Transportation Order Lead Time",
            description_="The time from placing a transport order to the execution of the shipment.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Lead', 'Order', 'PurchaseOrder', 'Shipment'],
            formula_="Average Time from Transportation Order Placement to Shipment Movement",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
