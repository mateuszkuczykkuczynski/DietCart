from django.contrib import admin

# Register your models here.
from apps.accounts.models import CustomUser

admin.site.register(CustomUser)