# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Account,Transaction
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# def login_view(request):
#     # Handle login logic
def account_dashboard(request):
    account = Account.objects.get(user=request.user)
    return render(request, 'account_dashboard.html', {'account': account})

def transfer_funds(request):
    if request.method == 'POST':
        sender_account = Account.objects.get(user=request.user)
        recipient_account_number = request.POST.get('recipient_account')
        amount = float(request.POST.get('amount'))
        
        if sender_account.balance >= amount:
            recipient_account = Account.objects.get(account_number=recipient_account_number)
            sender_account.balance -= amount
            recipient_account.balance += amount
            sender_account.save()
            recipient_account.save()

            # Record transactions for sender and receiver
            Transaction.objects.create(account=sender_account, transaction_type='debit', amount=amount, description="Fund Transfer")
            Transaction.objects.create(account=recipient_account, transaction_type='credit', amount=amount, description="Received Transfer")
            
            return redirect('account_dashboard')
    return render(request, 'transfer_funds.html')