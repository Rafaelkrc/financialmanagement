from django.db import models
from categories.models import Category, SubCategory
from bank_account.models import BankAccount
from account_postings.metrics import add_bank_balance_on_debit, add_bank_balance_on_credit, update_bank_balance


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
        # Verifica se o lançamento já existe no banco de dados
        if self.pk:
            original = AccountPosting.objects.get(pk=self.pk)

            # Se houver uma alteração no débito, reverte o impacto do lançamento original
            if original.debit_value != self.debit_value:
                update_bank_balance(self.bank, original.debit_value)

            # Se houver uma alteração no crédito, reverte o impacto do lançamento original
            if original.credit_value != self.credit_value:
                update_bank_balance(self.bank, original.credit_value)

        if self.credit_value < 0:
            self.credit_value = abs(self.credit_value)  # Garante que o valor seja positivo
        super().save(*args, **kwargs)

        if self.debit_value > 0:
            self.debit_value = -abs(self.debit_value)  # Garante que o valor seja negativo

        super().save(*args, **kwargs)

        # Atualiza o saldo com os novos valores
        if self.debit_value != 0:
            add_bank_balance_on_debit(self.bank, self.debit_value)
        elif self.credit_value != 0:
            add_bank_balance_on_credit(self.bank, self.credit_value)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Reverte o impacto do lançamento no saldo da conta bancária antes de deletá-lo
        if self.debit_value != 0:
            update_bank_balance(self.bank, self.debit_value)  # Reverte o débito
        elif self.credit_value != 0:
            update_bank_balance(self.bank, self.credit_value)  # Reverte o crédito

        super().delete(*args, **kwargs)  # Deleta o lançamento

    def category_name(self):
        return self.category.name
    category_name.name = 'Category'

    def subcategory_name(self):
        return self.subcategory.name
    subcategory_name.name = 'SubCategory'

    def bank_name(self):
        return self.bank.name
    bank_name.name = 'Bank'
