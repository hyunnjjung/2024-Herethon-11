from django.urls import path
from . import views

urlpatterns = [
    path('coin-history/', views.coin_history, name='coin_history'),
    path('coin-purchase/', views.coin_purchase, name='coin_purchase'),
    path('cash-conversion/', views.cash_conversion, name='cash_conversion'),
]