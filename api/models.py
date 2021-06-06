from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null = 'false', blank = 'false')
    category = models.CharField(max_length=100, null = 'false', blank = 'false')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name
