from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register
from .models import Company
from .models import Cars

admin.site.register(Cars)
admin.site.register(Company)
admin.site.register(Register,UserAdmin)

# Register your models here.
