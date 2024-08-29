# Generated by Django 5.0.7 on 2024-08-29 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default='S', on_delete=django.db.models.deletion.PROTECT, related_name='subcategory_category', to='categories.category')),
            ],
        ),
    ]
