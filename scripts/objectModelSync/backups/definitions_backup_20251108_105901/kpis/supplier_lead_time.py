from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_LEAD_TIME",
            name_="Supplier Lead Time",
            description_="The amount of time between when an order is placed with a supplier and when the order is received.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Lead', 'Order', 'Supplier'],
            formula_="Average Time from Order Placement to Receipt",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
