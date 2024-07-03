from django.shortcuts import render, redirect
from .models import Coin, CoinTransaction
from django.contrib.auth.decorators import login_required

@login_required
def coin_history(request):
    transaction_type = request.GET.get('transaction_type', 'all')
    
    if transaction_type == 'all':
        transactions = CoinTransaction.objects.filter(user=request.user).order_by('-timestamp')
    elif transaction_type == 'purchase':
        transactions = CoinTransaction.objects.filter(user=request.user, transaction_type='구매').order_by('-timestamp')
    elif transaction_type == 'use':
        transactions = CoinTransaction.objects.filter(user=request.user, transaction_type='사용').order_by('-timestamp')
    else:
        transactions = CoinTransaction.objects.filter(user=request.user).order_by('-timestamp')
    
    user_coins = Coin.objects.filter(user=request.user)
    
    context = {
        'user_coins': user_coins,
        'transactions': transactions,
        'transaction_type': transaction_type,
    }
    return render(request, 'coin_history.html', context)

def coin_purchase(request):
    pass

def cash_conversion(request):
    pass