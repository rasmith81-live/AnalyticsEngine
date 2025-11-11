import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class DamageFreeDeliveryRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DAMAGE_FREE_DELIVERY_RATE",
            name_="Damage-Free Delivery Rate",
            description_="The percentage of deliveries made without any damage to the goods.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery'],
            formula_="(Number of Damage-Free Deliveries / Total Number of Deliveries) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
