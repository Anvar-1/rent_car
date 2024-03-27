from django.db import models
from app.brand.models import Brand

class Car(models.Model):
    name = models.CharField(max_length=100)
    km_limit_per_day_info = models.CharField(max_length=100)
    car_rental_depozit_amount_info = models.CharField(max_length=100)
    daily_rental_price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.
