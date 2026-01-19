from django.db import models

# Create your models here.
#Model of the Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name

#Model of the MenuItem
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

    #To calculate the cost
    def get_cost(self):
        #To get all the recipe linked to the menu
        requirements = self.reciperequirement_set.all()

        #Calculating the total cost
        total_cost = round(sum(req.ingredient.price * req.quantity for req in requirements), 2)
        return total_cost


#Model of the RecipeRequirement
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.menu_item.name} - {self.ingredient.name} ({self.quantity})"


#Model of the Purchase
class Purchase(models.Model):
    menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    record = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu.name} - {self.record}"

