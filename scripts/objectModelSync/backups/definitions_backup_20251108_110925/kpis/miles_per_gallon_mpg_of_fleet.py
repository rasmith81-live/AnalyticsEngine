from analytics_models.definitions.kpis.base_kpi import BaseKPI

class MilesPerGallonMpgOfFleet(BaseKPI):
    def __init__(self):
        super().__init__(
            code="MILES_PER_GALLON_MPG_OF_FLEET",
            name_="Average Miles per Gallon (MPG) of Fleet",
            description_="The average fuel efficiency of the company's transportation fleet. A higher MPG indicates more fuel-efficient and environmentally-friendly transportation operations.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder'],
            formula_="Total Miles Driven / Total Gallons of Fuel Used",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
