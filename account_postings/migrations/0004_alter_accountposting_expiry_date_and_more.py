# Generated by Django 5.0.7 on 2024-08-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_postings', '0003_accountposting_expiry_date_accountposting_issue_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountposting',
            name='expiry_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accountposting',
            name='issue_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
