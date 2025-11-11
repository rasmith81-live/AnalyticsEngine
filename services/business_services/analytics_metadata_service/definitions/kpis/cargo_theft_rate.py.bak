import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CargoTheftRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CARGO_THEFT_RATE",
            name_="Cargo Theft Rate",
            description_="The frequency of cargo theft incidents per total shipments, illustrating the level of security threats faced by the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Shipment'],
            formula_="(Number of Cargo Theft Incidents / Total Units of Cargo Shipped) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
