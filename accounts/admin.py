from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'phone_number', 'is_admin')
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

   # readonly_fields = ( 'password',)
    ordering = ('-date_joined',)
admin.site.register(Account, AccountAdmin)
