from django.contrib import admin
from django.contrib.admin import ModelAdmin
from categories.models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'type', 'active',)
    search_fields = ('name',)
    ordering = ('name',)

    def __str__(self):
        return self.name


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ('category', 'name', 'active',)
    search_fields = ('name',)
    ordering = ('name',)

    def __str__(self):
        return self.name
