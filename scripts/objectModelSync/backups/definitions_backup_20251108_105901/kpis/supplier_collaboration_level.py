from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierCollaborationLevel(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_COLLABORATION_LEVEL",
            name_="Supplier Collaboration Level",
            description_="The extent to which the buying organization works with suppliers to achieve mutual benefits.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Supplier'],
            formula_="Qualitative Assessment Score based on Predefined Collaboration Criteria",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
