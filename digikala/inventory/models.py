from django.db import models


class Laptop(models.Model):
    CHOICES = (
        (1, 'lenovo'),
        (2, 'msi'),
        (3, 'asus'),
        (4, 'hp'),
    )
    brand = models.IntegerField(choices=CHOICES)
    weight = models.FloatField()


class Mobile(models.Model):
    brand = models.CharField(max_length=50)
    seri = models.CharField(max_length=50)
