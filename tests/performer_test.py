import unittest
from src.performer import Performer
class TestPerformer(unittest.TestCase):
    def setUp(self):
        self.performer= Performer("Jill")

    def test_performer_has_name(self):
        self.assertEqual("Jill", self.performer.name)

    def test_performer_has_earning(self):
        self.assertEqual(0,self.performer.earnings)
    
    def test_increase_earning(self):
        self.performer.increase_earnings(50)
        self.assertEqual(50, self.performer.earnings)