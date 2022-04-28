from django.contrib import admin
from .models import Cat

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')

admin.site.register(Cat, CatAdmin)