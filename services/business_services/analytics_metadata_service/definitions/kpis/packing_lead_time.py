import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_LEAD_TIME",
            name_="Packing Lead Time",
            description_="The time taken from initiating packing operations to the completion of packing, critical for timely deliveries.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Lead', 'Order'],
            formula_="Total Packing Time / Total Orders Packed",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
