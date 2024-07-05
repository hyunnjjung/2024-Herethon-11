from django.urls import path
from . import views

urlpatterns = [
    path('coin-history/', views.coin_history, name='coin_history'),
    path('coin-purchase/', views.coin_purchase, name='coin_purchase'),
    path('cash-conversion/', views.cash_conversion, name='cash_conversion'),
    path('process-coin-purchase/', views.process_coin_purchase, name='process_coin_purchase'),
    path('process-cash-conversion/', views.process_cash_conversion, name='process_cash_conversion'),  # 추가된 부분
    path('coin5/', views.coin5, name='coin5'),
]
