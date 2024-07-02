from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
import json
from rest_framework import status
from product.tests.factories import CategoryFactory 

from bookstore.product.models import Category

class CategoryViewSet (APITestCase):
    client = APIClient( )
    
    def setUp(self):
        self.category = CategoryFactory (title='books')   
         
    def test_get_all_product(self):        
        response = self.client.get(
            reverse('category-list', kwargs = {'version': 'v1'})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)
        
        self.assertEqual(category_data[0]['title'],self.category.title)
        
        
    def test_create_category(self):
        data = json.dumps({
            'title': 'tecnology',
        })
        
        response= self.client.post(
            reverse('category-list',kwargs={'version': 'v1'}),
            data=data,
            content_type = 'application/json'
        )
        
        import pdb; pdb.set_trace()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_category = Category.objects.get(title = 'technology')
        self.assertEqual(created_category.title, 'technology')
    





