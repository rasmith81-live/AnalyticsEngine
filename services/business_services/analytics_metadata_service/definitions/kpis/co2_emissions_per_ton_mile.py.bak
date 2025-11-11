import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class Co2EmissionsPerTonMile(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CO2_EMISSIONS_PER_TON_MILE",
            name_="CO2 Emissions per Ton-Mile",
            description_="The amount of CO2 emitted for transporting one ton of material over one mile.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder', 'Shipment'],
            formula_="Total CO2 Emissions / (Total Weight of Shipments * Total Miles)",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
