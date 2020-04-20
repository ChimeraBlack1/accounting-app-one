from django.contrib import admin

from .models import Account, Item

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_number", "account_name","account_type", "account_balance")

admin.site.register(Account, AccountAdmin)
