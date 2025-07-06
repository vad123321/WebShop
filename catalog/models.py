from django.db import models


class Category(models.Model):
    # Модель категорії товару
    name = models.CharField(max_length=100, unique=True)
    # ->
    def __str__(self) -> str:
        return str(self.name)


class Producer(models.Model):
    # Модель виробника товару
    name = models.CharField(max_length=100, unique=True)
    # ->
    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    # Модель самого товару
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='products/')
    price = models.FloatField()
    count = models.IntegerField()
    # ->
    def __str__(self) -> str:
        return str(self.name)
