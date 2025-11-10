from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OnTimePickupRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ON_TIME_PICKUP_RATE",
            name_="On-time Pickup Rate",
            description_="The percentage of pickups that occur at the scheduled time.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=[],
            formula_="(Number of On-time Pickups / Total Number of Pickups) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
