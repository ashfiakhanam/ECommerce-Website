from django.test import TestCase
from store.views.checkout import *

class CheckoutTest(TestCase):
    def Testpost(self, request):
      address = request.POST.get('address')
      phone = request.POST.get('phone')
      customer = request.session.get('customer')
      cart = request.session.get('cart')
      products = Product.get_products_by_id(list(cart.keys()))
      print(address , phone , customer)

      for product in products:
          order = Order(customer = Customer(id = customer),
                        product = product,
                        price = product.price,
                        address = address,
                        phone = phone,
                        quantity = cart.get(str(product.id))

                        )
          order.save()
          request.session['cart'] ={}



class TestCheckModels(TestCase):    
    def test1(self):
        checkout = 1
        self.assertEqual("checkout", "checkout")
        

