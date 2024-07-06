import factory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DajangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator ([True, False])
    
    class Meta:
        model = Category
        
class ProductFactory(factory.django.DajangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttibute(CategoryFactory)
    title = factory.Faker('pystr')
    
    @factory.post_generation
    def category(self, creat, extracted, **kwargs):
        if not creat:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)
                
    class Meta:
        model = Product