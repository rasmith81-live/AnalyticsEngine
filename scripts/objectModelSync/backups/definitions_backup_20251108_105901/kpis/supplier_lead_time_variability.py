from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierLeadTimeVariability(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_LEAD_TIME_VARIABILITY",
            name_="Supplier Lead Time Variability",
            description_="The consistency of supplier lead times over a period, with lower variability indicating more reliable delivery schedules.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Delivery', 'Lead', 'Supplier'],
            formula_="Standard Deviation of Supplier Lead Time",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
