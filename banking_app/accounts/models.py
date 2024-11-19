from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=[('Savings', 'Savings'), ('Checking', 'Checking')])

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    recipient_account = models.CharField(max_length=20, null=True, blank=True)  # For transfers
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw'), ('Transfer', 'Transfer')]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.transaction_type} - ${self.amount}"
class BillPayment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    biller_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.biller_name} - ${self.amount}"
