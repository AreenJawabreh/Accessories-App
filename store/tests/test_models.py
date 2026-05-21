from django.test import TestCase
from store.models import Product, Category
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django') 

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    def test_category_model_entry(self):
        """
        Test Category model defualt name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django') 
        User.objectes.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, created_by_id=1, title='django beginners', slug='django-beginners', price='20.00', image='django')

    def test_product_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
    def test_product_model_entry(self):
        """
        Test Product model defualt name
        """
        data = self.data1
        self.assertEqual(str(data), 'django beginners')