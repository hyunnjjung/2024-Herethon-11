from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Coin, CoinTransaction

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

@login_required
def coin_purchase(request):
    return render(request, 'coinUp.html')

@login_required
def process_coin_purchase(request):
    if request.method == 'POST':
        coin_option = request.POST.get('coin_option')
        payment_method = request.POST.get('payment_method')

        # 유효성 검사
        if coin_option and payment_method:
            coin_amount = int(coin_option)
            
            user_coin, created = Coin.objects.get_or_create(user=request.user)
            user_coin.amount += coin_amount
            user_coin.save()
            
            CoinTransaction.objects.create(
                user=request.user,
                transaction_type='구매',
                amount=coin_amount,
            )
            return redirect('coin_history')
    return redirect('coin_purchase')

@login_required
def cash_conversion(request):
    if request.method == 'POST':
        account_holder = request.POST.get('account_holder')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        
        user_coins = Coin.objects.filter(user=request.user).first()
        if user_coins and user_coins.amount > 0:
            cash_amount = user_coins.amount * 500
            # 모든 코인을 환전
            CoinTransaction.objects.create(
                user=request.user,
                transaction_type='사용',
                amount=-user_coins.amount
            )
            user_coins.amount = 0
            user_coins.save()

            return render(request, 'conversion_complete.html', {'cash_amount': cash_amount, 'account_holder': account_holder, 'bank_name': bank_name, 'account_number': account_number})
    return render(request, 'coinToMoney.html')

@login_required
def process_cash_conversion(request):
    if request.method == 'POST':
        account_holder = request.POST.get('account_holder')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        
        user_coins = Coin.objects.filter(user=request.user).first()
        if user_coins and user_coins.amount > 0:
            cash_amount = user_coins.amount * 500
            # 모든 코인을 환전
            CoinTransaction.objects.create(
                user=request.user,
                transaction_type='사용',
                amount=-user_coins.amount
            )
            user_coins.amount = 0
            user_coins.save()

            return render(request, 'conversion_complete.html', {'cash_amount': cash_amount, 'account_holder': account_holder, 'bank_name': bank_name, 'account_number': account_number})
    return redirect('cash_conversion')
