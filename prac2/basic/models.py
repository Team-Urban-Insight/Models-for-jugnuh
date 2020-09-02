from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_provider = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class Service_Provider(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    aadhaar_card = models.BigIntegerField()
    bank_account = models.CharField(max_length=256)
    rating = models.IntegerField()
    phone_no = models.BigIntegerField()

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_no = models.BigIntegerField()

    def __str__(self):
        return self.user.username

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    provider = models.ForeignKey(Service_Provider, on_delete=models.CASCADE)
    rating = models.IntegerField()
