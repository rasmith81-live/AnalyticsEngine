from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ProcurementCostSavings(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROCUREMENT_COST_SAVINGS",
            name_="Procurement Cost Savings",
            description_="The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management. Reflects the direct financial impact of procurement activities and supports budget optimization.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=["Supplier", "PurchaseOrder", "Contract"],
            formula_="Baseline Spend - Current Spend",
            aggregation_methods=["sum", "average"],
            time_periods=["monthly", "quarterly", "annually"]
        )
