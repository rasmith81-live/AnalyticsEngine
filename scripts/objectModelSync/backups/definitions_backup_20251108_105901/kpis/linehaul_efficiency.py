from analytics_models.definitions.kpis.base_kpi import BaseKPI

class LinehaulEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LINEHAUL_EFFICIENCY",
            name_="Linehaul Efficiency",
            description_="The efficiency of transportation between two points excluding pickup and delivery operations.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'PurchaseOrder'],
            formula_="Total Loaded Miles / (Total Miles Driven - Empty Miles)",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
