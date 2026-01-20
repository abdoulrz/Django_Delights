from django.test import TestCase
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from django.urls import reverse
from django.contrib.auth.models import User

class InventoryLogicTests(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create Ingredients
        self.flour = Ingredient.objects.create(name="Flour", quantity=100, price=0.5)
        self.sugar = Ingredient.objects.create(name="Sugar", quantity=100, price=0.2)
        
        # Create Menu Item
        self.cake = MenuItem.objects.create(name="Cake", price=10.0)
        
        # Create Recipe (Cake needs 2 Flour + 1 Sugar)
        RecipeRequirement.objects.create(menu_item=self.cake, ingredient=self.flour, quantity=2)
        RecipeRequirement.objects.create(menu_item=self.cake, ingredient=self.sugar, quantity=1)

    def test_get_cost(self):
        """Test that get_cost calculates correctly based on ingredients."""
        # Cost = (2 * 0.5) + (1 * 0.2) = 1.2
        self.assertEqual(self.cake.get_cost(), 1.2)

    def test_purchase_deducts_inventory(self):
        """Test that purchasing an item reduces ingredient stock."""
        url = reverse('purchase')
        data = {'menu': self.cake.id}
        
        # Perform purchase
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # Check redirect (success)

        # Refresh from DB
        self.flour.refresh_from_db()
        self.sugar.refresh_from_db()

        # Check deductions
        self.assertEqual(self.flour.quantity, 98) # Started 100, Used 2
        self.assertEqual(self.sugar.quantity, 99) # Started 100, Used 1

    def test_insufficient_inventory_prevents_purchase(self):
        """Test that purchase fails if not enough ingredients."""
        # Set flour to almost empty (only 1 left, need 2)
        self.flour.quantity = 1
        self.flour.save()

        url = reverse('purchase')
        data = {'menu': self.cake.id}

        # Try purchase
        response = self.client.post(url, data)
        
        # Should stay on page (200 OK) with error, NOT redirect
        self.assertEqual(response.status_code, 200)
        
        # Check no deduction happened
        self.flour.refresh_from_db()
        self.assertEqual(self.flour.quantity, 1)        
        
        # Ensure no purchase record created
        self.assertEqual(Purchase.objects.count(), 0)
