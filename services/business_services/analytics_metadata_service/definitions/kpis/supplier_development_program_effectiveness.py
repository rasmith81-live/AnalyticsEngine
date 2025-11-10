import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplierDevelopmentProgramEffectiveness(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_DEVELOPMENT_PROGRAM_EFFECTIVENESS",
            name_="Supplier Development Program Effectiveness",
            description_="The effectiveness of programs aimed at improving suppliers' sustainability performance, in the context of ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Supplier'],
            formula_="(Supplier Performance After Development - Supplier Performance Before Development) / Supplier Performance Before Development",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
