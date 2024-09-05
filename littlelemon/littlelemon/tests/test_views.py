from django.test import TestCase
from Restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=60)
        self.menu2 = Menu.objects.create(title="Cake", price=120, inventory=80)

    def test_get_all_menus(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'IceCream')
        self.assertEqual(response.data[1]['title'], 'Cake')