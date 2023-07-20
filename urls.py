from django.urls import path
from home.views import ExpenseListCreateView

urlpatterns = [
    path('api/expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    # Add more URL patterns as needed
]
