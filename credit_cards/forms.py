from django import forms
from . import models


class CreditCardForm(forms.ModelForm):

    class Meta:
        model = models.CreditCard
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'credit_limit': forms.NumberInput(attrs={'class': 'form-control'}),
            'standart_debit_account': forms.Select(attrs={'class': 'form-control'}),
            'invoice_closing_date': forms.NumberInput(attrs={'class': 'form-control'}),
            'day_of_invoice': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Nome:',
            'bank': 'Banco:',
            'currency': 'Moeda:',
            'credit_limit': 'Limite de Crédito:',
            'standart_debit_account': 'Conta para Débito:',
            'invoice_closing_date': 'Dia do Fechamento da Fatura:',
            'day_of_invoice': 'Dia do Vencimento:',
            'active': 'Ativo:'
        }
