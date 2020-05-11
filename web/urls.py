
from django.urls import path

from web import views

urlpatterns = [
    path('expense-list/', views.expenselist, name='expense-list'),
    path('income-list/', views.incomeelist, name='income-list'),
]
