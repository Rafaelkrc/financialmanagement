from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'type', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-control'}),
        }


class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = models.SubCategory
        fields = ['category', 'name', 'active']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-control'}),
        }
