from django.contrib import admin
from django.contrib.admin import ModelAdmin
from account_postings.models import AccountPosting


@admin.register(AccountPosting)
class AccountPostingAdmin(ModelAdmin):
    list_display = ('create_date', 'issue_date', 'description', 'category', 'subcategory', 'bank', 'expiry_date', 'debit_value', 'credit_value',)
    search_fields = ('create_date', 'description', 'category', 'subcategory', 'bank',)
    ordering = ('create_date', 'description', 'category', 'subcategory', 'bank',)

    def __str__(self):
        return self.description
