from analytics_models.definitions.kpis.base_kpi import BaseKPI

class BuyerEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="BUYER_EFFICIENCY",
            name_="Buyer Efficiency",
            description_="The number of purchase orders processed per buyer, indicating the efficiency of the",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Employee', 'Order', 'PurchaseOrder'],
            formula_="Total Orders Processed or Cost Savings / Number of Buyers",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
