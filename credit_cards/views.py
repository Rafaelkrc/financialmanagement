from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms, models


class CreditCardListView(ListView):
    model = models.CreditCard
    template_name = 'credit_card_list.html'
    context_object_name = 'credit_cards'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CreditCardCreateView(CreateView):
    model = models.CreditCard
    template_name = 'credit_card_create.html'
    form_class = forms.CreditCardForm
    success_url = reverse_lazy('credit_card_list')


class CreditCardDetailView(DetailView):
    model = models.CreditCard
    template_name = 'credit_card_detail.html'


class CreditCardUpdateView(UpdateView):
    model = models.CreditCard
    template_name = 'credit_card_update.html'
    form_class = forms.CreditCardForm
    success_url = reverse_lazy('credit_card_list')


class CreditCardDeleteView(DeleteView):
    model = models.CreditCard
    template_name = 'credit_card_delete.html'
    success_url = reverse_lazy('credit_card_list')
