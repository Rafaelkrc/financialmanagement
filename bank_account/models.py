from django.db import models


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
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name', 'bank']

    def __str__(self) -> str:
        return self.name

    def currency_symbol(self):
        return self.currency.symbol
    currency_symbol.symbol = 'Symbol'
