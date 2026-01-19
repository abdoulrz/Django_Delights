from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("history/", views.history, name="history"),
    path("purchase/", views.PurchaseCreateView.as_view(), name="purchase"),
    path("balance_sheet/", views.balance_sheet, name="balance_sheet"),
    path("ingredient/", views.IngredientCreateView.as_view(), name="ingredient"),
    path("ingredient/update/<int:pk>", views.IngredientUpdateView.as_view(), name="ingredient_update"),
    path("requirement/", views.RequirementCreateView.as_view(), name="requirement"),
    path("add_menu/", views.MenuCreateView.as_view(), name="add_menu"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),

]
