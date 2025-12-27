from django.urls import path
from .views import (
    ExpenseListCreateView,
    ExpenseDetailView,
    CategoryListCreateView,
    CategoryDetailView
)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),

    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
]
