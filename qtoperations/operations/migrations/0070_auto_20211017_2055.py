# Generated by Django 3.2.4 on 2021-10-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0069_rename_companyid_sub_customers_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
    ]
