from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostOfOwnershipTco(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_OF_OWNERSHIP_TCO",
            name_="Total Cost of Ownership (TCO)",
            description_="A calculation of all costs associated with acquiring, operating, and maintaining a good or service over its entire lifecycle.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Product', 'PurchaseOrder'],
            formula_="Sum of All Costs Related to Acquisition, Use, and Disposal of Product/Service",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
