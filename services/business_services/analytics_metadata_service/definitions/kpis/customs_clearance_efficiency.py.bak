import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CustomsClearanceEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMS_CLEARANCE_EFFICIENCY",
            name_="Customs Clearance Efficiency",
            description_="The average time it takes for goods to clear customs, reflecting the effectiveness of security procedures in international trade.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Shipment'],
            formula_="Sum of Customs Clearance Times / Total Number of Shipments",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['custom']
        )
