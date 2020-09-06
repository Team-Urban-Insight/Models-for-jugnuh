from django.contrib import admin
from .models import Service, Service_Category, Provides, Schedule

# Register your models here.
admin.site.register(Service)
admin.site.register(Service_Category)
admin.site.register(Provides)
admin.site.register(Schedule)
