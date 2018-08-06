from django.db import models

class Inventory(models.Model):
    capacity = models.IntegerField(default=0)
    addr = models.CharField(max_length=500)

class Laptop(models.Model):
    CHOICES = (
        (1, 'lenovo'),
        (2, 'msi'),
        (3, 'asus'),
        (4, 'hp'),
    )
    brand = models.IntegerField(choices=CHOICES, default=2)
    weight = models.FloatField()
    prince = models.IntegerField(null=True)
    deleted = models.BooleanField(default=False)
    inventory = models.ForeignKey(Inventory, related_name='inventory', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "laptop model %d weight %f" % (self.brand, self.weight)


class Mobile(models.Model):
    brand = models.CharField(max_length=50)
    seri = models.CharField(max_length=50)




