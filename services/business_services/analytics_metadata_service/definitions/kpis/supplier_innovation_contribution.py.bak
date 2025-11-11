import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplierInnovationContribution(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_INNOVATION_CONTRIBUTION",
            name_="Supplier Innovation Contribution",
            description_="The extent to which suppliers contribute to innovation in products, processes, or services, enhancing competitiveness and value creation.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Product', 'Supplier'],
            formula_="(Number of Supplier Innovations Adopted / Total Innovations) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
