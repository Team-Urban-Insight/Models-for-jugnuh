from django.contrib import admin
from .models import Service, Service_Category, Provides

# Register your models here.
admin.site.register(Service)
admin.site.register(Service_Category)
admin.site.register(Provides)
