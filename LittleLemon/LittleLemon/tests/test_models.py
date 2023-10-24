from django.test import TestCase
from reservation.models import Menu

class MenuItemTest(TestCase):
    def testMenu(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.__str__(), "IceCream")


        
