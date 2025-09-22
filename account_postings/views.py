from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from . import forms, models


class AccountPostingListView(LoginRequiredMixin, ListView):
    model = models.AccountPosting
    template_name = 'account_posting_list.html'
    context_object_name = 'account_postings'
    months_pt = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
        7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro',
    }

    def get_queryset(self):
        queryset = super().get_queryset().order_by('expiry_date')
        month = self.request.GET.get('mes') or timezone.now().month
        year = self.request.GET.get('ano') or timezone.now().year

        if month and year:
            queryset = queryset.filter(expiry_date__year=year, expiry_date__month=month)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = timezone.now().month
        current_year = timezone.now().year

        selected_month = int(self.request.GET.get('mes', current_month))
        selected_year = int(self.request.GET.get('ano', current_year))

        context['selected_month'] = selected_month
        context['selected_year'] = selected_year
        context['months_pt'] = self.months_pt
        return context


class AccountPostingCreateDebitView(LoginRequiredMixin, CreateView):
    model = models.AccountPosting
    form_class = forms.AccountPostingDebitForm
    template_name = 'account_posting_create_debit.html'
    success_url = reverse_lazy('account_postings_list')


class AccountPostingCreateCreditView(LoginRequiredMixin, CreateView):
    model = models.AccountPosting
    form_class = forms.AccountPostingCreditForm
    template_name = 'account_posting_create_credit.html'
    success_url = reverse_lazy('account_postings_list')


class AccountPostingDetailView(LoginRequiredMixin, DetailView):
    model = models.AccountPosting
    template_name = 'account_posting_detail.html'


class AccountPostingUpdateCreditView(LoginRequiredMixin, UpdateView):
    model = models. AccountPosting
    template_name = 'account_posting_update_credit.html'
    form_class = forms.AccountPostingCreditForm
    success_url = reverse_lazy('account_postings_list')


class AccountPostingUpdateDebitView(LoginRequiredMixin, UpdateView):
    model = models. AccountPosting
    template_name = 'account_posting_update_debit.html'
    form_class = forms.AccountPostingDebitForm
    success_url = reverse_lazy('account_postings_list')


class AccountPostingDeleteView(LoginRequiredMixin, DeleteView):
    model = models.AccountPosting
    template_name = 'account_posting_delete.html'
    success_url = reverse_lazy('account_postings_list')
