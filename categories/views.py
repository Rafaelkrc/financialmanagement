from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms, models


class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CategoryCreateView(CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDetailView(DetailView):
    model = models.Category
    template_name = 'category_detail.html'


class CategoryUpdateView(UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')


class SubCategoryListView(ListView):
    model = models.SubCategory
    template_name = 'subcategory_list.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SubCategoryCreateView(CreateView):
    model = models.SubCategory
    template_name = 'subcategory_create.html'
    form_class = forms.SubCategoryForm
    success_url = reverse_lazy('subcategory_list')


class SubCategoryDetailView(DetailView):
    model = models.SubCategory
    template_name = 'subcategory_detail.html'


class SubCategoryUpdateView(UpdateView):
    model = models.SubCategory
    template_name = 'subcategory_update.html'
    form_class = forms.SubCategoryForm
    success_url = reverse_lazy('subcategory_list')


class SubCategoryDeleteView(DeleteView):
    model = models.SubCategory
    template_name = 'subcategory_delete.html'
    success_url = reverse_lazy('subcategory_list')
