from django.urls import path
from .views import (
    ExpenseListCreateView,
    ExpenseDetailView,
    CategoryListCreateView,
    CategoryDetailView,
    ExpenseSummaryView,
    CategoryBreakdownView,
    TopCategoriesView,
)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),

    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    path("expenses/summary/", ExpenseSummaryView.as_view()),
    path("expenses/category-breakdown/", CategoryBreakdownView.as_view()),
    path("expenses/top-categories/", TopCategoriesView.as_view()),
]
