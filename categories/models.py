from django.db import models


class Category(models.Model):
    TYPE_CHOICE = (('E', 'Entrada'), ('S', 'Saída'), ('T', 'Transferência'),)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=1, choices=TYPE_CHOICE, blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default='S', related_name='subcategory_category')
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def category_name(self):
        return self.category.name
    category_name.name = 'Category'
