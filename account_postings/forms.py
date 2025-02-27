from django import forms
from . import models
from bank_account.models import BankAccount
from django.utils import timezone
from categories.models import Category, SubCategory


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


class AccountPostingTransferForm(forms.ModelForm):
    from_bank = forms.ModelChoiceField(queryset=BankAccount.objects.all(), label="Conta de origem", widget=forms.Select(attrs={'class': 'form-select'}))
    to_bank = forms.ModelChoiceField(queryset=BankAccount.objects.all(), label="Conta de destino", widget=forms.Select(attrs={'class': 'form-select'}))
    value = forms.DecimalField(max_digits=20, decimal_places=2, label="Valor da transferência", widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.AccountPosting
        fields = ["category", "subcategory", "description", "issue_date", "expiry_date"]
        widgets = {
            'issue_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', "id": "id_category", "readonly": "readonly"}),
            'subcategory': forms.Select(attrs={'class': 'form-control', "id": "id_category", "readonly": "readonly"}),
            'from_bank': forms.Select(attrs={'class': 'form-select'}),
            'to_bank': forms.Select(attrs={'class': 'form-select'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'issue_date': 'Emissão',
            'description': 'Descrição',
            'category': 'Categoria',
            'subcategory': 'Sub-Categoria',
            'expiry_date': 'Vencimento',
            'value': 'Valor',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fixed_category = Category.objects.get(name="Transferência")
        fixed_subcategory = SubCategory.objects.get(name="Transferência")
        self.fields["category"].initial = fixed_category
        self.fields["category"].queryset = Category.objects.filter(id=fixed_category.id)
        self.fields["subcategory"].initial = fixed_subcategory
        self.fields["subcategory"].queryset = SubCategory.objects.filter(id=fixed_subcategory.id)

    def clean(self):
        cleaned_data = super().clean()
        from_bank = cleaned_data.get("from_bank")
        to_bank = cleaned_data.get("to_bank")
        value = cleaned_data.get("value")

        if from_bank == to_bank:
            raise forms.ValidationError("A conta de origem e destino não podem ser a mesma.")

        if value <= 0:
            raise forms.ValidationError("O valor da transferência deve ser positivo.")

        return cleaned_data


# Inicializa o campo de data com a data atual
issue_date = forms.DateField(
    widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
    initial=timezone.now().strftime('%d/%m/%Y')  # Define a data atual formatada
)


expiry_date = forms.DateField(
    widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
    initial=timezone.now().strftime('%d/%m/%Y')  # Define a data atual formatada
)
