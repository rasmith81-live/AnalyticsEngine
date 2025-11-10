from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DeliveryInFullOnTimeDifotRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DELIVERY_IN_FULL_ON_TIME_DIFOT_RATE",
            name_="Delivery In Full, On Time (DIFOT) Rate",
            description_="The percentage of deliveries made in full and on time.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery'],
            formula_="(Number of On-Time and Complete Deliveries / Total Number of Deliveries) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
