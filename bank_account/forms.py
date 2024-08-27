from django import forms
from . import models


class CurrencyForm(forms.ModelForm):

    class Meta:
        model = models.Currency
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'symbol': forms.TextInput(attrs={'class': 'form-control'}), }
        labels = {'name': 'Nome', 'symbol': 'Simbolo', }


class BankAccountForm(forms.ModelForm):

    class Meta:
        model = models.BankAccount
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'iban': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'opening_balance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Nome',
            'bank': 'Banco',
            'iban': 'IBAN',
            'currency': 'Moeda',
            'opening_balance': 'Saldo Inicial',
            'active': 'Ativa',
        }
