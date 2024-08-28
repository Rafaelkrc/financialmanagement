from django.db import models


class Category(models.Model):
    TYPE_CHOICE = (('E', 'Entrada'), ('S', 'Saída'), ('T', 'Transferência'),)
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=1, choices=TYPE_CHOICE, blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
