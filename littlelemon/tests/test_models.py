from django.test import TestCase
from ..Restaurant.models import Menu, Booking
from ..Restaurant.serializers import MenuSerializer

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu(title='Pasta', price=10.99, inventory=10)
        self.assertEqual(item.get_item(), 'Pasta : 10.99')
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title='Pasta', price=10.99, inventory=10)
        self.item2 = Menu.objects.create(title='Chicken', price=15.99, inventory=20)
        self.item3 = Menu.objects.create(title='Beef', price=5.99, inventory=30)
        
        self.test_menu_items = Menu.objects.filter(
            pk__in=[self.item1.pk, self.item2.pk, self.item3.pk]
        )
        
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        
        response_data = response.data['menu']
        serialized_data = MenuSerializer(self.test_menu_items, many=True)
        self.assertEqual(response_data, serialized_data.data)
        
