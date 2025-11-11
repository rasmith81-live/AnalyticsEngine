import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplierConsolidationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_CONSOLIDATION_RATE",
            name_="Supplier Consolidation Rate",
            description_="The extent to which the buying organization has decreased its number of suppliers to optimize the supply base.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Supplier'],
            formula_="(Original Number of Suppliers - Current Number of Suppliers) / Original Number of Suppliers * 100",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
