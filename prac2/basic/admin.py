from django.contrib import admin

from .models import Service_Provider, Review
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
# Register your models here.
admin.site.register(Service_Provider)
admin.site.register(Review)
