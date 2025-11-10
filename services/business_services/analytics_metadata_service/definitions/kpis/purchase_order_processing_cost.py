import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PurchaseOrderProcessingCost(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PURCHASE_ORDER_PROCESSING_COST",
            name_="Purchase Order Processing Cost",
            description_="The total cost associated with processing each purchase order, including labor, overhead, and technology.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Total Cost of Processing Purchase Orders / Total Number of Purchase Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
