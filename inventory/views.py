from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm, LoginForm
from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

#The register logic
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, "inventory/register.html", {"form": form})


#The login logic
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home page after successful login
            else:
                # Add error message to form
                form.add_error(None, "Invalid username or password")
        return render(request, "inventory/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "inventory/login.html", {"form": form})

#The logout logic
def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout


@login_required
def home(request):
    context = {"ingredients": Ingredient.objects.all()}
    return render(request, "inventory/home.html", context)
@login_required
def menu(request):
    context = {"menu_items": MenuItem.objects.all()}
    return render(request, "inventory/menu.html", context)

#History button
@login_required
def history(request):
    if request.method == "GET":
        context = {"history": Purchase.objects.all().order_by('-record')}
        return render(request, "inventory/history.html", context)

# Adding the Createview of  the ingredient 
class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/add_ingredient.html"
    success_url = reverse_lazy("home")

# Adding the Updateview of  the ingredient 
class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/update_ingredient.html"
    success_url = reverse_lazy("home")

# Adding the Createview of  the MenuItem 
class MenuCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/add_menu.html"
    success_url = reverse_lazy("home")


# Adding the Createview of  the RecipeRequirement 
class RequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/add_requirement.html"
    success_url = reverse_lazy("home")

# Adding the purchase view
class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase.html"
    success_url = reverse_lazy("home")


#Adding the balance sheet logic
@login_required
def balance_sheet(request):
    purchased = Purchase.objects.all()
    revenue = sum(item.menu.price for item in purchased)
    cost = sum(item.menu.get_cost() for item in purchased)    
    profit = revenue - cost
    if profit < 0:
        profit = "No profit"
    context = {"cost": cost, "revenue": revenue, "profit": profit}
    return render(request, "inventory/balance.html", context)