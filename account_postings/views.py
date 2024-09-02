from django.views.generic import ListView
from django.utils import timezone
from . import models


class AccounPostingListView(ListView):
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
