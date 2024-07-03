from django.urls import path
from . import views

urlpatterns = [
    path('coin-history/', views.coin_history, name='coin_history'),
]