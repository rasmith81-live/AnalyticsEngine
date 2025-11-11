import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingErrorResolutionTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_ERROR_RESOLUTION_TIME",
            name_="Packing Error Resolution Time",
            description_="The average time taken to resolve packing errors, impacting customer satisfaction and operational efficiency.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Customer'],
            formula_="Total Time to Resolve Errors / Total Number of Errors",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['custom']
        )
