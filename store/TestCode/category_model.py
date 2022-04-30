from django.test import TestCase
from store.models.category import *


class CategoryTest(TestCase):
    def testget_all_categories(self):
        name = Category.objects.create(name="Django Testings")
        self.assertQuerysetEqual(Category.get_all_categories(), ["<Category: Django Testings>"], ordered=False)


    def test__str__(self):
        name = Category.objects.create(name="Django Testings")        
        self.assertEqual(str(name), "Django Testings")