from django.db import models
from basic.models import Service_Provider

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="img/icons")
    description = models.CharField(max_length=2000)

class Service_Category(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    cost_per_unit = models.CharField(max_length=20)
    category_description = models.CharField(max_length=2000)
