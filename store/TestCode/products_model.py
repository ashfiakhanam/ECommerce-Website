from django.test import TestCase
from store.models.product import *


class ProductTest(TestCase):    
    def test1(self):
        name = "Cloth"
        price = 100
        category = "Kids"
        description = ""
        image = None
        self.assertEqual(str(name), "Cloth")

