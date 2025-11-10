import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainSecurityLevelBenchmarking(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_SECURITY_LEVEL_BENCHMARKING",
            name_="Supply Chain Security Level Benchmarking",
            description_="The process of comparing the organization's supply chain security level against industry standards or best practices.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Organization's Security Level Score / Industry Benchmark Score) * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
