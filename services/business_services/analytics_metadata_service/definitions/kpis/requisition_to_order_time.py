import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class RequisitionToOrderTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="REQUISITION_TO_ORDER_TIME",
            name_="Requisition-to-Order Time",
            description_="The time elapsed from when a purchase requisition is initiated to when the purchase order is created.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Total Time from Requisition to Purchase Order / Number of Requisitions",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
