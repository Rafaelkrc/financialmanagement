from django.db import models
from django.core.exceptions import ValidationError
from django.apps import apps


class Currency(models.Model):
    name = models.CharField(max_length=15)
    symbol = models.CharField(max_length=2)

    class Meta:
        ordering = ['name', 'symbol']

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField(max_length=30)
    bank = models.CharField(max_length=50)
    iban = models.CharField(max_length=25, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='account_currency')
    opening_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        update_from_posting = kwargs.pop('update_from_posting', False)
        AccountPosting = apps.get_model('account_postings', 'AccountPosting')  # Importação tardia apenas quando o método for executado

        # Se for uma nova instância, define o saldo atual igual ao saldo inicial
        if not self.pk:
            # Caso seja uma nova conta (não existe no banco de dados ainda)
            if self.current_balance == 0:  # Caso o saldo atual não tenha sido definido, ele será igual ao saldo inicial
                self.current_balance = self.opening_balance
        else:
            if not update_from_posting:
                # Se a conta já existir, obtém o saldo atual do banco de dados para comparação
                original = BankAccount.objects.get(pk=self.pk)
                # Verifica se há movimentações
                if AccountPosting.objects.filter(bank=self).exists():
                    # Se houver movimentações, impede a modificação do saldo inicial ou atual
                    if self.opening_balance != original.opening_balance or self.current_balance != original.current_balance:
                        raise ValidationError("Não é possível modificar o saldo inicial ou atual! Já houve movimentação na conta.")
                    # Impede alterações manuais no saldo atual
                    self.current_balance = original.current_balance
            else:
                super().save(*args, **kwargs)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name', 'bank']

    def __str__(self) -> str:
        return self.name

    def currency_symbol(self):
        return self.currency.symbol
    currency_symbol.symbol = 'Symbol'
