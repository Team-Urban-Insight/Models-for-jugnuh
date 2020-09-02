from django.db import models
from basic.models import Service_Provider, User
# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, models.SET_NULL)
    amount = models.IntegerField()


class OrderItem(models.Model):
    duration = models.IntegerField()
    order_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['provider', 'order']

    provider = models.ForeignKey(Service_Provider, models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
