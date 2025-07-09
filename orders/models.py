from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Order(models.Model):
    # Модель замовлення (Інформація про товар у кошику користувача)
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=500)

    # Repr:
    def __str__(self) -> str:
        return str(self.title)

