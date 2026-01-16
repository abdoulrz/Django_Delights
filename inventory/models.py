from django.db import models

# Create your models here.
#Model of the Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    price = models.FloatField()

#Model of the MenuItem
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()


#Model of the RecipeRequirement
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()


#Model of the Purchase
class Purchase(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    record = models.DateTimeField(auto_now_add=True)

