from django.shortcuts import render
from .models import Account, Transaction, BillPayment

def account_summary(request, account_id):
    account = Account.objects.get(id=account_id)
    return render(request, 'accounts/account_summary.html', {'account': account})
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def transfer_funds(request, account_id):
    sender_account = get_object_or_404(Account, id=account_id)
    if request.method == "POST":
        recipient_number = request.POST['recipient_account']
        amount = float(request.POST['amount'])
        recipient_account = Account.objects.get(account_number=recipient_number)
        
        if sender_account.balance >= amount:
            sender_account.balance -= amount
            recipient_account.balance += amount
            sender_account.save()
            recipient_account.save()

            # Record transaction
            Transaction.objects.create(account=sender_account, recipient_account=recipient_number, amount=amount, transaction_type='Transfer')
            messages.success(request, "Transfer successful!")
        else:
            messages.error(request, "Insufficient balance.")
        return redirect('account_summary', account_id=account_id)

    return render(request, 'accounts/transfer_funds.html', {'account': sender_account})

def pay_bill(request, account_id):
    account = Account.objects.get(id=account_id)
    if request.method == "POST":
        biller_name = request.POST['biller_name']
        amount = float(request.POST['amount'])
        
        if account.balance >= amount:
            account.balance -= amount
            account.save()

            # Record payment
            BillPayment.objects.create(account=account, biller_name=biller_name, amount=amount)
            messages.success(request, "Bill paid successfully!")
        else:
            messages.error(request, "Insufficient balance.")
        return redirect('account_summary', account_id=account_id)

    return render(request, 'accounts/pay_bill.html', {'account': account})
def transaction_history(request, account_id):
    account = Account.objects.get(id=account_id)
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'accounts/transaction_history.html', {'account': account, 'transactions': transactions})
