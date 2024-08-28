from django.contrib import admin
from django.contrib.admin import ModelAdmin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'type', 'active',)
    search_fields = ('name',)
    ordering = ('name',)

    def __str__(self):
        return self.name
