from django.db import models
from categories.models import Category, SubCategory
from bank_account.models import BankAccount


class AccountPosting(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    issue_date = models.DateField()
    description = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='account_posting_category')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='account_posting_category')
    bank = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name='account_posting_bank_account')
    expiry_date = models.DateField()
    debit_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    credit_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Garante que o valor seja sempre negativo
        if self.debit_value > 0:
            self.debit_value = -self.debit_value
        super().save(*args, **kwargs)

        # Garante que o valor seja sempre positivo
        if self.credit_value < 0:
            self.credit_value = self.credit_value * -1
        super().save(*args, **kwargs)

    def category_name(self):
        return self.category.name
    category_name.name = 'Category'

    def subcategory_name(self):
        return self.subcategory.name
    subcategory_name.name = 'SubCategory'

    def bank_name(self):
        return self.bank.name
    bank_name.name = 'Bank'
