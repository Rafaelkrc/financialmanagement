# Generated by Django 5.0.7 on 2024-08-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_postings', '0004_alter_accountposting_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountposting',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='accountposting',
            name='issue_date',
            field=models.DateField(),
        ),
    ]
