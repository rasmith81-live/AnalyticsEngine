from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CashToCashCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CASH_TO_CASH_CYCLE_TIME",
            name_="Cash-to-Cash Cycle Time",
            description_="The time between the outlay of cash for raw materials and receiving cash from customers for product sales, impacting liquidity and cash flow.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Customer', 'Inventory', 'Product'],
            formula_="(Days Inventory Outstanding + Days Sales Outstanding) - Days Payable Outstanding",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['custom']
        )
