from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
import json
from rest_framework import status
from product.tests.factories import CategoryFactory 
from order.tests.factories import UserFactory
from product.models import Product

class TestOrderViewSet (APITestCase):
    client = APIClient( )
    
    def setUp(self):
        self.user = UserFactory(
            title='pro controller',
            price = 200.00,
        )    
    def test_get_all_product(self):
        
        response = self.client.get(
            reverse('product-list', kwargs = {'version': 'v1'})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)
        
        self.assertEqual(product_data[0]['title'],self.product.title)
        self.assertEqual(product_data[0]['price'],self.product.price)
        self.assertEqual(product_data[0]['active'],self.product.active)
        
    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'notebook',
            'price':800.00,
            'category_ids': [category.id]
        })
        
        response= self.client.post(
            reverse('product-list',kwargs={'version': 'v1'}),
            data=data,
            content_type = 'application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_product = Product.objects.get(title = 'notebook')
        self.assertEqual(created_product.price, 800.00)
    





