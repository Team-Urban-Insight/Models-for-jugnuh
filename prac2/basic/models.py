from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_provider = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    phone_no = models.BigIntegerField( blank=True, null=True, default=None)
    address = models.CharField(max_length=500, blank=True, null=True, default=None)
    pincode = models.IntegerField( blank=True, null=True, default=None)

class Service_Provider(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to="img/profile_pics", blank=True, null=True, default=None)
    is_verified = models.BooleanField(default=False)
    police_verification_document = models.ImageField(upload_to="img/police_verification", blank=True, null=True, default=None)
    aadhaar_card = models.ImageField(upload_to="img/aadhaar_image", blank=True, null=True, default=None)
    bank_account = models.CharField(max_length=256, blank=True, null=True, default=None)
    avg_rating = models.FloatField(blank=True, null=True, default=0)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Service_Provider, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.provider)

    # Overriding default save() method
    def save(self, *args, **kwargs):

        # logic to update 'avg_rating' field of respective Provider
        
        # REVIEW: Alse prevent multiple ratings (in views)
        selected_provider = Service_Provider.objects.get(user=self.provider)
        # Get the no. of existing ratings of that provider
        total_ratings_no = Review.objects.filter(provider=self.provider).count()
        prev_ratings_avg = selected_provider.avg_rating
        total_ratings_sum = prev_ratings_avg * total_ratings_no

        selected_provider.avg_rating = (total_ratings_sum + self.rating)/(total_ratings_no+1)
        selected_provider.save()

        super().save(*args, **kwargs)  # Call the "real" save() method.
