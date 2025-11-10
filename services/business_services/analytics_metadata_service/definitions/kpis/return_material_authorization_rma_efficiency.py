import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ReturnMaterialAuthorizationRmaEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="RETURN_MATERIAL_AUTHORIZATION_RMA_EFFICIENCY",
            name_="Return Material Authorization (RMA) Efficiency",
            description_="The efficiency of handling returned materials, impacting customer satisfaction and inventory levels.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Customer', 'Inventory', 'Return'],
            formula_="(Number of RMAs Processed within Target Time / Total RMAs Issued) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
