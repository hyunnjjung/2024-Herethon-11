from django.contrib import admin
from .models import Coin, CoinTransaction

admin.site.register(Coin)
admin.site.register(CoinTransaction)
