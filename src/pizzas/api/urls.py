from django.urls import path
from . import views

urlpatterns = [
    path("pizza/", views.PizzaListCreateView.as_view()),
    path("size/", views.SizeListCreateView.as_view()),
    path("topping/", views.ToppingListCreateView.as_view()),
    path("pizza/<int:pk>", views.PizzaUpdateRetriveDeleteView.as_view()),
]
