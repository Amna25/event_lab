import unittest
from src.customer import Customer
from src.performer import Performer
from src.event import Event

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.performer= Performer("jill")
        self.customer= Customer("Greg",100, self.performer)
        self.event= Event("circus", 5, [self.customer], [self.performer])
    
    def test_evvent_has_name(self):
        self.assertEqual("circus",self.event.name)

    def test_event_has_ticket_price(self):
        self.assertEqual(5, self.event.ticket_price)
    def test_event_revenue_start_0(self):
        self.assertEqual(0, self.event.revenue)

    def test_event_has_customer(self):
        self.assertEqual(1, len(self.event.customers))

    def test_event_has_performer(self):
        self.assertEqual(1, len(self.event.performers))

    
    
    