import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingProcessCycleEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_PROCESS_CYCLE_EFFICIENCY",
            name_="Packing Process Cycle Efficiency",
            description_="The ratio of value-added time to total packing cycle time, indicating the efficiency of packing processes.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Value-Added Time / Total Cycle Time) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )
