import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class MobileSalesEnablementUtilization(BaseKPI):
    def __init__(self):
        super().__init__(
            code="MOBILE_SALES_ENABLEMENT_UTILIZATION",
            name_="Mobile Sales Enablement Utilization",
            description_="The percentage of the sales team that uses mobile tools and applications to enable sales activities.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Number of Sales Representatives Using Mobile Tools / Total Number of Sales Representatives) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
