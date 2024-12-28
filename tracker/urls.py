from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_budget', views.add_budget, name='add_budget'),
    path('view_transactions/<int:budget_id>/', views.view_transactions, name='view_transactions'),
    path('add_transaction/<int:budget_id>/', views.add_transaction, name='add_transaction'),
    path('delete_budget/<int:budget_id>/', views.delete_budget, name='delete_budget'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction')
]