from django import forms
from . import models
from django.utils import timezone


class AccountPostingDebitForm(forms.ModelForm):

    class Meta:
        model = models.AccountPosting
        fields = ['issue_date', 'description', 'category', 'subcategory', 'bank', 'expiry_date', 'debit_value',]
        widgets = {
            'issue_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'bank': forms.Select(attrs={'class': 'form-select'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'debit_value': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'issue_date': 'Emissão',
            'description': 'Descrição',
            'category': 'Categoria',
            'subcategory': 'Sub-Categoria',
            'bank': 'Conta',
            'expiry_date': 'Vencimento',
            'debit_value': 'Valor',
        }


# Inicializa o campo de data com a data atual
issue_date = forms.DateField(
    widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
    initial=timezone.now().strftime('%d/%m/%Y')  # Define a data atual formatada
)


expiry_date = forms.DateField(
    widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
    initial=timezone.now().strftime('%d/%m/%Y')  # Define a data atual formatada
)


class AccountPostingCreditForm(forms.ModelForm):

    class Meta:
        model = models.AccountPosting
        fields = ['issue_date', 'description', 'category', 'subcategory', 'bank', 'expiry_date', 'credit_value',]
        widgets = {
            'issue_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'bank': forms.Select(attrs={'class': 'form-select'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'credit_value': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'issue_date': 'Emissão',
            'description': 'Descrição',
            'category': 'Categoria',
            'subcategory': 'Sub-Categoria',
            'bank': 'Conta',
            'expiry_date': 'Vencimento',
            'credit_value': 'Valor',
        }


# Inicializa o campo de data com a data atual
issue_date = forms.DateField(
    widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
    initial=timezone.now().strftime('%d/%m/%Y')  # Define a data atual formatada
)


expiry_date = forms.DateField(
    widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
    initial=timezone.now().strftime('%d/%m/%Y')  # Define a data atual formatada
)
