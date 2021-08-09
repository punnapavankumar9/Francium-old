from django.contrib import admin
from .models import UserPofile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserPofile, UserProfileAdmin)