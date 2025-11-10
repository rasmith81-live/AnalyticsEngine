import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LocalSourcingPercentage(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LOCAL_SOURCING_PERCENTAGE",
            name_="Local Sourcing Percentage",
            description_="The proportion of materials and services sourced locally, supporting local economies and reducing transportation emissions as suggested by ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Local Supplier Spend / Total Procurement Spend) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
