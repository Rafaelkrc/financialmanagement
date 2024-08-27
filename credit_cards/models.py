from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from bank_account.models import BankAccount, Currency


class CreditCard(models.Model):
    name = models.CharField(max_length=30)
    bank = models.CharField(max_length=50)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='card_currency')
    credit_limit = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    standart_debit_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name='standart_bank')
    invoice_closing_date = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)], help_text='Informe o dia do fechamento da fatura (1 a 31).', default=1)
    day_of_invoice = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)], help_text='Informe o dia do vencimento da fatura (1 a 31).', default=1)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name', 'bank', 'invoice_closing_date', ]

    def __str__(self) -> str:
        return self.name

    def currency_symbol(self):
        return self.currency.symbol
    currency_symbol.symbol = 'Symbol'

    def debit_account(self):
        return self.standart_debit_account.name
    debit_account.name = 'Standart Account'
