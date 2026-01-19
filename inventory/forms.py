from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

#Ingredient form
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

#MenuItem form
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

#RecipeRequirement form
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

#Purchase form
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["menu"]

#login forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)