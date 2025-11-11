import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplierDiversity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_DIVERSITY",
            name_="Supplier Diversity",
            description_="The diversity of the company's supplier base, including factors such as the number of small and minority-owned businesses used as suppliers. A diverse supplier base can bring a range of benefits, including access to new markets and innovation.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Supplier'],
            formula_="(Spend with Diverse Suppliers / Total Spend) * 100",
            aggregation_methods=['sum', 'min', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
