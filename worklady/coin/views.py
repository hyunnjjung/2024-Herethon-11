from django.shortcuts import render
from .models import Coin, CoinTransaction
from django.contrib.auth.decorators import login_required

@login_required
def coin_history(request):
    user_coins = Coin.objects.filter(user=request.user)
    transactions = CoinTransaction.objects.filter(user=request.user).order_by('-timestamp')
    
    context = {
        'user_coins': user_coins,
        'transactions': transactions
    }
    return render(request, 'coin_history.html', context)