from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    account_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.transaction_type} - {self.amount}"
