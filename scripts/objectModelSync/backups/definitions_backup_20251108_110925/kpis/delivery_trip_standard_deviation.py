from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DeliveryTripStandardDeviation(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DELIVERY_TRIP_STANDARD_DEVIATION",
            name_="Delivery Trip Standard Deviation",
            description_="The variability in delivery trip duration.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery'],
            formula_="Standard Deviation of Delivery Trip Distances or Times",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
