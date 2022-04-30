from django.test import TestCase
from store.views.login import *


class LoginTest(TestCase):    
    def testget(self):
        request = 'login.html'
        self.assertEqual(str(request), "login.html")

    def Testpost(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
            else:
                error_message = "Email or Password invaid!"
        else:
            error_message = "Email or Password invaid!"



