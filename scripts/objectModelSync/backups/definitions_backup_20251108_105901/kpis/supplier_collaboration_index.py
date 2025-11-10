from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierCollaborationIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_COLLABORATION_INDEX",
            name_="Supplier Collaboration Index",
            description_="A measure of the quality and depth of collaborative efforts between the organization and its suppliers, impacting innovation and performance.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['QualityMetric', 'Supplier'],
            formula_="Sum of collaboration scores / Number of Suppliers",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
