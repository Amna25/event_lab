import unittest
from src.performer import Performer
from src.customer import Customer
class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.performer= Performer("jill")
        self.customer= Customer("Greg",100, self.performer)

    def test_customer_has_name(self):
        self.assertEqual("Greg", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_has_favouriet_performer(self):
        self.assertEqual(self.performer, self.customer.favourite_performer)

    def test_customer_check_money(self):
        self.assertEqual(100, self.customer.check_money())

    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(90, self.customer.check_money())

    def test_customer_says_favourite_performer(self):
        self.assertEqual(self.performer, self.customer.say_favourite_performer())

