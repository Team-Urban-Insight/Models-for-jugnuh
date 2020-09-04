from django.db import models
from basic.models import Service_Provider, User
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    duration = models.IntegerField()
    order_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['provides', 'order']

    provides = models.ForeignKey('services.Provides', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.user.username  # not able to use customer's name - type user error
