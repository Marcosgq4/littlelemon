from django.test import TestCase
from Restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu(title='Pasta', price=10.99, inventory=10)
        self.assertEqual(item.get_item(), 'Pasta : 10.99')

        
