import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class EthicalSourcingIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ETHICAL_SOURCING_INDEX",
            name_="Ethical Sourcing Index",
            description_="A measure of the extent to which sourcing policies and practices align with ethical standards, in accordance with ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Sum of Ethical Criteria Scores) / (Total Number of Suppliers * Maximum Score per Supplier)",
            aggregation_methods=['sum', 'max', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
