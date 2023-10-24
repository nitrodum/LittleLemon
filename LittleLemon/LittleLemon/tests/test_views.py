from django.test import TestCase
from reservation.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="GreekSalad", price=50, inventory=100)
    
    def test_getall(self):
        IceCream = Menu.objects.get(title="IceCream")
        GreekSalad = Menu.objects.get(title="GreekSalad")
        self.assertEqual(IceCream.__str__(), "IceCream")
        self.assertEqual(IceCream.price, 80)
        self.assertEqual(GreekSalad.__str__(), "GreekSalad")
        self.assertEqual(GreekSalad.price, 50)
