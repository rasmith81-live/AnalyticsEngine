from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostPerTonMile(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_TON_MILE",
            name_="Cost per Ton-Mile",
            description_="The cost to transport one ton of material one mile.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder', 'Shipment'],
            formula_="Total Transportation Costs / (Total Weight of Shipments * Total Miles)",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
