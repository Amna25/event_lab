class Event:
    def __init__(self,name,ticket_price,customers,performers):
        self.name=name
        self.ticket_price= ticket_price
        self.customers= customers
        self.performers=performers
        self.revenue= 0

        