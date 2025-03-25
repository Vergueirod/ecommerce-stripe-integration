from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    def price_show(self):
        return "{:.2f}".format(self.price)