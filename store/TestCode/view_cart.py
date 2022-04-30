from django.test import TestCase
from store.views.cart import *

class CartTest(TestCase):
    def testget(self):
        products = 1
        self.assertEqual(str(products), "1")

