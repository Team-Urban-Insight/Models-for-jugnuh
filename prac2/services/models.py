from django.db import models
from basic.models import Service_Provider
from orders.models import OrderItem

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="img/icons", null=True, blank=True)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.service_name

class Service_Category(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    cost_per_unit = models.CharField(max_length=20)
    category_description = models.CharField(max_length=2000)

    def __str__(self):
        new_str = str(self.service)+"- "+str(self.category_name)
        return new_str

class Schedule(models.Model):
    end_date_time = models.DateTimeField()

    class Meta:
        unique_together = ['provider', 'order_item']

    provider = models.OneToOneField(Service_Provider, on_delete=models.CASCADE)
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.provider

class Provides(models.Model):
    provider = models.ForeignKey(Service_Provider, on_delete=models.CASCADE)
    service_category = models.ForeignKey(Service_Category, on_delete=models.CASCADE)

    def __str__(self):
        str2 = str(self.provider) +'- '+str(self.service_category.category_name)
        return str2
