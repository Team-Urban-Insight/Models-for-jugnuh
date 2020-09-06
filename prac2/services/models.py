from django.db import models
from basic.models import Service_Provider

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="img/icons", null=True, blank=True)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.service_name

class Service_Category(models.Model):

    SERVICE_DURATION_CHOICES = [
        ('Hour', 'Hour'),
        ('Day', 'Day'),
        ('Month', 'Month')
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    cost_per_unit = models.CharField(max_length=20, choices=SERVICE_DURATION_CHOICES, default="Hour")
    category_description = models.CharField(max_length=2000)

    class Meta:
        verbose_name_plural = 'Service Categories'
        ordering = ['service']

    def __str__(self):
        new_str = str(self.service)+"- "+str(self.category_name)
        return new_str

class Schedule(models.Model):
    end_date_time = models.DateTimeField()

    class Meta:
        unique_together = ['provider', 'order_item']

    provider = models.OneToOneField(Service_Provider, on_delete=models.CASCADE)
    order_item = models.OneToOneField('orders.OrderItem', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.provider)

class Provides(models.Model):
    provider = models.ForeignKey(Service_Provider, on_delete=models.CASCADE)
    service_category = models.ForeignKey(Service_Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Provides"
        ordering = ['provider']

    def __str__(self):
        str2 = str(self.provider.user.first_name) +'-> '+str(self.service_category.service) + '-> '+str(self.service_category.category_name)
        return str2
