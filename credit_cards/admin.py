from django.contrib import admin
from django.contrib.admin import ModelAdmin
from credit_cards.models import CreditCard


@admin.register(CreditCard)
class CreditCardAdmin(ModelAdmin):
    list_display = ('name', 'bank', 'currency', 'credit_limit', 'standart_debit_account', 'invoice_closing_date', 'day_of_invoice', 'active',)
    search_fields = ('name', 'bank__name',)
    ordering = ('name',)

    def __str__(self):
        return self.name
