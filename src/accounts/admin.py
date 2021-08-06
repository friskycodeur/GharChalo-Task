from django.contrib import admin
from .models import User

# Register your models here.

admin.site.site_url = "/"


@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")
