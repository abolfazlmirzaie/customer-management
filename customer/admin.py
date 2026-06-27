from django.contrib import admin
from .models import *

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['name', 'email']
    inlines = [NoteInline]