from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')

# Register your models here.
admin.site.register(Menu, MenuAdmin)