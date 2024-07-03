from django.db import models
from worklady.signup.models import CustomUser

class Coin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.amount} coins'

class CoinTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)  # '구매' 또는 '사용'
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.transaction_type} {self.amount} coins at {self.timestamp}'
