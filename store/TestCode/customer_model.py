from django.test import TestCase
from store.models.customer import *


class CustomerTest(TestCase):    
    def testCustomer(self):
        first_name = Customer.objects.create(first_name="Django")
        last_name = Customer.objects.create(first_name="Test")
        phone = Customer.objects.create(phone="017123456789")
        email = models.EmailField()
        password = Customer.objects.create(password="abcd1234")
        self.assertEqual(Customer.get_customer_by_email(email), False)
        self.assertEqual(Customer.isExists(Customer), False)

