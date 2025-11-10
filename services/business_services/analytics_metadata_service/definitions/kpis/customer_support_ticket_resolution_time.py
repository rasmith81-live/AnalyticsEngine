from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerSupportTicketResolutionTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME",
            name_="Customer Support Ticket Resolution Time",
            description_="The average time it takes for the sales or support team to resolve customer issues or support tickets.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'PurchaseOrder', 'SupportTicket'],
            formula_="Total Time Taken to Resolve Tickets / Number of Tickets Resolved",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['custom']
        )
