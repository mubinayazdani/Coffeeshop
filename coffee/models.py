from django.db import models


# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    imaage = models.CharField(max_length=2083)

    def __str__(self):
        return f'{self.name}'