from django.db import models
from django.contrib.auth.models import User

from decimal import Decimal

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=50, null=False)
    buying_price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name

class VehicleSold(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    selling_date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00), help_text='Selling Price')
    seller = models.ForeignKey(User, related_name='seller_user', on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(User, related_name='buyer_user', on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(blank=True)
