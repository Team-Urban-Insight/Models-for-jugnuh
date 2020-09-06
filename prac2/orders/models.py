from django.db import models
from basic.models import Service_Provider, User
from services.models import Schedule
import datetime
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.user.first_name


class OrderItem(models.Model):
    duration = models.IntegerField()
    order_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['provides', 'order']
        verbose_name_plural = 'Order Items'

    provides = models.ForeignKey('services.Provides', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def auto_create_schedule(self):
        duration_unit = str(self.provides.service_category.cost_per_unit)
        time_added = datetime.timedelta(hours=self.duration)

        if duration_unit == 'Hour':
            time_added = datetime.timedelta(hours=self.duration)
        elif duration_unit == 'Day':
            time_added = datetime.timedelta(days=self.duration)
        elif duration_unit == 'Month':
            time_added = datetime.timedelta(months=self.duration)

        end_date = datetime.datetime.now() + time_added

        new_schedule = Schedule.objects.create(
                    end_date_time=end_date,
                    provider=self.provides.provider,
                    order_item=self
            )
        new_schedule.save()


    def save(self, *args, **kwargs):

        super().save(*args, **kwargs) # Call the actual save() function
        self.auto_create_schedule()


    def __str__(self):
        ret_value = str(self.order.user.first_name)+'-> '+str(self.provides.service_category)
        return ret_value
