from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'created_date')
    list_filter = ('first_name', 'last_name', 'phone', 'email', 'created_date')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'created_date')
    ordering = ('first_name', 'last_name', 'phone', 'email', 'created_date')
