import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LeadTimeReduction(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_TIME_REDUCTION",
            name_="Lead Time Reduction",
            description_="The amount by which the time from order placement to delivery is reduced, improving supply chain responsiveness.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Delivery', 'Lead', 'Order', 'PurchaseOrder'],
            formula_="(Original Lead Time - Current Lead Time) / Original Lead Time * 100",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
