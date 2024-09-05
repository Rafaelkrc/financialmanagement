from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Currency, BankAccount


@admin.register(Currency)
class CurrencyAdmin(ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name',)
    ordering = ('name',)

    def __str__(self):
        return self.name


@admin.register(BankAccount)
class BankAccountAdmin(ModelAdmin):
    list_display = ('name', 'bank', 'iban', 'opening_balance', 'currency_symbol', 'current_balance', 'active')
    search_fields = ('name', 'bank',)
    ordering = ('name', 'bank',)

    def __str__(self) -> str:
        return self.name
