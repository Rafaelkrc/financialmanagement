from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms, models


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')


class SubCategoryListView(LoginRequiredMixin, ListView):
    model = models.SubCategory
    template_name = 'subcategory_list.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SubCategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.SubCategory
    template_name = 'subcategory_create.html'
    form_class = forms.SubCategoryForm
    success_url = reverse_lazy('subcategory_list')


class SubCategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.SubCategory
    template_name = 'subcategory_detail.html'


class SubCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.SubCategory
    template_name = 'subcategory_update.html'
    form_class = forms.SubCategoryForm
    success_url = reverse_lazy('subcategory_list')


class SubCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.SubCategory
    template_name = 'subcategory_delete.html'
    success_url = reverse_lazy('subcategory_list')


def load_subcategories(request, category_id):
    subcategories = models.SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})
