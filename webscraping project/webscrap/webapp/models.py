from django.db import models

# Create your models here.
class mobile(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Image = models.CharField(max_length=2083)

