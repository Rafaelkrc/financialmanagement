from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms, models


class CurrencyListView(LoginRequiredMixin, ListView):
    model = models.Currency
    template_name = 'currency_list.html'
    context_object_name = 'coins'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CurrencyCreateView(LoginRequiredMixin, CreateView):
    model = models.Currency
    form_class = forms.CurrencyForm
    template_name = 'currency_create.html'
    success_url = reverse_lazy('currency_list')


class CurrencyDetailView(LoginRequiredMixin, DetailView):
    model = models.Currency
    template_name = 'currency_detail.html'


class CurrencyUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Currency
    template_name = 'currency_update.html'
    form_class = forms.CurrencyForm
    success_url = reverse_lazy('currency_list')


class CurrencyDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Currency
    template_name = 'currency_delete.html'
    success_url = reverse_lazy('currency_list')


class BankAccountListView(LoginRequiredMixin, ListView):
    model = models.BankAccount
    template_name = 'bank_account_list.html'
    context_object_name = 'bank_accounts'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        bank = self.request.GET.get('bank')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if bank:
            queryset = queryset.filter(bank__icontains=bank)
        return queryset


class BankAccountCreateView(LoginRequiredMixin, CreateView):
    model = models.BankAccount
    form_class = forms.BankAccountForm
    template_name = 'bank_account_create.html'
    success_url = reverse_lazy('bank_account_list')


class BankAccountDetailView(LoginRequiredMixin, DetailView):
    model = models.BankAccount
    template_name = 'bank_account_detail.html'


class BankAccountUpdateView(LoginRequiredMixin, UpdateView):
    model = models.BankAccount
    template_name = 'bank_account_update.html'
    form_class = forms.BankAccountForm
    success_url = reverse_lazy('bank_account_list')


class BankAccountDeleteView(LoginRequiredMixin, DeleteView):
    model = models.BankAccount
    template_name = 'bank_account_delete.html'
    success_url = reverse_lazy('bank_account_list')
