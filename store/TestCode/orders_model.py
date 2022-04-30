from django.test import TestCase
from store.models.orders import *


class OrderTest(TestCase):    
    def test1(self):
        product = "Django Testings"
        customer = "user"
        quantity = 1
        price = 1000
        address = "Dhaka"
        phone = "1234567890"
        date = "03-03-2010"
        status = False
        self.assertEqual(str(address), "Dhaka")
        

