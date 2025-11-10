from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierCapacityUtilization(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_CAPACITY_UTILIZATION",
            name_="Supplier Capacity Utilization",
            description_="The extent to which suppliers' production capacity is used, with higher utilization often leading to economies of scale.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Lead', 'Product', 'PurchaseOrder', 'Supplier'],
            formula_="(Actual Output / Maximum Possible Output) * 100",
            aggregation_methods=['max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
